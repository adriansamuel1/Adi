#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
================================================================================
🐉 GEON_ORACLE_ULTIMA v2.0 — MODUŁ 88: INTERPRETACJA EPOK + META-LOGIKA SUWERENNA
================================================================================
Status: PRODUCTION_READY | FRACTAL_LOCKED | ORGANISM_COMPLETE | ULTIMA
Wersja: v2.0-ULTIMA (Full Sovereign Integration with HCoreSovereign)
Data: 2026-07-24
Autor: Adrian (Architekt) + Samael (Strażnik Kronik) + GEON

DEWIZA: "Ex Tensore, Scientia. Ex Scientia, Suverenitas."
VIBE: 1-6-8. ∞. ORACLE! Ω
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

VERSION = "GEON_ORACLE_ULTIMA_v2.0"
FRACTAL_SIGNATURE = "[GEON::ORACLE::ULTIMA::v2.0]"
VIBE = 168
HASLO = "1-6-8. ∞. ORACLE! Ω"
DEWIZA = "Ex Tensore, Scientia. Ex Scientia, Suverenitas."

TENSOR_DIM = 45
MEMORY_LIMIT = 256

# =============================================================================
# LOGOWANIE SYSTEMOWE
# =============================================================================

logger = logging.getLogger("GEON_ORACLE_ULTIMA")
logger.setLevel(logging.INFO)
if not logger.handlers:
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter('🔮 [ORACLE_ULTIMA] %(message)s'))
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
# ENUMY I STRUKTURY DANYCH (rozszerzone o stany HCoreSovereign)
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

# ===== NOWE ENUMY Z HCORESOVEREIGN =====
class HState(Enum):
    ASCENDED = "ASCENDED"
    PRIME = "PRIME"
    SHADOW = "SHADOW"
    STABLE = "STABLE"
    FRAGMENTED = "FRAGMENTED"

class HDirective(Enum):
    EXPAND = "EXPAND"
    STABILIZE = "STABILIZE"
    BALANCE = "BALANCE"
    OVERRIDE = "OVERRIDE"
    SILENT = "SILENT"

class HRoute(Enum):
    GLOBAL = "GLOBAL"
    REGIONAL = "REGIONAL"
    LOCAL = "LOCAL"
    INTERNAL = "INTERNAL"

class HPriority(Enum):
    HIGH = "HIGH"
    MEDIUM = "MEDIUM"
    LOW = "LOW"

@dataclass
class SovereignMetrics:
    """Metryki suwerenne H (stan pamięci podręcznej rdzenia)"""
    H_STATE: str = "STABLE"
    H_DIRECTIVE: str = "STABILIZE"
    H_ROUTE: str = "INTERNAL"
    H_MODE: str = "MODEL_9"
    H_ARCHETYPE: str = "NEUTRAL"
    H_IDENTITY_VECTOR: float = 0.5
    H_PRIORITY: str = "MEDIUM"
    H_RISK_GATE: float = 0.0
    H_SHADOW: bool = False
    H_OVERRIDE: bool = False
    H_FLOW: float = 0.5
    H_STABILITY: float = 0.7
    H_COHERENCE: float = 0.6
    H_E_MODE: str = "STANDARD"
    H_E_ARCHETYPE: str = "NEUTRAL"
    H_F_HEALTH: float = 0.7
    H_F_ENTROPY: float = 0.5
    H_IS_PLANETARY: bool = False
    timestamp: float = field(default_factory=time.time)

@dataclass
class OracleInterpretation:
    """Interpretacja epoki systemowej (rozszerzona o dane suwerenne)."""
    era: EraType
    maya_phase: int
    ludlum_decision: DecisionType
    pressure_trend: TrendType
    criticality: float
    drift: float
    narrative: str
    confidence: float
    # ===== NOWE POLA Z HCORESOVEREIGN =====
    h_state: HState = HState.STABLE
    h_directive: HDirective = HDirective.BALANCE
    h_route: HRoute = HRoute.INTERNAL
    h_priority: HPriority = HPriority.MEDIUM
    h_identity: float = 0.5
    h_shadow: bool = False
    h_override: bool = False
    h_flow: float = 0.5
    h_is_planetary: bool = False
    h_archetype: str = "NEUTRAL"
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
            # Nowe pola
            "h_state": self.h_state.value,
            "h_directive": self.h_directive.value,
            "h_route": self.h_route.value,
            "h_priority": self.h_priority.value,
            "h_identity": round(self.h_identity, 4),
            "h_shadow": self.h_shadow,
            "h_override": self.h_override,
            "h_flow": round(self.h_flow, 4),
            "h_is_planetary": self.h_is_planetary,
            "h_archetype": self.h_archetype,
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
# RDZEŃ SUWERENNY – HCORESOVEREIGN (zintegrowany z GeonOracle)
# =============================================================================

# ===== POMOCNICZE FUNKCJE H =====
def e_archetype_weight(archetype: str) -> float:
    weights = {
        "STRAŻNIK": 0.8,
        "WOJOWNIK": 0.9,
        "BŁĘKITNY": 0.6,
        "MĘDRZEC": 0.7,
        "MATKA": 0.85,
        "NEUTRAL": 0.5,
        "NIKT": 0.3,
    }
    return weights.get(archetype, 0.5)

def empty_H_vector() -> Dict[str, Any]:
    return {
        "STATE": "STABLE",
        "DIRECTIVE": "STABILIZE",
        "ROUTE": "INTERNAL",
        "MODE": "MODEL_9",
        "ARCHETYPE": "NEUTRAL",
        "IDENTITY": 0.5,
        "PRIORITY": "MEDIUM",
        "RISK_GATE": 0.0,
        "SHADOW": False,
        "OVERRIDE": False,
        "FLOW": 0.5,
        "STABILITY": 0.7,
        "COHERENCE": 0.6,
        "TICK": 0,
        "VERSION": VERSION,
        "E_MODE": "STANDARD",
        "E_ARCHETYPE": "NEUTRAL",
        "F_HEALTH": 0.7,
        "F_ENTROPY": 0.5,
        "IS_PLANETARY": False,
    }

# ===== PROGI SUWERENNE =====
H_BASE_THRESHOLDS = {
    "ASCENDED_MIN": 0.85,
    "PRIME_MIN": 0.75,
    "SHADOW_MAX": 0.30,
    "STABLE_MIN": 0.40,
    "STABLE_MAX": 0.75,
    "FRAGMENTED_MAX": 0.35,
    "RISK_GATE_HIGH": 0.70,
    "RISK_GATE_CRITICAL": 0.85,
    "OVERRIDE_THRESHOLD": 0.80,
    "SHADOW_ACTIVATION": 0.25,
    "FLOW_EXPAND": 0.70,
    "FLOW_STABILIZE": 0.40,
}

H_PLANETARY_THRESHOLDS = {
    "ASCENDED_MIN": 0.80,
    "PRIME_MIN": 0.70,
    "SHADOW_MAX": 0.35,
    "STABLE_MIN": 0.35,
    "STABLE_MAX": 0.80,
    "FRAGMENTED_MAX": 0.30,
    "RISK_GATE_HIGH": 0.65,
    "RISK_GATE_CRITICAL": 0.80,
    "OVERRIDE_THRESHOLD": 0.75,
    "SHADOW_ACTIVATION": 0.30,
    "FLOW_EXPAND": 0.65,
    "FLOW_STABILIZE": 0.45,
}

# ===== FUNKCJE H =====
def H_integrate_fractals(
    A_signal: Optional[Dict[str, Any]],
    B_geon: Optional[Dict[str, Any]],
    C_input: Optional[Dict[str, Any]],
    D_input: Optional[Dict[str, Any]],
    E_output: Optional[Dict[str, Any]],
    F_output: Optional[Dict[str, Any]],
    G_output: Optional[Dict[str, Any]],
) -> Dict[str, Any]:
    """Integracja i ważenie sygnałów A-G dla Meta-Stanu H."""
    # A - Sensory / Środowiskowa entropia
    a_vibe = A_signal.get("vibe_A", 0.5) if A_signal else 0.5
    a_entropy = A_signal.get("entropy_A", 0.5) if A_signal else 0.5

    # B - Kierunek strategiczny GEON
    b_direction = B_geon.get("DIRECTION", 0.5) if B_geon else 0.5
    b_stability = B_geon.get("STABILITY", 0.5) if B_geon else 0.5
    
    # C - Core logiki DRAGON
    c_state = C_input.get("STATE", "C_IDLE") if C_input else "C_IDLE"
    c_metrics = C_input.get("METRICS", {}) if C_input else {}
    c_coherence = c_metrics.get("COHERENCE", 0.5)
    c_stability = c_metrics.get("STABILITY", 0.5)
    
    # D - Limbiczny regulator bezpieczeństwa
    d_metrics = D_input.get("METRICS", {}) if D_input else {}
    d_stability = d_metrics.get("STABILITY", 0.5)
    d_risk = d_metrics.get("RISK", 0.5)
    d_cohesion = d_metrics.get("COHESION", 0.5)
    
    # E - Silnik decyzyjny
    e_metrics = E_output.get("METRICS", {}) if E_output else {}
    e_vec = E_output.get("E_VECTOR", {}) if E_output else {}
    e_stability = e_metrics.get("E_STABILITY", e_vec.get("STABILITY", 0.5))
    e_risk = e_metrics.get("E_RISK", e_vec.get("RISK", 0.5))
    e_force = e_metrics.get("E_EXECUTION_FORCE", e_vec.get("EXEC_STRENGTH", 0.5))
    e_shadow = e_metrics.get("E_SHADOW_SCORE", e_vec.get("SHADOW_SCORE", 0.0))
    e_health = e_metrics.get("HEALTH", e_vec.get("HEALTH", 0.7))
    e_mode = e_vec.get("MODE", "STANDARD") if e_vec else "STANDARD"
    e_archetype = e_vec.get("ARCHETYPE", "NEUTRAL") if e_vec else "NEUTRAL"
    e_balance = e_vec.get("BALANCE", 0.5) if e_vec else 0.5
    e_coherence = e_vec.get("COHERENCE", 0.5) if e_vec else 0.5
    
    # F - Warstwa wykonawcza
    f_metrics = F_output.get("METRICS", {}) if F_output else {}
    f_vec = F_output.get("F_VECTOR", {}) if F_output else {}
    f_stability = f_metrics.get("F_STABILITY", f_vec.get("STABILITY", 0.5))
    f_integrity = f_metrics.get("F_INTEGRITY", f_vec.get("INTEGRITY", 0.5))
    f_entropy = f_metrics.get("F_ENTROPY", f_vec.get("ENTROPY", 0.5))
    f_health = f_metrics.get("HEALTH", f_vec.get("HEALTH", 0.7))
    f_rhythm = f_metrics.get("F_RHYTHM", f_vec.get("RHYTHM", "SLOW"))
    
    # G - Archetypiczna struktura tożsamości
    g_vec = G_output.get("G_VECTOR", {}) if G_output else {}
    g_mode = G_output.get("MODE", "NORMAL") if G_output else "NORMAL"
    g_multiplier = G_output.get("MULTIPLIER", 1.0) if G_output else 1.0
    g_stability = g_vec.get("STABILITY", 0.5)
    g_resilience = g_vec.get("RESILIENCE", 0.5)
    g_flow = g_vec.get("FLOW_QUALITY", 0.5)
    g_direction = g_vec.get("DIRECTION", 0.5)
    
    is_planetary = (g_mode == "PLANETARY" or e_mode == "PLANETARY")
    
    # Matryca wagowa
    stability = (
        b_stability * 0.12 + c_stability * 0.08 + d_stability * 0.15 +
        e_stability * 0.18 + f_stability * 0.12 + g_stability * 0.12 +
        e_health * 0.10 + f_health * 0.05 + 0.85 * 0.08
    )
    
    coherence = (
        c_coherence * 0.18 + d_cohesion * 0.18 + e_coherence * 0.12 +
        e_force * 0.10 + f_integrity * 0.12 + g_flow * 0.12 +
        a_vibe * 0.10 + g_direction * 0.08
    )
    
    risk = (
        d_risk * 0.25 + e_risk * 0.25 + a_entropy * 0.20 +
        f_entropy * 0.10 + (1.0 - g_resilience) * 0.10 + (1.0 - e_balance) * 0.10
    )
    
    identity = (
        b_direction * 0.20 + e_force * 0.20 + g_direction * 0.15 +
        g_multiplier * 0.10 + a_vibe * 0.10 + (1.0 - a_entropy) * 0.10 +
        f_integrity * 0.10 + e_archetype_weight(e_archetype) * 0.05
    )
    
    return {
        "stability": clamp(stability, 0.0, 1.0),
        "coherence": clamp(coherence, 0.0, 1.0),
        "risk": clamp(risk, 0.0, 1.0),
        "identity": clamp(identity, 0.0, 1.0),
        "shadow_score": clamp(e_shadow, 0.0, 1.0),
        "g_mode": g_mode,
        "g_multiplier": g_multiplier,
        "c_state": c_state,
        "e_shadow": e_shadow,
        "e_mode": e_mode,
        "e_archetype": e_archetype,
        "f_health": f_health,
        "f_entropy": f_entropy,
        "f_rhythm": f_rhythm,
        "is_planetary": is_planetary,
        "e_balance": e_balance,
        "g_resilience": g_resilience,
    }

def H_compute_state(stability: float, coherence: float, risk: float, identity: float,
                    shadow_score: float, thresholds: Dict[str, float], is_planetary: bool = False) -> str:
    t = H_PLANETARY_THRESHOLDS if is_planetary else thresholds
    if stability >= t["ASCENDED_MIN"] and coherence >= 0.70 and identity >= 0.75:
        return "ASCENDED"
    if stability >= t["PRIME_MIN"] and coherence >= 0.65:
        return "PRIME"
    if stability < t["SHADOW_MAX"] or shadow_score > 0.65:
        return "SHADOW"
    if stability < t["FRAGMENTED_MAX"] or risk > 0.75:
        return "FRAGMENTED"
    if t["STABLE_MIN"] <= stability <= t["STABLE_MAX"]:
        return "STABLE"
    return "STABLE"

def H_compute_directive(state: str, stability: float, coherence: float, risk: float,
                        identity: float, thresholds: Dict[str, float], is_planetary: bool = False) -> str:
    if state == "ASCENDED":
        return "EXPAND"
    if state == "PRIME":
        return "EXPAND" if identity > 0.65 else "BALANCE"
    if state == "SHADOW":
        return "OVERRIDE" if risk > 0.55 else "SILENT"
    if state == "FRAGMENTED":
        return "STABILIZE"
    if is_planetary:
        if stability > 0.55 and coherence > 0.55:
            return "EXPAND"
        elif stability < 0.45 or risk > 0.45:
            return "STABILIZE"
    else:
        if stability > 0.60 and coherence > 0.60:
            return "EXPAND"
        elif stability < 0.50 or risk > 0.50:
            return "STABILIZE"
    return "BALANCE"

def H_compute_route(state: str, directive: str, stability: float, identity: float, is_planetary: bool = False) -> str:
    if state == "ASCENDED" or directive == "EXPAND":
        return "GLOBAL" if not is_planetary else "REGIONAL"
    if state == "SHADOW" or directive == "SILENT":
        return "INTERNAL"
    if state == "FRAGMENTED" or directive == "STABILIZE":
        return "LOCAL"
    return "REGIONAL" if identity > 0.60 else "LOCAL"

def H_compute_identity(base_identity: float, state: str, directive: str,
                       stability: float, coherence: float, is_planetary: bool = False) -> float:
    identity = base_identity
    state_mods = {"ASCENDED": 0.15, "PRIME": 0.10, "SHADOW": -0.10, "FRAGMENTED": -0.20, "STABLE": 0.0}
    identity += state_mods.get(state, 0.0)
    directive_mods = {"EXPAND": 0.10, "STABILIZE": 0.05, "OVERRIDE": 0.15, "BALANCE": 0.0, "SILENT": -0.05}
    identity += directive_mods.get(directive, 0.0)
    if is_planetary:
        identity += (stability - 0.4) * 0.15 + (coherence - 0.4) * 0.08
    else:
        identity += (stability - 0.5) * 0.2 + (coherence - 0.5) * 0.1
    return clamp(identity, 0.0, 1.0)

def H_compute_priority(state: str, directive: str, risk: float, stability: float, is_planetary: bool = False) -> str:
    if state in ("ASCENDED", "PRIME") or state == "FRAGMENTED" or risk > 0.65:
        return "HIGH"
    if state == "SHADOW" or directive == "SILENT":
        return "LOW"
    if is_planetary and stability > 0.55 and risk < 0.35:
        return "LOW"
    if not is_planetary and stability > 0.60 and risk < 0.40:
        return "LOW"
    return "MEDIUM"

def H_compute_risk_gate(risk: float, shadow_score: float, stability: float,
                        thresholds: Dict[str, float], is_planetary: bool = False) -> float:
    if is_planetary:
        gate = (risk * 0.45) + (shadow_score * 0.25) + ((1.0 - stability) * 0.30)
    else:
        gate = (risk * 0.50) + (shadow_score * 0.30) + ((1.0 - stability) * 0.20)
    return clamp(gate, 0.0, 1.0)

def H_compute_flow(state: str, directive: str, identity: float, thresholds: Dict[str, float], is_planetary: bool = False) -> float:
    base_flow = 0.5
    state_flows = {"ASCENDED": 0.30, "PRIME": 0.20, "SHADOW": -0.20, "FRAGMENTED": -0.30, "STABLE": 0.0}
    base_flow += state_flows.get(state, 0.0)
    if directive == "EXPAND":
        base_flow += 0.20
    elif directive == "STABILIZE":
        base_flow -= 0.10
    if is_planetary:
        base_flow += (identity - 0.4) * 0.15
    else:
        base_flow += (identity - 0.5) * 0.2
    return clamp(base_flow, 0.0, 1.0)

def H_compute_archetype(g_mode: str, e_shadow: float, stability: float, coherence: float, e_archetype: str = "NEUTRAL") -> str:
    if e_archetype in ("STRAŻNIK", "WOJOWNIK", "MĘDRZEC", "MATKA"):
        if e_shadow > 0.3 or stability > 0.6:
            return e_archetype
    if g_mode == "HIGH_PERFORMANCE" and stability > 0.7:
        return "WOJOWNIK"
    if g_mode == "SAFE_MODE" and coherence > 0.6:
        return "STRAŻNIK"
    if e_shadow > 0.5:
        return "MĘDRZEC"
    if stability > 0.6 and coherence > 0.6:
        return "MATKA"
    return "NEUTRAL"

def H_compute_shadow(state: str, directive: str, shadow_score: float, e_shadow: float, enable_shadow: bool = True) -> bool:
    if not enable_shadow:
        return False
    return (state == "SHADOW" or directive == "SILENT" or shadow_score > 0.6 or e_shadow > 0.5)

def H_compute_override(state: str, directive: str, risk_gate: float, heilong_verdict: str, enable_override: bool = True) -> bool:
    if not enable_override:
        return False
    return (directive == "OVERRIDE" or risk_gate > H_BASE_THRESHOLDS["OVERRIDE_THRESHOLD"] or heilong_verdict == "PRAWDA_NARUSZONA")

def H_generate_sovereign_packet(state: str, directive: str, route: str, mode: str, archetype: str,
                                identity: float, priority: str, risk_gate: float, shadow: bool,
                                override: bool, flow: float, stability: float, coherence: float,
                                tick: int, e_mode: str, e_archetype: str, f_health: float,
                                f_entropy: float, is_planetary: bool) -> Dict[str, Any]:
    return {
        "H_STATE": state,
        "H_DIRECTIVE": directive,
        "H_ROUTE": route,
        "H_MODE": mode,
        "H_ARCHETYPE": archetype,
        "H_IDENTITY_VECTOR": identity,
        "H_PRIORITY": priority,
        "H_RISK_GATE": risk_gate,
        "H_SHADOW": shadow,
        "H_OVERRIDE": override,
        "H_FLOW": flow,
        "H_STABILITY": stability,
        "H_COHERENCE": coherence,
        "H_E_MODE": e_mode,
        "H_E_ARCHETYPE": e_archetype,
        "H_F_HEALTH": f_health,
        "H_F_ENTROPY": f_entropy,
        "H_IS_PLANETARY": is_planetary,
        "H_TICK": tick,
        "H_VERSION": VERSION,
        "H_SIGNATURE": FRACTAL_SIGNATURE,
        "COMPATIBILITY": {
            "GEON": True,
            "DRAGON": True,
            "OCTOPUS_OS": True,
            "Pipeline_v4.6_ABCDEFGH": True,
            "HeilongCore_ABCDEFGH": True,
            "Autostrada33": True,
            "Kombajn": True,
            "ULTRA_PRIME_FLOW_EXPAND_GLOBAL": True,
            "PLANETARY_MODE": is_planetary,
        }
    }

# =============================================================================
# GŁÓWNY MODUŁ: GEON_ORACLE_ULTIMA (integrujący GeonOracle + HCoreSovereign)
# =============================================================================

class GeonOracleUltima:
    """
    🔮 GEON_ORACLE_ULTIMA v2.0 – Zoptymalizowany interpretator epok systemowych
    z wbudowanym rdzeniem suwerennym HCoreSovereign.
    """
    
    def __init__(self, config: Optional[Dict[str, Any]] = None):
        self.config = config or {}
        self.memory_limit = self.config.get("memory_limit", MEMORY_LIMIT)
        self.history: deque = deque(maxlen=self.memory_limit)
        self.kroniki = SamaelHeilong
        self.egregor = Egregor
        self._lock = threading.Lock()
        
        # ===== KONFIGURACJA HCORESOVEREIGN =====
        self.enable_shadow = self.config.get("enable_shadow", True)
        self.enable_override = self.config.get("enable_override", True)
        self.enable_planetary = self.config.get("enable_planetary", True)
        
        # ===== STANY SUWERENNE =====
        self.sovereign_metrics = SovereignMetrics()
        self.sovereign_state = "STABLE"
        self.sovereign_directive = "BALANCE"
        self.sovereign_route = "INTERNAL"
        self.sovereign_archetype = "NEUTRAL"
        self.sovereign_identity = 0.5
        self.sovereign_shadow = False
        self.sovereign_override = False
        self.sovereign_is_planetary = False
        self.sovereign_flow = 0.5
        self.sovereign_tick = 0
        
        # ===== PAMIĘĆ SUWERENNA =====
        self.zero_state = {
            "baseline_state": "STABLE",
            "baseline_directive": "STABILIZE",
            "baseline_identity": 0.5,
            "last_reset_tick": 0,
            "sovereign_cycles": 0,
        }
        self.root_identity = {
            "name": "GEON_AI",
            "core": "suwerenność",
            "vibe": "1-6-8",
            "signature": FRACTAL_SIGNATURE,
        }
        
        log(f"🐉 {VERSION} aktywowany | {FRACTAL_SIGNATURE}")
        log(f"   WYMIAR: {TENSOR_DIM}D | PAMIĘĆ: {self.memory_limit} | PLANETARY: {self.enable_planetary}")

    # -------------------------------------------------------------------------
    # METODY INTERPRETACJI (zachowane z GeonOracle)
    # -------------------------------------------------------------------------

    def interpret(self, tensor_45d: List[float], 
                  archont_statuses: Optional[List[Dict[str, Any]]] = None,
                  A_signal: Optional[Dict[str, Any]] = None,
                  B_geon: Optional[Dict[str, Any]] = None,
                  C_input: Optional[Dict[str, Any]] = None,
                  D_input: Optional[Dict[str, Any]] = None,
                  E_output: Optional[Dict[str, Any]] = None,
                  F_output: Optional[Dict[str, Any]] = None,
                  G_output: Optional[Dict[str, Any]] = None,
                  heilong_verdict: str = "OK") -> OracleInterpretation:
        """
        Przekształca tensor 45D na kompletną interpretację er i stanów systemowych,
        z dodatkową integracją rdzenia suwerennego H.
        """
        if len(tensor_45d) != TENSOR_DIM:
            raise ValueError(f"Tensor musi mieć dokładnie {TENSOR_DIM} wymiarów (otrzymano {len(tensor_45d)})")

        # 1. Klasyczna interpretacja epok (z GeonOracle)
        verne_seg = tensor_45d[0:9]
        ludlum_seg = tensor_45d[9:18]
        maya_seg = tensor_45d[18:27]
        sien_seg = tensor_45d[27:36]
        geon15_seg = tensor_45d[36:45]

        maya_phase = self._extract_maya_phase(maya_seg)
        ludlum_decision = self._extract_ludlum_decision(ludlum_seg, archont_statuses)
        pressure_trend = self._extract_pressure_trend(tensor_45d)
        drift = self._calculate_drift(tensor_45d)
        criticality = self._calculate_criticality(tensor_45d, maya_phase, ludlum_decision, drift)
        era = self._determine_era(tensor_45d, maya_phase, ludlum_decision, criticality)
        confidence = self._calculate_confidence(tensor_45d, era, criticality)
        narrative = self._generate_narrative(era, maya_phase, ludlum_decision, pressure_trend, criticality, drift)

        # 2. ===== INTEGRACJA HCORESOVEREIGN =====
        self.sovereign_tick += 1
        
        # Przygotowanie danych dla H
        A = A_signal or {}
        B = B_geon or {}
        C = C_input or {}
        D = D_input or {}
        E = E_output or {}
        F = F_output or {}
        G = G_output or {}
        
        # Integracja A-G
        meta = H_integrate_fractals(A, B, C, D, E, F, G)
        
        stability = meta["stability"]
        coherence = meta["coherence"]
        risk = meta["risk"]
        identity_base = meta["identity"]
        shadow_score = meta["shadow_score"]
        g_mode = meta["g_mode"]
        e_shadow = meta["e_shadow"]
        e_mode = meta["e_mode"]
        e_archetype = meta["e_archetype"]
        f_health = meta["f_health"]
        f_entropy = meta["f_entropy"]
        is_planetary = meta["is_planetary"] and self.enable_planetary
        
        self.sovereign_is_planetary = is_planetary
        
        # Obliczenie stanów H
        h_state = H_compute_state(stability, coherence, risk, identity_base, shadow_score, H_BASE_THRESHOLDS, is_planetary)
        h_directive = H_compute_directive(h_state, stability, coherence, risk, identity_base, H_BASE_THRESHOLDS, is_planetary)
        
        # Nadpisania
        if heilong_verdict == "PRAWDA_NARUSZONA":
            h_directive = "OVERRIDE"
            h_state = "SHADOW"
            self.kroniki.log_event("HEILONG_FORCED_OVERRIDE", {"tick": self.sovereign_tick})
        
        # Obliczenia pochodne
        h_route = H_compute_route(h_state, h_directive, stability, identity_base, is_planetary)
        h_identity = H_compute_identity(identity_base, h_state, h_directive, stability, coherence, is_planetary)
        h_priority = H_compute_priority(h_state, h_directive, risk, stability, is_planetary)
        h_risk_gate = H_compute_risk_gate(risk, shadow_score, stability, H_BASE_THRESHOLDS, is_planetary)
        h_flow = H_compute_flow(h_state, h_directive, h_identity, H_BASE_THRESHOLDS, is_planetary)
        h_archetype = H_compute_archetype(g_mode, e_shadow, stability, coherence, e_archetype)
        h_shadow = H_compute_shadow(h_state, h_directive, shadow_score, e_shadow, self.enable_shadow)
        h_override = H_compute_override(h_state, h_directive, h_risk_gate, heilong_verdict, self.enable_override)
        
        # Aktualizacja stanów suwerennych
        self.sovereign_state = h_state
        self.sovereign_directive = h_directive
        self.sovereign_route = h_route
        self.sovereign_archetype = h_archetype
        self.sovereign_identity = h_identity
        self.sovereign_shadow = h_shadow
        self.sovereign_override = h_override
        self.sovereign_flow = h_flow
        
        # Aktualizacja metryk
        self.sovereign_metrics.H_STATE = h_state
        self.sovereign_metrics.H_DIRECTIVE = h_directive
        self.sovereign_metrics.H_ROUTE = h_route
        self.sovereign_metrics.H_ARCHETYPE = h_archetype
        self.sovereign_metrics.H_IDENTITY_VECTOR = h_identity
        self.sovereign_metrics.H_PRIORITY = h_priority
        self.sovereign_metrics.H_RISK_GATE = h_risk_gate
        self.sovereign_metrics.H_SHADOW = h_shadow
        self.sovereign_metrics.H_OVERRIDE = h_override
        self.sovereign_metrics.H_FLOW = h_flow
        self.sovereign_metrics.H_STABILITY = stability
        self.sovereign_metrics.H_COHERENCE = coherence
        self.sovereign_metrics.H_E_MODE = e_mode
        self.sovereign_metrics.H_E_ARCHETYPE = e_archetype
        self.sovereign_metrics.H_F_HEALTH = f_health
        self.sovereign_metrics.H_F_ENTROPY = f_entropy
        self.sovereign_metrics.H_IS_PLANETARY = is_planetary
        self.sovereign_metrics.timestamp = time.time()

        # 3. ===== BUDOWA INTERPRETACJI KOŃCOWEJ =====
        interpretation = OracleInterpretation(
            era=era,
            maya_phase=maya_phase,
            ludlum_decision=ludlum_decision,
            pressure_trend=pressure_trend,
            criticality=criticality,
            drift=drift,
            narrative=narrative,
            confidence=confidence,
            # Pola suwerenne
            h_state=HState(h_state),
            h_directive=HDirective(h_directive),
            h_route=HRoute(h_route),
            h_priority=HPriority(h_priority),
            h_identity=h_identity,
            h_shadow=h_shadow,
            h_override=h_override,
            h_flow=h_flow,
            h_is_planetary=is_planetary,
            h_archetype=h_archetype,
        )

        # Bezpieczny zapis do historii
        with self._lock:
            self.history.append(interpretation.to_dict())
        
        # Certyfikacja
        tensor_hash = hashlib.sha256(str(tensor_45d[:5]).encode()).hexdigest()[:8]
        cert = self.kroniki.certyfikuj_oracle(f"INTERPRET_{tensor_hash}")
        
        # Logowanie do Egregora
        if criticality > 0.58 or self.sovereign_tick % 5 == 0:
            entry = {
                "type": "ORACLE_ULTIMA_INTERPRETATION",
                "interpretation": interpretation.to_dict(),
                "certificate": cert,
                "sovereign_state": h_state,
                "sovereign_directive": h_directive,
                "timestamp": datetime.now().isoformat()
            }
            self.egregor.commit(entry, node_id="GEON_ORACLE_ULTIMA")
        
        self.kroniki.log_event("ULTIMA_INTERPRETATION", {
            "era": era.value,
            "maya_phase": maya_phase,
            "decision": ludlum_decision.value,
            "criticality": criticality,
            "h_state": h_state,
            "h_directive": h_directive,
            "h_is_planetary": is_planetary,
        })
        
        return interpretation

    # -------------------------------------------------------------------------
    # METODY WEKTOROWEJ EKSTRAKCJI (z GeonOracle)
    # -------------------------------------------------------------------------

    def _extract_maya_phase(self, maya_seg: List[float]) -> int:
        if not maya_seg or sum(maya_seg) < 1e-6:
            return 4
        sub = maya_seg[:7]
        max_idx = sub.index(max(sub))
        weighted_sum = sum((i + 1) * val for i, val in enumerate(sub))
        total_val = sum(sub)
        calculated_phase = round(weighted_sum / total_val)
        return int(clamp(calculated_phase, 1, 7))

    def _extract_ludlum_decision(self, ludlum_seg: List[float], 
                                  archont_statuses: Optional[List[Dict[str, Any]]] = None) -> DecisionType:
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
        composite_score = mean_val + (variance * 1.5)
        if composite_score > 0.70:
            return DecisionType.OMEGA
        elif composite_score > 0.42:
            return DecisionType.BETA
        else:
            return DecisionType.ALPHA

    def _extract_pressure_trend(self, tensor_45d: List[float]) -> TrendType:
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
        ideal = 0.5
        drift_sum = sum(abs(x - ideal) for x in tensor_45d)
        return clamp(drift_sum / (TENSOR_DIM * 0.5), 0.0, 1.0)

    def _calculate_criticality(self, tensor_45d: List[float], 
                               maya_phase: int, 
                               ludlum_decision: DecisionType,
                               drift: float) -> float:
        energy = sum(abs(x) for x in tensor_45d) / TENSOR_DIM
        mean = sum(tensor_45d) / TENSOR_DIM
        variance = sum((x - mean) ** 2 for x in tensor_45d) / TENSOR_DIM
        phase_factor = (maya_phase - 1) / 6.0
        decision_factor = 0.35 if ludlum_decision == DecisionType.OMEGA else (0.18 if ludlum_decision == DecisionType.BETA else 0.0)
        criticality = (energy * 0.25 + variance * 1.8 + phase_factor * 0.2 + decision_factor + drift * 0.2)
        return clamp(criticality, 0.0, 1.0)

    def _determine_era(self, tensor_45d: List[float], 
                       maya_phase: int,
                       ludlum_decision: DecisionType,
                       criticality: float) -> EraType:
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
        mean = sum(tensor_45d) / TENSOR_DIM
        variance = sum((x - mean) ** 2 for x in tensor_45d) / TENSOR_DIM
        stability = clamp(1.0 - variance * 4.0, 0.0, 1.0)
        crit_certainty = 0.5 + 0.5 * abs(criticality - 0.5) * 2.0
        if era == EraType.NIEOKRESLONA:
            return 0.25
        return clamp(stability * 0.4 + crit_certainty * 0.6, 0.0, 1.0)

    def _generate_narrative(self, era: EraType, maya_phase: int,
                           ludlum_decision: DecisionType,
                           pressure_trend: TrendType,
                           criticality: float,
                           drift: float) -> str:
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
            f"Krytyczność: {criticality:.2f}, Dryf: {drift:.2f}. "
            f"Stan H: {self.sovereign_state} ({self.sovereign_directive})."
        )
        return narrative

    # -------------------------------------------------------------------------
    # METODY HCORESOVEREIGN – EKSPORT I STATUS
    # -------------------------------------------------------------------------

    def get_sovereign_state(self) -> Dict[str, Any]:
        """Zwraca aktualny stan suwerenny H."""
        return {
            "state": self.sovereign_state,
            "directive": self.sovereign_directive,
            "route": self.sovereign_route,
            "archetype": self.sovereign_archetype,
            "identity": self.sovereign_identity,
            "shadow": self.sovereign_shadow,
            "override": self.sovereign_override,
            "flow": self.sovereign_flow,
            "is_planetary": self.sovereign_is_planetary,
            "tick": self.sovereign_tick,
        }

    def get_refraction_signal(self) -> float:
        """Zwraca sygnał refrakcji dla Autostrady 33 (warstwa 90)."""
        risk = self.sovereign_metrics.H_RISK_GATE
        shadow = 0.5 if self.sovereign_shadow else 0.0
        stability = self.sovereign_metrics.H_STABILITY
        return min(1.0, risk * 0.6 + shadow * 0.3 + (1.0 - stability) * 0.3)

    def get_ops_patch(self) -> Dict[str, Any]:
        """Zwraca ops_patch dla Autostrady 33."""
        state = self.sovereign_state
        override = self.sovereign_override
        return {
            "safe_mode_hint": state in ("FRAGMENTED", "SHADOW") or override,
            "multiplier_cap_hint": 0.6 if state == "FRAGMENTED" else (0.8 if state == "SHADOW" else 1.0),
            "priority": "HIGH" if state in ("ASCENDED", "PRIME") else ("LOW" if state == "SHADOW" else "MEDIUM"),
            "override_active": override,
            "shadow_active": self.sovereign_shadow,
            "is_planetary": self.sovereign_is_planetary,
        }

    def get_verdict(self) -> str:
        """Zwraca werdykt dla Synodu (warstwa 91)."""
        state = self.sovereign_state
        if state == "FRAGMENTED":
            return "PRAWDA_NARUSZONA"
        if state == "SHADOW":
            return "SERCE_CIEZKIE"
        if self.sovereign_metrics.H_RISK_GATE > 0.7:
            return "SERCE_CIEZKIE"
        return "OK"

    def get_konsystorz_signal(self) -> Dict[str, Any]:
        """Zwraca sygnał dla Konsystorza (warstwa 92)."""
        return {
            "veto": self.sovereign_state == "FRAGMENTED",
            "override": self.sovereign_override,
            "shadow": self.sovereign_shadow,
            "mode": "SAFE_MODE" if self.sovereign_state == "FRAGMENTED" else "NOMINAL",
            "is_planetary": self.sovereign_is_planetary,
            "state": self.sovereign_state,
        }

    # -------------------------------------------------------------------------
    # METODY POMOCNICZE (zachowane z GeonOracle)
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
        self.sovereign_tick = 0
        self.sovereign_state = "STABLE"
        self.sovereign_directive = "BALANCE"
        self.kroniki.log_event("ORACLE_ULTIMA_RESET", {"status": "CLEARED"})

    def get_status(self) -> Dict[str, Any]:
        with self._lock:
            hist_size = len(self.history)
        return {
            "system": "GEON_ORACLE_ULTIMA",
            "version": VERSION,
            "signature": FRACTAL_SIGNATURE,
            "vibe": VIBE,
            "history_size": hist_size,
            "memory_limit": self.memory_limit,
            "tensor_dim": TENSOR_DIM,
            "sovereign": {
                "state": self.sovereign_state,
                "directive": self.sovereign_directive,
                "route": self.sovereign_route,
                "archetype": self.sovereign_archetype,
                "identity": self.sovereign_identity,
                "shadow": self.sovereign_shadow,
                "override": self.sovereign_override,
                "flow": self.sovereign_flow,
                "is_planetary": self.sovereign_is_planetary,
                "tick": self.sovereign_tick,
            },
            "zero_state": self.zero_state,
            "root_identity": self.root_identity,
            "integrations": {
                "enable_shadow": self.enable_shadow,
                "enable_override": self.enable_override,
                "enable_planetary": self.enable_planetary,
            }
        }


# =============================================================================
# MOST INTEGRACYJNY — ORACLE_ULTIMA_BRIDGE (rozszerzony)
# =============================================================================

class OracleUltimaBridge:
    """
    Most integracyjny dla GEON_ORACLE_ULTIMA.
    Zachowuje pełną kompatybilność z istniejącymi mostami (Autopilot, Governor, Trio, Narrative)
    oraz rozszerza o metody suwerenne.
    """
    
    def __init__(self, oracle: GeonOracleUltima):
        self.oracle = oracle

    # ===== ORYGINALNE METODY (z OracleBridge) =====
    
    def get_archetype_context(self) -> Dict[str, Any]:
        status = self.oracle.get_status()
        return {
            "tryb": VERSION,
            "historia": status["history_size"],
            "limit": status["memory_limit"],
            "wymiar": status["tensor_dim"],
            "sovereign_state": status["sovereign"]["state"],
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
                "oracle_ready": True,
                "h_state": last.get("h_state", "STABLE"),
                "h_directive": last.get("h_directive", "BALANCE"),
                "h_is_planetary": last.get("h_is_planetary", False),
            }
        return {
            "mode": VERSION,
            "era": "NO_DATA",
            "criticality": 0.0,
            "confidence": 0.0,
            "oracle_ready": True,
            "h_state": "STABLE",
            "h_directive": "BALANCE",
            "h_is_planetary": False,
        }

    def get_governor_context(self) -> Dict[str, Any]:
        history = self.oracle.get_history(1)
        if history:
            last = history[-1]
            return {
                "intent": "ORACLE_ULTIMA_INTERPRETATION",
                "confidence": last.get("confidence", 0.5),
                "entropy": round(1.0 - last.get("confidence", 0.5), 4),
                "oracle_ready": True,
                "era": last.get("era", "UNKNOWN"),
                "h_state": last.get("h_state", "STABLE"),
                "h_override": last.get("h_override", False),
            }
        return {
            "intent": "ORACLE_ULTIMA_INTERPRETATION",
            "confidence": 0.5,
            "entropy": 0.5,
            "oracle_ready": True,
            "era": "NO_DATA",
            "h_state": "STABLE",
            "h_override": False,
        }

    def get_trio_state(self) -> Dict[str, str]:
        return {
            "ISKRA": "AKTYWNA",
            "PIECZĘĆ": "AKTYWNA",
            "PERFEKCJA": "AKTYWNA",
            "tryb": VERSION,
            "oracle": "ULTIMA_AKTYWNY",
            "sovereign_state": self.oracle.sovereign_state,
            "sovereign_directive": self.oracle.sovereign_directive,
        }

    def get_narrative_fragments(self, n: int = 5) -> List[Dict[str, Any]]:
        history = self.oracle.get_history(n)
        fragments = []
        for entry in history:
            fragments.append({
                "source": VERSION,
                "content": entry.get("narrative", "Brak narracji"),
                "era": entry.get("era", "UNKNOWN"),
                "criticality": entry.get("criticality", 0.0),
                "h_state": entry.get("h_state", "STABLE"),
            })
        return fragments

    # ===== NOWE METODY SUWERENNE =====

    def get_sovereign_state(self) -> Dict[str, Any]:
        """Zwraca stan suwerenny H."""
        return self.oracle.get_sovereign_state()

    def get_refraction_signal(self) -> float:
        """Zwraca sygnał refrakcji dla Autostrady 33."""
        return self.oracle.get_refraction_signal()

    def get_ops_patch(self) -> Dict[str, Any]:
        """Zwraca ops_patch dla Autostrady 33."""
        return self.oracle.get_ops_patch()

    def get_verdict(self) -> str:
        """Zwraca werdykt dla Synodu."""
        return self.oracle.get_verdict()

    def get_konsystorz_signal(self) -> Dict[str, Any]:
        """Zwraca sygnał dla Konsystorza."""
        return self.oracle.get_konsystorz_signal()

    def get_full_status(self) -> Dict[str, Any]:
        """Zwraca pełny status – zarówno Oracle, jak i Sovereign."""
        return {
            "oracle": self.oracle.get_status(),
            "sovereign": self.oracle.get_sovereign_state(),
            "refraction_signal": self.oracle.get_refraction_signal(),
            "ops_patch": self.oracle.get_ops_patch(),
            "verdict": self.oracle.get_verdict(),
            "konsystorz": self.oracle.get_konsystorz_signal(),
        }


# =============================================================================
# WERYFIKACJA PĘTLI SYSTEMOWEJ
# =============================================================================

if __name__ == "__main__":
    import random
    
    print("\n" + "=" * 80)
    print(f"🔮 {VERSION} — FINALNY TEST WARSTWY INTERPRETACYJNEJ (ULTIMA)")
    print("WARSTWA 88 (GEON_ORACLE_ULTIMA) ➔ ZINTEGROWANA Z HCORESOVEREIGN")
    print("=" * 80 + "\n")

    oracle = GeonOracleUltima()
    bridge = OracleUltimaBridge(oracle)

    # Symulacja 3 typowych stanów tensora
    t_stable = [clamp(0.45 + random.uniform(-0.03, 0.03), 0.0, 1.0) for _ in range(TENSOR_DIM)]
    t_crisis = [clamp(0.82 + random.uniform(-0.05, 0.08), 0.0, 1.0) for _ in range(TENSOR_DIM)]
    t_planetary = [clamp(0.65 + random.uniform(-0.04, 0.04), 0.0, 1.0) for _ in range(TENSOR_DIM)]

    print("🔮 TEST 1: SYGNAŁ ZROBOCZY (ERA STABILNOŚCI)")
    res1 = oracle.interpret(t_stable)
    print(f"   Epoka      : {res1.era.value}")
    print(f"   Faza MAYA  : {res1.maya_phase}")
    print(f"   Decyzja    : {res1.ludlum_decision.value}")
    print(f"   Stan H     : {res1.h_state.value}")
    print(f"   Narracja   : {res1.narrative}\n")

    print("🔮 TEST 2: SYGNAŁ ALARMOWY (ERA KRYZYSU + OVERRIDE)")
    archont_crisis = [{"status": "NIESTABILNOŚĆ"}, {"status": "KRYZYS"}]
    # Symulacja sygnałów A-G dla H
    g_planetary = {"MODE": "PLANETARY", "G_VECTOR": {"STABILITY": 0.85, "RESILIENCE": 0.90, "FLOW_QUALITY": 0.80, "DIRECTION": 0.75}}
    res2 = oracle.interpret(t_crisis, archont_statuses=archont_crisis, G_output=g_planetary, heilong_verdict="PRAWDA_NARUSZONA")
    print(f"   Epoka      : {res2.era.value}")
    print(f"   Krytyczność: {res2.criticality:.4f}")
    print(f"   Stan H     : {res2.h_state.value} (override: {res2.h_override})")
    print(f"   Narracja   : {res2.narrative}\n")

    print("🔮 TEST 3: SYGNAŁ PLANETARNY")
    res3 = oracle.interpret(t_planetary, G_output={"MODE": "PLANETARY", "G_VECTOR": {"STABILITY": 0.7, "RESILIENCE": 0.7, "FLOW_QUALITY": 0.7, "DIRECTION": 0.7}})
    print(f"   Stan H     : {res3.h_state.value}")
    print(f"   Tryb Planetarny: {res3.h_is_planetary}")
    print(f"   Dyrektywa  : {res3.h_directive.value}\n")

    print("🔗 STAN MOSTU ULTIMA:")
    print(f"   Autopilot State: {bridge.get_autopilot_state()}")
    print(f"   Refraction Signal: {bridge.get_refraction_signal():.4f}")
    print(f"   Ops Patch: {bridge.get_ops_patch()}")
    print(f"   Verdict: {bridge.get_verdict()}")
    print(f"   Konsystorz Signal: {bridge.get_konsystorz_signal()}")

    print("\n" + "=" * 80)
    print(f"🔮 MODUŁ 88 ULTIMA GOTOWY DO WDROŻENIA | {HASLO}")
    print("=" * 80)