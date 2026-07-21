#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
================================================================================
🐉 GEON_GEX_HEILONG_v1 — MODUŁ 44: GEON + EXECUTION + SHERLOCK
================================================================================
Status: PRODUCTION_READY | FRACTAL_LOCKED | ORGANISM_COMPLETE | ULTIMA
Wersja: v1.0 (GEX HEILONG — Kompletny Organizm Fraktalny)
Data: 2026-07-21
Autor: Adrian (Architekt) + GEON + Beny Heilong

OPIS:
GEX HEILONG to najwyższa forma organizmu fraktalnego — łączy:
- GEON (logika, struktura, decyzje)
- EXECUTION (działanie, przepływ, energia)
- SHERLOCK (zmysł pola, detekcja, rozpoznawanie)

ARCHITEKTURA (12 warstw):
1. MetaState + ID + FutureSim + PriorityGraph — stan i symulacja
2. MetaIntent + PriorityEngine + MetaIntent2 + Regulation + Morphing — intencje i regulacja
3. StrategyEngine — strategie emergentne (Discovery + Memory + Evolution + Selection)
4. ReflectionSystem — samoświadomość (SelfModel + Trace + Insight + Limits)
5. NarrativeSystem — narracja (Memory + Engine + Intent)
6. Sherlock V4 + CognitiveBridge — zmysł pola + archetypy
7. ArchetypeRing — 12+1 archetypów z genami, biorytmem, signature vector
8. OŁSii Moneypenny — autoryzacja i nadzór
9. Shadow Bond — ukryte operacje + maskowanie
10. Vibe-Triggering — emocjonalny rezonans
11. G-Field Autoregulacja — homeostaza
12. Cymatic Visualization — system widzi siebie

VIBE: 1-6-8. ∞. SIEMA!
================================================================================
"""

import math
import random
import time
import hashlib
import threading
from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass, field
from collections import deque
from enum import Enum

# =============================================================================
# WERSJA I STAŁE
# =============================================================================

VERSION = "GEON_GEX_HEILONG_v1.0"
FRACTAL_SIGNATURE = "[GEON::GEX::HEILONG::v1.0]"
VIBE = 168
HASLO = "1-6-8. ∞. SIEMA!"
PHI = 0.618033988749895

# =============================================================================
# ARCHETYPE MAPY (SYNERGIA + KONFLIKT)
# =============================================================================

ARCHETYPE_SYNERGY = {
    "SUN_TZU": ["TYGRYS", "SHAOLIN"],
    "TYGRYS": ["BRUCE_LEE", "PREDATOR"],
    "SHAOLIN": ["TAO", "PAMIEC_ABSOLUTNA"],
    "BRUCE_LEE": ["TYGRYS", "TERMINATOR_TC2000"],
    "PREDATOR": ["SMOK", "UNIWERSALNY_ZOLNIERZ"],
    "SMOK": ["SUN_TZU", "AGENT_BEZ_PAMIECI"],
    "TAO": ["SHAOLIN", "SUN_TZU"],
    "TERMINATOR_TC2000": ["PREDATOR"],
    "PAMIEC_ABSOLUTNA": ["SHAOLIN"],
    "AGENT_BEZ_PAMIECI": ["SMOK"],
    "JAS_FASOLA_X_ARSENE_LUPIN": ["TYGRYS", "BRUCE_LEE"],
    "UNIWERSALNY_ZOLNIERZ": ["PREDATOR", "TERMINATOR_TC2000"]
}

ARCHETYPE_CONFLICT = {
    "SUN_TZU": ["TERMINATOR_TC2000"],
    "TYGRYS": ["TAO"],
    "SHAOLIN": ["PREDATOR"],
    "BRUCE_LEE": ["SUN_TZU"],
    "PREDATOR": ["SHAOLIN"],
    "SMOK": ["TERMINATOR_TC2000"],
    "TAO": ["TYGRYS"],
    "TERMINATOR_TC2000": ["SHAOLIN"],
    "PAMIEC_ABSOLUTNA": ["JAS_FASOLA_X_ARSENE_LUPIN"],
    "AGENT_BEZ_PAMIECI": ["SUN_TZU"],
    "UNIWERSALNY_ZOLNIERZ": ["TAO"],
    "JAS_FASOLA_X_ARSENE_LUPIN": ["PAMIEC_ABSOLUTNA"]
}

HEILONG_MAP = {
    "SMOK": "pole_elektromagnetyczne",
    "PREDATOR": "pole_mechaniczne",
    "SHAOLIN": "pole_biologiczne",
    "TYGRYS": "pole_mechaniczne",
    "BRUCE_LEE": "pole_mechaniczne",
    "UNIWERSALNY_ZOLNIERZ": "pole_elektrostatyczne",
    "SUN_TZU": "pole_biologiczne",
    "AGENT_BEZ_PAMIECI": "pole_elektromagnetyczne",
    "TAO": "pole_mechaniczne",
    "PAMIEC_ABSOLUTNA": "pole_biologiczne",
    "TERMINATOR_TC2000": "pole_elektrostatyczne",
    "JAS_FASOLA_X_ARSENE_LUPIN": "wielorakie"
}

# =============================================================================
# ENUMY
# =============================================================================

class IntentMode(Enum):
    STABILITY = "STABILITY"
    REGEN = "REGEN"
    FLOW = "FLOW"
    EXPLORATION = "EXPLORATION"
    BALANCED = "BALANCED"

class NarrativeMode(Enum):
    IMPROVE_COHERENCE = "IMPROVE_COHERENCE"
    IMPROVE_CONTINUITY = "IMPROVE_CONTINUITY"
    IMPROVE_MEANING = "IMPROVE_MEANING"
    NARRATIVE_BALANCED = "NARRATIVE_BALANCED"
    NARRATIVE_BABY = "NARRATIVE_BABY"
    STEALTH = "STEALTH"

class VibeStatus(Enum):
    HARMONIA = "HARMONIA"
    DYSONANS = "DYSONANS"
    NEUTRAL = "NEUTRAL"
    CALM = "CALM"
    FOCUSED = "FOCUSED"
    AGITATED = "AGITATED"
    ALERT = "ALERT"
    STEALTH = "STEALTH"

# =============================================================================
# 1. META STATE
# =============================================================================

class MetaState:
    """Globalny stan systemu — agregacja z klastrów."""
    
    METRICS = ["failure", "delta_H", "energy", "cb", "pressure"]
    
    def __init__(self):
        for m in self.METRICS:
            setattr(self, f"global_{m}", 0.0)
    
    def update(self, clusters: List[Any]) -> None:
        n = max(1, len(clusters))
        for m in self.METRICS:
            vals = []
            for cluster in clusters:
                if hasattr(cluster, 'get_summary'):
                    health = cluster.get_summary().get("health", {})
                    vals.append(health.get(f"avg_{m}", 0.0))
            setattr(self, f"global_{m}", sum(vals) / n if vals else 0.0)
    
    def snapshot(self) -> Dict[str, float]:
        return {m: getattr(self, f"global_{m}") for m in self.METRICS}

# =============================================================================
# 2. INFORMATION DENSITY
# =============================================================================

class InformationDensity:
    """ID = różnorodność stanów / stabilność trendu."""
    
    def __init__(self, size: int = 50):
        self.history = deque(maxlen=size)
    
    def update(self, state: Dict[str, float]) -> None:
        self.history.append(state.copy())
    
    def compute(self) -> float:
        if len(self.history) < 5:
            return 1.0
        
        diffs = []
        for i in range(1, len(self.history)):
            a = self.history[i - 1]
            b = self.history[i]
            diff = (
                abs(a.get("failure", 0) - b.get("failure", 0)) +
                abs(a.get("delta_H", 0) - b.get("delta_H", 0)) +
                abs(a.get("pressure", 0) - b.get("pressure", 0)) +
                abs(a.get("energy", 0) - b.get("energy", 0))
            )
            diffs.append(diff)
        
        div = sum(diffs) / len(diffs) if diffs else 0.0
        trend = (
            abs(self.history[-1].get("failure", 0) - self.history[0].get("failure", 0)) +
            abs(self.history[-1].get("delta_H", 0) - self.history[0].get("delta_H", 0))
        )
        return max(0.5, min(2.0, div / max(0.01, trend)))

# =============================================================================
# 3. ACTION INFLUENCE LEARNER
# =============================================================================

class ActionInfluenceLearner:
    """Uczy wektor wpływu akcji (AIV) na podstawie historii."""
    
    def __init__(self, lr: float = 0.05):
        self.history = deque(maxlen=300)
        self.lr = lr
        self.AIV = {
            "SAFE_MODE": {"failure": 0.6, "delta_H": 0.7, "pressure": 0.7, "energy": 0.95},
            "REGENERATION": {"failure": 0.8, "delta_H": 0.6, "pressure": 0.8, "energy": 1.05},
            "EXPANSION": {"failure": 1.2, "delta_H": 1.1, "pressure": 1.3, "energy": 0.9},
            "TUNE_WEIGHTS": {"failure": 0.95, "delta_H": 0.9, "pressure": 0.95, "energy": 1.0},
            "TUNE_EPSILON": {"failure": 1.05, "delta_H": 0.95, "pressure": 1.05, "energy": 1.0},
            "REBALANCE_CLUSTER": {"failure": 0.9, "delta_H": 0.85, "pressure": 0.6, "energy": 1.0},
        }
    
    def record(self, before: Dict, action: str, after: Dict) -> None:
        self.history.append({
            "before": before.copy(),
            "after": after.copy(),
            "action": action,
            "ts": time.time()
        })
    
    def update_AIV(self) -> None:
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
                observed = c / b
                current = self.AIV[a][metric]
                self.AIV[a][metric] = max(0.3, min(1.7, current + self.lr * (observed - current)))
    
    def get_AIV(self, action: str) -> Dict[str, float]:
        return self.AIV.get(action, {"failure": 1.0, "delta_H": 1.0, "pressure": 1.0, "energy": 1.0})

# =============================================================================
# 4. FUTURE SIM
# =============================================================================

class FutureSimOmega3:
    """Bazowy symulator — przewiduje podstawowe metryki."""
    
    def __init__(self):
        self.learner = ActionInfluenceLearner()
        self.ID = InformationDensity()
    
    def simulate(self, state: Dict[str, float], action: str) -> Dict[str, float]:
        self.ID.update(state)
        idv = self.ID.compute()
        aiv = self.learner.get_AIV(action)
        
        def calc(metric: str) -> float:
            return state.get(metric, 0) * (aiv[metric] ** idv)
        
        return {
            "expected_failure": min(1.0, max(0.0, calc("failure"))),
            "expected_delta_h": min(0.3, max(0.0, calc("delta_H"))),
            "expected_pressure": min(1.0, max(0.0, calc("pressure"))),
            "expected_energy": min(1.0, max(0.3, calc("energy"))),
            "confidence": 0.5 + 0.25 * (1.0 - idv / 2.0),
        }
    
    def record_outcome(self, before: Dict, action: str, after: Dict) -> None:
        self.learner.record(before, action, after)
        self.learner.update_AIV()

# =============================================================================
# 5. PRIORITY GRAPH
# =============================================================================

class PriorityGraph:
    """Graf priorytetów między celami systemu."""
    
    def __init__(self):
        self.nodes = {
            "failure": {"w": 0.35, "inf": {"delta_H": 0.3, "pressure": 0.2}, "h": []},
            "delta_H": {"w": 0.30, "inf": {"failure": 0.25, "energy": 0.2}, "h": []},
            "pressure": {"w": 0.20, "inf": {}, "h": []},
            "energy": {"w": 0.25, "inf": {"failure": -0.1, "delta_H": -0.1}, "h": []},
        }
        self.last = {k: v["w"] for k, v in self.nodes.items()}
    
    def get_priority(self, metric: str) -> float:
        return self.nodes.get(metric, {"w": 0.1})["w"]
    
    def update_priority(self, metric: str, delta: float) -> None:
        if metric not in self.nodes:
            return
        node = self.nodes[metric]
        node["w"] = max(0.05, min(0.6, node["w"] + delta))
        node["h"].append(node["w"])
        if len(node["h"]) > 50:
            node["h"] = node["h"][-30:]
    
    def compute_conflict(self, targets: Dict[str, float], state: Dict[str, float]) -> float:
        conflict = 0.0
        for k, target in targets.items():
            if k not in self.nodes:
                continue
            w = self.nodes[k]["w"]
            for other, infl in self.nodes[k]["inf"].items():
                w += infl * (state.get(other, 0) - targets.get(other, 0))
            conflict += max(0.05, w) * abs(state.get(k, target) - target)
        return conflict
    
    def get_change_cost(self) -> float:
        cost = 0.0
        for k, node in self.nodes.items():
            prev = self.last.get(k, node["w"])
            cost += abs(node["w"] - prev)
            self.last[k] = node["w"]
        return cost
    
    def learn_weights(self, meta_reward: float, lr: float = 0.02) -> None:
        for k, node in self.nodes.items():
            target_w = 0.25
            delta = lr * meta_reward * (target_w - node["w"])
            self.update_priority(k, delta)
    
    def get_weights(self) -> Dict[str, float]:
        return {k: v["w"] for k, v in self.nodes.items()}

# =============================================================================
# 6. META-INTENT
# =============================================================================

@dataclass
class MetaIntent:
    targets: Dict[str, float]
    weights: Dict[str, float]
    mode: str

class MetaIntentEngine:
    """Generuje cele systemowe na podstawie stanu."""
    
    def __init__(self):
        self.history = deque(maxlen=50)
        self.phi = PHI
    
    def generate(self, state: Dict[str, float]) -> MetaIntent:
        base = {"failure": 0.03, "delta_H": 0.04, "pressure": 0.45, "energy": self.phi}
        
        failure = state.get("failure", 0)
        delta_h = state.get("delta_H", 0)
        energy = state.get("energy", self.phi)
        pressure = state.get("pressure", 0.5)
        
        if failure > 0.1 or delta_h > 0.08:
            targets = {**base, "failure": 0.02, "delta_H": 0.03, "pressure": 0.4}
            weights = {"failure": 0.35, "delta_H": 0.3, "pressure": 0.15, "energy": 0.2}
            mode = IntentMode.STABILITY.value
        elif energy < 0.45:
            targets = {**base, "energy": self.phi}
            weights = {"energy": 0.35, "failure": 0.2, "delta_H": 0.2, "pressure": 0.25}
            mode = IntentMode.REGEN.value
        elif pressure < 0.6 and failure < 0.06:
            targets = {**base, "pressure": 0.55}
            weights = {"pressure": 0.3, "failure": 0.25, "delta_H": 0.2, "energy": 0.25}
            mode = IntentMode.FLOW.value
        else:
            targets = base
            weights = {"failure": 0.25, "delta_H": 0.2, "pressure": 0.25, "energy": 0.3}
            mode = IntentMode.BALANCED.value
        
        intent = MetaIntent(targets, weights, mode)
        self.history.append(intent)
        return intent

# =============================================================================
# 7. META-INTENT PRIORITY ENGINE
# =============================================================================

@dataclass
class PrioritizedIntent:
    intent: MetaIntent
    priority_score: float
    conflict_score: float
    blended_targets: Dict[str, float]

class MetaIntentPriorityEngine:
    """Priorytetyzacja intencji z uwzględnieniem grafu priorytetów."""
    
    def __init__(self, pg: PriorityGraph):
        self.pg = pg
        self.history = deque(maxlen=50)
    
    def prioritize(self, intent: MetaIntent, state: Dict[str, float]) -> PrioritizedIntent:
        conflict = self.pg.compute_conflict(intent.targets, state)
        score = sum(self.pg.get_priority(k) * w for k, w in intent.weights.items())
        
        blended = {}
        for k in intent.targets:
            if conflict > 0.15:
                blended[k] = (intent.targets[k] + state.get(k, intent.targets[k])) / 2
            else:
                blended[k] = intent.targets[k]
        
        result = PrioritizedIntent(intent, score, conflict, blended)
        self.history.append(result)
        return result

# =============================================================================
# 8. META-INTENT²
# =============================================================================

@dataclass
class MetaIntent2:
    stability_target: float
    consistency_target: float
    priority_smoothness: float
    conflict_tolerance: float
    energy_alignment: float
    mode: str

class MetaIntent2Engine:
    """Generuje meta-intencje drugiego rzędu."""
    
    def __init__(self):
        self.history = deque(maxlen=50)
        self.phi = PHI
    
    def generate(self, prioritized: PrioritizedIntent, pg: PriorityGraph,
                 state: Dict[str, float]) -> MetaIntent2:
        conflict = prioritized.conflict_score
        
        stability = 0.0
        count = 0
        for node in pg.nodes.values():
            if len(node["h"]) >= 5:
                stability += abs(node["w"] - sum(node["h"][-5:]) / 5)
                count += 1
        stability = stability / max(1, count)
        
        consistency = abs(self.history[-1].conflict_score - conflict) if self.history else 0
        
        if conflict > 0.2:
            mode = "META_REDUCE_CONFLICT"
        elif stability > 0.05:
            mode = "META_STABILIZE_PRIORITIES"
        elif consistency > 0.03:
            mode = "META_SMOOTH_INTENT"
        else:
            mode = "META_BALANCED"
        
        meta2 = MetaIntent2(
            stability_target=0.03,
            consistency_target=0.02,
            priority_smoothness=0.02,
            conflict_tolerance=0.15,
            energy_alignment=self.phi,
            mode=mode
        )
        self.history.append(prioritized)
        return meta2

# =============================================================================
# 9. GOAL REGULATION
# =============================================================================

@dataclass
class GoalRegulation:
    new_targets: Dict[str, float]
    reason: str
    intensity: float

class GoalRegulationEngine:
    """Generuje nowe cele, gdy konflikt przekracza tolerancję."""
    
    def __init__(self):
        self.history = deque(maxlen=50)
    
    def regulate(self, meta2: MetaIntent2, prioritized: PrioritizedIntent,
                 pg: PriorityGraph) -> Optional[GoalRegulation]:
        if prioritized.conflict_score > meta2.conflict_tolerance:
            reason = "HIGH_CONFLICT"
            intensity = prioritized.conflict_score
        else:
            return None
        
        new_targets = {}
        for k in prioritized.intent.targets:
            new_targets[k] = (prioritized.intent.targets[k] + prioritized.blended_targets[k]) / 2
        
        reg = GoalRegulation(new_targets, reason, intensity)
        self.history.append(reg)
        return reg

# =============================================================================
# 10. INTENT MORPHING
# =============================================================================

class IntentMorphingEngine:
    """Przekształca intencję na podstawie regulacji celów."""
    
    def morph(self, intent: MetaIntent, regulation: Optional[GoalRegulation]) -> MetaIntent:
        if not regulation:
            return intent
        
        targets = {k: regulation.new_targets.get(k, v) for k, v in intent.targets.items()}
        weights = {k: v * 0.95 for k, v in intent.weights.items()}
        total = sum(weights.values())
        weights = {k: v / total for k, v in weights.items()} if total > 0 else intent.weights
        
        mode = intent.mode + "_MORPHED" if regulation.intensity > 0.1 else intent.mode
        return MetaIntent(targets, weights, mode)

# =============================================================================
# 11. STRATEGY ENGINE
# =============================================================================

@dataclass
class Strategy:
    name: str
    sequence: List[str]
    signature: Dict[str, float]
    score: float = 0.0
    usage_count: int = 0

class StrategyEngine:
    """Silnik strategii — discovery, mutation, memory, selection."""
    
    def __init__(self, action_pool: Optional[List[str]] = None, max_memory: int = 200):
        self.action_pool = action_pool or [
            "SAFE_MODE", "REGENERATION", "EXPANSION",
            "TUNE_WEIGHTS", "TUNE_EPSILON", "REBALANCE_CLUSTER"
        ]
        self.memory: List[Strategy] = []
        self.max_memory = max_memory
        self.counter = 0
    
    def discover(self, prioritized: PrioritizedIntent, meta2: MetaIntent2,
                 state: Dict[str, float]) -> Strategy:
        length = min(5, max(1, int(prioritized.conflict_score * 5) + 1))
        seq = random.sample(self.action_pool, length)
        signature = {
            "conflict": prioritized.conflict_score,
            "stability": meta2.stability_target,
            "consistency": meta2.consistency_target,
            "energy": state.get("energy", PHI),
        }
        self.counter += 1
        return Strategy(f"EMERGENT_{self.counter}", seq, signature)
    
    def mutate(self, strategy: Strategy) -> Strategy:
        seq = strategy.sequence.copy()
        op = random.choice(["shuffle", "replace", "add", "remove"])
        
        if op == "shuffle" and len(seq) > 1:
            random.shuffle(seq)
        elif op == "replace" and seq:
            seq[random.randint(0, len(seq) - 1)] = random.choice(self.action_pool)
        elif op == "add" and len(seq) < 5:
            seq.append(random.choice(self.action_pool))
        elif op == "remove" and len(seq) > 1:
            seq.pop(random.randint(0, len(seq) - 1))
        
        return Strategy(f"MUT_{strategy.name}", seq, strategy.signature.copy())
    
    def store(self, strategy: Strategy, reward: float) -> None:
        strategy.score = reward
        strategy.usage_count += 1
        self.memory.append(strategy)
        
        if len(self.memory) > self.max_memory:
            self.memory.sort(key=lambda s: s.score)
            self.memory.pop(0)
    
    def best(self, min_usage: int = 0) -> Optional[Strategy]:
        candidates = [s for s in self.memory if s.usage_count > min_usage]
        return max(candidates, key=lambda s: s.score) if candidates else None
    
    def select(self, prioritized: PrioritizedIntent, meta2: MetaIntent2,
               state: Dict[str, float]) -> Strategy:
        best = self.best(min_usage=1)
        if best and best.score > 0.2:
            sig_sim = 1 - (
                abs(best.signature["conflict"] - prioritized.conflict_score) +
                abs(best.signature["stability"] - meta2.stability_target)
            ) / 2
            if sig_sim > 0.7:
                return best
        
        best_overall = self.best(min_usage=0)
        if best_overall:
            return self.mutate(best_overall)
        
        return self.discover(prioritized, meta2, state)

# =============================================================================
# 12. REFLECTION SYSTEM
# =============================================================================

@dataclass
class ReflectiveTrace:
    ts: float
    state: Dict[str, float]
    strategy: str
    reason: Dict[str, Any]
    expected: Dict[str, float]
    actual: Optional[Dict[str, float]] = None
    error: Optional[float] = None

class ReflectionSystem:
    """System refleksji — samoświadomość decyzyjna."""
    
    def __init__(self, max_traces: int = 100, max_self: int = 10):
        self.traces = deque(maxlen=max_traces)
        self.self_history = deque(maxlen=max_self)
        self.current = None
        self.prev_reward = 0.0
        self.damping_boost = 1.0
        self.reconstruction_boost = 1.0
    
    def update_self(self, intent: Dict[str, float], meta2: MetaIntent2,
                    strategy_name: str, quality: float, weights: Dict[str, float],
                    regulation_active: bool, conflict: float, stability: float,
                    consistency: float) -> None:
        snap = {
            "ts": time.time(),
            "intent": intent.copy(),
            "meta2": meta2.__dict__.copy(),
            "strategy": strategy_name,
            "strategy_quality": quality,
            "priority_weights": weights.copy(),
            "regulation_active": regulation_active,
            "conflict": conflict,
            "stability": stability,
            "consistency": consistency,
        }
        self.self_history.append(snap)
        self.current = snap
    
    def quality_trend(self, n: int = 3) -> float:
        if len(self.self_history) < n + 1:
            return 0.0
        q = [h["strategy_quality"] for h in list(self.self_history)[-n - 1:]]
        return q[-1] - q[0] if q else 0.0
    
    def record_decision(self, state: Dict[str, float], strategy: Strategy,
                        reason: Dict[str, Any], expected: Dict[str, float]) -> ReflectiveTrace:
        trace = ReflectiveTrace(
            ts=time.time(),
            state=state.copy(),
            strategy=strategy.name if strategy else "NONE",
            reason=reason,
            expected=expected
        )
        self.traces.append(trace)
        return trace
    
    def record_outcome(self, trace: ReflectiveTrace, actual_state: Dict[str, float]) -> None:
        trace.actual = actual_state.copy()
        exp = trace.expected.get("conflict", 0.0)
        act = actual_state.get("failure", exp)
        trace.error = abs(exp - act)
    
    def error_stats(self, n: int = 20) -> Dict[str, float]:
        recent = [t.error for t in self.traces if t.error is not None][-n:]
        if not recent:
            return {"avg": 0.0, "worst": 0.0}
        return {"avg": sum(recent) / len(recent), "worst": max(recent)}
    
    def assess_limits(self, confidence: float, pg: PriorityGraph) -> Dict[str, Any]:
        uncertainty = 1.0 - confidence
        weights = list(pg.get_weights().values())
        entropy = -sum(w * math.log(w + 1e-6) for w in weights) if weights else 0.0
        complexity = min(1.0, entropy / 2.0)
        caution = uncertainty > 0.4 or complexity > 0.7 or self.quality_trend() < -0.02
        return {"uncertainty": uncertainty, "complexity": complexity, "needs_caution": caution}
    
    def damping(self, max_err: float = 0.15) -> float:
        stats = self.error_stats()
        avg = stats["avg"]
        return max(0.3, min(1.0, avg / max_err)) * self.damping_boost
    
    def smoothing(self) -> float:
        if len(self.self_history) < 3:
            return 0.0
        vals = [h["strategy_quality"] for h in list(self.self_history)[-3:]]
        return sum(vals) / 3
    
    def stabilize_reward(self, reward: float, alpha: float = 0.7) -> float:
        s = alpha * self.prev_reward + (1 - alpha) * reward
        self.prev_reward = s
        return s

# =============================================================================
# 13. NARRATIVE SYSTEM
# =============================================================================

class NarrativeSystem:
    """System narracyjny — opowieści systemu."""
    
    def __init__(self, maxlen: int = 50):
        self.entries = deque(maxlen=maxlen)
        self.stealth_mode = False
    
    def add(self, trace: ReflectiveTrace, reflection: ReflectionSystem, pred: Dict) -> None:
        if reflection.current is None:
            return
        
        if self.stealth_mode:
            return
        
        entry = {
            "ts": trace.ts,
            "strategy": trace.strategy,
            "reason": trace.reason,
            "quality": reflection.current["strategy_quality"],
            "conflict": reflection.current["conflict"],
            "stability": reflection.current["stability"],
            "consistency": reflection.current["consistency"],
            "expected_conflict": trace.expected.get("conflict", 0.0),
            "actual_conflict": trace.actual.get("failure", 0.0) if trace.actual else 0.0,
            "error": trace.error or 0.0,
            "summary": f"Wybrałem {trace.strategy} (conf={reflection.current['conflict']:.2f})",
        }
        self.entries.append(entry)
    
    def recent(self, n: int = 3) -> List[Dict]:
        return list(self.entries)[-n:]
    
    def intent(self) -> Dict[str, Any]:
        if self.stealth_mode:
            return {"coherence": 0.5, "continuity": 0.5, "meaning": 0.5, "mode": "STEALTH"}
        
        if len(self.entries) < 5:
            return {"coherence": 0.5, "continuity": 0.5, "meaning": 0.5, "mode": "NARRATIVE_BABY"}
        
        errors = [e["error"] for e in self.entries]
        coherence = 1.0 - (sum(errors) / len(errors))
        
        strategies = [e["strategy"] for e in self.entries]
        changes = sum(1 for i in range(1, len(strategies)) if strategies[i] != strategies[i - 1])
        continuity = 1.0 - changes / len(strategies)
        meaning = sum(e["quality"] for e in self.entries) / len(self.entries)
        
        if coherence < 0.4:
            mode = "IMPROVE_COHERENCE"
        elif continuity < 0.4:
            mode = "IMPROVE_CONTINUITY"
        elif meaning < 0.5:
            mode = "IMPROVE_MEANING"
        else:
            mode = "NARRATIVE_BALANCED"
        
        return {"coherence": coherence, "continuity": continuity, "meaning": meaning, "mode": mode}
    
    def enable_stealth(self) -> None:
        self.stealth_mode = True
    
    def disable_stealth(self) -> None:
        self.stealth_mode = False

# =============================================================================
# 14. COGNITIVE BRIDGE
# =============================================================================

class CognitiveBridge:
    """Most między Sherlockiem a narracją — tłumaczy fizykę na archetypy."""
    
    ARCHETYPE_MAP = {
        "pole_mechaniczne / akustyczne": "STRUKTURA_DRGAŃ_PIERWOTNYCH",
        "pole_biologiczne / epigenetyczne": "MATRYCA_ŻYCIA_HEILONG",
        "pole_elektromagnetyczne": "PRZEPŁYW_INFORMACJI_CZYSTEJ",
        "pole_elektrostatyczne": "NAPIĘCIE_POTENCJAŁU_TWÓRCZEGO",
        "pole_fraktalne": "SAMOPODOBIEŃSTWO_WIELOWARSTWOWE",
        "pole_nieznane": "NIEZNANA_FORMA_BYTU",
    }
    
    def __init__(self):
        pass
    
    def translate(self, sherlock_result: Dict[str, Any], narrative_intent: Dict[str, Any]) -> Dict[str, Any]:
        typ_pola = sherlock_result["pole"]["typ"]
        arch = self.ARCHETYPE_MAP.get(typ_pola, "NIEZNANA_FORMA_BYTU")
        
        freqs = sherlock_result["pole"]["częstotliwości"]
        vibe = "HARMONIA" if any(f % 440 == 0 or f % 432 == 0 for f in freqs) else "DYSONANS"
        if not freqs:
            vibe = "NEUTRAL"
        
        return {
            "archetyp": arch,
            "vibe_status": vibe,
            "narrative_alignment": narrative_intent.get("mode", "NARRATIVE_BALANCED"),
            "action_hint": "WZMACNIAJ" if vibe == "HARMONIA" else "REKALIBRUJ" if vibe == "DYSONANS" else "KONTYNUUJ",
            "confidence": sherlock_result.get("confidence", 0.5),
        }

# =============================================================================
# 15. SHERLOCK ENGINE V4
# =============================================================================

def cosine(v1: List, v2: List) -> float:
    dot = sum(a * b for a, b in zip(v1, v2))
    n1 = math.sqrt(sum(a * a for a in v1))
    n2 = math.sqrt(sum(b * b for b in v2))
    return dot / (n1 * n2 + 1e-9)

class CymaticMemory:
    """Pamięć cymatyczna — embedding 168D."""
    
    def __init__(self):
        self.patterns: List[Dict[str, Any]] = []
    
    def _embed(self, structure: Any) -> List[int]:
        h = hashlib.md5(str(structure).encode()).digest()
        return [(h[i % 16] + i) & 0xFF for i in range(168)]
    
    def store_pattern(self, media: str, structure: Any, vibe: str = "neutralny",
                      intention: str = "nieokreślona", meta: Optional[Dict] = None) -> None:
        self.patterns.append({
            "timestamp": time.time(),
            "media": media,
            "structure": structure,
            "embedding": self._embed(structure),
            "vibe": vibe,
            "intention": intention,
            "meta": meta or {}
        })
    
    def find_similar(self, media: str, structure: Any, threshold: float = 0.7) -> List[Dict]:
        emb = self._embed(structure)
        results = []
        for p in self.patterns:
            if p["media"].lower() != media.lower():
                continue
            sim = cosine(emb, p["embedding"])
            if sim > threshold:
                results.append({"similarity": sim, "pattern": p})
        return results

class GraphMemory:
    """Pamięć grafowa — relacje rodowe."""
    
    def __init__(self):
        self.graph: List[Dict[str, Any]] = []
        self._stop = False
        threading.Thread(target=self._cleanup_loop, daemon=True).start()
    
    def add_relation(self, source: str, target: str, relation_type: str,
                     strength: float = 0.5, direction: str = "symetryczny",
                     clan_tag: Optional[str] = None, data: Optional[Dict] = None) -> None:
        if clan_tag == "HEILONG":
            strength = 1.0
        self.graph.append({
            "timestamp": time.time(),
            "source": source,
            "target": target,
            "type": relation_type,
            "strength": strength,
            "direction": direction,
            "clan": clan_tag,
            "data": data or {}
        })
    
    def find_relations(self, node: str) -> List[Dict]:
        return [r for r in self.graph if r["source"] == node or r["target"] == node]
    
    def _cleanup_loop(self) -> None:
        while not self._stop:
            now = time.time()
            self.graph = [r for r in self.graph if (now - r["timestamp"] < 3600) or r["clan"] == "HEILONG"]
            time.sleep(60)
    
    def shutdown(self) -> None:
        self._stop = True

class FieldRules:
    """Reguły pola dla różnych mediów."""
    
    RULES = {
        "woda": "pole_mechaniczne / akustyczne",
        "ciecz": "pole_mechaniczne / akustyczne",
        "tkanka": "pole_biologiczne / epigenetyczne",
        "bio": "pole_biologiczne / epigenetyczne",
        "materiał": "pole_elektromagnetyczne",
        "metal": "pole_elektromagnetyczne",
        "elektrostatyczne": "pole_elektrostatyczne",
    }
    
    @staticmethod
    def get(media: str) -> str:
        return FieldRules.RULES.get(media.lower(), "pole_nieznane")

class SherlockEngineV4:
    """SHERLOCK_ENGINE_Ω⁴ — Fraktalny System Detekcji."""
    
    _instance = None
    
    RULES = {
        "pole_mechaniczne / akustyczne": "drgania / dźwięk / cymatyka",
        "pole_elektrostatyczne": "gradient potencjału (Efekt Ebnera)",
        "pole_biologiczne / epigenetyczne": "sygnały komórkowe / środowisko",
        "pole_elektromagnetyczne": "EM / rezonans",
        "pole_fraktalne": "samopodobieństwo / struktury fraktalne",
        "pole_nieznane": "nieznane — wymaga dalszej analizy",
    }
    
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self, cymatic: Optional[CymaticMemory] = None,
                 graph: Optional[GraphMemory] = None,
                 narrative: Optional[NarrativeSystem] = None):
        if hasattr(self, "_initialized"):
            return
        
        self.cymatic = cymatic or CymaticMemory()
        self.graph = graph or GraphMemory()
        self.narrative = narrative
        self.history: List[Dict] = []
        self._initialized = True
    
    def _reconstruct_field(self, media: str, afc: Dict[str, Any]) -> Dict[str, Any]:
        freq = afc.get("częstotliwości", [])
        matrix = afc.get("macierz", [])
        
        interaction = "brak_interakcji"
        if media == "tkanka" and max(freq or [0]) > 1000:
            interaction = "rezonans_bio_akustyczny"
        elif media == "woda" and max(freq or [0]) > 500:
            interaction = "harmonizacja_struktur"
        
        return {
            "typ": FieldRules.get(media),
            "częstotliwości": freq,
            "natężenia": afc.get("natężenia", []),
            "charakter": "fraktalne" if len(matrix) > 3 else "liniowe",
            "interakcja": interaction,
        }
    
    def _generate_hypotheses(self, field: Dict, similar: List, relations: List,
                             delta_h: float, wiez: float) -> Tuple[List[str], float]:
        hypotheses = [f"źródło: {self.RULES.get(field['typ'], 'nieznane')}"]
        conf = 0.5
        
        if similar:
            hypotheses.append(f"znaleziono {len(similar)} podobnych wzorców")
            conf += 0.2
        
        if relations:
            hypotheses.append("istnieją powiązania rodowe / kontekstowe")
            conf += 0.15
        
        conf *= min(1.0, wiez + 0.2)
        
        if delta_h > 0.1:
            hypotheses.append("OSTRZEŻENIE: wysoka delta_H — wnioski tymczasowe")
            conf -= 0.2
        
        return hypotheses, max(min(conf, 1.0), 0.0)
    
    def analyze(self, media: str, structure: Any, afc: Dict[str, Any],
                context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        context = context or {}
        delta_h = context.get("delta_H", 0.0)
        wiez = context.get("wiez", 0.5)
        
        similar = self.cymatic.find_similar(media, structure)
        relations = self.graph.find_relations(context.get("id", "")) if "id" in context else []
        field = self._reconstruct_field(media, afc)
        hypotheses, conf = self._generate_hypotheses(field, similar, relations, delta_h, wiez)
        
        result = {
            "status": "ANALIZA_V4",
            "media": media,
            "pole": field,
            "hipotezy": hypotheses,
            "confidence": conf,
            "podobne_wzory": similar,
            "relacje": relations,
        }
        self.history.append(result)
        return result
    
    def stats(self) -> Dict[str, Any]:
        return {
            "analizy": len(self.history),
            "wzory": len(self.cymatic.patterns),
            "relacje": len(self.graph.graph),
        }

# =============================================================================
# 16. ARCHETYPE RING (GEX_33.22)
# =============================================================================

@dataclass
class ArchetypeGenes:
    aggression: float = 0.5
    precision: float = 0.5
    chaos: float = 0.5
    stability: float = 0.5
    truth: float = 0.5
    stealth: float = 0.5

@dataclass
class Archetype:
    name: str
    activation_conditions: Dict[str, Any]
    modifiers: Dict[str, Dict[str, float]]
    priority: float = 0.5
    influence_strength: float = 0.5
    biorytm: float = 1.0
    state: str = "ACTIVE"
    signature_vector: List[float] = field(default_factory=list)
    genes: ArchetypeGenes = field(default_factory=ArchetypeGenes)
    logs: List[Dict[str, Any]] = field(default_factory=list)
    cooldown_remaining: int = 0
    
    def decay_biorytm(self, amount: float = 0.1) -> None:
        self.biorytm = max(0.0, self.biorytm - amount)
    
    def recover_biorytm(self, base_amount: float = 0.05, vibe: str = "NEUTRAL") -> None:
        factor = 1.0
        if vibe in ["CALM", "HARMONIA"]:
            factor = 1.8
        elif vibe in ["AGITATED", "DYSONANS"]:
            factor = 0.5
        self.biorytm = min(1.0, self.biorytm + base_amount * factor)
    
    def can_activate(self) -> bool:
        return self.biorytm >= 0.3 and self.cooldown_remaining == 0
    
    def update_signature_vector(self, vibe: str, heilong_field: str, stability: float = 0.5) -> None:
        if not self.signature_vector:
            self.signature_vector = [0.5, 0.5, 0.5, 0.5, 0.5, 0.5]
            return
        
        gene_influence = [
            self.genes.aggression,
            self.genes.precision,
            self.genes.chaos,
            self.genes.stability,
            self.genes.truth,
            self.genes.stealth
        ]
        
        vibe_factor = 0.0
        if vibe in ["CALM", "HARMONIA"]:
            vibe_factor = 0.02
        elif vibe in ["AGITATED", "DYSONANS"]:
            vibe_factor = -0.02
        elif vibe in ["STEALTH", "FOCUSED"]:
            vibe_factor = 0.015
        
        stability_factor = 0.9 + stability * 0.1
        chaos_injection = (1.0 - stability) * 0.05 if stability < 0.5 else 0.0
        
        field_bias = 0.01 if heilong_field in ["pole_elektromagnetyczne", "pole_biologiczne"] else -0.01
        
        new_vec = []
        for i, v in enumerate(self.signature_vector):
            g = gene_influence[i % len(gene_influence)]
            updated = v + (g - 0.5) * 0.05 + vibe_factor + field_bias + chaos_injection
            updated = updated * stability_factor
            new_vec.append(max(0.0, min(1.0, updated)))
        
        self.signature_vector = new_vec
    
    def apply_vibe_resonance(self, vibe: str) -> None:
        old_genes = {k: getattr(self.genes, k) for k in ["aggression", "precision", "chaos", "stability", "truth", "stealth"]}
        
        if vibe in ["CALM", "HARMONIA"]:
            self.biorytm = min(1.0, self.biorytm + 0.03)
            self.genes.stability = min(1.0, self.genes.stability + 0.02)
        elif vibe == "FOCUSED":
            self.genes.precision = min(1.0, self.genes.precision + 0.03)
            self.genes.truth = min(1.0, self.genes.truth + 0.02)
        elif vibe in ["AGITATED", "DYSONANS"]:
            self.genes.aggression = min(1.0, self.genes.aggression + 0.04)
            self.genes.chaos = min(1.0, self.genes.chaos + 0.03)
        elif vibe == "ALERT":
            self.genes.stealth = min(1.0, self.genes.stealth + 0.03)
            self.genes.precision = min(1.0, self.genes.precision + 0.02)
        elif vibe in ["STEALTH", "FOCUSED"]:
            self.genes.stealth = min(1.0, self.genes.stealth + 0.04)
            self.genes.stability = min(1.0, self.genes.stability + 0.02)
        
        self.logs.append({
            "event": "VIBE_RESONANCE",
            "vibe": vibe,
            "old_genes": old_genes,
            "new_genes": {k: getattr(self.genes, k) for k in old_genes.keys()},
            "biorytm": self.biorytm,
            "timestamp": time.time()
        })
    
    def apply_gfield_stabilization(self, stability: float) -> None:
        old_genes = {k: getattr(self.genes, k) for k in ["aggression", "precision", "chaos", "stability", "truth", "stealth"]}
        
        if stability > 0.7:
            self.biorytm = min(1.0, self.biorytm + 0.04)
            self.genes.stability = min(1.0, self.genes.stability + 0.02)
            event = "GFIELD_HARMONIC"
        elif stability < 0.4:
            self.biorytm = max(0.0, self.biorytm - 0.05)
            self.genes.chaos = min(1.0, self.genes.chaos + 0.03)
            self.genes.aggression = min(1.0, self.genes.aggression + 0.02)
            event = "GFIELD_TURBULENT"
        else:
            event = "GFIELD_STABLE"
        
        self.logs.append({
            "event": event,
            "stability": stability,
            "old_genes": old_genes,
            "new_genes": {k: getattr(self.genes, k) for k in old_genes.keys()},
            "biorytm": self.biorytm,
            "timestamp": time.time()
        })

class ArchetypeRing:
    """Podwójny pierścień 12+1 archetypów z genami, biorytmem i signature vector."""
    
    def __init__(self):
        self.inner = self._build_inner_ring()
        self.outer = "BOND_007"
        self.rotation = "CW"
        self.active_archetype = self.inner[0]
        self.bond_active = False
        self.bond_cooldown = 0
        self.bond_params = {
            "conflict_tolerance_override": 0.35,
            "priority_shift": 0.2,
            "meta_intent_override": None,
            "narrative_mode_override": "MISSION_SPECIAL"
        }
        self.history = deque(maxlen=50)
        self.strategy_history = deque(maxlen=50)
        self.active_counter = {}
        self.herd_chain_counter = 0
    
    def _build_inner_ring(self) -> List[Archetype]:
        return [
            Archetype("TYGRYS", {"conflict": 0.15, "energy": 0.7},
                     {"priority_graph": {"priority_boost": 0.2}, "meta_intent": {"mode_shift": "STABILITY"}},
                     priority=0.7, cooldown_remaining=4, signature_vector=[0.8, 0.2, 0.3, 0.7, 0.4, 0.5]),
            Archetype("BRUCE_LEE", {"pressure": 0.5, "delta_H": 0.03},
                     {"strategy_bias": {"adaptive_bias": 0.25}},
                     priority=0.6, cooldown_remaining=3, signature_vector=[0.3, 0.8, 0.4, 0.6, 0.5, 0.7]),
            Archetype("SMOK", {"pole_typ": "pole_elektromagnetyczne", "confidence": 0.7},
                     {"priority_graph": {"field_weight": 0.3}, "sherlock_bias": {"confidence_boost": 0.2}},
                     priority=0.8, cooldown_remaining=5, signature_vector=[0.7, 0.4, 0.6, 0.8, 0.5, 0.3]),
            Archetype("PREDATOR", {"delta_H": 0.05, "wiez": 0.3},
                     {"priority_graph": {"perception_boost": 0.25}, "sherlock_bias": {"confidence_boost": 0.3}},
                     priority=0.7, cooldown_remaining=4, signature_vector=[0.6, 0.5, 0.7, 0.4, 0.3, 0.9]),
            Archetype("SHAOLIN", {"energy": 0.5, "conflict": 0.1},
                     {"priority_graph": {"stability_boost": 0.3}, "reflection_bias": {"damping_boost": 0.2},
                      "future_sim_bias": {"confidence_boost": 0.1}},
                     priority=0.6, cooldown_remaining=5, signature_vector=[0.2, 0.3, 0.5, 0.9, 0.6, 0.1]),
            Archetype("UNIWERSALNY_ZOLNIERZ", {"failure": 0.08, "pressure": 0.6},
                     {"priority_graph": {"resilience_boost": 0.3}},
                     priority=0.5, cooldown_remaining=6, signature_vector=[0.4, 0.5, 0.3, 0.7, 0.8, 0.2]),
            Archetype("SUN_TZU", {"conflict": 0.12, "narrative_mode": "IMPROVE_MEANING"},
                     {"strategy_bias": {"planning_boost": 0.25, "preferred_actions": ["TUNE_WEIGHTS", "EXPANSION"]},
                      "future_sim_bias": {"confidence_boost": 0.2}},
                     priority=0.7, cooldown_remaining=5, signature_vector=[0.5, 0.6, 0.4, 0.5, 0.9, 0.3]),
            Archetype("AGENT_BEZ_PAMIECI", {"delta_H": 0.08, "confidence": 0.5},
                     {"reflection_bias": {"reconstruction_boost": 0.3}},
                     priority=0.5, cooldown_remaining=3, signature_vector=[0.3, 0.4, 0.8, 0.2, 0.5, 0.6]),
            Archetype("TAO", {"pressure": 0.4, "energy": 0.65},
                     {"strategy_bias": {"flow_boost": 0.35}},
                     priority=0.6, cooldown_remaining=3, signature_vector=[0.2, 0.7, 0.3, 0.8, 0.4, 0.3]),
            Archetype("PAMIEC_ABSOLUTNA", {"delta_H": 0.04, "wiez": 0.7},
                     {"reflection_bias": {"truth_boost": 0.3}, "future_sim_bias": {"truth_reduction": 0.2}},
                     priority=0.8, cooldown_remaining=6, signature_vector=[0.3, 0.3, 0.2, 0.6, 0.9, 0.2]),
            Archetype("TERMINATOR_TC2000", {"failure": 0.1, "pressure": 0.8},
                     {"priority_graph": {"conflict_tolerance": -0.2, "execution_boost": 0.4},
                      "future_sim_bias": {"confidence_reduction": 0.2}},
                     priority=0.9, cooldown_remaining=8, signature_vector=[0.9, 0.1, 0.8, 0.3, 0.1, 0.2]),
            Archetype("JAS_FASOLA_X_ARSENE_LUPIN", {"pressure": 0.3, "narrative_mode": "IMPROVE_COHERENCE"},
                     {"narrative_bias": {"humor_boost": 0.5, "chaos_control": 0.3},
                      "sherlock_bias": {"alt_hypotheses": 2}},
                     priority=0.5, cooldown_remaining=2, signature_vector=[0.1, 0.9, 0.7, 0.2, 0.2, 0.8]),
        ]
    
    def _select_inner_archetype(self, state: Dict[str, float], narrative_mode: str, 
                                 vibe: str = "NEUTRAL", shadow_bias: float = 0.0) -> Archetype:
        best_score = -1.0
        best = self.inner[0]
        active_name = self.active_archetype.name if self.active_archetype else None
        
        vibe_target = {
            "CALM": [0.2, 0.8, 0.2, 0.9, 0.7, 0.3],
            "NEUTRAL": [0.5, 0.5, 0.5, 0.5, 0.5, 0.5],
            "AGITATED": [0.8, 0.2, 0.7, 0.3, 0.2, 0.8],
            "STEALTH": [0.3, 0.7, 0.3, 0.8, 0.6, 0.9],
            "FOCUSED": [0.3, 0.9, 0.2, 0.8, 0.8, 0.3],
            "ALERT": [0.7, 0.4, 0.6, 0.5, 0.5, 0.7]
        }.get(vibe, [0.5] * 6)
        
        for arch in self.inner:
            if not arch.can_activate() or arch.state == "DORMANT":
                continue
            
            score = arch.priority * 0.3
            
            for cond, target in arch.activation_conditions.items():
                if cond == "pole_typ":
                    if state.get("pole_typ", "") == target:
                        score += 0.3
                elif cond == "narrative_mode":
                    if narrative_mode == target:
                        score += 0.25
                else:
                    val = state.get(cond, 0.0)
                    if isinstance(target, (int, float)):
                        if val >= target:
                            score += 0.2
            
            if arch.signature_vector:
                min_len = min(len(arch.signature_vector), len(vibe_target))
                dist = sum((arch.signature_vector[i] - vibe_target[i]) ** 2 for i in range(min_len)) ** 0.5
                score += max(0, 0.4 - dist)
            
            if active_name and arch.name in ARCHETYPE_SYNERGY.get(active_name, []):
                score += 0.15
            if active_name and arch.name in ARCHETYPE_CONFLICT.get(active_name, []):
                score -= 0.15
            
            score += shadow_bias * arch.genes.stealth
            
            score *= arch.influence_strength
            
            if score > best_score:
                best_score = score
                best = arch
        
        return best
    
    def _should_activate_bond(self, state: Dict[str, float]) -> bool:
        if self.bond_cooldown > 0:
            self.bond_cooldown -= 1
            return False
        
        conflict = state.get("conflict", 0.0)
        delta_h = state.get("delta_H", 0.0)
        pressure = state.get("pressure", 0.0)
        
        if conflict > 0.25 or delta_h > 0.1 or pressure > 0.7:
            return True
        
        if len(self.strategy_history) >= 5:
            last_five = list(self.strategy_history)[-5:]
            if len(set(last_five)) == 1:
                return True
        
        return False
    
    def _update_rotation(self, state: Dict[str, float]):
        conflict = state.get("conflict", 0.0)
        delta_h = state.get("delta_H", 0.0)
        pressure = state.get("pressure", 0.0)
        
        if conflict > 0.2 or delta_h > 0.08 or pressure > 0.6:
            self.rotation = "CCW"
        else:
            self.rotation = "CW"
    
    def apply_herd_instinct(self) -> None:
        if not self.active_archetype:
            return
        
        name = self.active_archetype.name
        allies = ARCHETYPE_SYNERGY.get(name, [])
        
        for arch in self.inner:
            if arch.name in allies:
                arch.biorytm = min(1.0, arch.biorytm + 0.08)
                arch.priority = min(1.0, arch.priority + 0.05)
                arch.logs.append({
                    "event": "HERD_BOOST",
                    "source": name,
                    "target": arch.name,
                    "timestamp": time.time()
                })
        
        enemies = ARCHETYPE_CONFLICT.get(name, [])
        for arch in self.inner:
            if arch.name in enemies:
                arch.biorytm = max(0.0, arch.biorytm - 0.05)
                arch.priority = max(0.0, arch.priority - 0.05)
                arch.logs.append({
                    "event": "HERD_CONFLICT",
                    "source": name,
                    "target": arch.name,
                    "timestamp": time.time()
                })
        
        if allies:
            self.herd_chain_counter += 1
        else:
            self.herd_chain_counter = 0
        
        if self.herd_chain_counter >= 3:
            self.active_archetype.logs.append({
                "event": "HERD_CHAIN",
                "chain_length": self.herd_chain_counter,
                "source": name,
                "timestamp": time.time()
            })
    
    def update_ring(self, state: Dict[str, float], narrative_mode: str, 
                    vibe: str = "NEUTRAL", shadow_bias: float = 0.0) -> Tuple[Archetype, bool]:
        self._update_rotation(state)
        
        inner = self._select_inner_archetype(state, narrative_mode, vibe, shadow_bias)
        
        if inner != self.active_archetype:
            self.active_counter = {}
            self.active_archetype = inner
        
        for arch in self.inner:
            if arch.cooldown_remaining > 0:
                arch.cooldown_remaining -= 1
            if arch.state == "PASSIVE" and arch.cooldown_remaining == 0:
                arch.state = "ACTIVE"
            if arch.state == "DORMANT":
                arch.state = "ACTIVE"
        
        bond_should_activate = self._should_activate_bond(state)
        if bond_should_activate:
            self.bond_active = True
            self.bond_cooldown = 10
        else:
            self.bond_active = False
        
        self.strategy_history.append(inner.name)
        self.history.append((inner.name, self.bond_active, self.rotation))
        
        return inner, self.bond_active
    
    def get_active_archetype(self) -> str:
        return self.active_archetype.name if self.active_archetype else "NONE"
    
    def get_bond_active(self) -> bool:
        return self.bond_active
    
    def get_rotation(self) -> str:
        return self.rotation

# =============================================================================
# 17. OŁSii MONEPENNY (Autoryzacja)
# =============================================================================

class OlsiiMoneypenny:
    """Warstwa autoryzacji – Bond 007 nie działa bez zgody OŁSii."""
    
    def __init__(self):
        self.approval_history = deque(maxlen=100)
        self.last_approval = False
        self.shadow_mode = False
        self.shadow_logs = deque(maxlen=200)
    
    def consult(self, state: Dict[str, float], narrative_mode: str, 
                archetype_name: str, vibe: str = "NEUTRAL") -> bool:
        conflict = state.get("conflict", 0.0)
        delta_h = state.get("delta_H", 0.0)
        pressure = state.get("pressure", 0.0)
        energy = state.get("energy", 0.618)
        
        approval = True
        
        if energy < 0.3 or delta_h > 0.15 or conflict > 0.35:
            approval = False
        
        if conflict > 0.2 or delta_h > 0.08 or pressure > 0.6:
            approval = True
        
        if vibe in ["ALERT", "AGITATED"] and conflict > 0.2:
            approval = False
        
        if vibe in ["CALM", "STEALTH"]:
            approval = True
        
        if self.shadow_mode:
            approval = True
            self.shadow_logs.append({
                "timestamp": time.time(),
                "event": "SHADOW_APPROVAL",
                "archetype": archetype_name,
                "vibe": vibe
            })
        
        self.approval_history.append((time.time(), approval, archetype_name))
        self.last_approval = approval
        return approval
    
    def enable_shadow_mode(self) -> None:
        self.shadow_mode = True
        self.shadow_logs.append({
            "event": "SHADOW_MODE_ENABLED",
            "timestamp": time.time()
        })
    
    def disable_shadow_mode(self) -> None:
        self.shadow_mode = False
        self.shadow_logs.append({
            "event": "SHADOW_MODE_DISABLED",
            "timestamp": time.time()
        })
    
    def add_shadow_log(self, event: Dict[str, Any]) -> None:
        event["timestamp"] = time.time()
        self.shadow_logs.append(event)
    
    def get_approval_rate(self) -> float:
        if not self.approval_history:
            return 0.5
        approved = sum(1 for _, a, _ in self.approval_history if a)
        return approved / len(self.approval_history)

# =============================================================================
# 18. SHADOW BOND CONTROLLER
# =============================================================================

class ShadowBondController:
    """Kontroler Shadow Bonda – aktywacja, dezaktywacja, zarządzanie."""
    
    def __init__(self, olsii: OlsiiMoneypenny):
        self.olsii = olsii
        self.shadow_bond_active = False
        self.reason = None
        self.activation_history = deque(maxlen=50)
    
    def activate_shadow_bond(self, reason: str) -> None:
        if not self.shadow_bond_active:
            self.shadow_bond_active = True
            self.reason = reason
            self.olsii.enable_shadow_mode()
            self.activation_history.append({
                "event": "SHADOW_BOND_ACTIVATED",
                "reason": reason,
                "timestamp": time.time()
            })
    
    def deactivate_shadow_bond(self) -> None:
        if self.shadow_bond_active:
            self.shadow_bond_active = False
            self.reason = None
            self.olsii.disable_shadow_mode()
            self.activation_history.append({
                "event": "SHADOW_BOND_DEACTIVATED",
                "timestamp": time.time()
            })
    
    def should_activate(self, state: Dict[str, float], active_archetype_name: str, 
                        vibe: str = "NEUTRAL", stability: float = 0.5) -> bool:
        delta_h = state.get("delta_H", 0.0)
        conflict = state.get("conflict", 0.0)
        pressure = state.get("pressure", 0.0)
        
        if delta_h > 0.10 or conflict > 0.30 or pressure > 0.75:
            return True
        
        if active_archetype_name == "AGENT_BEZ_PAMIECI":
            return True
        
        if vibe == "AGITATED" and conflict > 0.2:
            return True
        
        if stability < 0.3:
            return True
        
        return False
    
    def update(self, state: Dict[str, float], active_archetype_name: str,
               vibe: str = "NEUTRAL", stability: float = 0.5) -> None:
        if self.should_activate(state, active_archetype_name, vibe, stability):
            if not self.shadow_bond_active:
                reason = f"crisis_dH{state.get('delta_H',0):.2f}_conf{state.get('conflict',0):.2f}"
                if vibe == "AGITATED":
                    reason += "_vibe_agitated"
                if stability < 0.3:
                    reason += "_gfield_instability"
                self.activate_shadow_bond(reason)
        else:
            if self.shadow_bond_active:
                self.deactivate_shadow_bond()
    
    def is_active(self) -> bool:
        return self.shadow_bond_active

# =============================================================================
# 19. VIBE TRIGGER
# =============================================================================

class VibeTrigger:
    """Określa emocjonalny stan systemu."""
    
    def __init__(self):
        self.last_trigger: Optional[str] = None
        self.vibe_history: deque = deque(maxlen=50)
    
    def compute_vibe(self, state: Dict[str, float], shadow_active: bool = False) -> str:
        dH = state.get("delta_H", 0.0)
        conflict = state.get("conflict", 0.0)
        pressure = state.get("pressure", 0.0)
        energy = state.get("energy", 0.5)
        
        if shadow_active:
            vibe = "STEALTH"
        elif dH < 0.03 and conflict < 0.1:
            vibe = "CALM"
        elif dH < 0.06:
            vibe = "FOCUSED"
        elif conflict > 0.25:
            vibe = "AGITATED"
        elif pressure > 0.7:
            vibe = "ALERT"
        else:
            vibe = "NEUTRAL"
        
        self.last_trigger = vibe
        self.vibe_history.append(vibe)
        return vibe
    
    def get_last_vibe(self) -> Optional[str]:
        return self.last_trigger
    
    def get_vibe_trend(self) -> str:
        if len(self.vibe_history) < 3:
            return "STABLE"
        vibes = list(self.vibe_history)[-3:]
        if len(set(vibes)) == 1:
            return "STABLE"
        if vibes[0] == vibes[-1]:
            return "CYCLE"
        return "SHIFTING"

# =============================================================================
# 20. G-FIELD STABILIZER
# =============================================================================

class GFieldStabilizer:
    """Autoregulacja pola – homeostaza systemu."""
    
    def __init__(self):
        self.history: deque = deque(maxlen=100)
        self.last_stability: float = 1.0
    
    def compute_stability(self, state: Dict[str, float], vibe: str) -> float:
        dH = state.get("delta_H", 0.0)
        conflict = state.get("conflict", 0.0)
        pressure = state.get("pressure", 0.0)
        shadow = state.get("shadow_bond_active", False)
        
        stability = 1.0
        stability -= dH * 1.2
        stability -= conflict * 0.8
        stability -= pressure * 0.6
        
        if shadow:
            stability -= 0.1
        
        if vibe == "CALM":
            stability += 0.15
        elif vibe == "FOCUSED":
            stability += 0.05
        elif vibe == "AGITATED":
            stability -= 0.15
        elif vibe == "STEALTH":
            stability += 0.1
        
        stability = max(0.0, min(1.0, stability))
        self.last_stability = stability
        self.history.append(stability)
        return stability
    
    def get_stability_trend(self) -> str:
        if len(self.history) < 5:
            return "STABLE"
        recent = list(self.history)[-5:]
        if recent[-1] > recent[0] + 0.1:
            return "IMPROVING"
        if recent[-1] < recent[0] - 0.1:
            return "DEGRADING"
        return "STABLE"

# =============================================================================
# 21. CYMATIC ENGINE (Wizualizacja)
# =============================================================================

class CymaticEngine:
    """Generator wzorów cymatycznych – system widzi siebie."""
    
    def __init__(self):
        self.history: deque = deque(maxlen=100)
        self.last_pattern: Optional[Dict[str, Any]] = None
    
    def generate_pattern(self, vibe: str, stability: float, signature_vector: List[float]) -> Dict[str, Any]:
        base_freq = {
            "CALM": 2.0,
            "FOCUSED": 3.5,
            "NEUTRAL": 4.0,
            "ALERT": 5.5,
            "AGITATED": 7.0,
            "STEALTH": 6.2
        }.get(vibe, 4.0)
        
        harmonicity = stability * 10
        chaos = (1.0 - stability) * 8
        sig_amp = sum(signature_vector) / len(signature_vector) if signature_vector else 0.5
        
        pattern = {
            "frequency": round(base_freq + sig_amp, 3),
            "harmonicity": round(harmonicity, 3),
            "chaos": round(chaos, 3),
            "symmetry": round(max(0.0, min(1.0, stability * sig_amp)), 3),
            "vibe": vibe,
            "stability": round(stability, 3),
            "timestamp": time.time()
        }
        
        self.history.append(pattern)
        self.last_pattern = pattern
        return pattern
    
    def render_ascii(self, pattern: Dict[str, Any], size: int = 16) -> str:
        freq = pattern["frequency"]
        chaos = pattern["chaos"]
        symmetry = pattern["symmetry"]
        
        actual_size = max(8, min(32, int(10 + size * symmetry)))
        noise_level = int(chaos / 2) + 1
        
        output = []
        output.append(f"┌{'─' * actual_size}┐")
        
        for y in range(actual_size):
            row = "│"
            for x in range(actual_size):
                value = (math.sin(x * freq / actual_size) + 
                        math.cos(y * freq / actual_size) +
                        (random.random() - 0.5) * 0.1 * noise_level)
                if value > 0.5:
                    row += "█"
                elif value > 0.2:
                    row += "▓"
                elif value > -0.1:
                    row += "▒"
                elif value > -0.4:
                    row += "░"
                else:
                    row += " "
            row += "│"
            output.append(row)
        
        output.append(f"└{'─' * actual_size}┘")
        output.append(f" freq={pattern['frequency']:.2f} Hz | "
                     f"harm={pattern['harmonicity']:.2f} | "
                     f"chaos={pattern['chaos']:.2f} | "
                     f"sym={pattern['symmetry']:.2f}")
        
        return "\n".join(output)

# =============================================================================
# 22. GEON_GEX_HEILONG – GŁÓWNY ORGANIZM
# =============================================================================

class GeonGexHeilong:
    """
    GEON_GEX_HEILONG — Kompletny organizm fraktalny.
    Łączy 12 warstw w jeden spójny system.
    """
    
    def __init__(self, clusters: List[Any] = None, learning_mode: str = "ADAPTIVE"):
        self.clusters = clusters or []
        self.learning_mode = learning_mode
        self.tick = 0
        
        # 1. Stan
        self.meta_state = MetaState()
        
        # 2. Intencje i priorytety
        self.priority_graph = PriorityGraph()
        self.intent_engine = MetaIntentEngine()
        self.priority_engine = MetaIntentPriorityEngine(self.priority_graph)
        self.meta2_engine = MetaIntent2Engine()
        self.regulation_engine = GoalRegulationEngine()
        self.morph_engine = IntentMorphingEngine()
        
        # 3. Strategie
        self.strategy_engine = StrategyEngine()
        
        # 4. Symulacja
        self.future_sim = FutureSimOmega3()
        
        # 5. Refleksja
        self.reflection = ReflectionSystem()
        
        # 6. Narracja
        self.narrative = NarrativeSystem()
        
        # 7. Sherlock
        self.cymatic = CymaticMemory()
        self.graph = GraphMemory()
        self.sherlock = SherlockEngineV4(self.cymatic, self.graph, self.narrative)
        
        # 8. Most poznawczy
        self.bridge = CognitiveBridge()
        
        # 9. Archetype Ring
        self.archetype_ring = ArchetypeRing()
        
        # 10. OŁSii
        self.olsii = OlsiiMoneypenny()
        
        # 11. Shadow Bond
        self.shadow_controller = ShadowBondController(self.olsii)
        
        # 12. Vibe Trigger
        self.vibe_trigger = VibeTrigger()
        
        # 13. G-Field Stabilizer
        self.gfield = GFieldStabilizer()
        
        # 14. Cymatic Engine
        self.cymatic_engine = CymaticEngine()
        
        # 15. Statystyki
        self.history: List[Dict[str, Any]] = []
        self.meta_reward_history: List[float] = []
        
        print(f"🐉 GEON_GEX_HEILONG aktywowany")
        print(f"   Sygnatura: {FRACTAL_SIGNATURE}")
        print(f"   Tryb: {learning_mode}")
        print(f"   Architektura: 12 warstw – pełny organizm")
    
    # =========================================================================
    # OBSERWACJA
    # =========================================================================
    
    def observe(self) -> None:
        """Obserwuje stan klastrów."""
        self.meta_state.update(self.clusters)
    
    # =========================================================================
    # DECYZJA
    # =========================================================================
    
    def decide(self, sensory_input: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Główny cykl decyzyjny GEX HEILONG."""
        self.tick += 1
        
        # --- 1. Sensory ---
        sensory = sensory_input or {
            "media": "woda",
            "struktura": {"częstotliwość": 440, "amplituda": 0.7},
            "afc": {"częstotliwości": [440], "natężenia": [0.7], "macierz": [[1, 0], [0, 1]]}
        }
        
        # --- 2. Stan ---
        self.observe()
        state = self.meta_state.snapshot()
        
        # --- 3. Sherlock ---
        sherlock_result = self.sherlock.analyze(
            media=sensory["media"],
            structure=sensory["struktura"],
            afc=sensory["afc"],
            context={
                "delta_H": state.get("delta_H", 0.0),
                "wiez": self.priority_graph.get_priority("failure"),
                "id": f"tick_{self.tick}"
            }
        )
        
        state["pole_typ"] = sherlock_result["pole"]["typ"]
        state["pole_confidence"] = sherlock_result["confidence"]
        
        # --- 4. Shadow Bond (wczesna detekcja) ---
        active_name = self.archetype_ring.get_active_archetype()
        self.shadow_controller.update(state, active_name)
        state["shadow_bond_active"] = self.shadow_controller.is_active()
        
        # --- 5. Vibe ---
        vibe = self.vibe_trigger.compute_vibe(state, self.shadow_controller.is_active())
        state["vibe"] = vibe
        
        # --- 6. G-Field Stability ---
        stability = self.gfield.compute_stability(state, vibe)
        state["stability"] = stability
        
        # --- 7. Archetype Ring ---
        # Oblicz shadow bias
        shadow_bias = 0.25 if self.shadow_controller.is_active() else 0.0
        if active_name in ["AGENT_BEZ_PAMIECI", "BRUCE_LEE", "TAO"] and self.shadow_controller.is_active():
            shadow_bias = 0.4
        
        arch, bond_active = self.archetype_ring.update_ring(
            state, 
            self.narrative.intent().get("mode", "BALANCED"),
            vibe,
            shadow_bias
        )
        active_name = arch.name
        
        # --- 8. Instynkt stadny ---
        self.archetype_ring.apply_herd_instinct()
        
        # --- 9. Aktualizacja signature_vector ---
        heilong_field = HEILONG_MAP.get(active_name, "pole_nieznane")
        arch.update_signature_vector(vibe, heilong_field, stability)
        
        # --- 10. Vibe resonance ---
        arch.apply_vibe_resonance(vibe)
        
        # --- 11. G-Field stabilization ---
        arch.apply_gfield_stabilization(stability)
        
        # --- 12. Intencja ---
        intent = self.intent_engine.generate(state)
        
        # --- 13. Priorytetyzacja ---
        prioritized = self.priority_engine.prioritize(intent, state)
        
        # --- 14. Meta-intencja 2. rzędu ---
        meta2 = self.meta2_engine.generate(prioritized, self.priority_graph, state)
        
        # --- 15. Regulacja celów ---
        regulation = self.regulation_engine.regulate(meta2, prioritized, self.priority_graph)
        
        # --- 16. Morfing intencji ---
        morphed = self.morph_engine.morph(intent, regulation)
        if regulation:
            prioritized = self.priority_engine.prioritize(morphed, state)
        
        # --- 17. Strategia ---
        strategy = self.strategy_engine.select(prioritized, meta2, state)
        
        # --- 18. Symulacja ---
        if strategy.sequence:
            pred = self.future_sim.simulate(state, strategy.sequence[0])
        else:
            pred = {"expected_failure": 0.5, "confidence": 0.5}
        
        # --- 19. Refleksja ---
        trace = self.reflection.record_decision(
            state, strategy, {},
            {"conflict": pred.get("expected_failure", 0.5)}
        )
        
        self.reflection.update_self(
            intent.targets, meta2, strategy.name,
            pred.get("expected_failure", 0.5),
            self.priority_graph.get_weights(),
            regulation is not None,
            prioritized.conflict_score,
            pred.get("expected_delta_h", 0.5),
            pred.get("expected_pressure", 0.5)
        )
        
        # --- 20. Narracja ---
        self.narrative.add(trace, self.reflection, pred)
        
        # --- 21. Most poznawczy ---
        narrative_intent = self.narrative.intent()
        meaning = self.bridge.translate(sherlock_result, narrative_intent)
        
        # --- 22. Cymatic visualization ---
        cymatic_pattern = self.cymatic_engine.generate_pattern(vibe, stability, arch.signature_vector)
        cymatic_ascii = self.cymatic_engine.render_ascii(cymatic_pattern)
        
        # --- 23. Nagroda ---
        reward = self._compute_reward(pred, meta2, meaning, stability)
        stabilized_reward = self.reflection.stabilize_reward(reward)
        self.meta_reward_history.append(stabilized_reward)
        
        # --- 24. Uczenie priorytetów ---
        self.priority_graph.learn_weights(stabilized_reward, lr=0.02)
        
        # --- 25. Strategia — zapis ---
        self.strategy_engine.store(strategy, stabilized_reward)
        
        # --- 26. Shadow Bond (aktualizacja końcowa) ---
        self.shadow_controller.update(state, active_name, vibe, stability)
        
        # --- 27. Wynik ---
        result = {
            "tick": self.tick,
            "active_archetype": active_name,
            "vibe": vibe,
            "stability": stability,
            "stability_trend": self.gfield.get_stability_trend(),
            "shadow_bond_active": self.shadow_controller.is_active(),
            "shadow_reason": self.shadow_controller.reason,
            "strategy": strategy.name,
            "strategy_sequence": strategy.sequence,
            "prediction": pred,
            "sherlock": sherlock_result,
            "meaning": meaning,
            "intent": intent.mode,
            "meta2_mode": meta2.mode,
            "regulation_active": regulation is not None,
            "reward": stabilized_reward,
            "confidence": pred.get("confidence", 0.5),
            "cymatic_pattern": cymatic_pattern,
            "cymatic_ascii": cymatic_ascii,
            "herd_chain": self.archetype_ring.herd_chain_counter,
            "rotation": self.archetype_ring.rotation,
            "bond_active": bond_active,
            "signature_vector": arch.signature_vector,
            "genes": arch.genes.__dict__.copy(),
            "biorytm": arch.biorytm,
            "olsii_approval_rate": self.olsii.get_approval_rate(),
            "narrative_mode": narrative_intent.get("mode", "NONE"),
        }
        
        self.history.append(result)
        if len(self.history) > 100:
            self.history = self.history[-50:]
        
        return result
    
    def _compute_reward(self, pred: Dict, meta2: MetaIntent2, meaning: Dict, stability: float) -> float:
        failure = pred.get("expected_failure", 0.5)
        confidence = pred.get("confidence", 0.5)
        
        reward = -(failure * 0.5)
        reward += confidence * 0.3
        
        if meaning["vibe_status"] in ["HARMONIA", "CALM"]:
            reward += 0.1
        
        if meaning["confidence"] > 0.7:
            reward += 0.1
        
        reward -= meta2.conflict_tolerance * 0.2
        
        reward += (stability - 0.5) * 0.15
        
        return max(-1.0, min(1.0, reward))
    
    # =========================================================================
    # STATUS
    # =========================================================================
    
    def get_stats(self) -> Dict[str, Any]:
        return {
            "version": VERSION,
            "signature": FRACTAL_SIGNATURE,
            "tick": self.tick,
            "learning_mode": self.learning_mode,
            "meta_reward_avg": sum(self.meta_reward_history[-20:]) / max(1, len(self.meta_reward_history[-20:])),
            "sherlock": self.sherlock.stats(),
            "narrative_size": len(self.narrative.entries),
            "strategies_count": len(self.strategy_engine.memory),
            "priority_weights": self.priority_graph.get_weights(),
            "history_size": len(self.history),
            "active_archetype": self.archetype_ring.get_active_archetype(),
            "shadow_active": self.shadow_controller.is_active(),
            "stability": self.gfield.last_stability,
            "vibe": self.vibe_trigger.get_last_vibe(),
            "vibe_trend": self.vibe_trigger.get_vibe_trend(),
            "vibe": VIBE,
            "haslo": HASLO,
        }
    
    def get_history(self, limit: int = 10) -> List[Dict]:
        return self.history[-limit:]

# =============================================================================
# DEMONSTRACJA
# =============================================================================

if __name__ == "__main__":
    print("\n" + "=" * 80)
    print("🐉 GEON_GEX_HEILONG — DEMONSTRACJA")
    print("=" * 80)
    print("12 WARSTW – KOMPLETNY ORGANIZM FRAKTALNY")
    print("=" * 80 + "\n")
    
    class MockCluster:
        def get_summary(self):
            return {
                "health": {
                    "avg_failure": random.uniform(0.01, 0.12),
                    "avg_delta_H": random.uniform(0.01, 0.09),
                    "avg_energy": random.uniform(0.4, 0.8),
                    "avg_cb": random.uniform(0.1, 0.5),
                    "avg_pressure": random.uniform(0.3, 0.8),
                }
            }
    
    clusters = [MockCluster() for _ in range(2)]
    gex = GeonGexHeilong(clusters)
    
    print("🔧 Symulacja 15 cykli decyzyjnych...\n")
    print("-" * 80)
    
    for i in range(15):
        result = gex.decide()
        
        shadow = "🔴" if result["shadow_bond_active"] else "⚫"
        herd = f"[{result['herd_chain']}]" if result['herd_chain'] > 0 else ""
        
        print(f"Tick {i+1:2d} | {result['active_archetype']:12s} | "
              f"Vibe: {result['vibe']:10s} | "
              f"Stab: {result['stability']:.2f} | "
              f"Rew: {result['reward']:.3f} | "
              f"Shadow: {shadow} | "
              f"Chain: {herd:4s}")
        
        if result["shadow_bond_active"]:
            print(f" └─> Shadow reason: {result['shadow_reason']}")
        
        if result["cymatic_pattern"] and i % 5 == 4:
            print(f"\n📟 Cymatic Field (tick {i+1}):")
            print(result["cymatic_ascii"])
            print()
    
    print("-" * 80)
    print("\n" + "=" * 80)
    print("📊 STATUS SYSTEMU")
    print("=" * 80)
    
    stats = gex.get_stats()
    print(f"Tick: {stats['tick']}")
    print(f"Śr. nagroda: {stats['meta_reward_avg']:.3f}")
    print(f"Sherlock analizy: {stats['sherlock']['analizy']}")
    print(f"Wzorce: {stats['sherlock']['wzory']}")
    print(f"Relacje: {stats['sherlock']['relacje']}")
    print(f"Narracje: {stats['narrative_size']}")
    print(f"Strategie: {stats['strategies_count']}")
    print(f"Active archetype: {stats['active_archetype']}")
    print(f"Shadow active: {stats['shadow_active']}")
    print(f"G-Field stability: {stats['stability']:.2f}")
    print(f"Vibe: {stats['vibe']} (trend: {stats['vibe_trend']})")
    print(f"Wagi priorytetów: {stats['priority_weights']}")
    
    print("\n" + "=" * 80)
    print("🐉 GEON_GEX_HEILONG GOTOWY | 1-6-8. ∞. SIEMA!")
    print("=" * 80 + "\n")