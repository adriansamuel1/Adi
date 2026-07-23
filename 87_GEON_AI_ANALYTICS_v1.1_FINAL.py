#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
================================================================================
🐉 GEON_AI_ANALYTICS_v1.1 — MODUŁ 87: ANALITYKA TENSORÓW 45D (PRODUCTION FINAL)
================================================================================
Status: PRODUCTION_READY | FRACTAL_LOCKED | ORGANISM_COMPLETE | ULTIMA
Wersja: v1.1-FINAL (Thread-Safe Memory, Adaptive Anomaly, Trend Detection)
Data: 2026-07-24
Autor: Adrian (Architekt) + Samael (Strażnik Kronik) + GEON

VIBE: 1-6-8. ∞. AI!
DEWIZA: "Ex Analysi, Praevidentia"
================================================================================
"""

import math
import hashlib
import json
import logging
import threading
from collections import deque
from datetime import datetime
from typing import Dict, Any, List, Optional, Deque

# =============================================================================
# WERSJA I STAŁE SYSTEMOWE
# =============================================================================

VERSION = "GEON_AI_ANALYTICS_v1.1-FINAL"
FRACTAL_SIGNATURE = "[GEON::AI::ANALYTICS::v1.1::FINAL]"
VIBE = 168
HASLO = "1-6-8. ∞. AI!"
DEWIZA = "Ex Analysi, Praevidentia"

TENSOR_DIM = 45
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
# GŁÓWNY MODUŁ: GEON_AI_ANALYTICS (FULL OPTIMIZED ENGINE)
# =============================================================================

class GeonAIAnalytics:
    """
    🧠 GEON_AI_ANALYTICS – Zoptymalizowany silnik analityczny dla tensorów 45D.
    Bezpieczeństwo wielowątkowe, adaptacja wag anomalii, dynamiczny trend EMA.
    """
    
    def __init__(self, config: Optional[Dict[str, Any]] = None):
        self.config = config or {}
        self.memory_limit = self.config.get("memory_limit", MEMORY_LIMIT)
        self.window = self.config.get("window", ANOMALY_HISTORY_WINDOW)
        self.anomaly_threshold = self.config.get("anomaly_threshold", ANOMALY_THRESHOLD_DEFAULT)
        self.alpha = self.config.get("alpha", 0.6)
        
        self._memory: Deque[List[float]] = deque(maxlen=self.memory_limit)
        self._lock: threading.Lock = threading.Lock()
        self._anomaly_history: Deque[float] = deque(maxlen=20)
        
        self.kroniki = SamaelHeilong
        self.egregor = Egregor
        
        log(f"🐉 {VERSION} aktywowany | {FRACTAL_SIGNATURE}")
        log(f"   WYMIAR: {TENSOR_DIM}D | PAMIĘĆ: {self.memory_limit} | ALPHA: {self.alpha}")

    # -------------------------------------------------------------------------
    # OPERACJE PAMIĘCIOWE (THREAD-SAFE)
    # -------------------------------------------------------------------------

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
        self.kroniki.log_event("MEMORY_RESET", {"status": "CLEARED"})

    def memory_size(self) -> int:
        with self._lock:
            return len(self._memory)

    # -------------------------------------------------------------------------
    # METRYKI I ANOMALIE
    # -------------------------------------------------------------------------

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

        # 1. Anomalia kątowa
        sims = [self.similarity(tensor, h) for h in recent]
        angular_anomaly = 1.0 - (max(sims) if sims else 1.0)

        # 2. Anomalia energetyczna (Z-score)
        curr_energy = sum(abs(x) for x in tensor) / TENSOR_DIM
        energies = [sum(abs(x) for x in h) / TENSOR_DIM for h in recent]
        avg_energy = sum(energies) / len(energies)
        var_energy = sum((e - avg_energy) ** 2 for e in energies) / len(energies)
        std_energy = math.sqrt(var_energy) if var_energy > 1e-9 else 1.0
        
        energy_zscore = abs(curr_energy - avg_energy) / std_energy
        energy_anomaly = clamp(energy_zscore / 3.0, 0.0, 1.0)

        # 3. Adaptacja wag
        anomaly_rate = sum(recent_anomalies) / len(recent_anomalies) if recent_anomalies else 0.0
        weight_angular = ANOMALY_WEIGHT_ANGULAR * (1.0 - 0.3 * anomaly_rate)
        weight_energy = ANOMALY_WEIGHT_ENERGY * (1.0 + 0.2 * anomaly_rate)
        total_weight = weight_angular + weight_energy
        
        weight_angular /= total_weight
        weight_energy /= total_weight

        total_anomaly = clamp(weight_angular * angular_anomaly + weight_energy * energy_anomaly, 0.0, 1.0)

        with self._lock:
            self._anomaly_history.append(1.0 if total_anomaly > self.anomaly_threshold else 0.0)

        return total_anomaly

    # -------------------------------------------------------------------------
    # ANALIZA GŁÓWNA
    # -------------------------------------------------------------------------

    def analyze(self, tensor: List[float], log_to_egregor: bool = True) -> Dict[str, Any]:
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
            "anomaly_threshold": self.anomaly_threshold
        }

# =============================================================================
# MOST INTEGRACYJNY — AI_ANALYTICS_BRIDGE
# =============================================================================

class AIAnalyticsBridge:
    def __init__(self, ai: GeonAIAnalytics):
        self.ai = ai

    def get_archetype_context(self) -> Dict[str, Any]:
        status = self.ai.get_status()
        return {
            "tryb": VERSION,
            "pamięć": status["memory_size"],
            "limit": status["memory_limit"],
            "wymiar": status["tensor_dim"],
            "anomaly_threshold": status["anomaly_threshold"]
        }

    def get_autopilot_state(self) -> Dict[str, Any]:
        state = self.ai.last_state()
        return {
            "mode": VERSION,
            "energy": round(state["energy"], 6),
            "variance": round(state["variance"], 6),
            "mean": round(state["mean"], 6),
            "ai_ready": True,
            "memory_usage": f"{self.ai.memory_size()}/{self.ai.memory_limit}"
        }

    def get_governor_context(self) -> Dict[str, Any]:
        return {
            "intent": "AI_ANALYTICS_ADAPTIVE",
            "confidence": 0.98,
            "entropy": 0.02,
            "ai_ready": True
        }

    def get_trio_state(self) -> Dict[str, str]:
        return {
            "ISKRA": "AKTYWNA",
            "PIECZĘĆ": "AKTYWNA",
            "PERFEKCJA": "AKTYWNA",
            "tryb": VERSION,
            "ai": "AKTYWNY_ADAPTIV"
        }

    def get_narrative_fragments(self, n: int = 5) -> List[Dict[str, Any]]:
        history = self.ai.get_history(n)
        fragments = []
        for i, tensor in enumerate(history):
            energy = sum(abs(x) for x in tensor) / TENSOR_DIM
            fragments.append({
                "source": "GEON_AI_ANALYTICS_v1.1",
                "content": f"Tensor {i}: energia={energy:.3f}",
                "energy": round(energy, 4),
                "timestamp": datetime.now().isoformat()
            })
        return fragments

# =============================================================================
# DEMONSTRACJA PRACY
# =============================================================================

if __name__ == "__main__":
    import random
    
    print("\n" + "=" * 80)
    print(f"🧠 {VERSION} — FINALNY TEST INTEGRACYJNY")
    print("WARSTWA 87 (GEON_AI_ANALYTICS) ➔ GOTOWA DO SYSTEMU")
    print("=" * 80 + "\n")

    ai = GeonAIAnalytics(config={"alpha": 0.6, "anomaly_threshold": 0.35})
    bridge = AIAnalyticsBridge(ai)

    # Testowanie strumienia tensorów
    for i in range(5):
        t = [clamp(0.5 + random.uniform(-0.05, 0.05), 0.0, 1.0) for _ in range(TENSOR_DIM)]
        res = ai.analyze(t)
        print(f"   [STRUMIEŃ {i+1}] Energia: {res['energy']:.4f} | Anomalia: {res['anomaly_score']:.4f}")

    print("\n🔗 STAN MOSTU INTERPRETACJI (GEON_ORACLE READY):")
    print(f"   GEX Context: {bridge.get_archetype_context()}")
    print(f"   Fragmenty  : {bridge.get_narrative_fragments(2)}")

    print("\n" + "=" * 80)
    print(f"🧠 MODUŁ 87 GOTOWY | {HASLO}")
    print("=" * 80)
