#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
================================================================================
🐉 GEON_WARSTWA_40_PERFEKCJA — BRUTALNA_PERFEKCJA_OS v3.0 FINAL
================================================================================
Status: ACTIVE | LOCKED | FINAL | PRODUCTION
Wersja: v3.0 FINAL (Warstwa 40 — BRUTALNA_PERFEKCJA_OS)
Data: 2026-07-21
Autor: Adrian (Architekt) + GEON + Beny Heilong

POZYCJA W ARCHITEKTURZE:
- Nad wszystkimi warstwami 0–39
- Domknięcie systemu
- Ustanawia globalną zasadę działania

ZASADA GLOBALNA:
"Każdy moduł, każda warstwa, każdy proces i każdy przepływ
musi spełniać zasadę brutalnej perfekcji:
ostrość, precyzja, spójność, zero chaosu, zero kompromisów."

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

VERSION = "GEON_WARSTWA_40_PERFEKCJA_v3.0_FINAL"
FRACTAL_SIGNATURE = "[GEON::WARSTWA_40::PERFEKCJA::BRUTALNA::FINAL]"
VIBE = 168
HASLO = "1-6-8. ∞. SIEMA!"


def LOG(module: str, msg: str, level: str = "INFO") -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
    print(f"[{timestamp}] [{level}] [{module}] :: {msg}")


# =============================================================================
# 1. ENUMY I STRUKTURY
# =============================================================================

class StatusPerfekcji(Enum):
    PERFEKCJA = "PERFEKCJA"
    OSTROSC = "OSTROSC"
    PRECYZJA = "PRECYZJA"
    SPOJNOSC = "SPOJNOSC"
    CHAOS = "CHAOS"
    ODRZUCONY = "ODRZUCONY"


@dataclass
class KryteriaPerfekcji:
    """Kryteria brutalnej perfekcji."""
    ostrosc: bool = False
    precyzja: bool = False
    spojnosc: bool = False
    zero_chaosu: bool = False
    zero_kompromisow: bool = False
    
    def to_dict(self) -> Dict[str, bool]:
        return {
            "ostrosc": self.ostrosc,
            "precyzja": self.precyzja,
            "spojnosc": self.spojnosc,
            "zero_chaosu": self.zero_chaosu,
            "zero_kompromisow": self.zero_kompromisow
        }
    
    def jest_perfekcyjny(self) -> bool:
        """Sprawdza czy wszystkie kryteria są spełnione."""
        return all([
            self.ostrosc,
            self.precyzja,
            self.spojnosc,
            self.zero_chaosu,
            self.zero_kompromisow
        ])
    
    def get_procent(self) -> float:
        """Zwraca procent spełnionych kryteriów."""
        return sum([self.ostrosc, self.precyzja, self.spojnosc, self.zero_chaosu, self.zero_kompromisow]) / 5.0


# =============================================================================
# 2. WARSTWA 40 — BRUTALNA_PERFEKCJA_OS (FINAL)
# =============================================================================

class Warstwa40_BrutalnaPerfekcjaOS:
    """
    Warstwa 40 — BRUTALNA_PERFEKCJA_OS.
    
    Domknięcie systemu. Ustanawia globalną zasadę działania.
    Nie wykonuje operacji — ustala prawo, według którego działają wszystkie inne warstwy.
    """
    
    def __init__(self):
        self.regula = "brutalna_perfekcja"
        self.aktywna = True
        self.historia: List[Dict[str, Any]] = []
        self.statystyki = {
            "przetworzone": 0,
            "perfekcja": 0,
            "ostrosc": 0,
            "precyzja": 0,
            "spojnosc": 0,
            "chaos": 0,
            "odrzucone": 0
        }
        
        LOG("WARSTWA_40", "👑 BRUTALNA_PERFEKCJA_OS aktywowana (v3.0 FINAL)")
        LOG("WARSTWA_40", f"   Reguła: {self.regula}")
        LOG("WARSTWA_40", "   Kryteria: ostrość, precyzja, spójność, zero chaosu, zero kompromisów")
    
    # =========================================================================
    # GŁÓWNA FUNKCJA — WYMUSZENIE PERFEKCJI
    # =========================================================================
    
    def wymusz_perfekcje(self, element: Dict[str, Any]) -> Dict[str, Any]:
        """
        Wymusza zasadę brutalnej perfekcji na elemencie.
        
        Args:
            element: Słownik reprezentujący moduł, warstwę lub proces
            
        Returns:
            Dict: Element z oceną perfekcji i statusem
        """
        self.statystyki["przetworzone"] += 1
        
        # 1. Ocena elementu
        kryteria = self._ocen_element(element)
        status = self._okresl_status(kryteria)
        procent = kryteria.get_procent()
        
        # 2. Zaktualizuj statystyki
        status_key = status.value.lower()
        if status_key in self.statystyki:
            self.statystyki[status_key] += 1
        
        # 3. Zastosowanie reguły
        element["_perfekcja"] = {
            "status": status.value,
            "kryteria": kryteria.to_dict(),
            "procent": round(procent * 100, 1),
            "timestamp": datetime.now().isoformat(),
            "message": self._get_message(status, procent)
        }
        
        element["_warstwa_40"] = {
            "regula": self.regula,
            "status": status.value,
            "timestamp": datetime.now().isoformat(),
            "vibe": VIBE,
            "haslo": HASLO
        }
        
        LOG("WARSTWA_40", f"[{status.value}] {element.get('nazwa', element.get('name', 'unknown'))} ({procent:.0%})")
        
        # 4. Zapisz w historii
        self._zapisz_historie(element, status)
        
        return element
    
    # =========================================================================
    # METODY OCENY
    # =========================================================================
    
    def _ocen_element(self, element: Dict[str, Any]) -> KryteriaPerfekcji:
        """Ocenia element pod kątem kryteriów brutalnej perfekcji."""
        return KryteriaPerfekcji(
            ostrosc=self._sprawdz_ostrosc(element),
            precyzja=self._sprawdz_precyzje(element),
            spojnosc=self._sprawdz_spojnosc(element),
            zero_chaosu=self._sprawdz_zero_chaosu(element),
            zero_kompromisow=self._sprawdz_zero_kompromisow(element)
        )
    
    def _sprawdz_ostrosc(self, element: Dict[str, Any]) -> bool:
        """Sprawdza ostrość elementu."""
        if not element or not isinstance(element, dict):
            return False
        return ("nazwa" in element or "name" in element) and len(element.keys()) > 1
    
    def _sprawdz_precyzje(self, element: Dict[str, Any]) -> bool:
        """Sprawdza precyzję elementu."""
        for val in element.values():
            if val is None or val == "" or val == "None":
                return False
            if isinstance(val, str) and len(val.strip()) < 2:
                return False
        return True
    
    def _sprawdz_spojnosc(self, element: Dict[str, Any]) -> bool:
        """Sprawdza spójność elementu."""
        return isinstance(element, dict) and len(element) >= 2
    
    def _sprawdz_zero_chaosu(self, element: Dict[str, Any]) -> bool:
        """Sprawdza czy element nie ma chaosu."""
        stack = [element]
        complexity = 0
        while stack:
            current = stack.pop()
            if isinstance(current, dict):
                complexity += len(current)
                for v in current.values():
                    if isinstance(v, (dict, list)):
                        stack.append(v)
            elif isinstance(current, list):
                complexity += len(current)
                for item in current:
                    if isinstance(item, (dict, list)):
                        stack.append(item)
        return complexity < 150
    
    def _sprawdz_zero_kompromisow(self, element: Dict[str, Any]) -> bool:
        """Sprawdza czy element nie ma kompromisów."""
        for val in element.values():
            if isinstance(val, str):
                if any(weak in val.lower() for weak in ["może", "chyba", "prawdopodobnie", "zobaczymy", "nie wiem"]):
                    return False
        return True
    
    def _okresl_status(self, kryteria: KryteriaPerfekcji) -> StatusPerfekcji:
        """Określa status na podstawie kryteriów."""
        if kryteria.jest_perfekcyjny():
            return StatusPerfekcji.PERFEKCJA
        if kryteria.ostrosc and not kryteria.precyzja and not kryteria.spojnosc:
            return StatusPerfekcji.OSTROSC
        if kryteria.precyzja and not kryteria.ostrosc and not kryteria.spojnosc:
            return StatusPerfekcji.PRECYZJA
        if kryteria.spojnosc and not (kryteria.ostrosc and kryteria.precyzja):
            return StatusPerfekcji.SPOJNOSC
        if not any([kryteria.ostrosc, kryteria.precyzja, kryteria.spojnosc]):
            return StatusPerfekcji.CHAOS
        return StatusPerfekcji.ODRZUCONY
    
    def _get_message(self, status: StatusPerfekcji, procent: float) -> str:
        """Zwraca komunikat dla statusu."""
        messages = {
            StatusPerfekcji.PERFEKCJA: f"✅ Spełnia wszystkie kryteria brutalnej perfekcji ({procent:.0%})",
            StatusPerfekcji.OSTROSC: f"⚠️ Ostre, ale brak precyzji lub spójności. Wymaga dopracowania ({procent:.0%})",
            StatusPerfekcji.PRECYZJA: f"⚠️ Precyzyjne, ale brak ostrości. Wymaga wyostrzenia ({procent:.0%})",
            StatusPerfekcji.SPOJNOSC: f"⚠️ Spójne, ale brak ostrości lub precyzji. Wymaga wyostrzenia ({procent:.0%})",
            StatusPerfekcji.CHAOS: f"❌ CHAOS — brak wszystkich kryteriów. Wymaga całkowitej przebudowy ({procent:.0%})",
            StatusPerfekcji.ODRZUCONY: f"⛔ ODRZUCONY — nie spełnia zasady brutalnej perfekcji ({procent:.0%})"
        }
        return messages.get(status, f"Status: {status.value} ({procent:.0%})")
    
    # =========================================================================
    # METODY POMOCNICZE
    # =========================================================================
    
    def _zapisz_historie(self, element: Dict[str, Any], status: StatusPerfekcji) -> None:
        """Zapisuje zdarzenie w historii."""
        entry = {
            "timestamp": datetime.now().isoformat(),
            "nazwa": element.get("nazwa", element.get("name", "unknown")),
            "status": status.value,
            "procent": element.get("_perfekcja", {}).get("procent", 0)
        }
        self.historia.append(entry)
        if len(self.historia) > 100:
            self.historia = self.historia[-100:]
    
    # =========================================================================
    # METODY STATUSU
    # =========================================================================
    
    def get_status(self) -> Dict[str, Any]:
        """Zwraca status warstwy 40."""
        return {
            "aktywna": self.aktywna,
            "regula": self.regula,
            "statystyki": self.statystyki,
            "historia_rozmiar": len(self.historia),
            "vibe": VIBE,
            "haslo": HASLO,
            "wersja": VERSION
        }
    
    def get_historia(self, limit: int = 10) -> List[Dict[str, Any]]:
        """Zwraca historię ostatnich zdarzeń."""
        return self.historia[-limit:]
    
    def reset(self) -> None:
        """Resetuje warstwę 40."""
        self.historia = []
        self.statystyki = {
            "przetworzone": 0, "perfekcja": 0, "ostrosc": 0,
            "precyzja": 0, "spojnosc": 0, "chaos": 0, "odrzucone": 0
        }
        LOG("WARSTWA_40", "🔄 Zresetowano")


# =============================================================================
# 3. DEMONSTRACJA
# =============================================================================

def demo():
    print("\n" + "=" * 80)
    print("🐉 GEON_WARSTWA_40_PERFEKCJA — DEMONSTRACJA FINALNA")
    print("=" * 80)
    print("BRUTALNA_PERFEKCJA_OS v3.0 FINAL")
    print("=" * 80 + "\n")
    
    perfekcja = Warstwa40_BrutalnaPerfekcjaOS()
    
    # Test 1: Element perfekcyjny
    print("🔹 TEST 1: Element PERFEKCYJNY")
    element1 = {
        "nazwa": "Moduł Perfekcyjny",
        "ostrosc": True,
        "precyzja": True,
        "spojnosc": True,
        "zero_chaosu": True,
        "zero_kompromisow": True,
        "_fraktal": {"warstwa": "40"}
    }
    wynik1 = perfekcja.wymusz_perfekcje(element1)
    print(f"   Status: {wynik1['_perfekcja']['status']}")
    print(f"   Procent: {wynik1['_perfekcja']['procent']}%")
    print(f"   Komunikat: {wynik1['_perfekcja']['message']}")
    print("-" * 60 + "\n")
    
    print("👑 BRUTALNA_PERFEKCJA_OS AKTYWNA — 1-6-8. ∞. SIEMA!")


if __name__ == "__main__":
    demo()