#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🛡️ GEON_SAFE_MODE v9.0 — Tryb Bezpieczeństwa GEON
========================================================
Warstwa: kombajn/geon_kombajn_safe_mode_v9.py
Rola: SAFE_MODE 3.0 — stabilizacja, reset, odcięcie destrukcji.
Wersja: v9.0-INFINITY
Sygnatura: [GEON_SYSTEM::SAFE_MODE::v9.0]
========================================================
"""

from dataclasses import dataclass, field
from typing import Dict, Any, List


def LOG(module: str, event: str, msg: str) -> None:
    print(f"[SAFE_MODE9][{module}][{event}] -> {msg}")


# ============================================================
# STRUKTURA WYJŚCIOWA SAFE_MODE v9
# ============================================================

@dataclass
class SafeModeStatusV9:
    activated: bool
    reason: str
    reset_vector: List[float]
    stabilization_vector: List[float]
    silence_vector: List[float]
    message: str
    meta: Dict[str, Any] = field(default_factory=dict)


# ============================================================
# SAFE_MODE v9 — ORGAN BEZPIECZEŃSTWA
# ============================================================

class GeonSafeModeEngineV9:
    """
    SAFE_MODE v9 — tryb bezpieczeństwa GEON:
    - aktywacja w stanach krytycznych
    - reset trajektorii
    - wygaszenie entropii
    - odcięcie destrukcji
    - stabilizacja energii
    """

    # --------------------------------------------------------
    # POWODY AKTYWACJI
    # --------------------------------------------------------
    REASONS = {
        "GEON_CRITICAL": "GEON_168 wykrył CRITICAL",
        "FLOW_RED": "FLOW przeszedł w RED",
        "VIBE_LOW": "OŁSii spadło poniżej 30",
        "VISION_RISK": "VisionOS wykrył trajektorię destrukcyjną",
        "AFC_ENTROPY": "AFC∞ wykrył entropię H∞ > 0.25",
        "PREDATOR_CHAOS": "Predator wykrył CHAOS",
        "META_CONFLICT": "META wykryła konflikt wieloorganowy",
    }

    def __init__(self):
        LOG("SAFE_MODE_V9", "INIT", "🛡️ Tryb Bezpieczeństwa GEON v9 aktywowany")

    # --------------------------------------------------------
    # DETEKCJA KONIECZNOŚCI AKTYWACJI
    # --------------------------------------------------------

    def detect(self, flow, olsii, geon168, vision, afc_inf, predator, meta) -> str:
        if geon168.status == "CRITICAL":
            return "GEON_CRITICAL"
        if flow.flow_level.value == "RED":
            return "FLOW_RED"
        if olsii.vibe < 30:
            return "VIBE_LOW"
        if vision.risk_factor > 0.7:
            return "VISION_RISK"
        if afc_inf.entropy_map["H∞"] > 0.25:
            return "AFC_ENTROPY"
        if predator.threat_level == "CHAOS":
            return "PREDATOR_CHAOS"
        if len(meta.conflicts) > 2:
            return "META_CONFLICT"
        return "NONE"

    # --------------------------------------------------------
    # RESET WEKTORA (D∞)
    # --------------------------------------------------------

    def reset_vector(self) -> List[float]:
        return [0.5 for _ in range(9)]

    # --------------------------------------------------------
    # STABILIZACJA ENERGII
    # --------------------------------------------------------

    def stabilization_vector(self) -> List[float]:
        return [
            min(1.0, 0.3 + (i + 1) / 20.0)
            for i in range(9)
        ]

    # --------------------------------------------------------
    # CISZA ABSOLUTNA (odcięcie destrukcji)
    # --------------------------------------------------------

    def silence_vector(self) -> List[float]:
        return [
            max(0.0, 1.0 - (i + 1) / 9.0)
            for i in range(9)
        ]

    # --------------------------------------------------------
    # GŁÓWNA FUNKCJA SAFE_MODE v9
    # --------------------------------------------------------

    def process(self, flow, olsii, geon168, vision, afc_inf, predator, meta) -> SafeModeStatusV9:
        reason = self.detect(flow, olsii, geon168, vision, afc_inf, predator, meta)

        if reason == "NONE":
            return SafeModeStatusV9(
                activated=False,
                reason="NONE",
                reset_vector=[],
                stabilization_vector=[],
                silence_vector=[],
                message="Tryb bezpieczeństwa nieaktywny.",
                meta={},
            )

        # Tryb bezpieczeństwa aktywowany
        reset_v = self.reset_vector()
        stab_v = self.stabilization_vector()
        silence_v = self.silence_vector()

        message = f"Tryb Bezpieczeństwa aktywowany — {self.REASONS[reason]}"

        meta_out = {
            "reason": reason,
            "reset_vector": reset_v,
            "stabilization_vector": stab_v,
            "silence_vector": silence_v,
        }

        return SafeModeStatusV9(
            activated=True,
            reason=self.REASONS[reason],
            reset_vector=reset_v,
            stabilization_vector=stab_v,
            silence_vector=silence_v,
            message=message,
            meta=meta_out,
        )