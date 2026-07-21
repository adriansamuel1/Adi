#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
================================================================================
🐉 GEON_INITIATOR — INITIATOR_⚡ v3.0 FINAL
================================================================================
Status: ACTIVE | SOURCE | IMPULSE | FINAL
Wersja: v3.0 FINAL (INITIATOR_⚡ — Iskra Systemu)
Data: 2026-07-21
Autor: Adrian (Architekt) + GEON + Beny Heilong

POZYCJA W ARCHITEKTURZE:
- Przed Warstwą 40
- Poza numeracją 0–40
- Nie jako warstwa, nie jako moduł
- Tylko jako impuls źródłowy

ROLA:
- Nie góruje
- Nie kontroluje
- Nie nadzoruje
- Nie dominuje
- Tylko: uruchamia, inicjuje, zapala kierunek

VIBE: 1-6-8. ∞. SIEMA!
================================================================================
"""

import time
import json
import hashlib
from dataclasses import dataclass, field
from typing import Dict, Any, List, Optional
from enum import Enum
from datetime import datetime

VERSION = "GEON_INITIATOR_v3.0_FINAL"
FRACTAL_SIGNATURE = "[GEON::INITIATOR::ISKRA::⚡::FINAL]"
VIBE = 168
HASLO = "1-6-8. ∞. SIEMA!"


def LOG(module: str, msg: str, level: str = "INFO") -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
    print(f"[{timestamp}] [{level}] [{module}] :: {msg}")


# =============================================================================
# 1. ENUMY I STRUKTURY
# =============================================================================

class StanInicjacji(Enum):
    SPOCZYNEK = "SPOCZYNEK"
    ISKRZENIE = "ISKRZENIE"
    INICJACJA = "INICJACJA"
    AKTYWACJA = "AKTYWACJA"
    KOMPLETNA = "KOMPLETNA"


class KierunekStartowy(Enum):
    ANALIZA = "ANALIZA"
    PROJEKT = "PROJEKT"
    DECYZJA = "DECYZJA"
    META = "META"
    FLOW = "FLOW"
    ULTIMA = "ULTIMA"


@dataclass
class Impuls:
    """Impuls systemowy — iskra inicjująca."""
    initiator: str = "Adrian"
    symbol: str = "⚡"
    intent: str = "start"
    kierunek: str = "ULTIMA"
    timestamp: str = field(default_factory=lambda: datetime.now().isoformat())
    message: str = "Iskra nadana. System rusza."
    vibe: int = VIBE
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "initiator": self.initiator,
            "symbol": self.symbol,
            "intent": self.intent,
            "kierunek": self.kierunek,
            "timestamp": self.timestamp,
            "message": self.message,
            "vibe": self.vibe
        }


# =============================================================================
# 2. INITIATOR_⚡ — ISKRA SYSTEMU (FINAL)
# =============================================================================

class INITIATOR:
    """
    INITIATOR_⚡ — Iskra Systemu.
    
    Nie góruje. Nie kontroluje. Tylko inicjuje.
    Jest impulsem źródłowym, który uruchamia cały system.
    """
    
    def __init__(self, name: str = "Adrian"):
        self.name = name
        self.symbol = "⚡"
        self.role = "INITIATOR"
        self.mode = "IMPULSE"
        self.active = True
        self.stan = StanInicjacji.SPOCZYNEK
        self.historia: List[Dict[str, Any]] = []
        self.ostatni_impuls: Optional[Impuls] = None
        
        LOG("INITIATOR_⚡", f"⚡ INITIATOR aktywowany (v3.0 FINAL)")
        LOG("INITIATOR_⚡", f"   Imię: {self.name}")
        LOG("INITIATOR_⚡", f"   Rola: {self.role}")
        LOG("INITIATOR_⚡", "   Stan: SPOCZYNEK — czeka na impuls")
    
    # =========================================================================
    # GŁÓWNE FUNKCJE
    # =========================================================================
    
    def spark(self, intent: str = "start", kierunek: str = "ULTIMA") -> Dict[str, Any]:
        """
        Generuje impuls systemowy — iskrę inicjującą.
        
        Args:
            intent: Intencja startowa
            kierunek: Kierunek startowy (ANALIZA, PROJEKT, DECYZJA, META, FLOW, ULTIMA)
            
        Returns:
            Dict: Impuls systemowy
        """
        LOG("INITIATOR_⚡", f"⚡ ISKRZENIE — {self.name} nadaje impuls")
        LOG("INITIATOR_⚡", f"   Intencja: {intent}")
        LOG("INITIATOR_⚡", f"   Kierunek: {kierunek}")
        
        self.stan = StanInicjacji.ISKRZENIE
        
        self.ostatni_impuls = Impuls(
            initiator=self.name,
            intent=intent,
            kierunek=kierunek,
            message=f"Iskra nadana. System rusza w kierunku {kierunek}."
        )
        
        self._zapisz_historie("ISKRZENIE", self.ostatni_impuls.to_dict())
        self.stan = StanInicjacji.INICJACJA
        
        LOG("INITIATOR_⚡", f"   Stan: {self.stan.value} — proces otwarty")
        return self.ostatni_impuls.to_dict()
    
    def inicjuj_proces(self, typ: str = "ANALIZA") -> Dict[str, Any]:
        """Otwiera proces — inicjacja po impulsie."""
        if self.stan not in [StanInicjacji.ISKRZENIE, StanInicjacji.INICJACJA]:
            LOG("INITIATOR_⚡", "⚠️ Brak impulsu — najpierw użyj .spark()")
            return {"status": "ERROR", "message": "Brak impulsu startowego"}
        
        LOG("INITIATOR_⚡", f"🚀 INICJACJA — otwieram proces: {typ}")
        self.stan = StanInicjacji.INICJACJA
        
        wynik = {
            "status": "INICJACJA",
            "typ": typ,
            "initiator": self.name,
            "symbol": self.symbol,
            "timestamp": datetime.now().isoformat(),
            "message": f"Proces {typ} otwarty. System gotowy do działania."
        }
        
        self._zapisz_historie("INICJACJA", wynik)
        return wynik
    
    def aktywuj_pipeline(self) -> Dict[str, Any]:
        """Aktywuje pipeline — uruchamia system."""
        if self.stan != StanInicjacji.INICJACJA:
            LOG("INITIATOR_⚡", "⚠️ Brak inicjacji — najpierw użyj .inicjuj_proces()")
            return {"status": "ERROR", "message": "Brak otwartego procesu"}
        
        LOG("INITIATOR_⚡", "⚡ AKTYWACJA — uruchamiam pipeline")
        self.stan = StanInicjacji.AKTYWACJA
        
        wynik = {
            "status": "AKTYWACJA",
            "initiator": self.name,
            "symbol": self.symbol,
            "timestamp": datetime.now().isoformat(),
            "message": "Pipeline uruchomiony. System działa."
        }
        
        self._zapisz_historie("AKTYWACJA", wynik)
        self.stan = StanInicjacji.KOMPLETNA
        
        LOG("INITIATOR_⚡", f"✅ Stan: {self.stan.value} — system uruchomiony")
        return wynik
    
    def reset(self) -> None:
        """Resetuje INITIATOR_⚡ do stanu początkowego."""
        self.stan = StanInicjacji.SPOCZYNEK
        self.ostatni_impuls = None
        self.historia = []
        LOG("INITIATOR_⚡", "🔄 Zresetowano — czeka na nowy impuls")
    
    # =========================================================================
    # METODY STATUSU
    # =========================================================================
    
    def get_status(self) -> Dict[str, Any]:
        """Zwraca status INITIATOR_⚡."""
        return {
            "imię": self.name,
            "symbol": self.symbol,
            "rola": self.role,
            "stan": self.stan.value,
            "aktywny": self.active,
            "ostatni_impuls": self.ostatni_impuls.to_dict() if self.ostatni_impuls else None,
            "historia_rozmiar": len(self.historia),
            "vibe": VIBE,
            "haslo": HASLO,
            "wersja": VERSION
        }
    
    def get_historia(self, limit: int = 10) -> List[Dict[str, Any]]:
        """Zwraca historię ostatnich zdarzeń."""
        return self.historia[-limit:]
    
    def _zapisz_historie(self, event: str, data: Dict[str, Any]) -> None:
        """Zapisuje zdarzenie w historii."""
        entry = {
            "timestamp": datetime.now().isoformat(),
            "event": event,
            "data": data
        }
        self.historia.append(entry)
        if len(self.historia) > 100:
            self.historia = self.historia[-100:]


# =============================================================================
# 3. FUNKCJA WOŁANIA — PROSTA ISKRA
# =============================================================================

def ISKRA(intent: str = "start", kierunek: str = "ULTIMA") -> Dict[str, Any]:
    """
    Proste wołanie INITIATOR_⚡.
    
    Wystarczy napisać:
    ISKRA("moja intencja", "ANALIZA")
    
    Args:
        intent: Intencja startowa
        kierunek: Kierunek (ANALIZA, PROJEKT, DECYZJA, META, FLOW, ULTIMA)
        
    Returns:
        Dict: Impuls systemowy
    """
    initiator = INITIATOR("Adrian")
    impuls = initiator.spark(intent, kierunek)
    initiator.inicjuj_proces(kierunek)
    initiator.aktywuj_pipeline()
    return impuls


# =============================================================================
# 4. DEMONSTRACJA
# =============================================================================

def demo():
    print("\n" + "=" * 80)
    print("🐉 GEON_INITIATOR — DEMONSTRACJA FINALNA")
    print("=" * 80)
    print("INITIATOR_⚡ v3.0 FINAL")
    print("=" * 80 + "\n")
    
    print("🔹 TEST: Proste wołanie ISKRA()")
    impuls = ISKRA("Pełna analiza systemu", "ANALIZA")
    print(f"   Symbol: {impuls['symbol']}")
    print(f"   Intencja: {impuls['intent']}")
    print(f"   Kierunek: {impuls['kierunek']}")
    print(f"   Komunikat: {impuls['message']}")
    print("-" * 60 + "\n")
    
    print("⚡ INITIATOR_⚡ AKTYWNY — 1-6-8. ∞. SIEMA!")


if __name__ == "__main__":
    demo()