#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🌀 AFC_INFINITY_CORE v9.0 — Fraktalny Układ Nerwowy GEON
========================================================
Warstwa: kombajn/afc_infinity_core.py
Rola: Generowanie pełnego fraktalnego atraktora D∞ na podstawie D1–D4.
Wersja: v9.0-INFINITY
Sygnatura: [GEON_SYSTEM::AFC::INFINITY::v9.0]
========================================================
"""

import math
from dataclasses import dataclass, field
from typing import List, Dict, Any


def LOG(module: str, event: str, msg: str) -> None:
    print(f"[AFC∞][{module}][{event}] -> {msg}")


# ============================================================
# STRUKTURA WYJŚCIOWA AFC-∞
# ============================================================

@dataclass
class AFCInfinityVector:
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
    core_9d: float
    stability_9d: float
    energy_map: Dict[str, float]
    entropy_map: Dict[str, float]
    meta_state: Dict[str, Any]


# ============================================================
# AFC-∞ — GŁÓWNY ORGAN
# ============================================================

class AFCInfinityCore:
    """
    AFC-∞ — pełny fraktalny układ nerwowy GEON.
    - D1–D4: warstwy bazowe
    - D5–D8: warstwy fraktalne
    - D9: atraktor równowagi
    - D∞: atraktor żywy (ciągły)
    - Energia, entropia, stabilność, meta-stan
    """

    def __init__(self):
        self.history_core: List[float] = []
        self.history_entropy: List[float] = []
        self.history_energy: List[float] = []
        LOG("AFC∞", "INIT", "Fraktalny układ nerwowy aktywowany")

    # --------------------------------------------------------
    # FUNKCJA ŚREDNIA
    # --------------------------------------------------------
    @staticmethod
    def avg(values: List[float]) -> float:
        return sum(values) / len(values) if values else 0.0

    # --------------------------------------------------------
    # FUNKCJA ENTROPIA
    # --------------------------------------------------------
    @staticmethod
    def entropy(values: List[float]) -> float:
        if not values:
            return 0.0
        mean = sum(values) / len(values)
        var = sum((v - mean) ** 2 for v in values) / len(values)
        return var

    # --------------------------------------------------------
    # FUNKCJA ENERGIA
    # --------------------------------------------------------
    @staticmethod
    def energy(values: List[float]) -> float:
        return sum(values)

    # --------------------------------------------------------
    # GŁÓWNA FUNKCJA AFC-∞
    # --------------------------------------------------------
    def build_layers(self, D1: List[float], D2: List[float],
                     D3: List[float], D4: List[float]) -> AFCInfinityVector:

        # --- KROK 1: D5 — integracja ---
        D5 = [(D1[i] + D2[i] + D3[i] + D4[i]) / 4.0 for i in range(9)]

        # --- KROK 2: D6 — stabilizacja ---
        D6 = [(D1[i] + D3[i] + D5[i]) / 3.0 for i in range(9)]

        # --- KROK 3: D7 — adaptacja ---
        D7 = [(D2[i] + D4[i] + D6[i]) / 3.0 for i in range(9)]

        # --- KROK 4: D8 — fraktalna harmonia ---
        D8 = [(D1[i] + D3[i] + D5[i] + D7[i]) / 4.0 for i in range(9)]

        # --- KROK 5: D9 — atraktor równowagi ---
        D9 = [(D1[i] + D8[i]) / 2.0 for i in range(9)]

        # --- KROK 6: D∞ — atraktor żywy ---
        core_9d = self.avg(D9)
        D_inf = [(D9[i] + core_9d) / 2.0 for i in range(9)]

        # --- Energia ---
        energy_map = {
            "E1": self.energy(D1),
            "E2": self.energy(D2),
            "E3": self.energy(D3),
            "E4": self.energy(D4),
            "E5": self.energy(D5),
            "E6": self.energy(D6),
            "E7": self.energy(D7),
            "E8": self.energy(D8),
            "E9": self.energy(D9),
            "E∞": self.energy(D_inf),
        }

        # --- Entropia ---
        entropy_map = {
            "H1": self.entropy(D1),
            "H2": self.entropy(D2),
            "H3": self.entropy(D3),
            "H4": self.entropy(D4),
            "H5": self.entropy(D5),
            "H6": self.entropy(D6),
            "H7": self.entropy(D7),
            "H8": self.entropy(D8),
            "H9": self.entropy(D9),
            "H∞": self.entropy(D_inf),
        }

        # --- Stabilność ---
        stability_9d = max(0.0, min(1.0, 1.0 - entropy_map["H9"] * 10.0))

        # --- Meta-stan ---
        meta_state = {
            "core": core_9d,
            "stability": stability_9d,
            "entropy": entropy_map["H∞"],
            "energy": energy_map["E∞"],
            "trend_core": self._trend(self.history_core, core_9d),
            "trend_entropy": self._trend(self.history_entropy, entropy_map["H∞"]),
            "trend_energy": self._trend(self.history_energy, energy_map["E∞"]),
        }

        # --- Aktualizacja historii ---
        self._update_history(core_9d, entropy_map["H∞"], energy_map["E∞"])

        return AFCInfinityVector(
            d1=D1, d2=D2, d3=D3, d4=D4,
            d5=D5, d6=D6, d7=D7, d8=D8, d9=D9,
            d_inf=D_inf,
            core_9d=core_9d,
            stability_9d=stability_9d,
            energy_map=energy_map,
            entropy_map=entropy_map,
            meta_state=meta_state,
        )

    # --------------------------------------------------------
    # TRENDY / HISTORIA
    # --------------------------------------------------------
    def _trend(self, history: List[float], value: float) -> float:
        if not history:
            return 0.0
        return value - history[-1]

    def _update_history(self, core: float, entropy: float, energy: float):
        self.history_core.append(core)
        self.history_entropy.append(entropy)
        self.history_energy.append(energy)

        if len(self.history_core) > 200:
            self.history_core.pop(0)
        if len(self.history_entropy) > 200:
            self.history_entropy.pop(0)
        if len(self.history_energy) > 200:
            self.history_energy.pop(0)