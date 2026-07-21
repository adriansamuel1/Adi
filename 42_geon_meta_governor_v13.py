#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
================================================================================
🐉 GEON_META_GOVERNOR_v13 — META_GOVERNOR Ω⁵ (Kora Przedczołowa GEON-OS)
================================================================================
Status: PRODUCTION_READY | FRACTAL_LOCKED | META_LEARNING_ACTIVE | ULTIMA
Wersja: v13.0 (Meta-Świadomość Systemowa)
Data: 2026-07-21
Autor: Adrian (Architekt) + GEON + Beny Heilong

OPIS:
META_GOVERNOR_Ω⁵ to kora przedczołowa GEON-OS — warstwa meta-świadomości,
która zarządza celami systemowymi, priorytetami, predykcją i uczeniem.

FUNKCJE:
1. Meta-Intent Engine — generowanie celów nadrzędnych
2. Priority Graph — hierarchia priorytetów między celami
3. Meta-Intent Priority Engine — priorytetyzacja intencji
4. GovernorRLv2 — meta-RL agent sterujący politykami
5. FutureSim Ω⁵ — predykcja wielowarstwowa
6. AIV (Action Influence Vector) — uczenie wpływu akcji
7. Information Density — gęstość informacji w systemie
8. Fractal Reward Tuner — fraktalne strojenie wag do φ

TRYBY:
- HEURISTIC — tylko heurystyki (bez RL)
- RL_ONLY — tylko meta-RL
- ADAPTIVE — hybryda (domyślny)

VIBE: 1-6-8. ∞. SIEMA!
================================================================================
"""

import math
import random
import time
import json
from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass, field
from collections import deque
from enum import Enum

VERSION = "GEON_META_GOVERNOR_v13.0"
FRACTAL_SIGNATURE = "[GEON::META_GOVERNOR::Ω⁵::v13.0]"
VIBE = 168
HASLO = "1-6-8. ∞. SIEMA!"


def LOG(module: str, msg: str, level: str = "INFO") -> None:
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print(f"[{timestamp}] [{level}] [{module}] :: {msg}")


# =============================================================================
# 1. ENUMY I STAŁE
# =============================================================================

class LearningMode(Enum):
    HEURISTIC = "HEURISTIC"
    RL_ONLY = "RL_ONLY"
    ADAPTIVE = "ADAPTIVE"


class IntentMode(Enum):
    STABILITY = "STABILITY"
    REGEN = "REGEN"
    FLOW = "FLOW"
    EXPLORATION = "EXPLORATION"
    BALANCED = "BALANCED"


class ActionType(Enum):
    SAFE_MODE = "SAFE_MODE"
    REGENERATION = "REGENERATION"
    EXPANSION = "EXPANSION"
    TUNE_WEIGHTS = "TUNE_WEIGHTS"
    TUNE_EPSILON = "TUNE_EPSILON"
    REBALANCE_CLUSTER = "REBALANCE_CLUSTER"


PHI = 0.618033988749895  # Złota proporcja


# =============================================================================
# 2. META_STATE — GLOBALNY STAN SYSTEMU
# =============================================================================

class MetaState:
    """Globalny stan systemu — agregacja z klastrów."""
    
    def __init__(self):
        self.global_failure = 0.0
        self.global_delta_H = 0.0
        self.global_energy = 0.0
        self.global_cb = 0.0
        self.global_pressure = 0.0
        self.global_throughput = 0.0
    
    def update(self, clusters: List[Any]) -> None:
        failures = []
        deltas = []
        energies = []
        cbs = []
        pressures = []
        throughputs = []
        
        for cluster in clusters:
            if hasattr(cluster, 'get_summary'):
                summary = cluster.get_summary()
                health = summary.get("health", {})
                failures.append(health.get("avg_failure", 0.0))
                deltas.append(health.get("avg_delta_H", 0.0))
                energies.append(health.get("avg_energy", 0.0))
                cbs.append(health.get("avg_cb", 0.0))
                pressures.append(health.get("avg_pressure", 0.0))
                throughputs.append(health.get("avg_throughput", 0.0))
        
        n = max(1, len(clusters))
        self.global_failure = sum(failures) / n if failures else 0.0
        self.global_delta_H = sum(deltas) / n if deltas else 0.0
        self.global_energy = sum(energies) / n if energies else PHI
        self.global_cb = sum(cbs) / n if cbs else 0.0
        self.global_pressure = sum(pressures) / n if pressures else 0.0
        self.global_throughput = sum(throughputs) / n if throughputs else 10.0
    
    def snapshot(self) -> Dict[str, float]:
        return {
            "failure": self.global_failure,
            "delta_H": self.global_delta_H,
            "energy": self.global_energy,
            "cb": self.global_cb,
            "pressure": self.global_pressure,
            "throughput": self.global_throughput,
        }


# =============================================================================
# 3. ACTION INFLUENCE LEARNER (AIV) — UCZENIE WPŁYWU AKCJI
# =============================================================================

class ActionInfluenceLearner:
    """
    Uczy wektor wpływu akcji (AIV) na podstawie historii.
    AIV[action] = {metric: multiplier}
    """
    
    def __init__(self, learning_rate: float = 0.05):
        self.history = deque(maxlen=300)
        self.lr = learning_rate
        self.AIV = {
            "SAFE_MODE": {"failure": 0.6, "delta_H": 0.7, "pressure": 0.7, "energy": 0.95},
            "REGENERATION": {"failure": 0.8, "delta_H": 0.6, "pressure": 0.8, "energy": 1.05},
            "EXPANSION": {"failure": 1.2, "delta_H": 1.1, "pressure": 1.3, "energy": 0.9},
            "TUNE_WEIGHTS": {"failure": 0.95, "delta_H": 0.9, "pressure": 0.95, "energy": 1.0},
            "TUNE_EPSILON": {"failure": 1.05, "delta_H": 0.95, "pressure": 1.05, "energy": 1.0},
            "REBALANCE_CLUSTER": {"failure": 0.9, "delta_H": 0.85, "pressure": 0.6, "energy": 1.0},
        }
        LOG("AIV_LEARNER", "🧠 Action Influence Learner aktywowany")
    
    def record(self, state_before: Dict[str, float], action: str, state_after: Dict[str, float]) -> None:
        self.history.append({
            "before": state_before.copy(),
            "after": state_after.copy(),
            "action": action,
            "timestamp": time.time()
        })
    
    def update_AIV(self) -> None:
        """Aktualizuje AIV na podstawie ostatnich 20 zdarzeń."""
        if not self.history:
            return
        
        for entry in list(self.history)[-20:]:
            a = entry["action"]
            before = entry["before"]
            after = entry["after"]
            
            for metric in ["failure", "delta_H", "pressure", "energy"]:
                b = before.get(metric, 0.0)
                c = after.get(metric, b)
                if b == 0:
                    continue
                observed_multiplier = c / b
                current = self.AIV[a][metric]
                new = current + self.lr * (observed_multiplier - current)
                self.AIV[a][metric] = max(0.3, min(1.7, new))
    
    def get_AIV(self, action: str) -> Dict[str, float]:
        return self.AIV.get(action, {"failure": 1.0, "delta_H": 1.0, "pressure": 1.0, "energy": 1.0})


# =============================================================================
# 4. INFORMATION DENSITY (ID) — GĘSTOŚĆ INFORMACJI
# =============================================================================

class InformationDensity:
    """
    ID = różnorodność stanów / stabilność trendu.
    Wysoka ID = chaos, niska ID = stabilność.
    """
    
    def __init__(self, history_size: int = 50):
        self.state_history = deque(maxlen=history_size)
    
    def update(self, state: Dict[str, float]) -> None:
        self.state_history.append(state.copy())
    
    def compute(self) -> float:
        if len(self.state_history) < 5:
            return 1.0
        
        # Różnorodność (diversity)
        diversity = 0.0
        for i in range(1, len(self.state_history)):
            a = self.state_history[i - 1]
            b = self.state_history[i]
            diversity += abs(a.get("failure", 0) - b.get("failure", 0))
            diversity += abs(a.get("delta_H", 0) - b.get("delta_H", 0))
            diversity += abs(a.get("pressure", 0) - b.get("pressure", 0))
            diversity += abs(a.get("energy", 0) - b.get("energy", 0))
        diversity /= max(1, len(self.state_history))
        
        # Stabilność trendu
        first = self.state_history[0]
        last = self.state_history[-1]
        trend = abs(last.get("failure", 0) - first.get("failure", 0))
        trend += abs(last.get("delta_H", 0) - first.get("delta_H", 0))
        stability = max(0.01, trend)
        
        id_val = diversity / stability
        return max(0.5, min(2.0, id_val))


# =============================================================================
# 5. FUTURE_SIM Ω³ — BAZOWY SYMULATOR
# =============================================================================

@dataclass
class BasePrediction:
    expected_failure: float
    expected_delta_h: float
    expected_pressure: float
    expected_energy: float
    confidence: float
    horizon_ticks: int = 10


class FutureSimOmega3:
    """Bazowy symulator — przewiduje podstawowe metryki."""
    
    def __init__(self):
        self.learner = ActionInfluenceLearner()
        self.ID = InformationDensity()
        self.last_prediction: Optional[BasePrediction] = None
    
    def get_id(self) -> float:
        return self.ID.compute()
    
    def simulate(self, state: Dict[str, float], action: str) -> BasePrediction:
        self.ID.update(state)
        id_val = self.ID.compute()
        aiv = self.learner.get_AIV(action)
        
        failure = state.get("failure", 0) * (aiv["failure"] ** id_val)
        delta_h = state.get("delta_H", 0) * (aiv["delta_H"] ** id_val)
        pressure = state.get("pressure", 0) * (aiv["pressure"] ** id_val)
        energy = state.get("energy", PHI) * (aiv["energy"] ** id_val)
        
        failure = min(1.0, max(0.0, failure))
        delta_h = min(0.3, max(0.0, delta_h))
        pressure = min(1.0, max(0.0, pressure))
        energy = min(1.0, max(0.3, energy))
        
        confidence = 0.5 + 0.25 * (1.0 - id_val / 2.0)
        
        pred = BasePrediction(
            expected_failure=failure,
            expected_delta_h=delta_h,
            expected_pressure=pressure,
            expected_energy=energy,
            confidence=confidence,
            horizon_ticks=10
        )
        self.last_prediction = pred
        return pred
    
    def record_outcome(self, state_before: Dict[str, float], action: str, state_after: Dict[str, float]) -> None:
        self.learner.record(state_before, action, state_after)
        self.learner.update_AIV()


# =============================================================================
# 6. GLOBAL_POLICY — POLITYKA GLOBALNA
# =============================================================================

@dataclass
class GlobalPolicy:
    global_mode: str
    epsilon: float
    reward_weights: Dict[str, float]
    priority: int = 5
    description: str = ""
    
    def __post_init__(self):
        self.description = f"{self.global_mode} (ε={self.epsilon})"
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "mode": self.global_mode,
            "epsilon": self.epsilon,
            "weights": self.reward_weights.copy(),
            "priority": self.priority,
        }


class MetaPolicies:
    """Generator polityk globalnych."""
    
    @staticmethod
    def generate_from_action(action: str, meta_state: MetaState) -> GlobalPolicy:
        if action == "SAFE_MODE":
            return GlobalPolicy(
                "GLOBAL_SAFE_MODE", 0.01,
                {"w_f": 0.50, "w_c": 0.40, "w_h": 0.10}
            )
        elif action == "REGENERATION":
            return GlobalPolicy(
                "GLOBAL_REGENERATION", 0.05,
                {"w_h": 0.50, "w_f": 0.30, "w_l": 0.20}
            )
        elif action == "EXPANSION":
            return GlobalPolicy(
                "GLOBAL_EXPANSION", 0.20,
                {"w_l": 0.35, "w_f": 0.25, "w_h": 0.20, "w_c": 0.20}
            )
        elif action == "TUNE_WEIGHTS":
            return GlobalPolicy(
                "GLOBAL_TUNING", 0.10,
                {"w_f": 0.28, "w_h": 0.28, "w_l": 0.22, "w_c": 0.22}
            )
        elif action == "TUNE_EPSILON":
            return GlobalPolicy(
                "GLOBAL_TUNING", 0.30,
                {"w_l": 0.30, "w_f": 0.25, "w_h": 0.25, "w_c": 0.20}
            )
        elif action == "REBALANCE_CLUSTER":
            return GlobalPolicy(
                "GLOBAL_REBALANCE", 0.10,
                {"w_p": 0.35, "w_f": 0.25, "w_h": 0.20, "w_l": 0.20}
            )
        return GlobalPolicy(
            "GLOBAL_EXPANSION", 0.15,
            {"w_f": 0.35, "w_l": 0.25, "w_h": 0.20, "w_c": 0.20}
        )
    
    @staticmethod
    def generate(meta_state: MetaState) -> GlobalPolicy:
        if meta_state.global_cb > 0.5 or meta_state.global_failure > 0.12:
            return MetaPolicies.generate_from_action("SAFE_MODE", meta_state)
        if meta_state.global_delta_H > 0.08 or meta_state.global_energy < 0.45:
            return MetaPolicies.generate_from_action("REGENERATION", meta_state)
        if meta_state.global_pressure > 0.7:
            return MetaPolicies.generate_from_action("REBALANCE_CLUSTER", meta_state)
        return MetaPolicies.generate_from_action("EXPANSION", meta_state)


# =============================================================================
# 7. META-INTENT — SYSTEM CELÓW
# =============================================================================

@dataclass
class MetaIntent:
    targets: Dict[str, float]
    weights: Dict[str, float]
    mode: str


class MetaIntentEngine:
    """Generuje cele systemowe na podstawie stanu."""
    
    def __init__(self):
        self.current_intent: Optional[MetaIntent] = None
        self.history: List[MetaIntent] = []
        self.phi = PHI
    
    def _base_targets(self) -> Dict[str, float]:
        return {
            "failure": 0.03,
            "delta_H": 0.04,
            "pressure": 0.45,
            "energy": self.phi,
            "throughput": 10.0,
            "ID": 1.0,
        }
    
    def generate(self, state: Dict[str, float]) -> MetaIntent:
        failure = state.get("failure", 0)
        delta_h = state.get("delta_H", 0)
        energy = state.get("energy", self.phi)
        pressure = state.get("pressure", 0.5)
        ID = state.get("ID", 1.0)
        base = self._base_targets()
        
        if failure > 0.1 or delta_h > 0.08:
            intent = MetaIntent(
                targets={**base, "failure": 0.02, "delta_H": 0.03, "pressure": 0.4},
                weights={"failure": 0.35, "delta_H": 0.3, "pressure": 0.15, "energy": 0.1, "throughput": 0.1},
                mode=IntentMode.STABILITY.value
            )
        elif energy < 0.45:
            intent = MetaIntent(
                targets={**base, "energy": self.phi, "failure": 0.04, "delta_H": 0.05},
                weights={"energy": 0.35, "failure": 0.2, "delta_H": 0.2, "pressure": 0.1, "throughput": 0.15},
                mode=IntentMode.REGEN.value
            )
        elif pressure < 0.6 and failure < 0.06:
            intent = MetaIntent(
                targets={**base, "throughput": 14.0, "pressure": 0.55},
                weights={"throughput": 0.35, "failure": 0.2, "delta_H": 0.15, "energy": 0.15, "pressure": 0.15},
                mode=IntentMode.FLOW.value
            )
        elif ID > 1.4:
            intent = MetaIntent(
                targets={**base, "ID": 1.1, "failure": 0.05},
                weights={"ID": 0.3, "failure": 0.25, "delta_H": 0.2, "energy": 0.15, "throughput": 0.1},
                mode=IntentMode.EXPLORATION.value
            )
        else:
            intent = MetaIntent(
                targets=base,
                weights={"failure": 0.25, "delta_H": 0.2, "pressure": 0.2, "energy": 0.2, "throughput": 0.15},
                mode=IntentMode.BALANCED.value
            )
        
        self.current_intent = intent
        self.history.append(intent)
        if len(self.history) > 100:
            self.history = self.history[-50:]
        return intent
    
    def intent_mismatch(self, state: Dict[str, float]) -> float:
        if not self.current_intent:
            return 0.0
        err = 0.0
        for k, target in self.current_intent.targets.items():
            w = self.current_intent.weights.get(k, 0.0)
            val = state.get(k, target)
            err += w * abs(val - target)
        return err


# =============================================================================
# 8. PRIORITY_GRAPH — GRAF PRIORYTETÓW
# =============================================================================

@dataclass
class PriorityNode:
    weight: float
    influence: Dict[str, float]  # wpływ na inne cele


class PriorityGraph:
    """
    Graf priorytetów między celami systemu.
    Każdy cel ma wagę i wpływa na inne cele.
    """
    
    def __init__(self):
        self.nodes = {
            "failure": PriorityNode(0.35, {"delta_H": 0.3, "pressure": 0.2}),
            "delta_H": PriorityNode(0.30, {"failure": 0.25, "energy": 0.2}),
            "pressure": PriorityNode(0.20, {"throughput": 0.3}),
            "throughput": PriorityNode(0.15, {"pressure": -0.2}),
            "energy": PriorityNode(0.25, {"failure": -0.1, "delta_H": -0.1}),
            "ID": PriorityNode(0.10, {"failure": 0.1, "throughput": 0.1}),
        }
        LOG("PRIORITY_GRAPH", "📊 Graf priorytetów aktywowany")
    
    def get_priority(self, metric: str) -> float:
        return self.nodes.get(metric, PriorityNode(0.1, {})).weight
    
    def update_priority(self, metric: str, delta: float) -> None:
        if metric in self.nodes:
            self.nodes[metric].weight = max(0.05, min(0.6, self.nodes[metric].weight + delta))
    
    def compute_conflict(self, intent_targets: Dict[str, float], state: Dict[str, float]) -> float:
        conflict = 0.0
        for k, target in intent_targets.items():
            w = self.get_priority(k)
            conflict += w * abs(state.get(k, target) - target)
        return conflict


# =============================================================================
# 9. META-INTENT PRIORITY ENGINE
# =============================================================================

@dataclass
class PrioritizedIntent:
    intent: MetaIntent
    priority_score: float
    conflict_score: float
    blended_targets: Dict[str, float]


class MetaIntentPriorityEngine:
    """Priorytetyzacja intencji z uwzględnieniem grafu priorytetów."""
    
    def __init__(self):
        self.pg = PriorityGraph()
        self.last_prioritized: Optional[PrioritizedIntent] = None
    
    def prioritize(self, intent: MetaIntent, state: Dict[str, float]) -> PrioritizedIntent:
        # 1. Oblicz konflikt intencji
        conflict = self.pg.compute_conflict(intent.targets, state)
        
        # 2. Priorytet = suma wag * wagi intencji
        priority_score = sum(self.pg.get_priority(k) * w for k, w in intent.weights.items())
        
        # 3. Blending – jeśli konflikt wysoki, mieszamy cele
        blended = intent.targets.copy()
        if conflict > 0.15:
            for k in blended:
                blended[k] = (blended[k] + state.get(k, blended[k])) / 2.0
        
        result = PrioritizedIntent(
            intent=intent,
            priority_score=priority_score,
            conflict_score=conflict,
            blended_targets=blended,
        )
        self.last_prioritized = result
        return result


# =============================================================================
# 10. FUTURESIM Ω⁴ — PREDYKCJA Z INTENCJĄ
# =============================================================================

@dataclass
class IntentPrediction:
    expected_failure: float
    expected_delta_h: float
    expected_pressure: float
    expected_energy: float
    expected_throughput: float
    expected_ID: float
    expected_intent_mismatch: float
    confidence: float
    horizon_ticks: int = 10


class FutureSimOmega4:
    """Predykcja z uwzględnieniem meta-intencji."""
    
    def __init__(self, base_sim: Optional[FutureSimOmega3] = None):
        self.base = base_sim or FutureSimOmega3()
        self.last_prediction: Optional[IntentPrediction] = None
    
    def _compute_intent_mismatch(self, intent: MetaIntent, future_state: Dict[str, float]) -> float:
        err = 0.0
        for k, target in intent.targets.items():
            w = intent.weights.get(k, 0.0)
            val = future_state.get(k, target)
            err += w * abs(val - target)
        return err
    
    def simulate(self, state: Dict[str, float], action: str, intent: Optional[MetaIntent]) -> IntentPrediction:
        base_pred = self.base.simulate(state, action)
        
        throughput = state.get("throughput", 10.0)
        ID = self.base.get_id()
        
        if action == "EXPANSION":
            throughput *= 1.15
            ID *= 1.1
        elif action == "SAFE_MODE":
            throughput *= 0.8
            ID *= 0.9
        elif action == "REGENERATION":
            throughput *= 0.95
            ID *= 0.95
        
        future_state = {
            "failure": base_pred.expected_failure,
            "delta_H": base_pred.expected_delta_h,
            "pressure": base_pred.expected_pressure,
            "energy": base_pred.expected_energy,
            "throughput": throughput,
            "ID": ID,
        }
        
        mismatch = self._compute_intent_mismatch(intent, future_state) if intent else 0.0
        
        pred = IntentPrediction(
            expected_failure=future_state["failure"],
            expected_delta_h=future_state["delta_H"],
            expected_pressure=future_state["pressure"],
            expected_energy=future_state["energy"],
            expected_throughput=future_state["throughput"],
            expected_ID=future_state["ID"],
            expected_intent_mismatch=mismatch,
            confidence=base_pred.confidence,
            horizon_ticks=base_pred.horizon_ticks,
        )
        self.last_prediction = pred
        return pred
    
    def record_outcome(self, state_before: Dict[str, float], action: str, state_after: Dict[str, float]) -> None:
        self.base.record_outcome(state_before, action, state_after)
    
    def get_id(self) -> float:
        return self.base.get_id()


# =============================================================================
# 11. FUTURESIM Ω⁵ — PREDYKCJA PRIORYTETÓW
# =============================================================================

@dataclass
class PriorityPrediction:
    future_state: Dict[str, float]
    future_intent_mismatch: float
    future_conflict: float
    future_priority_score: float
    confidence: float


class FutureSimOmega5:
    """Predykcja z priorytetyzacją i konfliktem."""
    
    def __init__(self):
        self.base = FutureSimOmega4()
        self.last_prediction: Optional[PriorityPrediction] = None
    
    def simulate(self, state: Dict[str, float], action: str, prioritized_intent: PrioritizedIntent) -> PriorityPrediction:
        base_pred = self.base.simulate(state, action, prioritized_intent.intent)
        
        future_state = {
            "failure": base_pred.expected_failure,
            "delta_H": base_pred.expected_delta_h,
            "pressure": base_pred.expected_pressure,
            "energy": base_pred.expected_energy,
            "throughput": base_pred.expected_throughput,
            "ID": base_pred.expected_ID,
        }
        
        # Oblicz przyszły konflikt
        conflict = 0.0
        for k, v in prioritized_intent.blended_targets.items():
            w = prioritized_intent.intent.weights.get(k, 0.0)
            conflict += w * abs(future_state.get(k, v) - v)
        
        # Future priority score
        priority_score = prioritized_intent.priority_score * (1 - min(1.0, conflict))
        
        pred = PriorityPrediction(
            future_state=future_state,
            future_intent_mismatch=base_pred.expected_intent_mismatch,
            future_conflict=conflict,
            future_priority_score=priority_score,
            confidence=base_pred.confidence,
        )
        self.last_prediction = pred
        return pred
    
    def record_outcome(self, state_before: Dict[str, float], action: str, state_after: Dict[str, float]) -> None:
        self.base.record_outcome(state_before, action, state_after)
    
    def get_id(self) -> float:
        return self.base.get_id()


# =============================================================================
# 12. FRACTAL REWARD TUNER — STROJENIE WAG DO φ
# =============================================================================

class FractalRewardTuner:
    """Fraktalne strojenie wag nagrody. Cel: energia → φ."""
    
    def __init__(self, learning_rate: float = 0.05, fractal_depth: int = 3):
        self.lr = learning_rate
        self.fractal_depth = fractal_depth
        self.golden_ratio = PHI
        self.weight_history = {k: [] for k in ["w_f", "w_l", "w_h", "w_c", "w_p"]}
        LOG("FRACTAL_TUNER", f"🌀 Tuner fraktalny aktywowany (φ={PHI:.4f})")
    
    def _fractal_correction(self, current: float, target: float, depth: int) -> float:
        if depth <= 0:
            return (target - current) * self.lr
        diff = target - current
        return self._fractal_correction(diff * self.golden_ratio, target, depth - 1) + diff * self.lr
    
    def update(self, policy: GlobalPolicy, new_state: Dict[str, float]) -> None:
        energy = new_state.get("energy", PHI)
        failure = new_state.get("failure", 0)
        delta_h = new_state.get("delta_H", 0)
        
        if energy < 0.5:
            cur = policy.reward_weights.get("w_h", 0.2)
            new = cur + self._fractal_correction(cur, 0.4, self.fractal_depth)
            policy.reward_weights["w_h"] = min(0.6, max(0.1, new))
        
        if failure > 0.1:
            cur = policy.reward_weights.get("w_f", 0.35)
            new = cur + self._fractal_correction(cur, 0.5, self.fractal_depth)
            policy.reward_weights["w_f"] = min(0.7, max(0.2, new))
        
        if delta_h > 0.07:
            cur = policy.reward_weights.get("w_h", 0.2)
            new = cur + self._fractal_correction(cur, 0.45, self.fractal_depth)
            policy.reward_weights["w_h"] = min(0.6, max(0.15, new))
        
        # Normalizacja
        total = sum(policy.reward_weights.values())
        if total > 0:
            for k in policy.reward_weights:
                policy.reward_weights[k] /= total
        
        for k, v in policy.reward_weights.items():
            self.weight_history[k].append(v)
            if len(self.weight_history[k]) > 100:
                self.weight_history[k] = self.weight_history[k][-50:]
    
    def get_fractal_state(self) -> Dict[str, Any]:
        return {
            "golden_ratio": self.golden_ratio,
            "depth": self.fractal_depth,
            "learning_rate": self.lr,
            "weight_history": {k: v[-10:] for k, v in self.weight_history.items() if v}
        }


# =============================================================================
# 13. GOVERNOR_RL_V2 — META-RL AGENT
# =============================================================================

class GovernorRLv2:
    """Meta-RL agent sterujący politykami globalnymi."""
    
    def __init__(self, lr: float = 0.12, gamma: float = 0.97, epsilon: float = 0.15):
        self.lr = lr
        self.gamma = gamma
        self.epsilon = epsilon
        self.q: Dict[Tuple, Dict[str, float]] = {}
        self.action_history: List[str] = []
        self.reward_history: List[float] = []
        LOG("GOVERNOR_RL", f"🧠 GovernorRLv2 aktywowany (ε={epsilon})")
    
    def actions(self) -> List[str]:
        return ["SAFE_MODE", "REGENERATION", "EXPANSION", "TUNE_WEIGHTS", "TUNE_EPSILON", "REBALANCE_CLUSTER"]
    
    def _discretize(self, s: Dict[str, float]) -> Tuple:
        return (
            min(19, int(s.get("failure", 0) * 20)),
            min(19, int(s.get("delta_H", 0) * 20)),
            min(19, int(s.get("pressure", 0) * 20)),
            min(9, int(s.get("energy", PHI) * 10)),
            min(9, int(s.get("ID", 1.0) * 5)),
        )
    
    def select(self, state: Dict[str, float]) -> str:
        ds = self._discretize(state)
        if random.random() < self.epsilon or ds not in self.q:
            action = random.choice(self.actions())
        else:
            action = max(self.q[ds], key=self.q[ds].get)
        
        self.action_history.append(action)
        if len(self.action_history) > 200:
            self.action_history = self.action_history[-100:]
        return action
    
    def update(self, s: Dict[str, float], a: str, r: float, s2: Dict[str, float]) -> None:
        ds = self._discretize(s)
        ds2 = self._discretize(s2)
        
        if ds not in self.q:
            self.q[ds] = {x: 0.0 for x in self.actions()}
        if ds2 not in self.q:
            self.q[ds2] = {x: 0.0 for x in self.actions()}
        
        old = self.q[ds][a]
        new = old + self.lr * (r + self.gamma * max(self.q[ds2].values()) - old)
        self.q[ds][a] = new
        self.reward_history.append(r)
        if len(self.reward_history) > 200:
            self.reward_history = self.reward_history[-100:]
    
    def set_exploration_rate(self, epsilon: float) -> None:
        self.epsilon = max(0.01, min(0.5, epsilon))
    
    def stats(self) -> Dict[str, Any]:
        return {
            "epsilon": self.epsilon,
            "q_size": len(self.q),
            "avg_reward": sum(self.reward_history[-20:]) / max(1, len(self.reward_history[-20:])),
            "action_distribution": {
                a: self.action_history.count(a) / max(1, len(self.action_history))
                for a in self.actions()
            }
        }


# =============================================================================
# 14. META_GOVERNOR_V13 — GŁÓWNY SILNIK
# =============================================================================

class MetaGovernorV13:
    """
    META_GOVERNOR_Ω⁵ — Kora Przedczołowa GEON-OS.
    Meta-świadomość systemowa.
    """
    
    def __init__(
        self,
        clusters: List[Any],
        learning_mode: str = "ADAPTIVE",
        epsilon: float = 0.15,
        rl_lr: float = 0.12,
        gamma: float = 0.97,
    ):
        self.clusters = clusters
        
        # Komponenty
        self.meta_state = MetaState()
        self.policies = MetaPolicies()
        self.rl = GovernorRLv2(lr=rl_lr, gamma=gamma, epsilon=epsilon)
        self.intent_engine = MetaIntentEngine()
        self.priority_engine = MetaIntentPriorityEngine()
        self.future_sim = FutureSimOmega5()
        self.reward_tuner = FractalRewardTuner()
        
        self.learning_mode = learning_mode
        
        # Stan
        self.last_policy: Optional[GlobalPolicy] = None
        self.last_state: Optional[Dict[str, float]] = None
        self.last_action: Optional[str] = None
        self.last_prioritized_intent: Optional[PrioritizedIntent] = None
        self.last_prediction: Optional[PriorityPrediction] = None
        self.meta_reward_history: List[float] = []
        self.tick = 0
        
        LOG("META_GOVERNOR", "🐉 META_GOVERNOR_Ω⁵ aktywowany")
        LOG("META_GOVERNOR", f"   Sygnatura: {FRACTAL_SIGNATURE}")
        LOG("META_GOVERNOR", f"   Tryb: {learning_mode}")
        LOG("META_GOVERNOR", f"   Epsilon: {epsilon}, Gamma: {gamma}, LR: {rl_lr}")
    
    def observe(self) -> None:
        """Obserwuje stan wszystkich klastrów."""
        self.meta_state.update(self.clusters)
    
    def _compute_meta_reward(self, state: Dict[str, float], prediction: Optional[PriorityPrediction] = None) -> float:
        failure = state.get("failure", 0)
        delta_h = state.get("delta_H", 0)
        pressure = state.get("pressure", 0)
        energy = state.get("energy", PHI)
        ID = state.get("ID", 1.0)
        
        energy_penalty = abs(energy - PHI)
        intent_mismatch = self.intent_engine.intent_mismatch(state)
        
        reward = -(
            0.30 * failure +
            0.20 * delta_h +
            0.10 * pressure +
            0.15 * energy_penalty +
            0.15 * intent_mismatch
        )
        
        if 0.58 < energy < 0.66:
            reward += 0.08
        if ID < 0.8:
            reward += 0.04
        
        if prediction:
            reward -= 0.1 * prediction.future_conflict
            reward += 0.05 * prediction.future_priority_score
        
        return reward
    
    def decide(self) -> GlobalPolicy:
        """Podejmuje decyzję o polityce globalnej."""
        state = self.meta_state.snapshot()
        state["ID"] = self.future_sim.get_id()
        
        # 1. Generuj intencję
        intent = self.intent_engine.generate(state)
        
        # 2. Priorytetyzuj intencję
        prioritized = self.priority_engine.prioritize(intent, state)
        self.last_prioritized_intent = prioritized
        
        # 3. Wybierz akcję
        if self.learning_mode == "HEURISTIC":
            action = None
            policy = MetaPolicies.generate(self.meta_state)
        elif self.learning_mode == "RL_ONLY":
            action = self.rl.select(state)
            policy = MetaPolicies.generate_from_action(action, self.meta_state)
        else:  # ADAPTIVE
            action = self.rl.select(state)
            policy = MetaPolicies.generate_from_action(action, self.meta_state)
        
        # 4. Przewiduj przyszłość
        self.last_prediction = self.future_sim.simulate(state, action, prioritized)
        
        self.last_policy = policy
        self.last_state = state
        self.last_action = action
        
        LOG("META_GOVERNOR", f"🎯 Decyzja: {policy.global_mode} (ε={policy.epsilon:.3f})")
        return policy
    
    def apply(self, policy: GlobalPolicy) -> None:
        """Zastosowuje politykę do wszystkich klastrów."""
        for cluster in self.clusters:
            if hasattr(cluster, "cluster_rl"):
                cluster.cluster_rl.apply_policies(policy)
            
            for node in getattr(cluster, "nodes", {}).values():
                if hasattr(node, "engine"):
                    engine = node.engine
                    if hasattr(engine, "self_healing"):
                        engine.self_healing.mode = policy.global_mode
                    if hasattr(engine, "rl_agent"):
                        engine.rl_agent.set_exploration_rate(policy.epsilon)
                    if hasattr(engine, "reward_engine"):
                        engine.reward_engine.update_weights(policy.reward_weights)
    
    def learn(self) -> None:
        """Uczy się na podstawie wyników polityki."""
        if not self.last_policy or not self.last_state:
            return
        
        self.tick += 1
        new_state = self.meta_state.snapshot()
        new_state["ID"] = self.future_sim.get_id()
        
        reward = self._compute_meta_reward(new_state, self.last_prediction)
        self.meta_reward_history.append(reward)
        if len(self.meta_reward_history) > 200:
            self.meta_reward_history = self.meta_reward_history[-100:]
        
        if self.last_action:
            self.rl.update(self.last_state, self.last_action, reward, new_state)
            self.future_sim.record_outcome(self.last_state, self.last_action, new_state)
            self.reward_tuner.update(self.last_policy, new_state)
    
    def get_stats(self) -> Dict[str, Any]:
        """Zwraca statystyki MetaGovernora."""
        return {
            "version": VERSION,
            "signature": FRACTAL_SIGNATURE,
            "tick": self.tick,
            "learning_mode": self.learning_mode,
            "rl_stats": self.rl.stats(),
            "fractal_state": self.reward_tuner.get_fractal_state(),
            "meta_reward_avg": sum(self.meta_reward_history[-20:]) / max(1, len(self.meta_reward_history[-20:])),
            "current_state": self.meta_state.snapshot(),
            "current_id": self.future_sim.get_id(),
            "last_policy": self.last_policy.to_dict() if self.last_policy else None,
            "last_intent": {
                "mode": self.last_prioritized_intent.intent.mode if self.last_prioritized_intent else None,
                "priority_score": self.last_prioritized_intent.priority_score if self.last_prioritized_intent else None,
                "conflict_score": self.last_prioritized_intent.conflict_score if self.last_prioritized_intent else None,
            } if self.last_prioritized_intent else None,
            "future_prediction": {
                "conflict": self.last_prediction.future_conflict if self.last_prediction else None,
                "priority_score": self.last_prediction.future_priority_score if self.last_prediction else None,
            } if self.last_prediction else None,
            "vibe": VIBE,
            "haslo": HASLO,
        }
    
    def reset(self) -> None:
        """Resetuje MetaGovernora."""
        self.tick = 0
        self.last_policy = None
        self.last_state = None
        self.last_action = None
        self.last_prioritized_intent = None
        self.last_prediction = None
        self.meta_reward_history = []
        LOG("META_GOVERNOR", "🔄 Zresetowano")


# =============================================================================
# 15. FABRYKA
# =============================================================================

class MetaGovernorV13Factory:
    """Fabryka tworząca MetaGovernorV13 z konfiguracją."""
    
    @staticmethod
    def create_default(clusters: List[Any]) -> MetaGovernorV13:
        return MetaGovernorV13(clusters, learning_mode="ADAPTIVE")
    
    @staticmethod
    def create_heuristic(clusters: List[Any]) -> MetaGovernorV13:
        return MetaGovernorV13(clusters, learning_mode="HEURISTIC")
    
    @staticmethod
    def create_rl_only(clusters: List[Any], epsilon: float = 0.1) -> MetaGovernorV13:
        return MetaGovernorV13(clusters, learning_mode="RL_ONLY", epsilon=epsilon)
    
    @staticmethod
    def create_high_exploration(clusters: List[Any]) -> MetaGovernorV13:
        return MetaGovernorV13(clusters, learning_mode="ADAPTIVE", epsilon=0.35)
    
    @staticmethod
    def create_fractal_optimized(clusters: List[Any]) -> MetaGovernorV13:
        gov = MetaGovernorV13(clusters, learning_mode="ADAPTIVE", epsilon=0.15)
        gov.reward_tuner.fractal_depth = 5
        gov.reward_tuner.lr = 0.08
        gov.rl.lr = 0.15
        gov.rl.gamma = 0.98
        return gov


# =============================================================================
# 16. DEMONSTRACJA
# =============================================================================

def demo():
    print("\n" + "=" * 80)
    print("🐉 META_GOVERNOR_Ω⁵ — DEMONSTRACJA")
    print("=" * 80)
    print("Kora Przedczołowa GEON-OS")
    print("=" * 80 + "\n")
    
    # Mocki
    class MockNode:
        def __init__(self, nid):
            self.node_id = nid
            self.engine = type('obj', (), {
                'self_healing': type('obj', (), {'mode': 'NORMAL'}),
                'rl_agent': type('obj', (), {'set_exploration_rate': lambda x: None}),
                'reward_engine': type('obj', (), {'update_weights': lambda x: None})
            })()
    
    class MockCluster:
        def __init__(self, cid):
            self.cluster_id = cid
            self.nodes = {f"n{i}": MockNode(f"n{i}") for i in range(3)}
            self.cluster_rl = type('obj', (), {'apply_policies': lambda x: None})
        
        def get_summary(self):
            return {
                "health": {
                    "avg_failure": random.uniform(0.01, 0.12),
                    "avg_delta_H": random.uniform(0.01, 0.09),
                    "avg_energy": random.uniform(0.4, 0.8),
                    "avg_cb": random.uniform(0.1, 0.5),
                    "avg_pressure": random.uniform(0.3, 0.8),
                    "avg_throughput": random.uniform(5, 18),
                }
            }
    
    # Inicjalizacja
    clusters = [MockCluster(f"CLUSTER_{i}") for i in range(2)]
    governor = MetaGovernorV13Factory.create_default(clusters)
    
    print("🔧 Symulacja 50 kroków z meta-intencjami i priorytetami...\n")
    
    for t in range(1, 51):
        governor.observe()
        policy = governor.decide()
        governor.apply(policy)
        governor.learn()
        
        if t % 10 == 0:
            stats = governor.get_stats()
            intent_mode = stats["last_intent"]["mode"] if stats["last_intent"] else "?"
            print(f"[Tick {t:3d}] Intent: {intent_mode:12s} | "
                  f"Policy: {policy.global_mode:18s} | "
                  f"ε={policy.epsilon:.3f} | "
                  f"Reward={stats['meta_reward_avg']:.4f} | "
                  f"ID={stats['current_id']:.3f}")
    
    print("\n" + "=" * 80)
    print("🐉 META_GOVERNOR_Ω⁵ GOTOWY | 1-6-8. ∞. SIEMA!")
    print("=" * 80 + "\n")


if __name__ == "__main__":
    demo()