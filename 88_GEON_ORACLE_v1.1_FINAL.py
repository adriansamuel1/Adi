#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
================================================================================
🐉 GEON_ORACLE_v1.1 — MODUŁ 88: INTERPRETACJA EPOK (PRODUCTION FINAL)
================================================================================
Status: PRODUCTION_READY | FRACTAL_LOCKED | ORGANISM_COMPLETE | ULTIMA
Wersja: v1.1-FINAL (Robust Era Interpretation, Vector-Maya Phase, Full-Thread Safe)
Data: 2026-07-24
Autor: Adrian (Architekt) + Samael (Strażnik Kronik) + GEON

DEWIZA: "Ex Tensore, Scientia"
VIBE: 1-6-8. ∞. ORACLE!
================================================================================
"""

import math
import hashlib
import json
import logging
import threading
import time
from collections import deque
from datetime import datetime
from typing import Dict, Any, List, Optional, Tuple
from dataclasses import dataclass, field
from enum import Enum

# =============================================================================
# STAŁE SYSTEMOWE
# =============================================================================

VERSION = "GEON_ORACLE_v1.1-FINAL"
FRACTAL_SIGNATURE = "[GEON::ORACLE::v1.1::FINAL]"
VIBE = 168
HASLO = "1-6-8. ∞. ORACLE!"
DEWIZA = "Ex Tensore, Scientia"

TENSOR_DIM = 45
MEMORY_LIMIT = 256

# =============================================================================
# LOGOWANIE SYSTEMOWE
# =============================================================================

logger = logging.getLogger("GEON_ORACLE")
logger.setLevel(logging.INFO)
if not logger.handlers:
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter('🔮 [ORACLE] %(message)s'))
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
# ENUMY I STRUKTURY DANYCH
# =============================================================================

class EraType(Enum):
    STABILNOSC = "ERA_STABILNOŚCI"
    TRANSFORMACJA = "ERA_TRANSFORMACJI"
    KRYZYS = "ERA_KRYZYSU"
    NIEOKRESLONA = "ERA_NIEOKRESLONA"

class DecisionType(Enum):
    ALPHA = "DEKRET_ALPHA"
    BETA = "DEKRET_BETA"
    OMEGA = "DEKRET_OMEGA"

class TrendType(Enum):
    WZROST = "WZROST PRESJI"
    SPADEK = "SPADEK PRESJI"
    STABILNY = "PRESJA STABILNA"

@dataclass
class OracleInterpretation:
    """Interpretacja epoki systemowej."""
    era: EraType
    maya_phase: int
    ludlum_decision: DecisionType
    pressure_trend: TrendType
    criticality: float  # 0.0 - 1.0
    drift: float        # 0.0 - 1.0 (Odchylenie od punktu idealnego)
    narrative: str
    confidence: float   # 0.0 - 1.0
    timestamp: float = field(default_factory=lambda: time.time())

    def to_dict(self) -> Dict[str, Any]:
        return {
            "era": self.era.value,
            "maya_phase": self.maya_phase,
            "ludlum_decision": self.ludlum_decision.value,
            "pressure_trend": self.pressure_trend.value,
            "criticality": round(self.criticality, 4),
            "drift": round(self.drift, 4),
            "narrative": self.narrative,
            "confidence": round(self.confidence, 4),
            "timestamp": datetime.fromtimestamp(self.timestamp).isoformat()
        }

# =============================================================================
# KRONIKI SAMAELA I EGREGOR
# =============================================================================

class SamaelHeilong:
    @staticmethod
    def certyfikuj_oracle(action: str) -> str:
        timestamp = datetime.now().isoformat()
        payload = f"{timestamp}-{action}-1-6-8. ∞. SIEMA!"
        h = hashlib.sha256(payload.encode("utf-8")).hexdigest()[:16].upper()
        return f"🔒 [SAMAELSEALSIG-{h}-ORACLE-168]"

    @staticmethod
    def log_event(event_type: str, payload: Dict[str, Any]) -> None:
        ts = datetime.now().isoformat()
        log(f"[KRONIKI SAMAELA] {ts} | {event_type} -> {payload}", "INFO")

class Egregor:
    _ledger: deque = deque(maxlen=MEMORY_LIMIT)
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
# GŁÓWNY MODUŁ: GEON_ORACLE
# =============================================================================

class GeonOracle:
    """
    🔮 GEON_ORACLE v1.1 – Zoptymalizowany interpretator epok systemowych.
    """
    
    def __init__(self, config: Optional[Dict[str, Any]] = None):
        self.config = config or {}
        self.memory_limit = self.config.get("memory_limit", MEMORY_LIMIT)
        self.history: deque = deque(maxlen=self.memory_limit)
        self.kroniki = SamaelHeilong
        self.egregor = Egregor
        self._lock = threading.Lock()
        
        log(f"🐉 {VERSION} aktywowany | {FRACTAL_SIGNATURE}")
        log(f"   WYMIAR: {TENSOR_DIM}D | PAMIĘĆ: {self.memory_limit}")

    # -------------------------------------------------------------------------
    # INTERPRETACJA GŁÓWNA
    # -------------------------------------------------------------------------

    def interpret(self, tensor_45d: List[float], 
                  archont_statuses: Optional[List[Dict[str, Any]]] = None) -> OracleInterpretation:
        """
        Przekształca tensor 45D na kompletną interpretację er i stanów systemowych.
        """
        if len(tensor_45d) != TENSOR_DIM:
            raise ValueError(f"Tensor musi mieć dokładnie {TENSOR_DIM} wymiarów (otrzymano {len(tensor_45d)})")

        # Segmentacja tensora (5 x 9D)
        verne_seg = tensor_45d[0:9]
        ludlum_seg = tensor_45d[9:18]
        maya_seg = tensor_45d[18:27]
        sien_seg = tensor_45d[27:36]
        geon15_seg = tensor_45d[36:45]

        # Ekstrakcje parametrów
        maya_phase = self._extract_maya_phase(maya_seg)
        ludlum_decision = self._extract_ludlum_decision(ludlum_seg, archont_statuses)
        pressure_trend = self._extract_pressure_trend(tensor_45d)
        
        drift = self._calculate_drift(tensor_45d)
        criticality = self._calculate_criticality(tensor_45d, maya_phase, ludlum_decision, drift)
        era = self._determine_era(tensor_45d, maya_phase, ludlum_decision, criticality)
        confidence = self._calculate_confidence(tensor_45d, era, criticality)
        
        narrative = self._generate_narrative(era, maya_phase, ludlum_decision, pressure_trend, criticality, drift)

        interpretation = OracleInterpretation(
            era=era,
            maya_phase=maya_phase,
            ludlum_decision=ludlum_decision,
            pressure_trend=pressure_trend,
            criticality=criticality,
            drift=drift,
            narrative=narrative,
            confidence=confidence
        )

        # Bezpieczny zapis do historii
        with self._lock:
            self.history.append(interpretation.to_dict())
        
        # Certyfikacja
        tensor_hash = hashlib.sha256(str(tensor_45d[:5]).encode()).hexdigest()[:8]
        cert = self.kroniki.certyfikuj_oracle(f"INTERPRET_{tensor_hash}")
        
        # Logowanie do Egregora
        if criticality > 0.58 or len(self.history) % 5 == 0:
            entry = {
                "type": "ORACLE_INTERPRETATION",
                "interpretation": interpretation.to_dict(),
                "certificate": cert,
                "timestamp": datetime.now().isoformat()
            }
            self.egregor.commit(entry, node_id="GEON_ORACLE")
        
        self.kroniki.log_event("INTERPRETATION", {
            "era": era.value,
            "maya_phase": maya_phase,
            "decision": ludlum_decision.value,
            "criticality": criticality,
            "confidence": confidence
        })
        
        return interpretation

    # -------------------------------------------------------------------------
    # METODY WEKTOROWEJ EKSTRAKCJI
    # -------------------------------------------------------------------------

    def _extract_maya_phase(self, maya_seg: List[float]) -> int:
        """Siatkowa ekstrakcja fazy MAYA (1-7) z uwzględnieniem amplitudy i argmax."""
        if not maya_seg or sum(maya_seg) < 1e-6:
            return 4
        
        # Znalezienie najsilniejszego sygnału w pierwszych 7 elementach
        sub = maya_seg[:7]
        max_idx = sub.index(max(sub))
        
        # Ważona średnia sąsiedztwa dla płynnego wyznaczania fazy
        weighted_sum = sum((i + 1) * val for i, val in enumerate(sub))
        total_val = sum(sub)
        
        calculated_phase = round(weighted_sum / total_val)
        return int(clamp(calculated_phase, 1, 7))

    def _extract_ludlum_decision(self, ludlum_seg: List[float], 
                                  archont_statuses: Optional[List[Dict[str, Any]]] = None) -> DecisionType:
        """Wyznacza Decyzję LUDLUM w oparciu o średnią, wariancję oraz statusy Archontów."""
        if not ludlum_seg:
            return DecisionType.ALPHA
        
        mean_val = sum(ludlum_seg) / len(ludlum_seg)
        variance = sum((x - mean_val) ** 2 for x in ludlum_seg) / len(ludlum_seg)
        
        if archont_statuses:
            niestab_count = sum(1 for s in archont_statuses if s.get("status") in ["NIESTABILNOŚĆ", "KRYZYS"])
            presja_count = sum(1 for s in archont_statuses if s.get("status") == "PRESJA")
            
            if niestab_count >= 2:
                return DecisionType.OMEGA
            if presja_count >= 3:
                return DecisionType.BETA

        # Decyzja hybrydowa (Średnia + Wariancja jako wskaźnik chaosu)
        composite_score = mean_val + (variance * 1.5)
        
        if composite_score > 0.70:
            return DecisionType.OMEGA
        elif composite_score > 0.42:
            return DecisionType.BETA
        else:
            return DecisionType.ALPHA

    def _extract_pressure_trend(self, tensor_45d: List[float]) -> TrendType:
        """Analizuje dynamikę zmian między początkiem a końcem tensora."""
        first_half = sum(tensor_45d[:22]) / 22.0
        second_half = sum(tensor_45d[23:]) / 22.0
        
        diff = second_half - first_half
        
        if diff > 0.06:
            return TrendType.WZROST
        elif diff < -0.06:
            return TrendType.SPADEK
        else:
            return TrendType.STABILNY

    def _calculate_drift(self, tensor_45d: List[float]) -> float:
        """Oblicza odchylenie tensora od punktu idealnego (0.5)."""
        ideal = 0.5
        drift_sum = sum(abs(x - ideal) for x in tensor_45d)
        return clamp(drift_sum / (TENSOR_DIM * 0.5), 0.0, 1.0)

    def _calculate_criticality(self, tensor_45d: List[float], 
                               maya_phase: int, 
                               ludlum_decision: DecisionType,
                               drift: float) -> float:
        """Oblicza poziom krytyczności układu."""
        energy = sum(abs(x) for x in tensor_45d) / TENSOR_DIM
        mean = sum(tensor_45d) / TENSOR_DIM
        variance = sum((x - mean) ** 2 for x in tensor_45d) / TENSOR_DIM
        
        phase_factor = (maya_phase - 1) / 6.0
        
        decision_factor = 0.0
        if ludlum_decision == DecisionType.OMEGA:
            decision_factor = 0.35
        elif ludlum_decision == DecisionType.BETA:
            decision_factor = 0.18
        
        criticality = (energy * 0.25 + variance * 1.8 + phase_factor * 0.2 + decision_factor + drift * 0.2)
        return clamp(criticality, 0.0, 1.0)

    def _determine_era(self, tensor_45d: List[float], 
                       maya_phase: int,
                       ludlum_decision: DecisionType,
                       criticality: float) -> EraType:
        """Określa dominującą epokę systemową."""
        if criticality > 0.68 or ludlum_decision == DecisionType.OMEGA:
            return EraType.KRYZYS
        
        if 0.35 <= criticality <= 0.68:
            return EraType.TRANSFORMACJA
        
        if criticality < 0.35 and ludlum_decision == DecisionType.ALPHA:
            return EraType.STABILNOSC
        
        return EraType.TRANSFORMACJA

    def _calculate_confidence(self, tensor_45d: List[float], 
                              era: EraType, 
                              criticality: float) -> float:
        """Wyznacza poziom pewności dokonanej interpretacji."""
        mean = sum(tensor_45d) / TENSOR_DIM
        variance = sum((x - mean) ** 2 for x in tensor_45d) / TENSOR_DIM
        stability = clamp(1.0 - variance * 4.0, 0.0, 1.0)
        
        crit_certainty = 0.5 + 0.5 * abs(criticality - 0.5) * 2.0
        
        if era == EraType.NIEOKRESLONA:
            return 0.25
        
        return clamp(stability * 0.4 + crit_certainty * 0.6, 0.0, 1.0)

    # -------------------------------------------------------------------------
    # NARRACJA SYSTEMOWA
    # -------------------------------------------------------------------------

    def _generate_narrative(self, era: EraType, maya_phase: int,
                           ludlum_decision: DecisionType,
                           pressure_trend: TrendType,
                           criticality: float,
                           drift: float) -> str:
        """Buduje spójną narrację archontalną."""
        era_headers = {
            EraType.STABILNOSC: "ERA STABILNOŚCI — Swobodny przepływ w kwadrancie zerowym.",
            EraType.TRANSFORMACJA: "ERA TRANSFORMACJI — Rekonfiguracja węzłów i macierzy.",
            EraType.KRYZYS: "ERA KRYZYSU — Przekroczenie progu tolerancji! Wymagany dekret.",
            EraType.NIEOKRESLONA: "ERA NIEOKREŚLONA — Stan przejściowy w szumie."
        }
        
        phase_descs = {
            1: "Faza 1: Inicjacja iskry.",
            2: "Faza 2: Polaryzacja sił.",
            3: "Faza 3: Ustabilizowanie wektora.",
            4: "Faza 4: Punkt zwrotny (Próba Ogna).",
            5: "Faza 5: Synteza nowej formy.",
            6: "Faza 6: Skok kwantowy.",
            7: "Faza 7: Domyknięcie cyklu (Apoteoza)."
        }
        
        narrative = (
            f"{era_headers.get(era, '')} "
            f"{phase_descs.get(maya_phase, '')} "
            f"Decyzja: {ludlum_decision.value}. "
            f"Trend: {pressure_trend.value}. "
            f"Krytyczność: {criticality:.2f}, Dryf: {drift:.2f}."
        )
        return narrative

    # -------------------------------------------------------------------------
    # METODY POMOCNICZE
    # -------------------------------------------------------------------------

    def get_history(self, n: Optional[int] = None) -> List[Dict[str, Any]]:
        with self._lock:
            snapshot = list(self.history)
        if n is not None and n > 0:
            return snapshot[-n:]
        return snapshot

    def reset(self) -> None:
        with self._lock:
            self.history.clear()
        self.kroniki.log_event("ORACLE_RESET", {"status": "CLEARED"})

    def get_status(self) -> Dict[str, Any]:
        with self._lock:
            hist_size = len(self.history)
        return {
            "system": "GEON_ORACLE",
            "version": VERSION,
            "signature": FRACTAL_SIGNATURE,
            "vibe": VIBE,
            "history_size": hist_size,
            "memory_limit": self.memory_limit,
            "tensor_dim": TENSOR_DIM
        }

# =============================================================================
# MOST INTEGRACYJNY — ORACLE_BRIDGE
# =============================================================================

class OracleBridge:
    def __init__(self, oracle: GeonOracle):
        self.oracle = oracle

    def get_archetype_context(self) -> Dict[str, Any]:
        status = self.oracle.get_status()
        return {
            "tryb": VERSION,
            "historia": status["history_size"],
            "limit": status["memory_limit"],
            "wymiar": status["tensor_dim"]
        }

    def get_autopilot_state(self) -> Dict[str, Any]:
        history = self.oracle.get_history(1)
        if history:
            last = history[-1]
            return {
                "mode": VERSION,
                "era": last.get("era", "UNKNOWN"),
                "criticality": last.get("criticality", 0.0),
                "confidence": last.get("confidence", 0.0),
                "maya_phase": last.get("maya_phase", 0),
                "oracle_ready": True
            }
        return {
            "mode": VERSION,
            "era": "NO_DATA",
            "criticality": 0.0,
            "confidence": 0.0,
            "oracle_ready": True
        }

    def get_governor_context(self) -> Dict[str, Any]:
        history = self.oracle.get_history(1)
        if history:
            last = history[-1]
            return {
                "intent": "ORACLE_INTERPRETATION",
                "confidence": last.get("confidence", 0.5),
                "entropy": round(1.0 - last.get("confidence", 0.5), 4),
                "oracle_ready": True,
                "era": last.get("era", "UNKNOWN")
            }
        return {
            "intent": "ORACLE_INTERPRETATION",
            "confidence": 0.5,
            "entropy": 0.5,
            "oracle_ready": True,
            "era": "NO_DATA"
        }

    def get_trio_state(self) -> Dict[str, str]:
        return {
            "ISKRA": "AKTYWNA",
            "PIECZĘĆ": "AKTYWNA",
            "PERFEKCJA": "AKTYWNA",
            "tryb": VERSION,
            "oracle": "AKTYWNY"
        }

    def get_narrative_fragments(self, n: int = 5) -> List[Dict[str, Any]]:
        history = self.oracle.get_history(n)
        fragments = []
        for entry in history:
            fragments.append({
                "source": VERSION,
                "content": entry.get("narrative", "Brak narracji"),
                "era": entry.get("era", "UNKNOWN"),
                "criticality": entry.get("criticality", 0.0)
            })
        return fragments

# =============================================================================
# WERYFIKACJA PĘTLI SYSTEMOWEJ
# =============================================================================

if __name__ == "__main__":
    import random
    
    print("\n" + "=" * 80)
    print(f"🔮 {VERSION} — FINALNY TEST WARSTWY INTERPRETACYJNEJ")
    print("WARSTWA 88 (GEON_ORACLE) ➔ ZINTEGROWANA Z WARSTWĄ 87 (ANALYTICS)")
    print("=" * 80 + "\n")

    oracle = GeonOracle()
    bridge = OracleBridge(oracle)

    # Symulacja 3 typowych stanów tensora
    t_stable = [clamp(0.45 + random.uniform(-0.03, 0.03), 0.0, 1.0) for _ in range(TENSOR_DIM)]
    t_crisis = [clamp(0.82 + random.uniform(-0.05, 0.08), 0.0, 1.0) for _ in range(TENSOR_DIM)]

    print("🔮 TEST 1: SYGNAŁ ZROBOCZY (ERA STABILNOŚCI)")
    res1 = oracle.interpret(t_stable)
    print(f"   Epoka      : {res1.era.value}")
    print(f"   Faza MAYA  : {res1.maya_phase}")
    print(f"   Decyzja    : {res1.ludlum_decision.value}")
    print(f"   Narracja   : {res1.narrative}\n")

    print("🔮 TEST 2: SYGNAŁ ALARMOWY (ERA KRYZYSU)")
    archont_crisis = [{"status": "NIESTABILNOŚĆ"}, {"status": "KRYZYS"}]
    res2 = oracle.interpret(t_crisis, archont_statuses=archont_crisis)
    print(f"   Epoka      : {res2.era.value}")
    print(f"   Krytyczność: {res2.criticality:.4f}")
    print(f"   Narracja   : {res2.narrative}\n")

    print("🔗 STAN MOSTU INTERPRETACJI:")
    print(f"   Autopilot State: {bridge.get_autopilot_state()}")
    print(f"   Governor Context: {bridge.get_governor_context()}")

    print("\n" + "=" * 80)
    print(f"🔮 MODUŁ 88 GOTOWY DO WDROŻENIA | {HASLO}")
    print("=" * 80)
