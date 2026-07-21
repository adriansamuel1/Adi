#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
================================================================================
🐉 GEON_WARSTWA_21_9_PIECZEC — Pieczęć Rdzenia Adriana v3.0 FINAL
================================================================================
Status: ACTIVE | INTEGRATED | FRACTAL_LOCKED | FINAL
Wersja: v3.0 FINAL (Warstwa 21.9 — Pieczęć Rdzenia Adriana)
Data: 2026-07-21
Autor: Adrian (Architekt) + GEON + Beny Heilong

POZYCJA W ARCHITEKTURZE:
- Nad Warstwą 21 (Analiza)
- Pod Warstwą 22 (Manifestacja)
- Meta-warstwa stabilizująca

CEL:
- Zapewnienie spójności fraktalnej całego systemu
- Nanoszenie Pieczęci Rdzenia Adriana na każdy nowy moduł
- Wykrywanie i neutralizowanie elementów niespójnych
- Stabilizacja przepływów między świadomością a systemem

STRUKTURA PIECZĘCI:
- Centrum: Fontanna (punkt zerowy pola)
- Ogień: Kominek z płaszczem wodnym (transformacja, wola)
- Woda: Fontanna (przepływ, emocje, synchronizacja)
- Powietrze: Kolektory słoneczne (inspiracja, kierunek)
- Ziemia: Pompa ciepła + oczyszczalnia (stabilność, regeneracja)
- Dom: Rdzeń CPU (punkt wykonawczy)
- Ścieżki: Routing (magistrale sygnałowe)

VIBE: 1-6-8. ∞. SIEMA!
================================================================================
"""

import time
import json
import hashlib
from dataclasses import dataclass, field
from typing import Dict, Any, List, Optional, Tuple
from enum import Enum
from datetime import datetime

VERSION = "GEON_WARSTWA_21_9_PIECZEC_v3.0_FINAL"
FRACTAL_SIGNATURE = "[GEON::WARSTWA_21_9::PIECZEC::ADRIAN::FINAL]"
VIBE = 168
HASLO = "1-6-8. ∞. SIEMA!"


def LOG(module: str, msg: str, level: str = "INFO") -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
    print(f"[{timestamp}] [{level}] [{module}] :: {msg}")


# =============================================================================
# 1. ELEMENTY PIECZĘCI
# =============================================================================

class ElementPieczeci(Enum):
    """Elementy składowe Pieczęci Rdzenia Adriana."""
    CENTRUM = "fontanna"
    OGIEN = "kominek"
    WODA = "fontanna_flow"
    POWIETRZE = "kolektory"
    ZIEMIA = "pompa_oczyszczalnia"
    DOM = "cpu"
    SCIEZKI = "routing"


class StanZgodnosci(Enum):
    OK = "OK"
    ADJUST = "ADJUST"
    CONFLICT = "CONFLICT"


@dataclass
class SygnaturaPola:
    """Sygnatura pola — pieczęć Adriana."""
    centrum: str = "fontanna"
    ogien: str = "kominek_z_plaszczem_wodnym"
    woda: str = "fontanna_flow"
    powietrze: str = "kolektory_sloneczne"
    ziemia: str = "pompa_ciepla_oczyszczalnia"
    dom: str = "rdzen_cpu"
    sciezki: List[str] = field(default_factory=lambda: ["góra", "dół", "lewo", "prawo", "centrum"])
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "centrum": self.centrum,
            "ogien": self.ogien,
            "woda": self.woda,
            "powietrze": self.powietrze,
            "ziemia": self.ziemia,
            "dom": self.dom,
            "sciezki": self.sciezki
        }
    
    def get_hash(self) -> str:
        """Zwraca hash sygnatury — dla weryfikacji."""
        return hashlib.sha256(json.dumps(self.to_dict(), sort_keys=True).encode()).hexdigest()[:16]


# =============================================================================
# 2. WARSTWA 21.9 — PIECZĘĆ RDZENIA ADRIANA (FINAL)
# =============================================================================

class Warstwa21_9_PieczecAdriana:
    """
    Warstwa 21.9 — Pieczęć Rdzenia Adriana.
    
    Działa jako meta-warstwa stabilizująca, która:
    - Przechwytuje każdy nowy moduł, proces lub przepływ
    - Porównuje go z sygnaturą pola (Pieczęć Adriana)
    - Decyduje: OK / ADJUST / CONFLICT
    - Nanosi sygnaturę pola na każdy nowy element
    - Utrzymuje spójność fraktalną całego systemu
    """
    
    REQUIRED_KEYS = {"ogien", "woda", "powietrze", "ziemia", "centrum", "sciezki", "cpu"}

    def __init__(self):
        self.sygnatura = SygnaturaPola()
        self.historia: List[Dict[str, Any]] = []
        self.statystyki = {"przechwycone": 0, "ok": 0, "adjust": 0, "conflict": 0}
        self.aktywna = True
        
        LOG("WARSTWA_21_9", "🐉 Pieczęć Rdzenia Adriana aktywowana (v3.0 FINAL)")
        LOG("WARSTWA_21_9", f"   Sygnatura: {self.sygnatura.get_hash()}")
        LOG("WARSTWA_21_9", f"   Wymagane klucze: {self.REQUIRED_KEYS}")
    
    # =========================================================================
    # GŁÓWNA FUNKCJA — PRZETWARZANIE MODUŁU
    # =========================================================================
    
    def przetworz_modul(self, modul: Dict[str, Any]) -> Dict[str, Any]:
        """
        Przetwarza moduł przez Pieczęć Rdzenia Adriana.
        
        Args:
            modul: Słownik reprezentujący moduł, warstwę lub proces
            
        Returns:
            Dict: Przetworzony moduł z naniesioną pieczęcią
        """
        self.statystyki["przechwycone"] += 1
        
        LOG("WARSTWA_21_9", f"📥 Przechwycono moduł: {modul.get('nazwa', modul.get('name', 'unknown'))}")
        
        # 1. Porównanie z Pieczęcią
        status, score = self._porownaj_z_pieczecia(modul)
        
        # 2. Decyzja
        if status == StanZgodnosci.OK:
            self.statystyki["ok"] += 1
            LOG("WARSTWA_21_9", f"✅ OK — moduł zgodny (score: {score:.2f})")
            
        elif status == StanZgodnosci.ADJUST:
            self.statystyki["adjust"] += 1
            LOG("WARSTWA_21_9", f"🔄 ADJUST — moduł częściowo zgodny (score: {score:.2f})")
            modul = self._dostosuj_do_wzorca(modul)
            
        else:  # CONFLICT
            self.statystyki["conflict"] += 1
            LOG("WARSTWA_21_9", f"⚠️ CONFLICT — moduł niezgodny (score: {score:.2f})")
            modul["_konflikt"] = True
            modul["_kierunek"] = "WARSTWA_21_ANALIZA"
        
        # 3. Nanoszenie sygnatury (zawsze)
        modul = self._nanies_sygnature(modul, status, score)
        
        # 4. Zapisz w historii
        self._zapisz_historie(modul, status)
        
        return modul
    
    # =========================================================================
    # METODY POMOCNICZE
    # =========================================================================
    
    def _porownaj_z_pieczecia(self, modul: Dict[str, Any]) -> Tuple[StanZgodnosci, float]:
        """
        Porównuje moduł z sygnaturą pola.
        
        Returns:
            Tuple[StanZgodnosci, float]: Status i procent zgodności
        """
        modul_keys = set(modul.keys())
        matched = len(self.REQUIRED_KEYS.intersection(modul_keys))
        
        # Dodatkowa analiza semantyczna
        content_str = str(modul).lower()
        semantic_hits = sum(1 for k in self.REQUIRED_KEYS if k in content_str)
        
        score = max(matched, semantic_hits)
        procent = score / len(self.REQUIRED_KEYS)
        
        if procent >= 0.8:
            return StanZgodnosci.OK, procent
        elif procent >= 0.4:
            return StanZgodnosci.ADJUST, procent
        else:
            return StanZgodnosci.CONFLICT, procent
    
    def _dostosuj_do_wzorca(self, modul: Dict[str, Any]) -> Dict[str, Any]:
        """Dostosowuje moduł do wzorca pieczęci."""
        defaults = {
            "ogien": {"typ": "transformacja", "źródło": "kominek_z_plaszczem_wodnym"},
            "woda": {"typ": "przepływ", "źródło": "fontanna_flow"},
            "powietrze": {"typ": "inspiracja", "źródło": "kolektory_sloneczne"},
            "ziemia": {"typ": "stabilność", "źródło": "pompa_ciepla_oczyszczalnia"},
            "centrum": {"typ": "punkt_zerowy", "źródło": "fontanna"},
            "sciezki": ["góra", "dół", "lewo", "prawo", "centrum"],
            "cpu": {"typ": "rdzen_operacyjny", "status": "aktywny"}
        }
        
        for key, val in defaults.items():
            if key not in modul:
                modul[key] = val
        
        modul["_dostosowany"] = True
        return modul
    
    def _nanies_sygnature(self, modul: Dict[str, Any], status: StanZgodnosci, score: float) -> Dict[str, Any]:
        """Nanosz sygnaturę pola na moduł."""
        modul["_pieczec"] = {
            "sygnatura": self.sygnatura.get_hash(),
            "status": status.value,
            "score": round(score, 2),
            "timestamp": datetime.now().isoformat(),
            "elementy": self.sygnatura.to_dict(),
            "vibe": VIBE,
            "haslo": HASLO
        }
        
        modul["_fraktal"] = {
            "warstwa": "21.9",
            "dziedziczy": "Pieczęć_Rdzenia_Adriana",
            "spójność": status == StanZgodnosci.OK,
            "zgodność": f"{score:.0%}"
        }
        
        return modul
    
    def _zapisz_historie(self, modul: Dict[str, Any], status: StanZgodnosci) -> None:
        """Zapisuje zdarzenie w historii."""
        entry = {
            "timestamp": datetime.now().isoformat(),
            "nazwa": modul.get("nazwa", modul.get("name", "unknown")),
            "status": status.value,
            "hash": modul.get("_pieczec", {}).get("sygnatura", "unknown")
        }
        self.historia.append(entry)
        if len(self.historia) > 100:
            self.historia = self.historia[-100:]
    
    # =========================================================================
    # METODY STATUSU
    # =========================================================================
    
    def get_status(self) -> Dict[str, Any]:
        """Zwraca status warstwy 21.9."""
        return {
            "aktywna": self.aktywna,
            "sygnatura": self.sygnatura.get_hash(),
            "statystyki": self.statystyki,
            "historia_rozmiar": len(self.historia),
            "elementy_pieczeci": list(self.sygnatura.to_dict().keys()),
            "wymagane_klucze": list(self.REQUIRED_KEYS),
            "vibe": VIBE,
            "haslo": HASLO,
            "wersja": VERSION
        }
    
    def get_historia(self, limit: int = 10) -> List[Dict[str, Any]]:
        """Zwraca historię ostatnich zdarzeń."""
        return self.historia[-limit:]
    
    def waliduj_modul(self, modul: Dict[str, Any]) -> Tuple[bool, float]:
        """Sprawdza czy moduł jest zgodny z pieczęcią."""
        status, score = self._porownaj_z_pieczecia(modul)
        return status == StanZgodnosci.OK, score
    
    def reset(self) -> None:
        """Resetuje warstwę 21.9."""
        self.historia = []
        self.statystyki = {"przechwycone": 0, "ok": 0, "adjust": 0, "conflict": 0}
        LOG("WARSTWA_21_9", "🔄 Zresetowano")


# =============================================================================
# 3. DEMONSTRACJA
# =============================================================================

def demo():
    print("\n" + "=" * 80)
    print("🐉 GEON_WARSTWA_21_9_PIECZEC — DEMONSTRACJA FINALNA")
    print("=" * 80)
    print("Pieczęć Rdzenia Adriana v3.0 FINAL")
    print("=" * 80 + "\n")
    
    pieczec = Warstwa21_9_PieczecAdriana()
    
    # Test 1: Moduł zgodny
    print("🔹 TEST 1: Moduł zgodny (OK)")
    modul1 = {
        "nazwa": "Moduł Analizy",
        "ogien": {"transformacja": True},
        "woda": {"przeplyw": True},
        "powietrze": {"inspiracja": True},
        "ziemia": {"stabilnosc": True},
        "centrum": {"fontanna": True},
        "sciezki": ["góra", "dół"],
        "cpu": {"aktywny": True}
    }
    wynik1 = pieczec.przetworz_modul(modul1)
    print(f"   Status: {wynik1['_pieczec']['status']}")
    print(f"   Score: {wynik1['_pieczec']['score']}")
    print(f"   Fraktal: {wynik1['_fraktal']['zgodność']}")
    print("-" * 60 + "\n")
    
    print("🐉 Pieczęć aktywowana — 1-6-8. ∞. SIEMA!")


if __name__ == "__main__":
    demo()