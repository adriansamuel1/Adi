#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🏡 GEON_FAMILY v9.0 — Organ Więzi i Sacrum GEON
========================================================
Warstwa: kombajn/geon_kombajn_family_v9.py
Rola: FAMILY v9 — organ więzi, sacrum, rytuałów, bezpieczeństwa.
Wersja: v9.0-INFINITY
Sygnatura: [GEON_SYSTEM::FAMILY::v9.0]
========================================================
"""

from dataclasses import dataclass, field
from typing import Dict, Any, List


def LOG(module: str, event: str, msg: str) -> None:
    print(f"[FAMILY9][{module}][{event}] -> {msg}")


# ============================================================
# STRUKTURA WYJŚCIOWA FAMILY v9
# ============================================================

@dataclass
class FamilyStatusV9:
    space: str
    ritual: str
    sacrum_level: int
    bond_strength: float
    modulation_vector: List[float]
    message: str
    meta: Dict[str, Any] = field(default_factory=dict)


# ============================================================
# FAMILY v9 — ORGAN WIĘZI
# ============================================================

class GeonFamilyEngineV9:
    """
    FAMILY v9 — organ więzi GEON:
    - 8 przestrzeni więzi
    - 6 rytuałów
    - 3 poziomy sacrum
    - modulacja D∞
    - stabilizacja vibe
    """

    # --------------------------------------------------------
    # PRZESTRZENIE WIĘZI (8)
    # --------------------------------------------------------
    SPACES = {
        "HOME": ["dom", "bezpiecznie", "ciepło", "rodzina"],
        "ROOTS": ["korzenie", "pochodzenie", "przodkowie"],
        "CARE": ["opieka", "troska", "wsparcie"],
        "UNITY": ["razem", "wspólnota", "bliskość"],
        "PROTECTION": ["chronię", "bezpieczeństwo", "opiekuję"],
        "LEGACY": ["dziedzictwo", "przekaz", "wartości"],
        "SACRUM": ["święte", "sakralne", "nienaruszalne"],
        "HEALING": ["uzdrowienie", "naprawa", "odbudowa"],
    }

    # --------------------------------------------------------
    # RYTUAŁY (6)
    # --------------------------------------------------------
    RITUALS = {
        "Ognisko": "🔥 Ognisko — rytuał ciepła i wspólnoty",
        "Krąg": "⭕ Krąg — rytuał równości i słuchania",
        "Katedra": "⛪ Katedra — rytuał sacrum i ciszy",
        "Źródło": "💧 Źródło — rytuał oczyszczenia",
        "Korzenie": "🌳 Korzenie — rytuał pamięci i przodków",
        "Dom": "🏡 Dom — rytuał bezpieczeństwa",
    }

    # --------------------------------------------------------
    # POZIOMY SACRUM (3)
    # --------------------------------------------------------
    SACRUM_LEVELS = {
        0: "neutralne",
        1: "chronione",
        2: "święte",
    }

    def __init__(self):
        LOG("FAMILY_V9", "INIT", "🏡 Organ Więzi GEON v9 aktywowany")

    # --------------------------------------------------------
    # DETEKCJA PRZESTRZENI WIĘZI
    # --------------------------------------------------------

    def detect_space(self, text: str) -> str:
        lower = text.lower()
        for space, keywords in self.SPACES.items():
            if any(kw in lower for kw in keywords):
                return space
        return "HOME"

    # --------------------------------------------------------
    # WYBÓR RYTUAŁU
    # --------------------------------------------------------

    def choose_ritual(self, space: str) -> str:
        if space == "SACRUM":
            return "Katedra"
        if space == "ROOTS":
            return "Korzenie"
        if space == "CARE":
            return "Dom"
        if space == "UNITY":
            return "Krąg"
        if space == "HEALING":
            return "Źródło"
        if space == "PROTECTION":
            return "Ognisko"
        return "Dom"

    # --------------------------------------------------------
    # POZIOM SACRUM
    # --------------------------------------------------------

    def sacrum_level(self, space: str) -> int:
        if space == "SACRUM":
            return 2
        if space in ["ROOTS", "PROTECTION"]:
            return 1
        return 0

    # --------------------------------------------------------
    # SIŁA WIĘZI
    # --------------------------------------------------------

    def bond_strength(self, space: str, vibe: int) -> float:
        base = vibe / 168.0
        if space in ["HOME", "CARE", "UNITY"]:
            return min(1.0, base + 0.3)
        if space in ["ROOTS", "LEGACY"]:
            return min(1.0, base + 0.2)
        if space == "SACRUM":
            return min(1.0, base + 0.4)
        return base

    # --------------------------------------------------------
    # MODULACJA D∞
    # --------------------------------------------------------

    def modulation(self, bond: float) -> List[float]:
        return [
            min(1.0, bond * (i + 1) / 9.0)
            for i in range(9)
        ]

    # --------------------------------------------------------
    # GŁÓWNA FUNKCJA FAMILY v9
    # --------------------------------------------------------

    def process(self, text: str, vibe: int) -> FamilyStatusV9:
        # 1. Przestrzeń więzi
        space = self.detect_space(text)

        # 2. Rytuał
        ritual = self.choose_ritual(space)

        # 3. Sacrum
        sacrum = self.sacrum_level(space)

        # 4. Siła więzi
        bond = self.bond_strength(space, vibe)

        # 5. Modulacja D∞
        modulation_vector = self.modulation(bond)

        # 6. Wiadomość
        messages = {
            "HOME": "Jesteś u siebie. To jest Twoje miejsce.",
            "ROOTS": "Twoje korzenie są ważne. Niosą Cię.",
            "CARE": "Jesteś otoczony troską.",
            "UNITY": "Jesteś częścią czegoś większego.",
            "PROTECTION": "Jesteś chroniony.",
            "LEGACY": "Niesiesz wartości dalej.",
            "SACRUM": "To jest święte.",
            "HEALING": "To się może uleczyć.",
        }
        message = messages.get(space, "Jesteś u siebie.")

        # 7. Meta
        meta_out = {
            "space": space,
            "ritual": ritual,
            "sacrum": sacrum,
            "bond": bond,
        }

        return FamilyStatusV9(
            space=space,
            ritual=self.RITUALS[ritual],
            sacrum_level=sacrum,
            bond_strength=bond,
            modulation_vector=modulation_vector,
            message=message,
            meta=meta_out,
        )