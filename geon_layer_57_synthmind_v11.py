#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GEON_LAYER_57 — SYNTHMIND v11 (ULTIMA FUSION)

Warstwa syntezy dla GEON_DRAGON_OS.
Łączy:
- SolarMind (warstwa 55) — myślenie planetarne
- HydroMind (warstwa 56) — pamięć wodna
- AFC‑9 sprzężenie zwrotne
- VisionOS (wizja syntezy)
- ShadowScan (cień syntezy)
- GlobalRhythmEngine
- SystemMirror
- GEON_168 / geon_core
- FAG_Core
- TagUniverse

Autor: Adrian (Architekt)
Vibe: 1-6-8. ∞. KLAWO JAK CHOLERA
"""

from dataclasses import dataclass, field
from enum import Enum
import logging
import math
import time
from typing import Dict, Any, List, Optional, Tuple

logger = logging.getLogger("GEON_SYNTHMIND")


# ============================================================
# ENUMY — STANY SYNTEZY
# ============================================================

class SynthMode(Enum):
    HARMONY = "harmony"          # pełna synteza
    FUSION = "fusion"            # łączenie
    SEPARATION = "separation"    # rozdzielenie
    EMERGENCY = "emergency"      # tryb kryzysowy
    CREATIVE = "creative"        # kreatywna synteza
    ANALYTIC = "analytic"        # analityczna synteza


class SynthState(Enum):
    STABLE = "stable"
    COHERENT = "coherent"
    TURBULENT = "turbulent"
    CRITICAL = "critical"
    RESONANT = "resonant"


@dataclass
class SynthVector:
    """Wektor syntezy 9D."""
    values: List[float]
    core: float
    stability: float
    coherence: float
    timestamp: float = field(default_factory=time.time)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "values": [round(v, 4) for v in self.values],
            "core": round(self.core, 4),
            "stability": round(self.stability, 4),
            "coherence": round(self.coherence, 4),
            "timestamp": self.timestamp
        }


@dataclass
class SynthDecision:
    """Decyzja syntezy."""
    mode: SynthMode
    state: SynthState
    confidence: float
    action: str
    meta: Dict[str, Any] = field(default_factory=dict)


@dataclass
class SynthTrajectory:
    """Trajektoria syntezy."""
    vector: float
    risk: float
    speed: float
    direction: str
    critical_points: List[int]
    timestamp: float = field(default_factory=time.time)


@dataclass
class SynthResult:
    """Pełny wynik syntezy."""
    vector: SynthVector
    decision: SynthDecision
    trajectory: SynthTrajectory
    shadow_score: int
    rhythm_sync: bool
    mode: str
    timestamp: float = field(default_factory=time.time)


# ============================================================
# SYNTHMIND CORE — SYNTEZA SOLAR + HYDRO
# ============================================================

class SynthMindCore:
    """SynthMindCore — synteza SolarMind i HydroMind.

    Wersja v11 — ULTIMA FUSION
    """

    ACTION_MAP = {
        SynthMode.HARMONY: "INTEGRATE",
        SynthMode.FUSION: "FUSE",
        SynthMode.SEPARATION: "SEPARATE",
        SynthMode.EMERGENCY: "PROTECT",
        SynthMode.CREATIVE: "EXPAND",
        SynthMode.ANALYTIC: "ANALYZE"
    }

    def __init__(self, system: Any):
        self.system = system
        
        # AFC-9 sprzężenie zwrotne
        self.stability_history: List[float] = []
        self.last_stability: float = 0.5
        
        # Historia syntezy
        self.history: List[SynthResult] = []
        self.stats = {
            "syntheses": 0,
            "modes": {m.value: 0 for m in SynthMode},
            "states": {s.value: 0 for s in SynthState},
            "avg_confidence": 0.0,
            "avg_shadow": 0.0
        }

        logger.info("[SynthMind] v11 ULTIMA FUSION aktywowany")

    # ============================================================
    # SHADOW SCAN — wykrywanie cienia w syntezie
    # ============================================================

    def _shadow_synthesis(self, solar_shadow: int, hydro_shadow: float) -> int:
        """Oblicza cień syntezy na podstawie cieni wejściowych."""
        weighted = solar_shadow * 0.6 + hydro_shadow * 0.4
        return min(10, max(0, int(round(weighted))))

    # ============================================================
    # AFC-9 — SPRZĘŻENIE ZWROTNE SYNTEZY
    # ============================================================

    def _afc9_synthesis(self, solar_core: float, hydro_core: float, 
                        solar_stability: float, hydro_stability: float) -> SynthVector:
        """Oblicza wektor syntezy z AFC-9."""
        d1 = [
            solar_core * 0.5 + hydro_core * 0.5,
            solar_stability * 0.6 + hydro_stability * 0.4,
            (solar_core + hydro_core) / 2.0,
            1.0 - abs(solar_core - hydro_core),
            solar_core,
            hydro_core,
            solar_stability,
            hydro_stability,
            self.last_stability
        ]
        
        d2 = [min(1.0, v * 0.9) for v in d1]
        d3 = [min(1.0, v * 1.1) for v in d1]
        d4 = [self.last_stability for _ in range(9)]
        
        def avg(vals: List[float]) -> float:
            return sum(vals) / len(vals) if vals else 0.0
        
        d5 = [avg([d1[i], d2[i], d3[i], d4[i]]) for i in range(9)]
        d6 = [avg([d1[i], d3[i], d5[i]]) for i in range(9)]
        d7 = [avg([d2[i], d4[i], d6[i]]) for i in range(9)]
        d8 = [avg([d1[i], d3[i], d5[i], d7[i]]) for i in range(9)]
        d9 = [avg([d1[i], d8[i]]) for i in range(9)]
        
        core = avg(d9)
        
        variance = sum((v - core) ** 2 for v in d9) / len(d9)
        stability = max(0.0, min(1.0, 1.0 - math.sqrt(variance) * 2.5))
        
        self.stability_history.append(stability)
        if len(self.stability_history) > 20:
            self.stability_history = self.stability_history[-20:]
        
        if len(self.stability_history) > 2:
            window = self.stability_history[-10:]
            mean = sum(window) / len(window)
            var = sum((v - mean) ** 2 for v in window) / len(window)
            self.last_stability = max(0.0, min(1.0, 1.0 - math.sqrt(var) * 2.5))
        
        coherence = max(0.0, min(1.0, 1.0 - abs(solar_core - hydro_core) * 0.5))
        
        return SynthVector(
            values=d9,
            core=core,
            stability=stability,
            coherence=coherence
        )

    # ============================================================
    # DECYZJA SYNTEZY
    # ============================================================

    def _synthesis_decision(self, vector: SynthVector, shadow_score: int, 
                            rhythm_sync: bool) -> SynthDecision:
        """Podejmuje decyzję syntezy."""
        if shadow_score > 6:
            state = SynthState.CRITICAL
            mode = SynthMode.EMERGENCY
        elif vector.stability < 0.3:
            state = SynthState.TURBULENT
            mode = SynthMode.SEPARATION
        elif vector.coherence < 0.4:
            state = SynthState.TURBULENT
            mode = SynthMode.FUSION
        elif vector.stability > 0.7 and vector.coherence > 0.7:
            state = SynthState.RESONANT
            mode = SynthMode.HARMONY
        elif vector.stability > 0.5:
            state = SynthState.COHERENT
            mode = SynthMode.CREATIVE if rhythm_sync else SynthMode.ANALYTIC
        else:
            state = SynthState.STABLE
            mode = SynthMode.FUSION
        
        confidence = vector.stability * 0.5 + vector.coherence * 0.3 + (1.0 - shadow_score / 10) * 0.2
        confidence = max(0.0, min(1.0, confidence))

        self.stats["modes"][mode.value] += 1
        self.stats["states"][state.value] += 1
        
        return SynthDecision(
            mode=mode,
            state=state,
            confidence=round(confidence, 4),
            action=self.ACTION_MAP.get(mode, "BALANCE"),
            meta={
                "stability": round(vector.stability, 4),
                "coherence": round(vector.coherence, 4),
                "shadow": shadow_score,
                "rhythm": rhythm_sync
            }
        )

    # ============================================================
    # TRAJEKTORIA SYNTEZY
    # ============================================================

    def _synthesis_trajectory(self, vector: SynthVector, decision: SynthDecision, 
                              shadow_score: int) -> SynthTrajectory:
        """Oblicza trajektorię syntezy."""
        trajectory_vector = vector.core * 0.6 + (1.0 - shadow_score / 10) * 0.4
        risk = (1.0 - vector.stability) * 0.6 + (1.0 - vector.coherence) * 0.3 + (shadow_score / 10) * 0.1
        speed = decision.confidence * 0.7 + vector.stability * 0.3
        
        direction_map = {
            SynthMode.HARMONY: "integration",
            SynthMode.EMERGENCY: "protection",
            SynthMode.CREATIVE: "expansion",
            SynthMode.ANALYTIC: "analysis"
        }
        direction = direction_map.get(decision.mode, "balance")
        
        if risk < 0.3:
            critical_points = [5, 12, 24]
        elif risk < 0.6:
            critical_points = [3, 7, 15]
        else:
            critical_points = [1, 3, 7]
        
        return SynthTrajectory(
            vector=round(trajectory_vector, 4),
            risk=round(max(0.0, min(1.0, risk)), 4),
            speed=round(max(0.0, min(1.0, speed)), 4),
            direction=direction,
            critical_points=critical_points
        )

    # ============================================================
    # GŁÓWNA METODA — PROCESS
    # ============================================================

    def process(self, solarmind_out: Optional[Dict[str, Any]] = None, 
                hydromind_out: Optional[Dict[str, Any]] = None) -> SynthResult:
        """Synteza wyjść SolarMind i HydroMind z obsługą brakujących danych."""
        solarmind_out = solarmind_out or {}
        hydromind_out = hydromind_out or {}

        self.stats["syntheses"] += 1
        logger.info("[SynthMind] Rozpoczynam syntezę")
        
        # 1. EKSTRAKCJA METRYK (Safe Get)
        solar_afc = solarmind_out.get("afc_vector", [0.5] * 9)
        solar_core = sum(solar_afc) / len(solar_afc) if solar_afc else 0.5
        solar_stability = float(solarmind_out.get("afc_stability", 0.5))
        
        solar_shadow_dict = solarmind_out.get("shadow") or {}
        solar_shadow = int(solar_shadow_dict.get("score", 0))
        solar_rhythm = bool(solarmind_out.get("rhythm_sync", True))
        
        hydro_state = hydromind_out.get("memory_state") or {}
        hydro_core = float(hydro_state.get("avg_stability", 0.5))
        hydro_stability = float(hydro_state.get("avg_stability", 0.5))
        hydro_shadow = float(hydro_state.get("avg_shadow", 0.0))
        hydro_rhythm = bool(hydro_state.get("rhythm_sync", True))
        
        # 2–6. OBLICZENIA LOGICZNE
        vector = self._afc9_synthesis(solar_core, hydro_core, solar_stability, hydro_stability)
        shadow_score = self._shadow_synthesis(solar_shadow, hydro_shadow)
        rhythm_sync = solar_rhythm and hydro_rhythm
        decision = self._synthesis_decision(vector, shadow_score, rhythm_sync)
        trajectory = self._synthesis_trajectory(vector, decision, shadow_score)
        
        result = SynthResult(
            vector=vector,
            decision=decision,
            trajectory=trajectory,
            shadow_score=shadow_score,
            rhythm_sync=rhythm_sync,
            mode=decision.mode.value
        )
        
        # 7. REJESTRACJA W HISTORII
        self.history.append(result)
        if len(self.history) > 200:
            self.history = self.history[-200:]
        
        n = self.stats["syntheses"]
        self.stats["avg_confidence"] = ((self.stats["avg_confidence"] * (n - 1)) + decision.confidence) / n
        self.stats["avg_shadow"] = ((self.stats["avg_shadow"] * (n - 1)) + shadow_score) / n
        
        logger.info(f"[SynthMind] Synteza zakończona — Mode: {decision.mode.value}, "
                   f"State: {decision.state.value}, Confidence: {decision.confidence:.3f}")
        
        return result

    # ============================================================
    # METODY POMOCNICZE
    # ============================================================

    def get_state(self) -> Dict[str, Any]:
        """Zwraca stan syntezy."""
        if not self.history:
            return {
                "mode": "idle",
                "state": "idle",
                "stability": 0.5,
                "coherence": 0.5,
                "shadow": 0,
                "rhythm": True
            }
        
        last = self.history[-1]
        return {
            "mode": last.mode,
            "state": last.decision.state.value,
            "stability": last.vector.stability,
            "coherence": last.vector.coherence,
            "shadow": last.shadow_score,
            "rhythm": last.rhythm_sync,
            "confidence": last.decision.confidence,
            "trajectory": {
                "vector": last.trajectory.vector,
                "risk": last.trajectory.risk,
                "speed": last.trajectory.speed,
                "direction": last.trajectory.direction
            }
        }

    def get_stats(self) -> Dict[str, Any]:
        """Zwraca statystyki syntezy."""
        return {
            "syntheses": self.stats["syntheses"],
            "modes": self.stats["modes"],
            "states": self.stats["states"],
            "avg_confidence": round(self.stats["avg_confidence"], 4),
            "avg_shadow": round(self.stats["avg_shadow"], 2),
            "last_stability": round(self.last_stability, 4),
            "history_size": len(self.history)
        }

    def get_history(self, limit: int = 10) -> List[SynthResult]:
        """Zwraca historię syntezy."""
        return self.history[-limit:]

    def reset(self) -> None:
        """Resetuje stan syntezy."""
        self.stability_history.clear()
        self.last_stability = 0.5
        self.history.clear()
        self.stats = {
            "syntheses": 0,
            "modes": {m.value: 0 for m in SynthMode},
            "states": {s.value: 0 for s in SynthState},
            "avg_confidence": 0.0,
            "avg_shadow": 0.0
        }
        logger.info("[SynthMind] Reset wykonany")


# ============================================================
# WARSTWA 57 — ADAPTER DLA GEON_DRAGON_OS
# ============================================================

class GeonLayer57SynthMindV11:
    """Adapter warstwy 57 dla GEON_DRAGON_OS — ULTIMA FUSION."""

    def __init__(self, system: Any):
        self.system = system
        self.core = SynthMindCore(system)
        logger.info("[Layer57] GeonLayer57SynthMindV11 aktywowany")

    def process(self, solarmind_out: Optional[Dict[str, Any]] = None, 
                hydromind_out: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Przetwarza syntezę SolarMind i HydroMind."""
        result = self.core.process(solarmind_out, hydromind_out)
        
        return {
            "synth_vector": result.vector.to_dict(),
            "synth_decision": {
                "mode": result.decision.mode.value,
                "state": result.decision.state.value,
                "confidence": result.decision.confidence,
                "action": result.decision.action,
                "meta": result.decision.meta
            },
            "synth_trajectory": {
                "vector": result.trajectory.vector,
                "risk": result.trajectory.risk,
                "speed": result.trajectory.speed,
                "direction": result.trajectory.direction,
                "critical_points": result.trajectory.critical_points
            },
            "synth_shadow": result.shadow_score,
            "synth_rhythm": result.rhythm_sync,
            "synth_mode": result.mode,
            "timestamp": result.timestamp
        }

    def get_state(self) -> Dict[str, Any]:
        return self.core.get_state()

    def get_stats(self) -> Dict[str, Any]:
        return self.core.get_stats()

    def get_history(self, limit: int = 10) -> List[Dict[str, Any]]:
        """Zwraca historię syntezy jako słowniki."""
        history = self.core.get_history(limit)
        return [
            {
                "mode": r.mode,
                "state": r.decision.state.value,
                "confidence": r.decision.confidence,
                "stability": r.vector.stability,
                "coherence": r.vector.coherence,
                "shadow": r.shadow_score,
                "rhythm": r.rhythm_sync
            }
            for r in history
        ]

    def reset(self) -> None:
        self.core.reset()
