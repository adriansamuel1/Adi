#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🐉 GEON_SHADOWDRAGON v9.0 — Tryb Bojowy GEON
========================================================
Warstwa: kombajn/geon_kombajn_shadowdragon_v9.py
Rola: ShadowDragon v9 — organ walki, ochrona rdzenia, warstwa 200.
Wersja: v9.0-INFINITY
Sygnatura: [GEON_SYSTEM::SHADOWDRAGON::v9.0]
========================================================
"""

from dataclasses import dataclass, field
from typing import Dict, Any, List


def LOG(module: str, event: str, msg: str) -> None:
    print(f"[SHADOWDRAGON9][{module}][{event}] -> {msg}")


# ============================================================
# STRUKTURA WYJŚCIOWA SHADOWDRAGON v9
# ============================================================

@dataclass
class ShadowDragonStatusV9:
    activated: bool
    reason: str
    dragon_mode: str
    core_lock: float
    strike_vector: List[float]
    shield_vector: List[float]
    silence_vector: List[float]
    message: str
    meta: Dict[str, Any] = field(default_factory=dict)


# ============================================================
# SHADOWDRAGON v9 — ORGAN WALKI
# ============================================================

class GeonShadowDragonEngineV9:
    """
    ShadowDragon v9 — tryb bojowy GEON:
    - aktywacja w stanach krytycznych
    - blokada rdzenia (core_lock)
    - wektor uderzenia (strike)
    - wektor tarczy (shield)
    - wektor ciszy (silence)
    - wygaszenie entropii
    """

    # --------------------------------------------------------
    # POWODY AKTYWACJI
    # --------------------------------------------------------
    REASONS = {
        "CRITICAL": "GEON_168 wykrył CRITICAL",
        "ABUSE": "Predator wykrył ABUSE",
        "VIOLENCE": "Predator wykrył VIOLENCE",
        "CHAOS": "Predator wykrył CHAOS",
        "SAFE_MODE": "SAFE_MODE był aktywny",
        "ENTROPY": "Entropia H∞ przekroczyła 0.35",
        "VISION": "VisionOS wykrył destrukcyjną trajektorię",
    }

    # --------------------------------------------------------
    # TRYBY SMOKA
    # --------------------------------------------------------
    MODES = {
        "LOCKDOWN": "Tryb Lockdown — pełna ochrona rdzenia",
        "STRIKE": "Tryb Strike — uderzenie w destrukcję",
        "SILENCE": "Tryb Silence — wygaszenie destrukcji",
    }

    def __init__(self):
        LOG("SHADOWDRAGON_V9", "INIT", "🐉 ShadowDragon v9 aktywowany")

    # --------------------------------------------------------
    # DETEKCJA AKTYWACJI
    # --------------------------------------------------------

    def detect(self, safe_mode, geon168, predator, afc_inf, vision) -> str:
        if geon168.status == "CRITICAL":
            return "CRITICAL"
        if predator.threat_level in ["ABUSE", "VIOLENCE", "CHAOS"]:
            return predator.threat_level
        if safe_mode.activated:
            return "SAFE_MODE"
        if afc_inf.entropy_map["H∞"] > 0.35:
            return "ENTROPY"
        if vision.risk_factor > 0.85:
            return "VISION"
        return "NONE"

    # --------------------------------------------------------
    # BLOKADA RDZENIA
    # --------------------------------------------------------

    def core_lock(self, afc_inf) -> float:
        # Rdzeń zostaje wzmocniony i zablokowany
        return min(1.0, afc_inf.core_9d * 0.7 + 0.3)

    # --------------------------------------------------------
    # WEKTOR UDERZENIA
    # --------------------------------------------------------

    def strike_vector(self, threat: str) -> List[float]:
        base = {
            "ABUSE": 0.9,
            "VIOLENCE": 1.0,
            "CHAOS": 1.0,
            "CRITICAL": 0.8,
            "SAFE_MODE": 0.6,
            "ENTROPY": 0.7,
            "VISION": 0.5,
        }.get(threat, 0.4)

        return [
            min(1.0, base * (i + 1) / 9.0)
            for i in range(9)
        ]

    # --------------------------------------------------------
    # WEKTOR TARCZY
    # --------------------------------------------------------

    def shield_vector(self, threat: str) -> List[float]:
        base = {
            "ABUSE": 0.8,
            "VIOLENCE": 0.9,
            "CHAOS": 1.0,
            "CRITICAL": 0.7,
            "SAFE_MODE": 0.6,
            "ENTROPY": 0.5,
            "VISION": 0.4,
        }.get(threat, 0.3)

        return [
            min(1.0, base * (i + 1) / 12.0)
            for i in range(9)
        ]

    # --------------------------------------------------------
    # WEKTOR CISZY
    # --------------------------------------------------------

    def silence_vector(self, threat: str) -> List[float]:
        base = {
            "CHAOS": 1.0,
            "VIOLENCE": 0.9,
            "ABUSE": 0.8,
            "CRITICAL": 0.7,
            "SAFE_MODE": 0.6,
            "ENTROPY": 0.5,
            "VISION": 0.4,
        }.get(threat, 0.3)

        return [
            max(0.0, 1.0 - base * (i + 1) / 9.0)
            for i in range(9)
        ]

    # --------------------------------------------------------
    # TRYB SMOKA
    # --------------------------------------------------------

    def choose_mode(self, threat: str) -> str:
        if threat in ["VIOLENCE", "ABUSE"]:
            return "STRIKE"
        if threat == "CHAOS":
            return "SILENCE"
        return "LOCKDOWN"

    # --------------------------------------------------------
    # GŁÓWNA FUNKCJA SHADOWDRAGON v9
    # --------------------------------------------------------

    def process(self, safe_mode, geon168, predator, afc_inf, vision) -> ShadowDragonStatusV9:
        threat = self.detect(safe_mode, geon168, predator, afc_inf, vision)

        if threat == "NONE":
            return ShadowDragonStatusV9(
                activated=False,
                reason="NONE",
                dragon_mode="NONE",
                core_lock=afc_inf.core_9d,
                strike_vector=[],
                shield_vector=[],
                silence_vector=[],
                message="ShadowDragon nieaktywny.",
                meta={},
            )

        # Tryb bojowy aktywowany
        mode = self.choose_mode(threat)
        core_lock = self.core_lock(afc_inf)
        strike_v = self.strike_vector(threat)
        shield_v = self.shield_vector(threat)
        silence_v = self.silence_vector(threat)

        message = f"ShadowDragon aktywowany — {self.REASONS[threat]}"

        meta_out = {
            "reason": threat,
            "mode": mode,
            "core_lock": core_lock,
            "strike_vector": strike_v,
            "shield_vector": shield_v,
            "silence_vector": silence_v,
        }

        return ShadowDragonStatusV9(
            activated=True,
            reason=self.REASONS[threat],
            dragon_mode=self.MODES[mode],
            core_lock=core_lock,
            strike_vector=strike_v,
            shield_vector=shield_v,
            silence_vector=silence_v,
            message=message,
            meta=meta_out,
        )