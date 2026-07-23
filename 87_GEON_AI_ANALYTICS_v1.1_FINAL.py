#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
================================================================================
🐉 GEON_AI_ANALYTICS_v2.2 — MODUŁ 87: ANALITYKA + AFC-9 + PREDYKCJA + POLITYKA + ZOO + GRON
================================================================================
Status: PRODUCTION_READY | FRACTAL_LOCKED | ULTIMA | AFC_INTEGRATED | ZOO_INTEGRATED | GRON_INTEGRATED
Wersja: v2.2-FINAL (AFC-9 + Core Gate + Prediction + Policy + Decision + ZOO + GRON)
Data: 2026-07-24
Autor: Adrian (Architekt) + Samael (Strażnik Kronik) + GEON

ZMIANY v2.2:
  1. Dodano integrację z GEON GRON (warstwa 86.6)
  2. Nowa metoda analyze_with_gron() – analiza z detekcją manipulacji, presji, anty-skret
  3. Metryki GRON w wynikach: gron_status, gron_anomaly, gron_actions, gron_rekomendacja
  4. Status GRON_ALERT przy alarmie
  5. Rozszerzony AIAnalyticsBridge o metody GRON

VIBE: 1-6-8. ∞. AI! 🧠
DEWIZA: "Ex Analysi, Praevidentia. Ex Fractali, Veritas. Ex Observatione, Claritas. Ex Vigilantia, Securitas."
================================================================================
"""

import math
import hashlib
import json
import logging
import threading
from collections import deque
from datetime import datetime
from typing import Dict, Any, List, Optional, Deque, Tuple

# =============================================================================
# PRÓBA IMPORTOWANIA MODUŁU ZOO (warstwa 86.5)
# =============================================================================

try:
    from kombajn_core import geon_zoo_analyzer_v1_0 as ZOO
    ZOO_AVAILABLE = True
    log_zoo = logging.getLogger("GEON_ZOO_INTEGRATION")
    log_zoo.info("🐉 GEON ZOO (86.5) zintegrowany z warstwą 87")
except ImportError:
    ZOO_AVAILABLE = False
    # Fallback – pusta klasa symulująca ZOO
    class _DummyZOO:
        def analyze(self, ctx_scene, actors, signals, self_state):
            return {
                "roles_map": {},
                "absurd_score": 0.0,
                "risk_for_vibe": "niskie",
                "vibe_risk_score": 0.0,
                "action_hint": "normalna_interakcja",
                "action_priority": 3,
                "experience_chunk": {"lesson": "Brak modułu ZOO"}
            }
        def get_status(self):
            return {"available": False}
        def reset(self):
            pass
        def get_last_experience(self):
            return None
        def get_history(self):
            return []
    ZOO = type('_DummyZOO', (), {'GEONZOOAnalyzer': _DummyZOO})()
    log_zoo = logging.getLogger("GEON_ZOO_INTEGRATION")
    log_zoo.warning("⚠️ GEON ZOO (86.5) NIE DOSTĘPNY – używana pusta implementacja")

# =============================================================================
# PRÓBA IMPORTOWANIA MODUŁU GRON (warstwa 86.6)
# =============================================================================

try:
    from kombajn_core import geon_gron_antyskret_v1_0 as GRON
    GRON_AVAILABLE = True
    log_gron = logging.getLogger("GEON_GRON_INTEGRATION")
    log_gron.info("🐉 GEON GRON (86.6) zintegrowany z warstwą 87")
except ImportError:
    GRON_AVAILABLE = False
    # Fallback – pusta klasa symulująca GRON
    class _DummyGRON:
        def __init__(self, config=None):
            self.last_status = "OK"
            self.tick_counter = 0
        def evaluate(self, wejscie, **kwargs):
            return {
                "status": "OK",
                "rekomendacja": "OBSERWACJA",
                "akcja_systemowa": {},
                "telemetry": {"anomaly": 0.0, "tick": self.tick_counter}
            }
        @property
        def tick_counter(self):
            return 0
    GRON = type('_DummyGRON', (), {'GronAntySkret': _DummyGRON})()
    log_gron = logging.getLogger("GEON_GRON_INTEGRATION")
    log_gron.warning("⚠️ GEON GRON (86.6) NIE DOSTĘPNY – używana pusta implementacja")

# =============================================================================
# WERSJA I STAŁE SYSTEMOWE
# =============================================================================

VERSION = "GEON_AI_ANALYTICS_v2.2-FINAL"
FRACTAL_SIGNATURE = "[GEON::AI::ANALYTICS::v2.2::ZOO_GRON_INTEGRATED]"
VIBE = 168
HASLO = "1-6-8. ∞. AI! 🧠"
DEWIZA = "Ex Analysi, Praevidentia. Ex Fractali, Veritas. Ex Observatione, Claritas. Ex Vigilantia, Securitas."

TENSOR_DIM = 45
VECTOR_DIM = 9  # AFC-9 wymiar
MEMORY_LIMIT = 512
ANOMALY_HISTORY_WINDOW = 32
ANOMALY_THRESHOLD_DEFAULT = 0.35
ANOMALY_WEIGHT_ANGULAR = 0.6
ANOMALY_WEIGHT_ENERGY = 0.4

# =============================================================================
# LOGOWANIE SYSTEMOWE
# =============================================================================

logger = logging.getLogger("GEON_AI_ANALYTICS")
logger.setLevel(logging.INFO)
if not logger.handlers:
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter('🧠 [AI] %(message)s'))
    logger.addHandler(handler)

def log(msg: str, level: str = "INFO") -> None:
    if level == "WARN":
        logger.warning(msg)
    elif level == "ERROR":
        logger.error(msg)
    else:
        logger.info(msg)

def clamp(x: float, lo: float, hi: float) -> float:
    return max(lo, min(hi, x))

def generate_context_hash(context: Dict[str, Any]) -> str:
    filtered_context = {k: v for k, v in context.items() 
                        if k not in ["timestamp", "request_id", "nonce"]}
    context_str = json.dumps(filtered_context, sort_keys=True, ensure_ascii=False, default=str)
    return hashlib.sha256(context_str.encode("utf-8")).hexdigest()

# =============================================================================
# KRONIKI SAMAELA I EGREGOR (THREAD-SAFE LEDGER)
# =============================================================================

class SamaelHeilong:
    @staticmethod
    def certyfikuj_tensor(action: str) -> str:
        timestamp = datetime.now().isoformat()
        payload = f"{timestamp}-{action}-1-6-8. ∞. SIEMA!"
        h = hashlib.sha256(payload.encode("utf-8")).hexdigest()[:16].upper()
        return f"🔒 [SAMAELSEALSIG-{h}-AI-168]"

    @staticmethod
    def log_event(event_type: str, payload: Dict[str, Any]) -> None:
        ts = datetime.now().isoformat()
        log(f"[KRONIKI SAMAELA] {ts} | {event_type} -> {payload}", "INFO")

class Egregor:
    _ledger: Deque[Dict[str, Any]] = deque(maxlen=MEMORY_LIMIT)
    _lock: threading.Lock = threading.Lock()
    
    @classmethod
    def commit(cls, entry: Dict[str, Any], node_id: str) -> None:
        entry["node_id"] = node_id
        entry["timestamp"] = datetime.now().isoformat()
        with cls._lock:
            cls._ledger.append(entry)
    
    @classmethod
    def query(cls, type_filter: Optional[str] = None) -> List[Dict[str, Any]]:
        with cls._lock:
            snapshot = list(cls._ledger)
        if type_filter:
            return [e for e in snapshot if e.get("type") == type_filter]
        return snapshot

# =============================================================================
# 1. AFC-9 – FILTR PRAWDY (deterministyczny, fraktalny)
# =============================================================================

def afc9(D1: List[float], D2: List[float], D3: List[float], D4: List[float]) -> List[float]:
    """
    AFC-9 – filtr prawdy.
    Wejście: 4 wektory po 9 elementów
    Wyjście: wektor D9 (9 elementów)
    """
    for vec in (D1, D2, D3, D4):
        if len(vec) != VECTOR_DIM:
            raise ValueError(f"Każdy wektor musi mieć dokładnie {VECTOR_DIM} elementów")
    
    D5 = [(D1[i] + D2[i] + D3[i] + D4[i]) / 4.0 for i in range(VECTOR_DIM)]
    D6 = [(D1[i] + D3[i] + D5[i]) / 3.0 for i in range(VECTOR_DIM)]
    D7 = [(D2[i] + D4[i] + D6[i]) / 3.0 for i in range(VECTOR_DIM)]
    D8 = [(D1[i] + D3[i] + D5[i] + D7[i]) / 4.0 for i in range(VECTOR_DIM)]
    D9 = [(D1[i] + D8[i]) / 2.0 for i in range(VECTOR_DIM)]
    return D9

# =============================================================================
# 2. CORE_ACCESS_GATE – MAPA PRAWDY
# =============================================================================

class CORE_ACCESS_GATE:
    """Mapa prawdy – weryfikacja dostępu do rdzenia."""
    
    def __init__(self):
        self.layers = [
            ["MAIN_ENTRANCE", "FALSE_PATH", "FALSE_PATH", "FALSE_PATH"],
            ["FALSE_PATH", "FALSE_PATH", "TRUE_VECTOR", "FALSE_PATH"],
            ["FALSE_PATH", "FALSE_PATH", "FALSE_PATH", "FALSE_PATH"],
        ]
        self.passed_layers = 0

    def step(self, segment_choice: int) -> bool:
        if self.passed_layers >= len(self.layers):
            return False
        seg_type = self.layers[self.passed_layers][segment_choice]
        if seg_type == "FALSE_PATH":
            return False
        self.passed_layers += 1
        return True

    def reached_core(self) -> bool:
        return self.passed_layers == len(self.layers)

    def reset(self) -> None:
        self.passed_layers = 0

# =============================================================================
# 3. GEONCORESTATE – PAMIĘĆ RDZENIA (historia + stabilność)
# =============================================================================

class GeonCoreState:
    """Pamięć stanu rdzenia AFC."""
    
    def __init__(self, history_size: int = 32):
        self.last_vector: Optional[List[float]] = None
        self.history = deque(maxlen=history_size)
        self.tick: int = 0

    def update(self, vector: List[float]) -> None:
        self.last_vector = vector.copy()
        self.history.append({"tick": self.tick, "vector": vector.copy()})
        self.tick += 1

    def stability_score(self) -> float:
        if len(self.history) < 2:
            return 1.0
        diffs = []
        prev = self.history[0]["vector"]
        for h in list(self.history)[1:]:
            cur = h["vector"]
            diff = sum(abs(a - b) for a, b in zip(prev, cur)) / len(cur)
            diffs.append(diff)
            prev = cur
        return 1.0 / (1.0 + sum(diffs) / len(diffs))

    def get_history(self) -> List[Dict[str, Any]]:
        return list(self.history)

# =============================================================================
# 4. GEONCOREDECISION_LAYER – WARSTWA DECYZYJNA
# =============================================================================

class GeonCoreDecisionLayer:
    """Warstwa decyzyjna: STABILIZE, EXPLORE, ALERT."""
    
    def __init__(self, stability_threshold: float = 0.7):
        self.stability_threshold = stability_threshold

    def decide(self, core_output: Dict[str, Any]) -> Dict[str, Any]:
        if core_output.get("status") != "TRUE":
            return {"mode": "IGNORE", "reason": "NO_CORE_ACCESS", "raw": core_output}
        
        vector = core_output.get("vector", [])
        stability = core_output.get("stability", 1.0)
        energy = sum(abs(x) for x in vector) / len(vector) if vector else 0.0
        
        if stability >= self.stability_threshold and energy < 3.0:
            mode = "STABILIZE"
        elif stability >= self.stability_threshold and energy >= 3.0:
            mode = "EXPLORE"
        else:
            mode = "ALERT"
        
        return {"mode": mode, "stability": stability, "energy": energy, "vector": vector}

# =============================================================================
# 5. GEONCOREPREDICTOR – PREDYKCJA I ANOMALIE
# =============================================================================

class GeonCorePredictor:
    """Predykcja i wykrywanie anomalii."""
    
    def __init__(self, window: int = 5, anomaly_threshold: float = 1.5):
        self.window = window
        self.anomaly_threshold = anomaly_threshold

    def predict(self, history: deque) -> Optional[List[float]]:
        if len(history) < self.window:
            return None
        vectors = [h["vector"] for h in list(history)[-self.window:]]
        dim = len(vectors[0])
        return [sum(v[i] for v in vectors) / self.window for i in range(dim)]

    def anomaly(self, vector: List[float], predicted: List[float]) -> bool:
        diff = sum(abs(a - b) for a, b in zip(vector, predicted)) / len(vector)
        return diff > self.anomaly_threshold

# =============================================================================
# 6. GEONCOREPOLICY_LAYER – POLITYKA SYSTEMOWA
# =============================================================================

class GeonCorePolicyLayer:
    """Meta-sterowanie zachowaniem rdzenia."""
    
    def __init__(self):
        self.mode_history = deque(maxlen=16)

    def apply_policy(self, decision: Dict[str, Any], anomaly: bool) -> Dict[str, Any]:
        mode = decision.get("mode", "IGNORE")
        if anomaly:
            final_mode = "HARD_ALERT"
        elif mode == "ALERT":
            final_mode = "SOFT_ALERT"
        elif mode == "EXPLORE":
            final_mode = "EXPLORE_EXTENDED"
        elif mode == "STABILIZE":
            final_mode = "MAINTAIN"
        else:
            final_mode = "IGNORE"
        
        self.mode_history.append(final_mode)
        return {"final_mode": final_mode, "history": list(self.mode_history)}

# =============================================================================
# 7. GEONCORELOOP – PĘTLA W CZASIE RZECZYWISTYM
# =============================================================================

class GeonCoreLoop:
    """Pętla AFC w czasie rzeczywistym (krok po kroku)."""
    
    def __init__(self, history_size: int = 32):
        self.state = GeonCoreState(history_size=history_size)

    def process_step(self, D1: List[float], D2: List[float], D3: List[float], D4: List[float]) -> Dict[str, Any]:
        D9 = afc9(D1, D2, D3, D4)
        gate = CORE_ACCESS_GATE()
        choices = [int(abs(x)) % 4 for x in D9[:3]]
        
        for choice in choices:
            if not gate.step(choice):
                return {"status": "FALSE", "stage": "CORE_GATE", "vector": D9, "choice": choice}
        
        if gate.reached_core():
            self.state.update(D9)
            return {
                "status": "TRUE",
                "stage": "CORE",
                "vector": D9,
                "stability": self.state.stability_score()
            }
        
        return {"status": "INCOMPLETE", "stage": "CORE_GATE", "vector": D9}

# =============================================================================
# 8. GEONCORESYSTEMV2 – INTEGRACJA AFC
# =============================================================================

class GeonCoreSystemV2:
    """Pełna integracja AFC-9 z pamięcią, predykcją, polityką."""
    
    def __init__(self, history_size: int = 32, stability_threshold: float = 0.7,
                 window: int = 5, anomaly_threshold: float = 1.5):
        self.loop = GeonCoreLoop(history_size=history_size)
        self.decision = GeonCoreDecisionLayer(stability_threshold=stability_threshold)
        self.predictor = GeonCorePredictor(window=window, anomaly_threshold=anomaly_threshold)
        self.policy = GeonCorePolicyLayer()

    def tick(self, D1: List[float], D2: List[float], D3: List[float], D4: List[float]) -> Dict[str, Any]:
        core_out = self.loop.process_step(D1, D2, D3, D4)
        decision = self.decision.decide(core_out)
        predicted = self.predictor.predict(self.loop.state.history)
        anomaly = False
        if predicted is not None and core_out.get("status") == "TRUE":
            anomaly = self.predictor.anomaly(core_out["vector"], predicted)
        policy = self.policy.apply_policy(decision, anomaly)
        return {
            "core": core_out,
            "decision": decision,
            "predicted": predicted,
            "anomaly": anomaly,
            "policy": policy
        }

    def get_state(self) -> GeonCoreState:
        return self.loop.state

# =============================================================================
# 9. GŁÓWNY MODUŁ: GEON_AI_ANALYTICS (ROZSZERZONY O AFC + ZOO + GRON)
# =============================================================================

class GeonAIAnalytics:
    """
    🧠 GEON_AI_ANALYTICS – Zoptymalizowany silnik analityczny dla tensorów 45D.
    ROZSZERZONY o AFC-9, pamięć stanu, pętlę, predykcję, politykę, ZOO oraz GRON.
    """
    
    def __init__(self, config: Optional[Dict[str, Any]] = None):
        self.config = config or {}
        self.memory_limit = self.config.get("memory_limit", MEMORY_LIMIT)
        self.window = self.config.get("window", ANOMALY_HISTORY_WINDOW)
        self.anomaly_threshold = self.config.get("anomaly_threshold", ANOMALY_THRESHOLD_DEFAULT)
        self.alpha = self.config.get("alpha", 0.6)
        
        # ===== ORYGINALNA PAMIĘĆ =====
        self._memory: Deque[List[float]] = deque(maxlen=self.memory_limit)
        self._lock: threading.Lock = threading.Lock()
        self._anomaly_history: Deque[float] = deque(maxlen=20)
        
        # ===== NOWY SUBSYSTEM AFC =====
        history_size = self.config.get("afc_history_size", 32)
        stability_threshold = self.config.get("stability_threshold", 0.7)
        window_pred = self.config.get("prediction_window", 5)
        anomaly_threshold_pred = self.config.get("anomaly_threshold_pred", 1.5)
        
        self.afc_system = GeonCoreSystemV2(
            history_size=history_size,
            stability_threshold=stability_threshold,
            window=window_pred,
            anomaly_threshold=anomaly_threshold_pred
        )
        
        # ===== SUBSYSTEM ZOO =====
        self.zoo_enabled = self.config.get("zoo_enabled", ZOO_AVAILABLE)
        if self.zoo_enabled and ZOO_AVAILABLE:
            try:
                self.zoo = ZOO.GEONZOOAnalyzer(config=self.config.get("zoo_config", {}))
                log("🦁 GEON ZOO (86.5) AKTYWNY w warstwie 87")
            except Exception as e:
                log(f"⚠️ Błąd inicjalizacji ZOO: {e}", "WARN")
                self.zoo = _DummyZOO()
                self.zoo_enabled = False
        else:
            self.zoo = _DummyZOO()
            self.zoo_enabled = False
            if not ZOO_AVAILABLE:
                log("⚠️ GEON ZOO NIE DOSTĘPNY – tryb offline", "WARN")
        
        # ===== SUBSYSTEM GRON =====
        self.gron_enabled = self.config.get("gron_enabled", GRON_AVAILABLE)
        if self.gron_enabled and GRON_AVAILABLE:
            try:
                from kombajn_core import geon_gron_antyskret_v1_0 as GRON_MODULE
                self.gron = GRON_MODULE.GronAntySkret(config=self.config.get("gron_config", {}))
                log("🐉 GEON GRON (86.6) AKTYWNY w warstwie 87")
            except Exception as e:
                log(f"⚠️ Błąd inicjalizacji GRON: {e}", "WARN")
                self.gron = _DummyGRON()
                self.gron_enabled = False
        else:
            self.gron = _DummyGRON()
            self.gron_enabled = False
            if not GRON_AVAILABLE:
                log("⚠️ GEON GRON NIE DOSTĘPNY – tryb offline", "WARN")
        
        self.kroniki = SamaelHeilong
        self.egregor = Egregor
        
        log(f"🐉 {VERSION} aktywowany | {FRACTAL_SIGNATURE}")
        log(f"   WYMIAR: {TENSOR_DIM}D | AFC: AKTYWNY | ZOO: {'AKTYWNY' if self.zoo_enabled else 'WYŁĄCZONY'} | GRON: {'AKTYWNY' if self.gron_enabled else 'WYŁĄCZONY'}")
        log(f"   PAMIĘĆ: {self.memory_limit} | ALPHA: {self.alpha}")

    # ========================================================================
    # ORYGINALNE METODY (ZACHOWANE BEZ ZMIAN)
    # ========================================================================

    def ingest(self, tensor: List[float]) -> None:
        if len(tensor) != TENSOR_DIM:
            raise ValueError(f"Tensor musi mieć dokładnie {TENSOR_DIM} wymiarów")
        with self._lock:
            self._memory.append(list(tensor))
            self.kroniki.log_event("TENSOR_INGEST", {"dim": len(tensor), "size": len(self._memory)})

    def get_history(self, n: Optional[int] = None) -> List[List[float]]:
        with self._lock:
            snapshot = list(self._memory)
        if n is not None and n > 0:
            return snapshot[-n:]
        return snapshot

    def reset(self) -> None:
        with self._lock:
            self._memory.clear()
            self._anomaly_history.clear()
        if self.zoo_enabled:
            self.zoo.reset()
        self.kroniki.log_event("MEMORY_RESET", {"status": "CLEARED"})

    def memory_size(self) -> int:
        with self._lock:
            return len(self._memory)

    @staticmethod
    def similarity(a: List[float], b: List[float]) -> float:
        dot = sum(x * y for x, y in zip(a, b))
        na = math.sqrt(sum(x * x for x in a))
        nb = math.sqrt(sum(y * y for y in b))
        if na < 1e-9 or nb < 1e-9:
            return 1.0 if (na < 1e-9 and nb < 1e-9) else 0.0
        return clamp(dot / (na * nb), -1.0, 1.0)

    def last_state(self) -> Dict[str, float]:
        with self._lock:
            if not self._memory:
                return {"energy": 0.0, "variance": 0.0, "mean": 0.0}
            t = self._memory[-1]
        n = len(t)
        mean = sum(t) / n
        energy = sum(abs(x) for x in t) / n
        variance = sum((x - mean) ** 2 for x in t) / n
        return {"energy": energy, "variance": variance, "mean": mean}

    def predict_next(self) -> List[float]:
        with self._lock:
            if not self._memory:
                return [0.0] * TENSOR_DIM
            if len(self._memory) < 2:
                return list(self._memory[-1])
            t_prev = list(self._memory[-2])
            t_curr = list(self._memory[-1])
        
        trend = sum(c - p for p, c in zip(t_prev, t_curr)) / TENSOR_DIM
        effective_alpha = clamp(self.alpha + trend * 0.5, 0.1, 0.95)
        
        predicted = []
        for p, c in zip(t_prev, t_curr):
            next_val = c + effective_alpha * (c - p)
            predicted.append(clamp(next_val, 0.0, 1.5))
        
        return predicted

    def anomaly_score(self, tensor: List[float]) -> float:
        if not self.memory_size() or len(tensor) != TENSOR_DIM:
            return 0.0
        
        with self._lock:
            recent = list(self._memory)[-self.window:]
            recent_anomalies = list(self._anomaly_history)[-10:]

        sims = [self.similarity(tensor, h) for h in recent]
        angular_anomaly = 1.0 - (max(sims) if sims else 1.0)

        curr_energy = sum(abs(x) for x in tensor) / TENSOR_DIM
        energies = [sum(abs(x) for x in h) / TENSOR_DIM for h in recent]
        avg_energy = sum(energies) / len(energies) if energies else 0.0
        var_energy = sum((e - avg_energy) ** 2 for e in energies) / len(energies) if energies else 1.0
        std_energy = math.sqrt(var_energy) if var_energy > 1e-9 else 1.0
        
        energy_zscore = abs(curr_energy - avg_energy) / std_energy if std_energy > 1e-9 else 0.0
        energy_anomaly = clamp(energy_zscore / 3.0, 0.0, 1.0)

        anomaly_rate = sum(recent_anomalies) / len(recent_anomalies) if recent_anomalies else 0.0
        weight_angular = ANOMALY_WEIGHT_ANGULAR * (1.0 - 0.3 * anomaly_rate)
        weight_energy = ANOMALY_WEIGHT_ENERGY * (1.0 + 0.2 * anomaly_rate)
        total_weight = weight_angular + weight_energy
        
        weight_angular /= total_weight if total_weight > 0 else 1.0
        weight_energy /= total_weight if total_weight > 0 else 1.0

        total_anomaly = clamp(weight_angular * angular_anomaly + weight_energy * energy_anomaly, 0.0, 1.0)

        with self._lock:
            self._anomaly_history.append(1.0 if total_anomaly > self.anomaly_threshold else 0.0)

        return total_anomaly

    # ========================================================================
    # METODY AFC INTEGRATION (ZACHOWANE)
    # ========================================================================

    def afc_transform(self, D1: List[float], D2: List[float], D3: List[float], D4: List[float]) -> List[float]:
        """Przetwarza 4 wektory 9D przez AFC-9."""
        return afc9(D1, D2, D3, D4)

    def core_gate_sequence(self, vector_9d: List[float]) -> Dict[str, Any]:
        """Przepuszcza wektor przez CORE_ACCESS_GATE."""
        gate = CORE_ACCESS_GATE()
        choices = [int(abs(x)) % 4 for x in vector_9d[:3]]
        for choice in choices:
            if not gate.step(choice):
                return {"status": "FALSE", "choice": choice}
        return {"status": "TRUE" if gate.reached_core() else "INCOMPLETE"}

    def afc_cycle(self, D1: List[float], D2: List[float], D3: List[float], D4: List[float]) -> Dict[str, Any]:
        """Wykonuje pełny cykl AFC – transformacja + gate + decyzja + polityka."""
        return self.afc_system.tick(D1, D2, D3, D4)

    def get_afc_state(self) -> Dict[str, Any]:
        """Zwraca stan rdzenia AFC."""
        state = self.afc_system.get_state()
        return {
            "tick": state.tick,
            "stability": state.stability_score(),
            "history_length": len(state.history),
            "last_vector": state.last_vector
        }

    def get_afc_decision(self) -> Dict[str, Any]:
        """Zwraca ostatnią decyzję AFC."""
        if not hasattr(self, '_last_afc_result'):
            return {"mode": "NO_DATA"}
        return self._last_afc_result.get("decision", {"mode": "NO_DATA"})

    def get_afc_policy(self) -> Dict[str, Any]:
        """Zwraca ostatnią politykę AFC."""
        if not hasattr(self, '_last_afc_result'):
            return {"final_mode": "NO_DATA"}
        return self._last_afc_result.get("policy", {"final_mode": "NO_DATA"})

    def analyze_with_afc(self, tensor_45d: List[float], 
                          log_to_egregor: bool = True) -> Dict[str, Any]:
        """
        Pełna analiza z wykorzystaniem AFC.
        Dzieli tensor 45D na 5 wektorów 9D i przepuszcza przez AFC.
        """
        if len(tensor_45d) != TENSOR_DIM:
            raise ValueError(f"Tensor musi mieć dokładnie {TENSOR_DIM} wymiarów")
        
        # Podział na 5 wektorów 9D
        segments = [tensor_45d[i:i+VECTOR_DIM] for i in range(0, TENSOR_DIM, VECTOR_DIM)]
        
        # AFC na pierwszych 4 segmentach
        afc_result = self.afc_cycle(segments[0], segments[1], segments[2], segments[3])
        self._last_afc_result = afc_result
        
        # Oryginalna analiza
        analysis = self.analyze(tensor_45d, log_to_egregor=False)
        
        # Łączenie wyników
        result = {
            "status": "ANALYSIS_WITH_AFC_COMPLETE",
            "analysis": analysis,
            "afc": {
                "core_status": afc_result["core"]["status"],
                "decision": afc_result["decision"]["mode"],
                "policy": afc_result["policy"]["final_mode"],
                "stability": afc_result["core"].get("stability", 0.0),
                "anomaly": afc_result["anomaly"]
            },
            "segments": [s[:5] for s in segments],  # tylko podgląd
            "certificate": self.kroniki.certyfikuj_tensor(f"AFC_ANALYSIS_{hash(str(tensor_45d[:5]))}")
        }
        
        if log_to_egregor:
            entry = {
                "type": "AFC_ANALYSIS",
                "decision": afc_result["decision"]["mode"],
                "policy": afc_result["policy"]["final_mode"],
                "stability": afc_result["core"].get("stability", 0.0)
            }
            self.egregor.commit(entry, node_id="GEON_AI_ANALYTICS_AFC")
        
        return result

    # ========================================================================
    # METODY ZOO INTEGRATION (ZACHOWANE)
    # ========================================================================

    def analyze_with_zoo(self, tensor_45d: List[float],
                         ctx_scene: Dict[str, Any],
                         actors: List[Dict[str, Any]],
                         signals: List[str],
                         log_to_egregor: bool = True) -> Dict[str, Any]:
        """
        Pełna analiza z wykorzystaniem ZOO (86.5).
        Łączy analizę tensora 45D z detekcją absurdów i ról.
        """
        result = self.analyze(tensor_45d, log_to_egregor=False)
        
        self_state = {"energy": result.get("energy", 0.5)}
        zoo_result = self.zoo.analyze(ctx_scene, actors, signals, self_state)
        
        result["zoo"] = zoo_result
        result["zoo_risk"] = zoo_result.get("vibe_risk_score", 0.0)
        result["absurd_score"] = zoo_result.get("absurd_score", 0.0)
        result["roles_map"] = zoo_result.get("roles_map", {})
        result["action_hint"] = zoo_result.get("action_hint", "normalna_interakcja")
        result["action_priority"] = zoo_result.get("action_priority", 3)
        result["experience_chunk"] = zoo_result.get("experience_chunk", {})
        
        if zoo_result.get("vibe_risk_score", 0.0) > 0.8:
            result["status"] = "ZOO_ALERT"
            result["anomaly_score"] = max(result.get("anomaly_score", 0.0), 0.7)
        elif zoo_result.get("vibe_risk_score", 0.0) > 0.5:
            result["status"] = "ZOO_CAUTION"
        
        result["zoo_certificate"] = self.kroniki.certyfikuj_tensor(f"ZOO_ANALYSIS_{hash(str(tensor_45d[:5]))}")
        
        if log_to_egregor and zoo_result.get("vibe_risk_score", 0.0) > 0.7:
            entry = {
                "type": "ZOO_ANALYSIS_ALERT",
                "absurd_score": zoo_result.get("absurd_score", 0.0),
                "vibe_risk_score": zoo_result.get("vibe_risk_score", 0.0),
                "roles": zoo_result.get("roles_map", {}),
                "action": zoo_result.get("action_hint", "unknown")
            }
            self.egregor.commit(entry, node_id="GEON_AI_ANALYTICS_ZOO")
        
        return result

    def get_zoo_status(self) -> Dict[str, Any]:
        if self.zoo_enabled:
            return self.zoo.get_status()
        return {"available": False, "enabled": self.zoo_enabled}

    def get_zoo_last_experience(self) -> Optional[Dict[str, Any]]:
        if self.zoo_enabled:
            return self.zoo.get_last_experience()
        return None

    def get_zoo_history(self) -> List[Dict[str, Any]]:
        if self.zoo_enabled:
            return self.zoo.get_history()
        return []

    # ========================================================================
    # NOWE METODY – GRON INTEGRATION
    # ========================================================================

    def analyze_with_gron(self, tensor_45d: List[float],
                          wejscie: Dict[str, float],
                          uderza_w_suwerennosc: bool = False,
                          harmonia_triady: float = 1.0,
                          ciaglosc_nacisku: float = 0.0,
                          pakiet: Optional[Dict[str, Any]] = None,
                          log_to_egregor: bool = True) -> Dict[str, Any]:
        """
        Pełna analiza z wykorzystaniem GRON (86.6).
        Łączy analizę tensora 45D z detekcją manipulacji, presji, anty-skret.
        
        Args:
            tensor_45d: Tensor 45D do analizy
            wejscie: Słownik z kluczami: narracja, presja, zmiany, konflikty, zasady
            uderza_w_suwerennosc: Czy manipulacja dotyka suwerenności
            harmonia_triady: Poziom harmonii (0-1)
            ciaglosc_nacisku: Ciągłość nacisku (0-1)
            pakiet: Opcjonalny pakiet dla detekcji Syzyfa
            log_to_egregor: Czy logować do Egregora
        """
        # 1. Oryginalna analiza tensora
        result = self.analyze(tensor_45d, log_to_egregor=False)
        
        # 2. Analiza GRON
        if self.gron_enabled and GRON_AVAILABLE:
            try:
                from kombajn_core import geon_gron_antyskret_v1_0 as GRON_MODULE
                wejscie_obj = GRON_MODULE.WejscieAntySkret(
                    narracja=wejscie.get("narracja", 0.0),
                    presja=wejscie.get("presja", 0.0),
                    zmiany=wejscie.get("zmiany", 0.0),
                    konflikty=wejscie.get("konflikty", 0.0),
                    zasady=wejscie.get("zasady", 0.0)
                )
                gron_result = self.gron.evaluate(
                    wejscie_obj,
                    uderza_w_suwerennosc=uderza_w_suwerennosc,
                    harmonia_triady=harmonia_triady,
                    ciaglosc_nacisku=ciaglosc_nacisku,
                    pakiet=pakiet
                )
            except Exception as e:
                log(f"⚠️ Błąd wykonania GRON: {e}", "WARN")
                gron_result = {"status": "OK", "rekomendacja": "OBSERWACJA", "akcja_systemowa": {}, "telemetry": {"anomaly": 0.0}}
        else:
            gron_result = {"status": "OK", "rekomendacja": "OBSERWACJA", "akcja_systemowa": {}, "telemetry": {"anomaly": 0.0}}
        
        # 3. Łączenie wyników
        result["gron"] = gron_result
        result["gron_status"] = gron_result.get("status", "OK")
        result["gron_anomaly"] = gron_result.get("telemetry", {}).get("anomaly", 0.0)
        result["gron_actions"] = gron_result.get("akcja_systemowa", {})
        result["gron_rekomendacja"] = gron_result.get("rekomendacja", "OBSERWACJA")
        result["gron_threshold"] = gron_result.get("telemetry", {}).get("threshold", 0.6)
        
        # 4. Status GRON_ALERT
        if gron_result.get("status") == "ALARM":
            result["status"] = "GRON_ALERT"
            result["anomaly_score"] = max(result.get("anomaly_score", 0.0), 0.8)
        
        # 5. Certyfikat
        result["gron_certificate"] = self.kroniki.certyfikuj_tensor(f"GRON_ANALYSIS_{hash(str(tensor_45d[:5]))}")
        
        # 6. Logowanie do Egregora
        if log_to_egregor and gron_result.get("status") == "ALARM":
            entry = {
                "type": "GRON_ALERT",
                "anomaly": result["gron_anomaly"],
                "actions": result["gron_actions"],
                "rekomendacja": result["gron_rekomendacja"],
                "threshold": result["gron_threshold"]
            }
            self.egregor.commit(entry, node_id="GEON_AI_ANALYTICS_GRON")
        
        # 7. Zapamiętaj ostatni wynik GRON dla mostu
        self._last_gron_result = gron_result
        
        log(f"🐉 GRON: status={gron_result.get('status')}, anomaly={result['gron_anomaly']:.2f}, actions={len(result['gron_actions'])}")
        
        return result

    def get_gron_status(self) -> Dict[str, Any]:
        """Zwraca status modułu GRON."""
        if self.gron_enabled and hasattr(self.gron, 'last_status'):
            return {
                "available": True,
                "enabled": self.gron_enabled,
                "status": self.gron.last_status,
                "tick": getattr(self.gron, 'tick_counter', 0)
            }
        return {"available": False, "enabled": self.gron_enabled, "status": "OK"}

    def get_gron_last_result(self) -> Optional[Dict[str, Any]]:
        """Zwraca ostatni wynik GRON."""
        return getattr(self, '_last_gron_result', None)

    # ========================================================================
    # ORYGINALNA METODA analyze() (ZACHOWANA)
    # ========================================================================

    def analyze(self, tensor: List[float], log_to_egregor: bool = True) -> Dict[str, Any]:
        """
        Oryginalna analiza tensorów 45D (zachowana dla kompatybilności).
        """
        self.ingest(tensor)
        
        state = self.last_state()
        anomaly = self.anomaly_score(tensor)
        predicted = self.predict_next()
        
        tensor_digest = hashlib.sha256(str(tensor[:5]).encode()).hexdigest()[:8]
        cert = self.kroniki.certyfikuj_tensor(f"ANALYSIS_{tensor_digest}")
        
        result = {
            "status": "ANALYSIS_COMPLETE",
            "energy": round(state["energy"], 6),
            "variance": round(state["variance"], 6),
            "mean": round(state["mean"], 6),
            "anomaly_score": round(anomaly, 6),
            "predicted_next": [round(x, 4) for x in predicted[:5]],
            "certificate": cert,
            "memory_size": self.memory_size()
        }
        
        if log_to_egregor:
            if anomaly > self.anomaly_threshold:
                entry = {
                    "type": "AI_ANALYSIS_ANOMALY",
                    "tensor_hash": generate_context_hash({"tensor": tensor[:5]}),
                    "energy": state["energy"],
                    "variance": state["variance"],
                    "anomaly": anomaly,
                    "certificate": cert
                }
                self.egregor.commit(entry, node_id="GEON_AI_ANALYTICS")
            elif self.memory_size() % 10 == 0:
                entry = {
                    "type": "AI_ANALYSIS_NORMAL",
                    "tensor_hash": generate_context_hash({"tensor": tensor[:5]}),
                    "energy": state["energy"],
                    "anomaly": anomaly
                }
                self.egregor.commit(entry, node_id="GEON_AI_ANALYTICS")
        
        return result

    def get_status(self) -> Dict[str, Any]:
        return {
            "system": "GEON_AI_ANALYTICS",
            "version": VERSION,
            "signature": FRACTAL_SIGNATURE,
            "vibe": VIBE,
            "memory_size": self.memory_size(),
            "memory_limit": self.memory_limit,
            "tensor_dim": TENSOR_DIM,
            "window": self.window,
            "alpha": self.alpha,
            "anomaly_threshold": self.anomaly_threshold,
            "afc": {
                "active": True,
                "history_size": len(self.afc_system.get_state().history),
                "stability": self.afc_system.get_state().stability_score()
            },
            "zoo": {
                "active": self.zoo_enabled,
                "history_size": len(self.get_zoo_history())
            },
            "gron": {
                "active": self.gron_enabled,
                "status": self.get_gron_status().get("status", "OK")
            }
        }

# =============================================================================
# MOST INTEGRACYJNY — AI_ANALYTICS_BRIDGE (ROZSZERZONY O ZOO + GRON)
# =============================================================================

class AIAnalyticsBridge:
    """
    Most integracyjny dla GEON_AI_ANALYTICS.
    Zachowuje pełną kompatybilność z istniejącymi mostami.
    ROZSZERZONY o metody ZOO i GRON.
    """
    
    def __init__(self, ai: GeonAIAnalytics):
        self.ai = ai

    # ===== ORYGINALNE METODY (ZACHOWANE) =====
    
    def get_archetype_context(self) -> Dict[str, Any]:
        status = self.ai.get_status()
        return {
            "tryb": VERSION,
            "pamięć": status["memory_size"],
            "limit": status["memory_limit"],
            "wymiar": status["tensor_dim"],
            "anomaly_threshold": status["anomaly_threshold"],
            "afc_active": status["afc"]["active"],
            "zoo_active": status["zoo"]["active"],
            "gron_active": status["gron"]["active"]
        }

    def get_autopilot_state(self) -> Dict[str, Any]:
        state = self.ai.last_state()
        afc_state = self.ai.get_afc_state()
        zoo_last = self.ai.get_zoo_last_experience()
        gron_last = self.ai.get_gron_last_result()
        return {
            "mode": VERSION,
            "energy": round(state["energy"], 6),
            "variance": round(state["variance"], 6),
            "mean": round(state["mean"], 6),
            "ai_ready": True,
            "memory_usage": f"{self.ai.memory_size()}/{self.ai.memory_limit}",
            "afc_stability": afc_state.get("stability", 0.0),
            "afc_tick": afc_state.get("tick", 0),
            "zoo_risk": zoo_last.get("vibe_risk_score", 0.0) if zoo_last else 0.0,
            "zoo_absurd": zoo_last.get("absurd_score", 0.0) if zoo_last else 0.0,
            "gron_status": gron_last.get("status", "OK") if gron_last else "OK",
            "gron_anomaly": gron_last.get("telemetry", {}).get("anomaly", 0.0) if gron_last else 0.0
        }

    def get_governor_context(self) -> Dict[str, Any]:
        afc_decision = self.ai.get_afc_decision()
        zoo_last = self.ai.get_zoo_last_experience()
        gron_last = self.ai.get_gron_last_result()
        return {
            "intent": "AI_ANALYTICS_ADAPTIVE",
            "confidence": 0.98,
            "entropy": 0.02,
            "ai_ready": True,
            "afc_mode": afc_decision.get("mode", "NO_DATA"),
            "zoo_risk": zoo_last.get("vibe_risk_score", 0.0) if zoo_last else 0.0,
            "zoo_action": zoo_last.get("action", "normalna_interakcja") if zoo_last else "unknown",
            "gron_status": gron_last.get("status", "OK") if gron_last else "OK",
            "gron_rekomendacja": gron_last.get("rekomendacja", "OBSERWACJA") if gron_last else "OBSERWACJA"
        }

    def get_trio_state(self) -> Dict[str, str]:
        return {
            "ISKRA": "AKTYWNA",
            "PIECZĘĆ": "AKTYWNA",
            "PERFEKCJA": "AKTYWNA",
            "tryb": VERSION,
            "ai": "AKTYWNY_ADAPTIV",
            "afc": "AKTYWNY",
            "zoo": "AKTYWNY" if self.ai.zoo_enabled else "WYŁĄCZONY",
            "gron": "AKTYWNY" if self.ai.gron_enabled else "WYŁĄCZONY"
        }

    def get_narrative_fragments(self, n: int = 5) -> List[Dict[str, Any]]:
        history = self.ai.get_history(n)
        fragments = []
        for i, tensor in enumerate(history):
            energy = sum(abs(x) for x in tensor) / TENSOR_DIM
            fragments.append({
                "source": VERSION,
                "content": f"Tensor {i}: energia={energy:.3f}",
                "energy": round(energy, 4),
                "timestamp": datetime.now().isoformat()
            })
        
        afc_state = self.ai.get_afc_state()
        fragments.append({
            "source": "AFC_CORE",
            "content": f"AFC: stabilność={afc_state.get('stability', 0):.3f}, tick={afc_state.get('tick', 0)}",
            "stability": afc_state.get("stability", 0.0),
            "timestamp": datetime.now().isoformat()
        })
        
        zoo_last = self.ai.get_zoo_last_experience()
        if zoo_last:
            fragments.append({
                "source": "ZOO_ANALYZER",
                "content": f"ZOO: absurd={zoo_last.get('absurd_score', 0):.3f}, risk={zoo_last.get('vibe_risk_score', 0):.3f}",
                "absurd": zoo_last.get('absurd_score', 0.0),
                "timestamp": datetime.now().isoformat()
            })
        
        gron_last = self.ai.get_gron_last_result()
        if gron_last:
            fragments.append({
                "source": "GRON_ANTYSKRET",
                "content": f"GRON: status={gron_last.get('status', 'OK')}, anomaly={gron_last.get('telemetry', {}).get('anomaly', 0):.3f}",
                "status": gron_last.get('status', 'OK'),
                "timestamp": datetime.now().isoformat()
            })
        
        return fragments[-n:]

    # ===== METODY AFC =====

    def get_afc_status(self) -> Dict[str, Any]:
        return self.ai.get_afc_state()

    def get_afc_decision(self) -> Dict[str, Any]:
        return self.ai.get_afc_decision()

    def get_afc_policy(self) -> Dict[str, Any]:
        return self.ai.get_afc_policy()

    def analyze_with_afc(self, tensor_45d: List[float]) -> Dict[str, Any]:
        return self.ai.analyze_with_afc(tensor_45d)

    # ===== METODY ZOO =====

    def get_zoo_status(self) -> Dict[str, Any]:
        return self.ai.get_zoo_status()

    def get_zoo_last_experience(self) -> Optional[Dict[str, Any]]:
        return self.ai.get_zoo_last_experience()

    def get_zoo_history(self) -> List[Dict[str, Any]]:
        return self.ai.get_zoo_history()

    def analyze_with_zoo(self, tensor_45d: List[float],
                         ctx_scene: Dict[str, Any],
                         actors: List[Dict[str, Any]],
                         signals: List[str]) -> Dict[str, Any]:
        return self.ai.analyze_with_zoo(tensor_45d, ctx_scene, actors, signals)

    def get_zoo_metrics(self) -> Dict[str, Any]:
        last = self.ai.get_zoo_last_experience()
        if not last:
            return {
                "absurd_score": 0.0,
                "vibe_risk_score": 0.0,
                "risk_for_vibe": "niskie",
                "action_hint": "normalna_interakcja",
                "action_priority": 3,
                "roles": {}
            }
        return {
            "absurd_score": last.get("absurd_score", 0.0),
            "vibe_risk_score": last.get("vibe_risk_score", 0.0),
            "risk_for_vibe": last.get("risk", "niskie"),
            "action_hint": last.get("action", "normalna_interakcja"),
            "action_priority": last.get("action_priority", 3),
            "roles": last.get("roles", {})
        }

    # ===== NOWE METODY GRON =====

    def get_gron_status(self) -> Dict[str, Any]:
        """Zwraca status GRON."""
        return self.ai.get_gron_status()

    def get_gron_last_result(self) -> Optional[Dict[str, Any]]:
        """Zwraca ostatni wynik GRON."""
        return self.ai.get_gron_last_result()

    def get_gron_metrics(self) -> Dict[str, Any]:
        """Zwraca metryki GRON dla Grid/Council/Synod."""
        last = self.ai.get_gron_last_result()
        if not last:
            return {
                "status": "OK",
                "anomaly": 0.0,
                "rekomendacja": "OBSERWACJA",
                "actions": {},
                "threshold": 0.6
            }
        return {
            "status": last.get("status", "OK"),
            "anomaly": last.get("telemetry", {}).get("anomaly", 0.0),
            "rekomendacja": last.get("rekomendacja", "OBSERWACJA"),
            "actions": last.get("akcja_systemowa", {}),
            "threshold": last.get("telemetry", {}).get("threshold", 0.6)
        }

    def get_gron_actions(self) -> Dict[str, Any]:
        """Zwraca akcje systemowe GRON dla Council/Konsystorza."""
        last = self.ai.get_gron_last_result()
        if not last:
            return {}
        return last.get("akcja_systemowa", {})

    def analyze_with_gron(self, tensor_45d: List[float],
                          wejscie: Dict[str, float],
                          **kwargs) -> Dict[str, Any]:
        """Wykonuje analizę z GRON."""
        return self.ai.analyze_with_gron(tensor_45d, wejscie, **kwargs)

    def get_full_status(self) -> Dict[str, Any]:
        """Zwraca pełny status – analityka + AFC + ZOO + GRON."""
        return {
            "analytics": self.ai.get_status(),
            "afc": self.ai.get_afc_state(),
            "zoo": {
                "status": self.ai.get_zoo_status(),
                "last_experience": self.ai.get_zoo_last_experience(),
                "metrics": self.get_zoo_metrics()
            },
            "gron": {
                "status": self.get_gron_status(),
                "last_result": self.get_gron_last_result(),
                "metrics": self.get_gron_metrics()
            },
            "last_decision": self.ai.get_afc_decision(),
            "last_policy": self.ai.get_afc_policy()
        }

# =============================================================================
# DEMONSTRACJA PRACY
# =============================================================================

if __name__ == "__main__":
    import random
    
    print("\n" + "=" * 80)
    print(f"🧠 {VERSION} — FINALNY TEST INTEGRACYJNY Z AFC + ZOO + GRON")
    print("WARSTWA 87 (GEON_AI_ANALYTICS) ➔ ROZSZERZONA O AFC-9 + ZOO + GRON")
    print("=" * 80 + "\n")

    # Konfiguracja z ZOO i GRON
    config = {
        "alpha": 0.6,
        "anomaly_threshold": 0.35,
        "stability_threshold": 0.7,
        "afc_history_size": 32,
        "zoo_enabled": True,
        "gron_enabled": True
    }
    
    ai = GeonAIAnalytics(config=config)
    bridge = AIAnalyticsBridge(ai)

    # 1. Test oryginalnej analizy
    print("🔬 TEST 1: ORYGINALNA ANALIZA TENSORA 45D")
    t = [clamp(0.5 + random.uniform(-0.05, 0.05), 0.0, 1.0) for _ in range(TENSOR_DIM)]
    res = ai.analyze(t)
    print(f"   Energia: {res['energy']:.4f} | Anomalia: {res['anomaly_score']:.4f}")

    # 2. Test AFC
    print("\n🔬 TEST 2: ANALIZA Z AFC")
    D1 = [0.5 + random.uniform(-0.1, 0.1) for _ in range(VECTOR_DIM)]
    D2 = [0.5 + random.uniform(-0.1, 0.1) for _ in range(VECTOR_DIM)]
    D3 = [0.5 + random.uniform(-0.1, 0.1) for _ in range(VECTOR_DIM)]
    D4 = [0.5 + random.uniform(-0.1, 0.1) for _ in range(VECTOR_DIM)]
    
    afc_result = ai.afc_cycle(D1, D2, D3, D4)
    print(f"   Core status: {afc_result['core']['status']}")
    print(f"   Decyzja: {afc_result['decision']['mode']}")
    print(f"   Polityka: {afc_result['policy']['final_mode']}")
    print(f"   Stabilność: {afc_result['core'].get('stability', 0):.4f}")

    # 3. Test ZOO
    print("\n🦁 TEST 3: ANALIZA Z ZOO")
    ctx_scene = {"description": "arcybiskup na stand-upie, politycy bez powodu"}
    actors = [
        {"name": "Aktor1", "lacks_reflection": True, "laughs_at_jokes_about_self": True},
        {"name": "Aktor2", "volume_db": 95, "logic_percent": 5},
        {"name": "Aktor3", "is_snobbish": True, "overestimates_status": True},
    ]
    signals = ["brak_samoświadomości"]
    
    zoo_result = ai.analyze_with_zoo(t, ctx_scene, actors, signals)
    print(f"   Status: {zoo_result['status']}")
    print(f"   Absurd Score: {zoo_result['absurd_score']:.2f}")
    print(f"   ZOO Risk: {zoo_result['zoo_risk']:.2f}")
    print(f"   Action: {zoo_result['action_hint']} (prio: {zoo_result['action_priority']})")
    print(f"   Roles: {zoo_result['roles_map']}")

    # 4. Test GRON
    print("\n🐉 TEST 4: ANALIZA Z GRON")
    wejscie = {
        "narracja": 0.9,
        "presja": 0.8,
        "zmiany": 0.7,
        "konflikty": 0.6,
        "zasady": 0.9
    }
    
    gron_result = ai.analyze_with_gron(
        t,
        wejscie,
        uderza_w_suwerennosc=True,
        harmonia_triady=0.2,
        ciaglosc_nacisku=0.8,
        pakiet={"intent": "PUSH", "target": "CORE", "payload": "SPAM"}
    )
    print(f"   Status: {gron_result['status']}")
    print(f"   GRON Status: {gron_result['gron_status']}")
    print(f"   GRON Anomaly: {gron_result['gron_anomaly']:.2f}")
    print(f"   GRON Rekomendacja: {gron_result['gron_rekomendacja']}")
    print(f"   GRON Actions: {list(gron_result['gron_actions'].keys())}")

    # 5. Stan mostu
    print("\n🔗 STAN MOSTU (ROZSZERZONEGO):")
    print(f"   Autopilot: {bridge.get_autopilot_state()}")
    print(f"   AFC Status: {bridge.get_afc_status()}")
    print(f"   ZOO Metrics: {bridge.get_zoo_metrics()}")
    print(f"   GRON Metrics: {bridge.get_gron_metrics()}")

    print("\n" + "=" * 80)
    print(f"🧠 MODUŁ 87 ZAKTUALIZOWANY (AFC + ZOO + GRON) | {HASLO}")
    print("=" * 80)