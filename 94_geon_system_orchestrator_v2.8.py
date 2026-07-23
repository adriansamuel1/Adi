#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
================================================================================
GEON SYSTEM ORCHESTRATOR v2.8 – FINAL PRODUCTION GRADE
================================================================================
System Status: PRODUCTION-READY | SELF-LEARNING | FAULT-TOLERANT
Architekt: Adrian Samuel Bogusławski
Data: Lipiec 2026

ZMIANY W STOSUNKU DO v2.7:
  1. Automatyczne wczytywanie checkpointu w konstruktorze.
  2. Rzadsze czyszczenie hashy (co 500 ticków) – mniejsze obciążenie.
  3. Kolejka wyjściowa (output_queue) dla asynchronicznej emisji.
  4. Eksport metryk do formatu JSON (Prometheus-ready).
  5. Okresowy reset wag Synodu – zapobiega dryfowi (co 2000 cykli).
  6. Ulepszona mediacja – zapamiętuje ostatnią decyzję.
  7. Pełny zestaw testów w sekcji `if __name__ == "__main__"`.
  8. Dodatkowe logowanie w trybie DEBUG.
================================================================================
"""

import heapq
import json
import logging
import math
import os
import time
from collections import deque
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional, Set, Tuple

# ============================================================================
# KONFIGURACJA
# ============================================================================
CONFIG = {
    "MAX_HEAP_SIZE": 1000,
    "CIRCUIT_BREAKER_LIMIT": 5,
    "CIRCUIT_BREAKER_WINDOW_TICKS": 10,
    "INTENT_TTL_SECONDS": 30,
    "RETRY_MAX_ATTEMPTS": 3,
    "RETRY_BACKOFF_MS": [100, 500, 2000],
    "DEDUPLICATE": True,
    "MAX_DLQ_SIZE": 500,
    "CHECKPOINT_INTERVAL": 1000,
    "CHECKPOINT_FILE": "orchestrator_checkpoint.json",
    # Adaptacyjne progi FSM
    "FSM_ADAPTATION_INTERVAL": 100,
    "FSM_TARGET_RATIOS": {"NOMINAL": 0.6, "CAUTION": 0.25, "SHIELDED": 0.10, "CRITICAL": 0.05},
    # PID
    "PID_KP": 1.2,
    "PID_KI": 0.1,
    "PID_KD": 0.05,
    "PID_SETPOINT": 0.6,
    "PID_INTEGRAL_MAX": 5.0,
    # Synod
    "SYNOD_MIN_VOTES": 3,
    "SYNOD_WEIGHTS": {"C_DRAGON": 1.35, "D_CORE": 1.00, "AUTOSTRADA": 0.85},
    "SYNOD_WEIGHT_MIN": 0.5,
    "SYNOD_WEIGHT_MAX": 2.0,
    "SYNOD_LEARNING_RATE": 0.02,
    "SYNOD_RESET_INTERVAL": 2000,  # Reset wag do bazowych co tyle cykli
}

# ============================================================================
# LOGOWANIE I POMOCNIKI
# ============================================================================
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] [GEON_OS] %(message)s"
)
logger = logging.getLogger("GEON_OS_ORCHESTRATOR")

def clamp(val: float, min_val: float = 0.0, max_val: float = 1.0) -> float:
    return max(min_val, min(max_val, val))

def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()

def now_epoch() -> float:
    return time.time()


# ============================================================================
# WARSTWA 90: AUTOSTRADA33 – SZYNA Z DEDUPLIKACJĄ O(1), DLQ I RETRY
# ============================================================================
class Autostrada33:
    def __init__(self, config: Optional[Dict[str, Any]] = None):
        self.config = CONFIG.copy()
        if config:
            self.config.update(config)

        self.intent_heap: List[Tuple[int, int, Dict[str, Any]]] = []
        self.seen_hashes: Set[int] = set()
        self.retry_queue: deque = deque()
        self.dead_letter_queue: List[Dict[str, Any]] = []
        self.output_queue: deque = deque()          # kolejka wyjściowa (asynchroniczna emisja)
        self.seq_counter: int = 0
        self.tick: int = 0
        self.cb_history: List[Tuple[int, str]] = []
        self.circuit_open: bool = False
        self.circuit_half_open: bool = False
        self.circuit_open_tick: int = 0

        self.metrics = {
            "submitted": 0,
            "processed": 0,
            "failed": 0,
            "retried": 0,
            "expired": 0,
            "dropped": 0,
            "dlq_count": 0,
            "output_queue_size": 0,
        }

    def _compute_hash(self, intent_type: str, payload: Dict[str, Any]) -> Optional[int]:
        try:
            payload_str = json.dumps(payload, sort_keys=True, default=str)
            return hash((intent_type, payload_str))
        except Exception:
            return None

    def push_intent(self, priority: int, intent_type: str, payload: Dict[str, Any]) -> bool:
        if self.circuit_open and not self.circuit_half_open:
            logger.warning("[AUTOSTRADA] Circuit Breaker OTWARTY – odrzucono: %s", intent_type)
            self.metrics["dropped"] += 1
            return False

        if len(self.intent_heap) >= self.config["MAX_HEAP_SIZE"]:
            logger.error("[AUTOSTRADA] Przepełnienie kopca! Odrzucam.")
            self.record_failure("HEAP_OVERFLOW")
            self.metrics["dropped"] += 1
            return False

        payload_hash = self._compute_hash(intent_type, payload)
        if self.config["DEDUPLICATE"] and payload_hash is not None:
            if payload_hash in self.seen_hashes:
                logger.debug("[AUTOSTRADA] Duplikat odrzucony: %s", intent_type)
                return True
            self.seen_hashes.add(payload_hash)

        self.seq_counter += 1
        msg = {
            "type": intent_type,
            "payload": payload,
            "priority": priority,
            "created_at": now_iso(),
            "timestamp_epoch": now_epoch(),
            "seq": self.seq_counter,
            "attempts": 0,
            "_hash": payload_hash,
        }
        heapq.heappush(self.intent_heap, (priority, self.seq_counter, msg))
        self.metrics["submitted"] += 1
        return True

    def pop_intent(self) -> Optional[Dict[str, Any]]:
        if self.circuit_open and not self.circuit_half_open:
            return None

        while self.intent_heap:
            _, _, msg = self.intent_heap[0]
            if self._is_expired(msg):
                heapq.heappop(self.intent_heap)
                self._remove_hash(msg)
                self.metrics["expired"] += 1
                logger.debug("[AUTOSTRADA] Intencja wygasła: %s", msg.get("type"))
            else:
                break

        if not self.intent_heap:
            return None

        _, _, msg = heapq.heappop(self.intent_heap)
        self._remove_hash(msg)
        self.metrics["processed"] += 1
        return msg

    def _is_expired(self, msg: Dict[str, Any]) -> bool:
        ts = msg.get("timestamp_epoch")
        if ts is None:
            return False
        return (now_epoch() - ts) > self.config["INTENT_TTL_SECONDS"]

    def _remove_hash(self, msg: Dict[str, Any]) -> None:
        h = msg.get("_hash")
        if h is not None:
            self.seen_hashes.discard(h)

    def requeue_with_backoff(self, msg: Dict[str, Any], error: str) -> None:
        attempts = msg.get("attempts", 0) + 1
        max_attempts = self.config["RETRY_MAX_ATTEMPTS"]

        if attempts <= max_attempts:
            backoff_ms = self.config["RETRY_BACKOFF_MS"][attempts - 1]
            msg["attempts"] = attempts
            msg["next_retry_tick"] = self.tick + (backoff_ms // 100)
            msg["last_error"] = error
            self.retry_queue.append(msg)
            self.metrics["retried"] += 1
            logger.info("[AUTOSTRADA] Retry #%d dla %s (za %d ticków)", attempts, msg.get("type"), backoff_ms // 100)
        else:
            msg["final_error"] = error
            msg["failed_at"] = now_iso()
            self._remove_hash(msg)
            self.dead_letter_queue.append(msg)
            if len(self.dead_letter_queue) > self.config["MAX_DLQ_SIZE"]:
                self.dead_letter_queue.pop(0)
            self.metrics["failed"] += 1
            self.metrics["dlq_count"] = len(self.dead_letter_queue)
            self.record_failure(f"RETRY_EXHAUSTED: {error}")
            logger.error("[AUTOSTRADA] Intencja przeniesiona do DLQ: %s", msg.get("type"))

    def process_retry_queue(self) -> None:
        while self.retry_queue:
            msg = self.retry_queue[0]
            if msg.get("next_retry_tick", 0) <= self.tick:
                self.retry_queue.popleft()
                priority = msg.get("priority", 5)
                self._remove_hash(msg)
                self.push_intent(priority, msg.get("type"), msg.get("payload", {}))
            else:
                break

    def record_failure(self, reason: str) -> None:
        self.cb_history.append((self.tick, reason))
        self._evaluate_circuit_breaker()

    def _evaluate_circuit_breaker(self) -> None:
        window = self.config["CIRCUIT_BREAKER_WINDOW_TICKS"]
        recent = [f for f in self.cb_history if (self.tick - f[0]) <= window]
        if len(recent) >= self.config["CIRCUIT_BREAKER_LIMIT"]:
            if not self.circuit_open:
                self.circuit_open = True
                self.circuit_open_tick = self.tick
                self.circuit_half_open = False
                logger.critical("[AUTOSTRADA] Circuit Breaker AKTYWOWANY! Awarie: %d", len(recent))

    def _prune_circuit_breaker_history(self) -> None:
        window = self.config["CIRCUIT_BREAKER_WINDOW_TICKS"]
        self.cb_history = [f for f in self.cb_history if (self.tick - f[0]) <= window]

    def _try_half_open(self) -> None:
        if self.circuit_open and not self.circuit_half_open:
            if (self.tick - self.circuit_open_tick) > self.config["CIRCUIT_BREAKER_WINDOW_TICKS"] * 2:
                self.circuit_half_open = True
                logger.info("[AUTOSTRADA] Próba przejścia w stan HALF-OPEN.")

    def reset_circuit(self) -> None:
        self.circuit_open = False
        self.circuit_half_open = False
        self.cb_history.clear()
        logger.info("[AUTOSTRADA] Circuit Breaker zresetowany.")

    def push_output(self, output: Dict[str, Any]) -> None:
        """Dodaje wynik do kolejki wyjściowej (asynchroniczna emisja)."""
        self.output_queue.append(output)
        self.metrics["output_queue_size"] = len(self.output_queue)

    def flush_output(self) -> List[Dict[str, Any]]:
        """Zwraca i czyści kolejkę wyjściową."""
        items = list(self.output_queue)
        self.output_queue.clear()
        self.metrics["output_queue_size"] = 0
        return items

    def tick_once(self) -> None:
        self.tick += 1
        self._prune_circuit_breaker_history()
        self._try_half_open()
        self.process_retry_queue()

        # Rzadsze czyszczenie hashy (co 500 ticków)
        if self.tick % 500 == 0:
            self._cleanup_seen_hashes()

    def _cleanup_seen_hashes(self) -> None:
        current_hashes = {msg.get("_hash") for _, _, msg in self.intent_heap if msg.get("_hash") is not None}
        self.seen_hashes.intersection_update(current_hashes)


# ============================================================================
# WARSTWA 87: DCoreArcanum – PREDYKCJA RYZYKA
# ============================================================================
class DCoreArcanum:
    def __init__(self):
        self.history: List[Dict[str, float]] = []
        self.weights = {"LINEAR": 0.4, "EXPONENTIAL": 0.6}

    def ingest_metrics(self, load: float, error_rate: float, latency_ms: float) -> float:
        risk_score = (load * 0.3) + (error_rate * 0.5) + (clamp(latency_ms / 1000.0, 0.0, 1.0) * 0.2)
        risk = clamp(risk_score, 0.0, 1.0)
        self.history.append({
            "LOAD": load, "ERROR_RATE": error_rate, "LATENCY": latency_ms,
            "RISK": risk, "timestamp": now_iso()
        })
        if len(self.history) > 1000:
            self.history.pop(0)
        return risk

    def predict_next_risk(self) -> Dict[str, Any]:
        if len(self.history) < 2:
            current = self.history[-1]["RISK"] if self.history else 0.0
            return {"predicted_risk": current, "trend": "STABLE", "confidence": 0.5}

        last = self.history[-1]["RISK"]
        prev = self.history[-2]["RISK"]

        linear = clamp(last + (last - prev), 0.0, 1.0)
        exp = (0.3 * last) + (0.7 * prev)
        fused = (linear * self.weights["LINEAR"]) + (exp * self.weights["EXPONENTIAL"])
        fused = clamp(fused, 0.0, 1.0)

        delta = fused - last
        trend = "RISING" if delta > 0.05 else ("FALLING" if delta < -0.05 else "STABLE")
        return {
            "predicted_risk": round(fused, 4),
            "trend": trend,
            "delta": round(delta, 4),
            "confidence": 0.88 if len(self.history) >= 20 else 0.60
        }


# ============================================================================
# WARSTWA 88+89: CDragonFSM – ADAPTACYJNE PROGI
# ============================================================================
class CDragonFSM:
    def __init__(self, config: Optional[Dict] = None):
        self.config = CONFIG.copy()
        if config:
            self.config.update(config)
        self.state: str = "NOMINAL"
        self.transition_log: List[Dict[str, Any]] = []
        self.risk_history: List[float] = []
        self.thresholds = {
            "CRITICAL": 0.85,
            "SHIELDED": 0.60,
            "CAUTION": 0.35,
        }
        self.adapt_counter = 0

    def evaluate(self, predicted_risk: float, system_faults: int) -> str:
        prev = self.state
        self.risk_history.append(predicted_risk)
        if len(self.risk_history) > 1000:
            self.risk_history = self.risk_history[-1000:]

        self.adapt_counter += 1
        if self.adapt_counter >= self.config["FSM_ADAPTATION_INTERVAL"]:
            self._adapt_thresholds()
            self.adapt_counter = 0

        t = self.thresholds
        if system_faults > 3 or predicted_risk >= t["CRITICAL"]:
            self.state = "CRITICAL"
        elif predicted_risk >= t["SHIELDED"]:
            self.state = "SHIELDED"
        elif predicted_risk >= t["CAUTION"]:
            self.state = "CAUTION"
        else:
            self.state = "NOMINAL"

        if prev != self.state:
            logger.warning("[C_FSM] Zmiana stanu: %s → %s (risk=%.2f, faults=%d)",
                           prev, self.state, predicted_risk, system_faults)
            self.transition_log.append({
                "from": prev, "to": self.state,
                "risk": predicted_risk, "timestamp": now_iso()
            })
        return self.state

    def _adapt_thresholds(self) -> None:
        if len(self.risk_history) < 50:
            return

        target = self.config["FSM_TARGET_RATIOS"]
        sorted_risks = sorted(self.risk_history)
        n = len(sorted_risks)

        def percentile(p):
            idx = int(p * n)
            return sorted_risks[min(idx, n - 1)]

        self.thresholds["CRITICAL"] = percentile(0.90 + (1 - target["CRITICAL"]))
        self.thresholds["SHIELDED"] = percentile(0.70 + (1 - target["SHIELDED"]))
        self.thresholds["CAUTION"] = percentile(0.40 + (1 - target["CAUTION"]))

        self.thresholds["CRITICAL"] = clamp(self.thresholds["CRITICAL"], 0.6, 0.95)
        self.thresholds["SHIELDED"] = clamp(self.thresholds["SHIELDED"], 0.4, 0.85)
        self.thresholds["CAUTION"] = clamp(self.thresholds["CAUTION"], 0.2, 0.65)

        logger.info("[C_FSM] Adaptacja progów: CRIT=%.2f, SHIELD=%.2f, CAUTION=%.2f",
                    self.thresholds["CRITICAL"], self.thresholds["SHIELDED"], self.thresholds["CAUTION"])


# ============================================================================
# WARSTWA 89: G_Core_PID – REGULATOR Z ANTI-WINDUP
# ============================================================================
class G_Core_PID:
    def __init__(self, config: Optional[Dict] = None):
        self.config = CONFIG.copy()
        if config:
            self.config.update(config)
        self.kp = self.config["PID_KP"]
        self.ki = self.config["PID_KI"]
        self.kd = self.config["PID_KD"]
        self.setpoint = self.config["PID_SETPOINT"]
        self.integral_max = self.config["PID_INTEGRAL_MAX"]
        self.integral = 0.0
        self.prev_error = 0.0
        self.multiplier = 1.0
        self.mode = "NORMAL"
        self.throttle = False

    def compute(self, load: float, risk: float) -> Tuple[float, str, bool]:
        error = self.setpoint - load

        # Anti-Windup Clamping
        self.integral = clamp(self.integral + error, -self.integral_max, self.integral_max)

        derivative = error - self.prev_error
        self.prev_error = error

        pid_output = self.kp * error + self.ki * self.integral + self.kd * derivative
        base_multiplier = clamp(pid_output + 1.0, 0.2, 1.8)

        risk_factor = 1.0 - risk * 0.6
        self.multiplier = clamp(base_multiplier * risk_factor, 0.1, 1.5)

        if risk > 0.75:
            self.mode = "SAFE_MODE"
        elif risk > 0.50:
            self.mode = "CAUTION"
        else:
            self.mode = "NORMAL"

        self.throttle = (load > 0.85) or (risk > 0.85)
        return self.multiplier, self.mode, self.throttle


# ============================================================================
# WARSTWA 91: GeonSynod – ZATRZYMYWANIE STANU GŁOSÓW, RESET WAG
# ============================================================================
class GeonSynod:
    def __init__(self, config: Optional[Dict] = None):
        self.config = CONFIG.copy()
        if config:
            self.config.update(config)
        self.votes: Dict[str, Dict[str, Any]] = {}
        self.last_votes: Dict[str, Dict[str, Any]] = {}
        self.consensus_history: List[Dict[str, Any]] = []
        self.mediation_count: int = 0
        self.weights = self.config["SYNOD_WEIGHTS"].copy()
        self.base_weights = self.weights.copy()  # kopia bazowa do resetu
        self.learning_rate = self.config["SYNOD_LEARNING_RATE"]
        self.reset_interval = self.config["SYNOD_RESET_INTERVAL"]
        self.cycle_counter = 0
        self.last_mediation_decision = None

    def submit_vote(self, source_node: str, decision: str, confidence: float) -> None:
        self.votes[source_node] = {
            "decision": decision,
            "confidence": clamp(confidence, 0.0, 1.0),
            "timestamp": now_iso()
        }

    def mediate(self, conflict_context: Dict[str, Any]) -> Dict[str, Any]:
        self.mediation_count += 1
        logger.info("[SYNOD] Mediacja #%d – konflikt: %s", self.mediation_count, conflict_context)

        outcomes = conflict_context.get("conflict_decisions", [])
        if outcomes:
            scores = {}
            for dec in outcomes:
                score = 0.0
                for src, vote in self.votes.items():
                    if vote.get("decision") == dec:
                        w = self.weights.get(src, 1.0)
                        score += w * vote.get("confidence", 0.5)
                scores[dec] = score
            if scores:
                best = max(scores, key=scores.get)
                self.last_mediation_decision = best
                return {"suggestion": best, "confidence": 0.85, "reason": "MEDIATION_WEIGHTED"}

        # Fallback – bezpieczny wybór
        self.last_mediation_decision = "C_SHIELD"
        return {"suggestion": "C_SHIELD", "confidence": 0.95, "reason": "MEDIATION_DEFENSIVE"}

    def reach_consensus(self) -> Optional[Dict[str, Any]]:
        if len(self.votes) < self.config["SYNOD_MIN_VOTES"]:
            logger.warning("[SYNOD] Za mało głosów (%d/%d).", len(self.votes), self.config["SYNOD_MIN_VOTES"])
            return None

        outcomes: Dict[str, float] = {}
        for src, vote in self.votes.items():
            decision = vote.get("decision")
            if decision:
                w = self.weights.get(src, 1.0) * vote.get("confidence", 1.0)
                outcomes[decision] = outcomes.get(decision, 0.0) + w

        if not outcomes:
            return None

        sorted_outcomes = sorted(outcomes.items(), key=lambda x: x[1], reverse=True)

        if len(sorted_outcomes) > 1 and math.isclose(sorted_outcomes[0][1], sorted_outcomes[1][1], abs_tol=1e-3):
            logger.info("[SYNOD] Remis – mediacja.")
            conflict_decisions = [o[0] for o in sorted_outcomes[:2]]
            mediation_res = self.mediate({"conflict_decisions": conflict_decisions})
            consensus_decision = mediation_res["suggestion"]
            confidence = mediation_res["confidence"]
        else:
            consensus_decision = sorted_outcomes[0][0]
            total_weight = sum(outcomes.values())
            confidence = sorted_outcomes[0][1] / total_weight if total_weight > 0 else 0.0

        recommendation = {
            "decision": consensus_decision,
            "confidence": clamp(confidence, 0.0, 1.0),
            "votes": self.votes.copy(),
            "timestamp": now_iso(),
            "mediation_count": self.mediation_count
        }

        self.consensus_history.append(recommendation)
        if len(self.consensus_history) > 50:
            self.consensus_history.pop(0)

        self.last_votes = self.votes.copy()
        self.votes = {}
        return recommendation

    def update_weights(self, success: bool, decision: str) -> None:
        """Aktualizuje wagi na podstawie zapamiętanych głosów."""
        for src, vote in self.last_votes.items():
            if vote.get("decision") == decision:
                delta = self.learning_rate if success else -self.learning_rate
                self.weights[src] = clamp(self.weights[src] + delta,
                                          self.config["SYNOD_WEIGHT_MIN"],
                                          self.config["SYNOD_WEIGHT_MAX"])
        logger.debug("[SYNOD] Wagi po aktualizacji: %s", self.weights)

    def reset_weights_to_base(self) -> None:
        """Resetuje wagi do wartości bazowych (zabezpieczenie przed dryfem)."""
        self.weights = self.base_weights.copy()
        logger.info("[SYNOD] Wagi zresetowane do wartości bazowych: %s", self.weights)

    def tick(self) -> None:
        """Wykonuje cykl okresowy – reset wag co określony interwał."""
        self.cycle_counter += 1
        if self.cycle_counter % self.reset_interval == 0:
            self.reset_weights_to_base()


# ============================================================================
# WARSTWA 92: GeonKonsystorz – PIECZĘĆ OSTATECZNA
# ============================================================================
class GeonKonsystorz:
    def __init__(self):
        self.seal_active = True
        self.veto_power = True
        self.approved_decisions: List[Dict[str, Any]] = []
        self.system_mode = "NOMINAL"
        self.last_seal_timestamp = now_iso()

    def approve(self, decision: Dict[str, Any]) -> bool:
        if not self.seal_active:
            logger.warning("[KONSYSTORZ] Pieczęć nieaktywna – odrzucono.")
            return False
        if decision.get("confidence", 0.0) < 0.5:
            logger.warning("[KONSYSTORZ] Zbyt niska pewność (%.2f) – weto.", decision.get("confidence"))
            return False

        approved = {
            "decision": decision,
            "seal_timestamp": now_iso(),
            "seal_id": f"SEAL_{len(self.approved_decisions)+1:04d}"
        }
        self.approved_decisions.append(approved)
        self.last_seal_timestamp = now_iso()
        logger.info("[KONSYSTORZ] Decyzja zatwierdzona: %s", approved["seal_id"])
        return True

    def veto(self, decision: Dict[str, Any]) -> bool:
        if not self.veto_power:
            logger.warning("[KONSYSTORZ] Brak uprawnień do veta.")
            return False
        logger.info("[KONSYSTORZ] Weto nałożone na decyzję: %s", decision)
        return True

    def set_mode(self, mode: str) -> None:
        allowed = ["NOMINAL", "SAFE_MODE", "CAUTION", "HIGH_PERFORMANCE", "STEALTH"]
        if mode in allowed:
            self.system_mode = mode
            logger.info("[KONSYSTORZ] Tryb zmieniony na: %s", mode)
        else:
            logger.error("[KONSYSTORZ] Nieznany tryb: %s", mode)

    def get_status(self) -> Dict[str, Any]:
        return {
            "seal_active": self.seal_active,
            "veto_power": self.veto_power,
            "system_mode": self.system_mode,
            "approved_count": len(self.approved_decisions),
            "last_seal": self.last_seal_timestamp
        }


# ============================================================================
# WARSTWA 94: GŁÓWNY ORCHESTRATOR Z ATOMOWYM CHECKPOINTEM I EMISJĄ
# ============================================================================
class GeonSystemOrchestrator:
    def __init__(self, config: Optional[Dict] = None):
        self.config = CONFIG.copy()
        if config:
            self.config.update(config)

        self.autostrada = Autostrada33(self.config)
        self.d_core = DCoreArcanum()
        self.fsm = CDragonFSM(self.config)
        self.g_core = G_Core_PID(self.config)
        self.synod = GeonSynod(self.config)
        self.konsystorz = GeonKonsystorz()

        self.tick_counter = 0
        self.checkpoint_interval = self.config["CHECKPOINT_INTERVAL"]
        self.checkpoint_file = self.config["CHECKPOINT_FILE"]

        # Automatyczne wczytanie checkpointu przy starcie
        if os.path.exists(self.checkpoint_file):
            self.load_checkpoint()

    def process_cycle(self, telemetry: Dict[str, float], feedback: Optional[bool] = None) -> Dict[str, Any]:
        self.tick_counter += 1

        # 0. Feedback dla Synodu
        if feedback is not None and self.synod.consensus_history:
            last_consensus = self.synod.consensus_history[-1]
            decision = last_consensus.get("decision")
            if decision:
                self.synod.update_weights(feedback, decision)

        # 0a. Cykl okresowy Synodu (reset wag)
        self.synod.tick()

        # 1. Takt Autostrady
        self.autostrada.tick_once()

        # 2. Ingestia metryk
        load = telemetry.get("load", 0.0)
        errors = telemetry.get("errors", 0.0)
        latency = telemetry.get("latency", 0.0)

        current_risk = self.d_core.ingest_metrics(load, errors, latency)
        prediction = self.d_core.predict_next_risk()

        # 3. FSM
        fault_count = len(self.autostrada.cb_history)
        fsm_state = self.fsm.evaluate(prediction["predicted_risk"], fault_count)

        # 4. G_Core (PID)
        buffer_pressure = len(self.autostrada.intent_heap) / self.autostrada.config["MAX_HEAP_SIZE"]
        multiplier, g_mode, throttle = self.g_core.compute(buffer_pressure, prediction["predicted_risk"])
        if throttle:
            self.autostrada.record_failure("G_THROTTLE")
        self.konsystorz.set_mode(g_mode)

        # 5. Synod – głosowanie
        d_vote = "PROCEED" if prediction["predicted_risk"] < 0.50 else "THROTTLE"
        fsm_vote = "PROCEED" if fsm_state == "NOMINAL" else ("C_SHIELD" if fsm_state in ["SHIELDED", "CRITICAL"] else "THROTTLE")
        bus_vote = "HALT" if self.autostrada.circuit_open else "PROCEED"

        self.synod.submit_vote("D_CORE", d_vote, prediction["confidence"])
        self.synod.submit_vote("C_DRAGON", fsm_vote, 0.95)
        self.synod.submit_vote("AUTOSTRADA", bus_vote, 0.90)

        consensus = self.synod.reach_consensus()

        # 6. Konsystorz
        approved = False
        if consensus:
            approved = self.konsystorz.approve(consensus)

        # 7. Wykonanie intencji
        executed_intent = None
        if approved and consensus and consensus["decision"] == "PROCEED":
            executed_intent = self.autostrada.pop_intent()
            if executed_intent:
                logger.info("[ORCHESTRATOR] Wykonano intencję: %s", executed_intent.get("type"))
                # Dodaj do kolejki wyjściowej (asynchroniczna emisja)
                self.autostrada.push_output({
                    "type": "EXECUTED_INTENT",
                    "intent": executed_intent,
                    "timestamp": now_iso(),
                    "tick": self.tick_counter
                })

        # 8. Atomowy Checkpoint
        if self.tick_counter % self.checkpoint_interval == 0:
            self._save_checkpoint()

        return {
            "tick": self.autostrada.tick,
            "current_risk": current_risk,
            "prediction": prediction,
            "fsm_state": fsm_state,
            "g_core": {"mode": g_mode, "multiplier": multiplier, "throttle": throttle},
            "consensus": consensus,
            "approved": approved,
            "executed_intent": executed_intent,
            "konsystorz_status": self.konsystorz.get_status(),
            "autostrada_metrics": self.autostrada.metrics,
            "synod_weights": self.synod.weights,
        }

    def _save_checkpoint(self) -> None:
        state = {
            "tick": self.tick_counter,
            "fsm_state": self.fsm.state,
            "fsm_thresholds": self.fsm.thresholds,
            "g_core": {
                "multiplier": self.g_core.multiplier,
                "mode": self.g_core.mode,
                "integral": self.g_core.integral,
                "prev_error": self.g_core.prev_error,
            },
            "synod_weights": self.synod.weights,
            "autostrada": {
                "heap_size": len(self.autostrada.intent_heap),
                "retry_queue_size": len(self.autostrada.retry_queue),
                "dlq_size": len(self.autostrada.dead_letter_queue),
                "circuit_open": self.autostrada.circuit_open,
                "metrics": self.autostrada.metrics,
            },
            "timestamp": now_iso()
        }
        temp_file = f"{self.checkpoint_file}.tmp"
        try:
            with open(temp_file, "w") as f:
                json.dump(state, f, indent=2)
            os.replace(temp_file, self.checkpoint_file)
            logger.info("[ORCHESTRATOR] Checkpoint zapisany atomowo (tick %d).", self.tick_counter)
        except Exception as e:
            logger.error("[ORCHESTRATOR] Błąd zapisu checkpoint: %s", e)
            if os.path.exists(temp_file):
                try:
                    os.remove(temp_file)
                except OSError:
                    pass

    def load_checkpoint(self) -> bool:
        if not os.path.exists(self.checkpoint_file):
            return False
        try:
            with open(self.checkpoint_file, "r") as f:
                state = json.load(f)
            self.tick_counter = state.get("tick", 0)
            self.fsm.state = state.get("fsm_state", "NOMINAL")
            self.fsm.thresholds = state.get("fsm_thresholds", self.fsm.thresholds)
            self.g_core.multiplier = state.get("g_core", {}).get("multiplier", 1.0)
            self.g_core.mode = state.get("g_core", {}).get("mode", "NORMAL")
            self.g_core.integral = state.get("g_core", {}).get("integral", 0.0)
            self.g_core.prev_error = state.get("g_core", {}).get("prev_error", 0.0)
            self.synod.weights = state.get("synod_weights", self.synod.weights)
            logger.info("[ORCHESTRATOR] Checkpoint załadowany (tick %d).", self.tick_counter)
            return True
        except Exception as e:
            logger.error("[ORCHESTRATOR] Błąd ładowania checkpoint: %s", e)
            return False

    def export_metrics(self) -> Dict[str, Any]:
        """Eksportuje wszystkie metryki systemowe do formatu JSON (Prometheus-ready)."""
        return {
            "orchestrator": {
                "tick": self.tick_counter,
                "fsm_state": self.fsm.state,
                "fsm_thresholds": self.fsm.thresholds,
                "g_mode": self.g_core.mode,
                "g_multiplier": self.g_core.multiplier,
                "synod_weights": self.synod.weights,
                "synod_mediation_count": self.synod.mediation_count,
                "konsystorz": self.konsystorz.get_status(),
            },
            "autostrada": {
                "metrics": self.autostrada.metrics,
                "circuit_open": self.autostrada.circuit_open,
                "heap_size": len(self.autostrada.intent_heap),
                "retry_queue_size": len(self.autostrada.retry_queue),
                "dlq_size": len(self.autostrada.dead_letter_queue),
                "output_queue_size": len(self.autostrada.output_queue),
            },
            "timestamp": now_iso()
        }

    def flush_output(self) -> List[Dict[str, Any]]:
        """Zwraca i czyści kolejkę wyjściową."""
        return self.autostrada.flush_output()


# ============================================================================
# SYMULACJA I TESTY
# ============================================================================
if __name__ == "__main__":
    logger.info("=== GEON SYSTEM ORCHESTRATOR v2.8 – TEST INTEGRACYJNY ===")

    orchestrator = GeonSystemOrchestrator()

    # 1. Test deduplikacji
    logger.info("\n--- TEST DEDUPLIKACJI ---")
    for i in range(3):
        orchestrator.autostrada.push_intent(priority=2, intent_type="SYNC", payload={"target": "db"})
    assert len(orchestrator.autostrada.seen_hashes) == 1
    logger.info("Deduplikacja: OK (tylko 1 unikalny hash)")

    # 2. Test retry i DLQ
    logger.info("\n--- TEST RETRY I DLQ ---")
    # Symulujemy intencję, która wielokrotnie zawodzi
    msg = {
        "type": "FAILING",
        "payload": {"data": "test"},
        "priority": 3,
        "attempts": 0,
        "_hash": None,
    }
    for i in range(4):
        orchestrator.autostrada.requeue_with_backoff(msg, f"test_error_{i}")
    assert len(orchestrator.autostrada.dead_letter_queue) == 1
    assert orchestrator.autostrada.metrics["failed"] == 1
    logger.info("Retry i DLQ: OK (intencja trafiła do DLQ po 3 próbach)")

    # 3. Test circuit breaker
    logger.info("\n--- TEST CIRCUIT BREAKER ---")
    for i in range(6):
        orchestrator.autostrada.record_failure(f"test_failure_{i}")
    assert orchestrator.autostrada.circuit_open is True
    logger.info("Circuit Breaker: OK (otwarty po 5 awariach)")

    # 4. Test pełnego cyklu z feedbackiem
    logger.info("\n--- TEST PEŁNEGO CYKLU ---")
    test_data = [
        ({"load": 0.2, "errors": 0.0, "latency": 40.0}, True),
        ({"load": 0.8, "errors": 0.3, "latency": 300.0}, False),
        ({"load": 0.3, "errors": 0.0, "latency": 50.0}, True),
    ]

    for i, (telemetry, fb) in enumerate(test_data, 1):
        logger.info("\n--- CYKL %d ---", i)
        res = orchestrator.process_cycle(telemetry, feedback=fb)
        print(f"Tick: {res['tick']} | Risk: {res['prediction']['predicted_risk']} | FSM: {res['fsm_state']}")
        print(f"Wagi Synodu: {orchestrator.synod.weights}")

    # 5. Test eksportu metryk i kolejki wyjściowej
    logger.info("\n--- TEST EKSPORTU METRYK I KOLEJKI WYJŚCIOWEJ ---")
    metrics = orchestrator.export_metrics()
    print(f"Metrics: {json.dumps(metrics, indent=2)[:200]}...")
    outputs = orchestrator.flush_output()
    print(f"Liczba elementów w kolejce wyjściowej: {len(outputs)}")

    # 6. Test checkpoint
    logger.info("\n--- TEST CHECKPOINT ---")
    orchestrator._save_checkpoint()
    assert os.path.exists(orchestrator.checkpoint_file)
    logger.info("Checkpoint zapisany pomyślnie.")

    logger.info("\n=== WSZYSTKIE TESTY ZAKOŃCZONE SUKCESEM ===")