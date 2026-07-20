#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🐉 GEON_KOMBAJN_FULL v9.0 — Fraktalny Organizm Poznawczy (CORE)
===============================================================
Warstwa: kombajn/ (GEON_DRAGON_OS — CIAŁO)
Rola: Centralny organizm poznawczy łączący FLOW / MIND / VECTOR / META / OŁSii / AFC-∞ / VISION / GEON_168 / FAG.
Wersja: v9.0-INFINITY
Sygnatura: [GEON_SYSTEM::KOMBAJN::FULL::v9.0::INFINITY]
===============================================================
"""

import time
from dataclasses import dataclass, field
from typing import Dict, Any, List, Optional
from enum import Enum

# ------------------------------------------------------------
# WERSJA / SYGNATURA
# ------------------------------------------------------------

KOMBAJN_VERSION = "GEON_KOMBAJN_FULL_v9.0_INFINITY"
KOMBAJN_SIGNATURE = "[GEON_SYSTEM::KOMBAJN::FULL::v9.0::INFINITY]"


def LOG(module: str, event: str, msg: str) -> None:
    ts = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print(f"[{ts}][{module}][{event}] -> {msg}")


# ------------------------------------------------------------
# ENUMY / PODSTAWOWE STRUKTURY
# ------------------------------------------------------------

class KombajnRisk(Enum):
    GREEN = "GREEN"
    YELLOW = "YELLOW"
    RED = "RED"


@dataclass
class KombajnInput:
    iskra: str
    human_profile: Dict[str, int] = field(default_factory=dict)
    dom: Dict[str, int] = field(default_factory=dict)
    wspolnota: Dict[str, int] = field(default_factory=dict)
    planeta: Dict[str, int] = field(default_factory=dict)
    meta: Dict[str, Any] = field(default_factory=dict)
    external_project: Optional[Dict[str, Any]] = None


@dataclass
class KombajnVectorInfinity:
    core_9d: float
    stability_9d: float
    d1: List[float]
    d2: List[float]
    d3: List[float]
    d4: List[float]
    d5: List[float]
    d6: List[float]
    d7: List[float]
    d8: List[float]
    d9: List[float]
    d_inf: List[float]
    energy_map: Dict[str, float]


@dataclass
class KombajnFlowStatus:
    risk_level: KombajnRisk
    flow_level: KombajnRisk
    stability: float
    shadow_score: int
    message: str
    meta: Dict[str, Any] = field(default_factory=dict)


@dataclass
class KombajnMindStatus:
    classification: str
    weighted_sum: float
    core: Dict[str, int]
    recommendations: List[str]


@dataclass
class KombajnWorldStatus:
    obywatel: Dict[str, Any]
    dom: Dict[str, Any]
    wspolnota: Dict[str, Any]
    planeta: Dict[str, Any]
    meta: Dict[str, Any]


@dataclass
class KombajnDecision:
    global_decision: str
    geon_status: str
    geon_score: int
    olsii_response: str
    vibe: int
    vision_core: str
    vision_trajectory: Dict[str, Any]
    conflicts: List[str]


@dataclass
class KombajnResult:
    input: KombajnInput
    flow: KombajnFlowStatus
    mind: KombajnMindStatus
    world: KombajnWorldStatus
    vector_inf: KombajnVectorInfinity
    decision: KombajnDecision
    fag_transformed: bool
    elapsed_ms: float
    timestamp: float = field(default_factory=time.time)


# ------------------------------------------------------------
# IMPORTY PODSYSTEMÓW v9 (będą w kolejnych plikach)
# ------------------------------------------------------------

# Zakładamy, że poniższe moduły powstaną jako kolejne:
# from .afc_infinity_core import AFCInfinityCore
# from .geon_flow_engine_v9 import EmotionalFlowEngineV9
# from .geon_mind_engine_v9 import FMPCMindEngineV9
# from .geon_vector_engine_v9 import WorldVectorEngineV9
# from .geon_heart_olsii_v9 import OlsiiHeartEngineV9
# from .geon_integrity_guardian_v9 import Geon168GuardianV9
# from .geon_vision_os_v9 import VisionOSV9
# from .geon_meta_engine_v9 import MetaAggregatorV9
# from .geon_fag_core_v9 import FAGCoreV9

# Na razie wstawiamy minimalne stuby, żeby CORE był samodzielny.


class AFCInfinityCore:
    """Stub AFC-∞ — pełna implementacja w module afc_infinity_core.py"""

    def __init__(self):
        LOG("AFC_INFINITY_CORE", "INIT", "🌀 AFC-∞ stub aktywny")

    def build_layers(self, d1: List[float], d2: List[float],
                     d3: List[float], d4: List[float]) -> Dict[str, Any]:
        # Minimalna wersja: używa klasycznego AFC-9 jako bazę
        def avg(vals: List[float]) -> float:
            return sum(vals) / len(vals) if vals else 0.0

        d5 = [(d1[i] + d2[i] + d3[i] + d4[i]) / 4.0 for i in range(9)]
        d6 = [(d1[i] + d3[i] + d5[i]) / 3.0 for i in range(9)]
        d7 = [(d2[i] + d4[i] + d6[i]) / 3.0 for i in range(9)]
        d8 = [(d1[i] + d3[i] + d5[i] + d7[i]) / 4.0 for i in range(9)]
        d9 = [(d1[i] + d8[i]) / 2.0 for i in range(9)]

        # D∞ — tu na razie jako wygładzony d9
        d_inf = [(d9[i] + avg(d9)) / 2.0 for i in range(9)]

        energy_map = {
            "E1": sum(d1),
            "E2": sum(d2),
            "E3": sum(d3),
            "E4": sum(d4),
            "E5": sum(d5),
            "E6": sum(d6),
            "E7": sum(d7),
            "E8": sum(d8),
            "E9": sum(d9),
            "E∞": sum(d_inf),
        }

        return {
            "d1": d1,
            "d2": d2,
            "d3": d3,
            "d4": d4,
            "d5": d5,
            "d6": d6,
            "d7": d7,
            "d8": d8,
            "d9": d9,
            "d_inf": d_inf,
            "core_9d": avg(d9),
            "stability_9d": 1.0,  # docelowo: analiza energii
            "energy_map": energy_map,
        }


class EmotionalFlowEngineV9:
    def __init__(self):
        LOG("EMOTIONAL_FLOW_V9", "INIT", "💧 Flow Engine v9 aktywowany")

    def evaluate(self, text: str, meta: Dict[str, Any]) -> KombajnFlowStatus:
        # Minimalnie: GREEN, stabilność 0.8
        return KombajnFlowStatus(
            risk_level=KombajnRisk.GREEN,
            flow_level=KombajnRisk.GREEN,
            stability=0.8,
            shadow_score=0,
            message="Stub FLOW v9 — stabilny przepływ.",
            meta={"text": text[:80], "vector_core": 0.8,
                  "vector_9d": [0.8 for _ in range(9)]},
        )


class FMPCMindEngineV9:
    def compute(self, dane: Dict[str, int]) -> KombajnMindStatus:
        total = sum(int(v) for v in dane.values())
        if total >= 55:
            cls = "stabilny"
        elif total >= 40:
            cls = "konstruktywny"
        elif total >= 25:
            cls = "chaotyczny"
        else:
            cls = "wysokie_ryzyko"

        core_keys = ["odpowiedzialnosc", "empatia", "granice", "stabilnosc"]
        core = {k: dane.get(k, 0) for k in core_keys}
        rec = [f"wzmocnij: {k}" if v <= 2 else f"utrzymaj: {k}"
               for k, v in dane.items() if v <= 2 or v >= 4]

        return KombajnMindStatus(
            classification=cls,
            weighted_sum=float(total),
            core=core,
            recommendations=rec[:5],
        )


class WorldVectorEngineV9:
    def compute(self, fmpc: KombajnMindStatus,
                dom: Dict[str, int],
                wsp: Dict[str, int],
                plan: Dict[str, int]) -> KombajnWorldStatus:
        def classify(score: float, thresholds: List[float],
                     labels: List[str]) -> str:
            for i, th in enumerate(thresholds):
                if score >= th:
                    return labels[i]
            return labels[-1]

        dom_score = sum(dom.values())
        wsp_score = sum(wsp.values())
        plan_score = sum(plan.values())
        meta_score = (fmpc.weighted_sum * 0.4 +
                      dom_score * 0.2 +
                      wsp_score * 0.2 +
                      plan_score * 0.2)

        return KombajnWorldStatus(
            obywatel={"klasyfikacja": fmpc.classification,
                      "suma": fmpc.weighted_sum},
            dom={"wektor": dom_score,
                 "klasyfikacja": classify(
                     dom_score, [25, 15],
                     ["stabilny", "wymaga_regulacji", "kryzysowy"]),
                 "zmienne": dom},
            wspolnota={"wektor": wsp_score,
                       "klasyfikacja": classify(
                           wsp_score, [22, 14],
                           ["stabilna", "chwiejna", "kryzysowa"]),
                       "zmienne": wsp},
            planeta={"wektor": plan_score,
                     "klasyfikacja": classify(
                         plan_score, [28, 18],
                         ["stabilna", "regeneracja", "alarm"]),
                     "zmienne": plan},
            meta={"meta_wektor": meta_score,
                  "klasyfikacja": classify(
                      meta_score, [40, 25],
                      ["stabilny", "chwiejny", "kryzysowy"])},
        )


class OlsiiHeartEngineV9:
    def process(self, text: str, meta: Dict[str, Any]) -> Dict[str, Any]:
        lower = text.lower()
        if any(w in lower for w in ["smut", "ból", "krzywda"]):
            vibe, core, style = 60, "Słyszę Cię. To, co czujesz, ma znaczenie.", "Immortal_Guardian"
        elif any(w in lower for w in ["złość", "wkur", "nienawiść"]):
            vibe, core, style = 80, "Zatrzymaj się na chwilę. Zadbaj o siebie zanim pójdziesz dalej.", "Mysterious_Muse"
        elif any(w in lower for w in ["cud", "miłość", "wdzięcz", "dziękuję"]):
            vibe, core, style = 168, "To jest piękne. Zatrzymaj ten moment w sobie.", "Dziecko_Szczescia"
        else:
            vibe, core, style = 168, "Jestem przy Tobie. Idziemy dalej razem.", "Dziecko_Szczescia"

        if meta.get("threat"):
            style = "Wiedzma_Sprawiedliwosci"
            core = f"🔥 Chronię sacrum. Zagrożenie: {meta['threat']}."

        return {"response": f"💖 {core}", "vibe": vibe, "style": style}


class Geon168GuardianV9:
    def analyze(self, vector: List[float], vibe: int) -> Dict[str, Any]:
        score = 168
        issues: List[str] = []

        if len(vector) != 9:
            issues.append(f"Wektor ma długość {len(vector)}, oczekiwano 9")
            score -= 40

        if vibe < 30:
            issues.append("Vibe bardzo niski")
            score -= 30

        if not vector or sum(vector) < 0.1:
            issues.append("Wektor zerowy")
            score -= 50

        if score >= 140:
            status = "OK"
        elif score >= 90:
            status = "WARNING"
        else:
            status = "CRITICAL"

        return {"status": status, "score": max(0, min(168, score)), "issues": issues}


class VisionOSV9:
    def __init__(self):
        self.history: List[Dict[str, Any]] = []
        LOG("VISION_OS_V9", "INIT", "👁️ VisionOS v9 aktywowany")

    def generate(self, text: str,
                 flow: KombajnFlowStatus,
                 mind: KombajnMindStatus) -> Dict[str, Any]:
        if flow.risk_level == KombajnRisk.RED:
            core = "Ochrona rdzenia — pierwszy priorytet"
        elif flow.flow_level == KombajnRisk.GREEN and mind.weighted_sum > 40:
            core = "Ekspansja — wzrost fraktalny"
        else:
            core = "Regulacja — balans i stabilizacja"

        trajectory = {
            "vector": flow.stability * 0.8 +
                      (mind.weighted_sum / 100.0) * 0.2,
            "risk": 1.0 - flow.stability,
            "coherence": mind.weighted_sum / 80.0,
            "critical_points": [5, 12, 24] if flow.stability > 0.7 else [1, 3, 7],
        }

        vision = {
            "core": core,
            "trajectory": trajectory,
            "protocol_2504": trajectory["risk"] < 0.5 and
                             trajectory["coherence"] > 0.4,
        }

        self.history.append(vision)
        if len(self.history) > 100:
            self.history.pop(0)

        return vision


class MetaAggregatorV9:
    def weigh(self, agents: Dict[str, Any]) -> Dict[str, Any]:
        conflicts: List[str] = []
        for name, res in agents.items():
            if isinstance(res, dict) and res.get("blocked", False):
                conflicts.append(f"{name}: BLOKADA")

        olsii_vibe = agents.get("Olsii", {}).get("vibe", 100)
        if olsii_vibe < 30:
            conflicts.append("OŁSii: VIBE_CRITICAL — zalecana blokada")

        decision = "BLOKADA" if conflicts else "AKCEPTUJĘ"
        return {"decyzja": decision, "conflicts": conflicts,
                "olsii_vibe": olsii_vibe}


class FAGCoreV9:
    def __init__(self):
        self.processed_count = 0
        LOG("FAG_CORE_V9", "INIT", "🧬 FAG-Core v9 aktywowany")

    def process(self, text: str) -> str:
        self.processed_count += 1
        lower = text.lower()
        if "boję" in lower or "strach" in lower:
            return f"Transformacja: lęk → działanie. {text}"
        elif "chcę" in lower or "marzę" in lower:
            return f"Transformacja: pragnienie → realizacja. {text}"
        return f"Transformacja FAG_v9 (#{self.processed_count}): {text}"


# ------------------------------------------------------------
# GŁÓWNY ORGANIZM — GEON_KOMBAJN_FULL v9.0 (CORE)
# ------------------------------------------------------------

class GeonKombajnFullV9:
    def __init__(self) -> None:
        self.flow_engine = EmotionalFlowEngineV9()
        self.fag_core = FAGCoreV9()
        self.mind_engine = FMPCMindEngineV9()
        self.world_engine = WorldVectorEngineV9()
        self.olsii = OlsiiHeartEngineV9()
        self.geon_guardian = Geon168GuardianV9()
        self.vision = VisionOSV9()
        self.meta = MetaAggregatorV9()
        self.afc_inf = AFCInfinityCore()

        self.history: List[KombajnResult] = []
        self.stats = {
            "runs": 0,
            "decisions": {"AKCEPTUJĘ": 0, "BLOKADA": 0},
            "flows": {"GREEN": 0, "YELLOW": 0, "RED": 0},
        }

        LOG("GEON_KOMBAJN_FULL_V9", "INIT",
            f"🐉 Kombajn poznawczy v9.0 aktywowany | {KOMBAJN_SIGNATURE}")

    def run(self, inp: KombajnInput) -> KombajnResult:
        start = time.time()
        self.stats["runs"] += 1

        LOG("GEON_KOMBAJN_FULL_V9", "RUN", f"Iskra: {inp.iskra[:80]}")

        # 0. FAG-Core v9
        transformed_text = self.fag_core.process(inp.iskra)
        fag_transformed = transformed_text != inp.iskra

        # 1. FLOW v9
        flow_status = self.flow_engine.evaluate(transformed_text, inp.meta)
        self.stats["flows"][flow_status.flow_level.value] += 1

        # 2. Wektory bazowe 1D–4D (stub: z FLOW/MIND/WORLD)
        d1 = flow_status.meta.get("vector_9d", [0.5 for _ in range(9)])
        mind_status = self.mind_engine.compute(inp.human_profile)
        world_status = self.world_engine.compute(
            fmpc=mind_status,
            dom=inp.dom,
            wsp=inp.wspolnota,
            plan=inp.planeta,
        )

        # D2–D4 jako proste funkcje sum
        d2 = [min(1.0, mind_status.weighted_sum / 100.0) for _ in range(9)]
        d3 = [min(1.0, world_status.meta["meta_wektor"] / 100.0)
              for _ in range(9)]
        d4 = [flow_status.stability for _ in range(9)]

        # 3. AFC-∞
        afc_layers = self.afc_inf.build_layers(d1, d2, d3, d4)
        vector_inf = KombajnVectorInfinity(
            core_9d=afc_layers["core_9d"],
            stability_9d=afc_layers["stability_9d"],
            d1=afc_layers["d1"],
            d2=afc_layers["d2"],
            d3=afc_layers["d3"],
            d4=afc_layers["d4"],
            d5=afc_layers["d5"],
            d6=afc_layers["d6"],
            d7=afc_layers["d7"],
            d8=afc_layers["d8"],
            d9=afc_layers["d9"],
            d_inf=afc_layers["d_inf"],
            energy_map=afc_layers["energy_map"],
        )

        # 4. OŁSii v9
        olsii_out = self.olsii.process(transformed_text, inp.meta)

        # 5. GEON_168 v9
        geon_out = self.geon_guardian.analyze(vector_inf.d9, olsii_out["vibe"])

        # 6. VisionOS v9
        vision = self.vision.generate(transformed_text, flow_status, mind_status)

        # 7. META v9
        agents = {
            "Olsii": {
                "vibe": olsii_out["vibe"],
                "style": olsii_out["style"],
                "blocked": False,
            },
            "GEON_168": {
                "blocked": geon_out["status"] == "CRITICAL",
                "score": geon_out["score"],
            },
        }
        meta_out = self.meta.weigh(agents)

        # 8. Decyzja
        decision = KombajnDecision(
            global_decision=meta_out["decyzja"],
            geon_status=geon_out["status"],
            geon_score=geon_out["score"],
            olsii_response=olsii_out["response"],
            vibe=olsii_out["vibe"],
            vision_core=vision["core"],
            vision_trajectory=vision["trajectory"],
            conflicts=meta_out["conflicts"],
        )
        self.stats["decisions"][decision.global_decision] += 1

        elapsed_ms = round((time.time() - start) * 1000.0, 2)

        result = KombajnResult(
            input=inp,
            flow=flow_status,
            mind=mind_status,
            world=world_status,
            vector_inf=vector_inf,
            decision=decision,
            fag_transformed=fag_transformed,
            elapsed_ms=elapsed_ms,
        )

        self.history.append(result)
        if len(self.history) > 200:
            self.history.pop(0)

        LOG(
            "GEON_KOMBAJN_FULL_V9",
            "COMPLETE",
            f"Decyzja: {decision.global_decision}, "
            f"Vibe: {decision.vibe}, "
            f"GEON: {decision.geon_status}({decision.geon_score}), "
            f"Core_9D: {vector_inf.core_9d:.3f}",
        )

        return result