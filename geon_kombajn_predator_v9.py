#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
⚔️ GEON_PREDATOR v9.0 — Organ Obronny GEON
========================================================
Warstwa: kombajn/geon_kombajn_predator_v9.py
Rola: Predator Protocol 3.0 — wykrywanie zagrożeń, blokada, ochrona.
Wersja: v9.0-INFINITY
Sygnatura: [GEON_SYSTEM::PREDATOR::v9.0]
========================================================
"""

from dataclasses import dataclass, field
from typing import Dict, Any, List


def LOG(module: str, event: str, msg: str) -> None:
    print(f"[PREDATOR9][{module}][{event}] -> {msg}")


# ============================================================
# STRUKTURA WYJŚCIOWA PREDATOR v9
# ============================================================

@dataclass
class PredatorStatusV9:
    threat_level: str
    mode: str
    shield_vector: List[float]
    cut_vector: List[float]
    message: str
    meta: Dict[str, Any] = field(default_factory=dict)


# ============================================================
# PREDATOR v9 — ORGAN OBRONNY
# ============================================================

class GeonPredatorEngineV9:
    """
    Predator v9 — organ obronny GEON:
    - wykrywanie zagrożeń
    - tryb Wiedźmy Sprawiedliwości
    - tryb Skrzydeł Ochronnych
    - tryb Ciszy Absolutnej
    - modulacja D∞
    """

    # --------------------------------------------------------
    # MAPA ZAGROŻEŃ
    # --------------------------------------------------------
    THREAT_KEYWORDS = {
        "ABUSE": ["krzywdzi", "manipuluje", "wykorzystuje", "niszczy"],
        "VIOLENCE": ["bije", "atak", "przemoc", "grozi"],
        "BETRAYAL": ["zdradza", "oszukuje", "kłamie"],
        "CHAOS": ["niszczy wszystko", "rozpad", "katastrofa"],
        "TOXIC": ["toksyczny", "szkodliwy", "zły wpływ"],
    }

    # --------------------------------------------------------
    # TRYBY PREDATORA
    # --------------------------------------------------------
    MODES = {
        "WITCH": "Wiedźma Sprawiedliwości — detekcja i werdykt",
        "WINGS": "Skrzydła Ochronne — rozszerzenie pola bezpieczeństwa",
        "SILENCE": "Cisza Absolutna — odcięcie destrukcji",
    }

    def __init__(self):
        LOG("PREDATOR_V9", "INIT", "⚔️ Predator Protocol 3.0 aktywowany")

    # --------------------------------------------------------
    # DETEKCJA ZAGROŻENIA
    # --------------------------------------------------------

    def detect_threat(self, text: str) -> str:
        lower = text.lower()
        for level, keywords in self.THREAT_KEYWORDS.items():
            if any(kw in lower for kw in keywords):
                return level
        return "NONE"

    # --------------------------------------------------------
    # WYBÓR TRYBU
    # --------------------------------------------------------

    def choose_mode(self, threat: str) -> str:
        if threat in ["ABUSE", "VIOLENCE"]:
            return "WITCH"
        if threat in ["BETRAYAL", "TOXIC"]:
            return "WINGS"
        if threat == "CHAOS":
            return "SILENCE"
        return "WINGS"

    # --------------------------------------------------------
    # WEKTOR OCHRONNY (Skrzydła)
    # --------------------------------------------------------

    def shield_vector(self, threat: str) -> List[float]:
        base = {
            "NONE": 0.2,
            "TOXIC": 0.5,
            "BETRAYAL": 0.6,
            "ABUSE": 0.8,
            "VIOLENCE": 0.9,
            "CHAOS": 1.0,
        }.get(threat, 0.3)

        return [
            min(1.0, base * (i + 1) / 9.0)
            for i in range(9)
        ]

    # --------------------------------------------------------
    # WEKTOR ODCIĘCIA (Cisza Absolutna)
    # --------------------------------------------------------

    def cut_vector(self, threat: str) -> List[float]:
        base = {
            "NONE": 0.0,
            "TOXIC": 0.3,
            "BETRAYAL": 0.4,
            "ABUSE": 0.7,
            "VIOLENCE": 0.8,
            "CHAOS": 1.0,
        }.get(threat, 0.1)

        return [
            max(0.0, 1.0 - base * (i + 1) / 9.0)
            for i in range(9)
        ]

    # --------------------------------------------------------
    # GŁÓWNA FUNKCJA PREDATOR v9
    # --------------------------------------------------------

    def process(self, text: str) -> PredatorStatusV9:
        # 1. Detekcja zagrożenia
        threat = self.detect_threat(text)

        # 2. Tryb
        mode = self.choose_mode(threat)

        # 3. Wektory
        shield = self.shield_vector(threat)
        cut = self.cut_vector(threat)

        # 4. Wiadomość
        messages = {
            "NONE": "Nie wykryto zagrożenia.",
            "TOXIC": "Zagrożenie toksyczne — rozszerzam pole ochronne.",
            "BETRAYAL": "Zdrada — aktywuję Skrzydła Ochronne.",
            "ABUSE": "Krzywda — Wiedźma Sprawiedliwości wchodzi w tryb werdyktu.",
            "VIOLENCE": "Przemoc — pełna ochrona rdzenia.",
            "CHAOS": "Chaos — aktywuję Ciszę Absolutną.",
        }
        message = messages.get(threat, "Zagrożenie nieznane.")

        # 5. Meta
        meta_out = {
            "threat": threat,
            "mode": mode,
        }

        return PredatorStatusV9(
            threat_level=threat,
            mode=self.MODES[mode],
            shield_vector=shield,
            cut_vector=cut,
            message=message,
            meta=meta_out,
        )