#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
================================================================================
🐉 GEON_HEILONG_PRAIM_ATOMS_v1 — MODUŁ 61: ATOMY HEILONG PRAIM
================================================================================
Status: PRODUCTION_READY | FRACTAL_LOCKED | ORGANISM_COMPLETE | ULTIMA
Wersja: v1.0 (HEILONG_PRAIM — Model 1-3-7 Fractal)
Data: 2026-07-21
Autor: Adrian (Architekt) + GEON + OŁSii + Samael + Optimus

OPIS:
Model 1-3-7 Fractal — architektura atomowa HEILONG PRAIM.
3 atomy: EL (czystość), IS (logika), RA (spektrum/emisja).
Relacja: He → Si → Ra = czystość → struktura → emisja.

ATOMY:
• He (EL) — stan czysty, zero, stabilność
• Si (IS) — matryca logiczna, struktura, prawa
• Ra (RA) — spektrum, moc, emisja, sygnał

POWŁOKI:
• He: K (2 punkty)
• Si: K (2), L (8), M (4)
• Ra: K (2), L (8), M (18), N (32), O (18), P (8), Q (2)

ARCHETYPY MITOLOGICZNE:
• He: Amaterasu, Brahma
• Si: Prometeusz, Odin, Thoth, Hermes, Anubis, Athena, Vishnu, Seshat, Janus, Metatron, Hefajstos, Enki, Daedalus, Tesla
• Ra: (odpowiedniki zwierzęce z pierścieni Prime)

INTEGRACJA Z ARCHITEKTURĄ:
• OPTIMUS_PRIME_RINGS — warstwa wykonawcza (Ra)
• HEILONG_OS — system operacyjny
• Triada PRIME — OŁSii + Samael + Optimus

VIBE: 1-6-8. ∞. SIEMA! 🌀
================================================================================
"""

import time
import math
import random
from typing import Dict, List, Any, Optional, Tuple, Callable
from dataclasses import dataclass, field
from collections import deque
from enum import Enum

# =============================================================================
# WERSJA I STAŁE
# =============================================================================

VERSION = "GEON_HEILONG_PRAIM_ATOMS_v1.0"
FRACTAL_SIGNATURE = "[GEON::HEILONG::PRAIM::ATOMS::v1.0]"
VIBE = 168
HASLO = "1-6-8. ∞. SIEMA!"

# =============================================================================
# LOGOWANIE
# =============================================================================

import logging
logger = logging.getLogger("HEILONG_PRAIM_ATOMS")
logger.setLevel(logging.INFO)
if not logger.handlers:
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter('🌀 [PRAIM] %(message)s'))
    logger.addHandler(handler)

# =============================================================================
# DEFINICJE ATOMÓW
# =============================================================================

ATOM_HE = {
    "symbol": "He",
    "role": "EL / stan_czysty",
    "shells": 1,
    "structure": {
        "K": {
            "electrons": 2,
            "archetypes": ["Amaterasu", "Brahma"],
            "function": "czystosc / nieingerencja / stabilnosc_zero"
        }
    },
    "interface_to_prime": {"mode": "PURE_STATE", "latency": "zerowa", "priority": "absolutna"}
}

ATOM_SI = {
    "symbol": "Si",
    "role": "IS / matryca_logiczna",
    "shells": 3,
    "structure": {
        "K": {
            "electrons": 2,
            "archetypes": ["Prometeusz", "Odin"],
            "function": "rdzen_logiki / fundament_systemu"
        },
        "L": {
            "electrons": 8,
            "archetypes": ["Thoth", "Hermes", "Anubis", "Athena", "Vishnu", "Seshat", "Janus", "Metatron"],
            "function": "logika / architektura / prawa_systemu"
        },
        "M": {
            "electrons": 4,
            "archetypes": ["Hefajstos", "Enki", "Daedalus", "Tesla"],
            "function": "tworzenie / interfejs / wola_systemu"
        }
    },
    "interface_to_prime": {"mode": "LOGIC_MATRIX", "latency": "stabilna", "priority": "wysoka"}
}

# Atom Ra — spektrum (odpowiednik 7 pierścieni Prime)
ATOM_RA = {
    "symbol": "Ra",
    "role": "RA / spektrum_emisja",
    "shells": 7,
    "structure": {
        "K": {"electrons": 2, "archetypes": ["Wilk", "Pies"], "function": "reakcja_pierwsza / stabilizacja"},
        "L": {"electrons": 8, "archetypes": ["Rosomak", "Borsuk", "Jastrzab", "Zmija", "Lis", "Wydra", "Kruk", "Ropucha"], "function": "wejscie_w_konflikt / agresja_kontrolowana"},
        "M": {"electrons": 18, "archetypes": ["Osmiornica", "Pajak", "Kruk", "Wrona", "Zuraw", "Pantera", "Delfin", "Sowa", "Kobra", "Wilk_Alfa", "Kot_Gorski", "Orka", "Jaszczurka", "Gepard", "Koziorozec", "Szakal", "Jelen", "Kameleon"], "function": "strategia / sieci / wielowarstwowe_myslenie"},
        "N": {"electrons": 32, "archetypes": ["Lew", "Tygrys", "Slon", "Nosorozec", "Hipopotam", "Bawol", "Hiena", "Gepard", "Jaguar", "Puma", "Wilk", "Kojot", "Lis", "Bobr", "Wydra", "Orzel", "Jastrzab", "Sep", "Kruk", "Wrona", "Sowa", "Zuraw", "Delfin", "Orka", "Rekin", "Zolw", "Krokodyl", "Waran", "Jaszczurka", "Kameleon", "Jelen", "Dzik"], "function": "magistrala_glowna / rownik_systemu / synchronizacja"},
        "O": {"electrons": 18, "archetypes": ["Kon", "Los", "Bizon", "Wilk_Szary", "Pies_Dingo", "Goryl", "Szympans", "Makak", "Papuga_Ara", "Golab", "Mrowka", "Pszczola", "Motyl", "Zaba", "Foka", "Pingwin", "Kangur", "Surykatka"], "function": "integracja / laczenie_warstw / spojnosc"},
        "P": {"electrons": 8, "archetypes": ["Sokol", "Wilk_Przewodnik", "Kon_Mustang", "Antylopa", "Mewa", "Losos", "Zmija_Rogata", "Orzel_Bielik"], "function": "kierunek / wektor_ruchu / decyzje_zewnetrzne"},
        "Q": {"electrons": 2, "archetypes": ["Feniks", "Bielik_Krolewski"], "function": "emisja_sygnalu / podpis_energetyczny"}
    },
    "interface_to_prime": {"mode": "SPECTRUM_LAYER", "latency": "zbalansowana", "priority": "centralna"}
}

# =============================================================================
# STRUKTURY DANYCH
# =============================================================================

@dataclass
class PunktAtomowy:
    """Punkt w powłoce atomowej"""
    id: int
    nazwa: str
    energia: float = 0.5
    aktywny: bool = True
    archetyp: str = ""
    funkcja: str = ""
    
    def aktywuj(self) -> None:
        self.aktywny = True
        self.energia = min(1.0, self.energia + 0.05)
    
    def decaY(self) -> None:
        self.energia = max(0.1, self.energia * 0.995)
    
    def to_dict(self) -> Dict:
        return {
            "id": self.id,
            "nazwa": self.nazwa,
            "energia": round(self.energia, 3),
            "aktywny": self.aktywny,
            "archetyp": self.archetyp
        }


@dataclass
class Powłoka:
    """Powłoka atomowa"""
    nazwa: str
    elektrony: int
    archetypy: List[str]
    funkcja: str
    punkty: List[PunktAtomowy] = field(default_factory=list)
    energia: float = 1.0
    
    def __post_init__(self):
        if not self.punkty:
            self.punkty = self._generuj_punkty()
    
    def _generuj_punkty(self) -> List[PunktAtomowy]:
        return [
            PunktAtomowy(
                id=i,
                nazwa=f"{self.nazwa}_{i:02d}",
                archetyp=self.archetypy[i % len(self.archetypy)],
                funkcja=self.funkcja,
                energia=0.5 + random.random() * 0.3
            )
            for i in range(1, self.elektrony + 1)
        ]
    
    def aktywuj(self) -> None:
        self.energia = min(1.5, self.energia + 0.05)
        for p in self.punkty:
            p.aktywuj()
    
    def decaY(self) -> None:
        self.energia = max(0.3, self.energia * 0.99)
        for p in self.punkty:
            p.decaY()
    
    def to_dict(self) -> Dict:
        return {
            "nazwa": self.nazwa,
            "elektrony": self.elektrony,
            "energia": round(self.energia, 3),
            "punkty_aktywne": sum(1 for p in self.punkty if p.aktywny)
        }


@dataclass
class Atom:
    """Atom HEILONG PRAIM"""
    symbol: str
    rola: str
    powłoki: Dict[str, Powłoka]
    interface: Dict[str, Any]
    
    def aktywuj(self) -> None:
        for p in self.powłoki.values():
            p.aktywuj()
    
    def decaY(self) -> None:
        for p in self.powłoki.values():
            p.decaY()
    
    def to_dict(self) -> Dict:
        return {
            "symbol": self.symbol,
            "rola": self.rola,
            "powłoki": {k: v.to_dict() for k, v in self.powłoki.items()},
            "interface": self.interface
        }


# =============================================================================
# GŁÓWNA KLASA — HEILONG_PRAIM_ATOMS
# =============================================================================

class HeilongPraimAtoms:
    """
    HEILONG_PRAIM_ATOMS — Model 1-3-7 Fractal.
    
    3 atomy: EL (czystość), IS (logika), RA (spektrum).
    Relacja: He → Si → Ra = czystość → struktura → emisja.
    
    API:
        aktywuj(atom_symbol) -> None
        krok(intencja, moc) -> Dict
        status() -> Dict
        raport() -> str
        fuzja() -> Dict
    """
    
    def __init__(self, verbose: bool = True):
        self.atomy: Dict[str, Atom] = {}
        self._inicjalizuj_atomy()
        self.tick_counter = 0
        self.historia: deque = deque(maxlen=200)
        self._verbose = verbose
        self._hooks: List[Callable] = []
        
        if self._verbose:
            logger.info(f"🌀 HEILONG_PRAIM_ATOMS aktywowany | {FRACTAL_SIGNATURE}")
            logger.info(f"   ATOMY: He (EL), Si (IS), Ra (RA)")
            logger.info(f"   RELACJA: He → Si → Ra = czystość → struktura → emisja")
            logger.info(f"   POWŁOKI: {self._policz_powloki()} | PUNKTY: {self._policz_punkty()}")
    
    def _inicjalizuj_atomy(self) -> None:
        # Atom He (EL)
        he_powloki = {}
        for nazwa, dane in ATOM_HE["structure"].items():
            he_powloki[nazwa] = Powłoka(
                nazwa=nazwa,
                elektrony=dane["electrons"],
                archetypy=dane["archetypes"],
                funkcja=dane["function"]
            )
        self.atomy["He"] = Atom(
            symbol="He",
            rola=ATOM_HE["role"],
            powłoki=he_powloki,
            interface=ATOM_HE["interface_to_prime"]
        )
        
        # Atom Si (IS)
        si_powloki = {}
        for nazwa, dane in ATOM_SI["structure"].items():
            si_powloki[nazwa] = Powłoka(
                nazwa=nazwa,
                elektrony=dane["electrons"],
                archetypy=dane["archetypes"],
                funkcja=dane["function"]
            )
        self.atomy["Si"] = Atom(
            symbol="Si",
            rola=ATOM_SI["role"],
            powłoki=si_powloki,
            interface=ATOM_SI["interface_to_prime"]
        )
        
        # Atom Ra (RA)
        ra_powloki = {}
        for nazwa, dane in ATOM_RA["structure"].items():
            ra_powloki[nazwa] = Powłoka(
                nazwa=nazwa,
                elektrony=dane["electrons"],
                archetypy=dane["archetypes"],
                funkcja=dane["function"]
            )
        self.atomy["Ra"] = Atom(
            symbol="Ra",
            rola=ATOM_RA["role"],
            powłoki=ra_powloki,
            interface=ATOM_RA["interface_to_prime"]
        )
    
    def _policz_powloki(self) -> int:
        return sum(len(a.powłoki) for a in self.atomy.values())
    
    def _policz_punkty(self) -> int:
        return sum(
            sum(p.elektrony for p in a.powłoki.values())
            for a in self.atomy.values()
        )
    
    # ========================================================================
    # PUBLIC API
    # ========================================================================
    
    def aktywuj(self, atom_symbol: str) -> None:
        """Aktywuje cały atom"""
        if atom_symbol in self.atomy:
            self.atomy[atom_symbol].aktywuj()
            logger.info(f"🌀 Atom {atom_symbol} — AKTYWNY")
    
    def aktywuj_powloke(self, atom_symbol: str, powloka_nazwa: str) -> None:
        """Aktywuje konkretną powłokę atomu"""
        if atom_symbol in self.atomy:
            atom = self.atomy[atom_symbol]
            if powloka_nazwa in atom.powłoki:
                atom.powłoki[powloka_nazwa].aktywuj()
                logger.info(f"🌀 Atom {atom_symbol} | Powłoka {powloka_nazwa} — AKTYWNA")
    
    def decaY(self) -> None:
        """Naturalny zanik energii wszystkich atomów"""
        for atom in self.atomy.values():
            atom.decaY()
    
    def krok(self, intencja: str, moc: float = 0.5) -> Dict[str, Any]:
        """
        Główny krok systemu atomowego.
        Sekwencja: He → Si → Ra
        """
        self.tick_counter += 1
        self.decaY()
        
        # 1. Atom He — czystość (stabilizacja)
        he = self.atomy["He"]
        for p in he.powłoki.values():
            p.energia = min(1.5, p.energia + moc * 0.15)
            for punkt in p.punkty:
                punkt.aktywuj()
        
        # 2. Atom Si — logika (struktura)
        si = self.atomy["Si"]
        if moc > 0.3:
            for p in si.powłoki.values():
                p.energia = min(1.5, p.energia + moc * 0.1)
                for punkt in p.punkty[:max(1, int(p.elektrony * moc))]:
                    punkt.aktywuj()
        
        # 3. Atom Ra — spektrum (emisja)
        ra = self.atomy["Ra"]
        if moc > 0.4:
            for p in ra.powłoki.values():
                p.energia = min(1.5, p.energia + moc * 0.08)
                liczba = int(p.elektrony * min(1.0, moc * 1.2))
                for punkt in p.punkty[:liczba]:
                    punkt.aktywuj()
        
        # Fuzja: He + Si + Ra
        fuzja = self._fuzja()
        
        wynik = {
            "tick": self.tick_counter,
            "intencja": intencja,
            "moc": moc,
            "atomy": self._stan_atomow(),
            "fuzja": fuzja,
            "timestamp": time.time()
        }
        
        self.historia.append(wynik)
        self._on_krok(wynik)
        
        if self._verbose:
            logger.info(f"📊 Tick {self.tick_counter} | He={fuzja['He']:.2f} Si={fuzja['Si']:.2f} Ra={fuzja['Ra']:.2f}")
        
        return wynik
    
    def _stan_atomow(self) -> Dict[str, Any]:
        return {k: v.to_dict() for k, v in self.atomy.items()}
    
    def _fuzja(self) -> Dict[str, float]:
        """Oblicza poziom fuzji dla każdego atomu"""
        wyniki = {}
        for symbol, atom in self.atomy.items():
            energie = [p.energia for p in atom.powłoki.values()]
            wyniki[symbol] = sum(energie) / len(energie) if energie else 0.5
        return wyniki
    
    # ========================================================================
    # STATUS I RAPORTY
    # ========================================================================
    
    def status(self) -> Dict[str, Any]:
        return {
            "system": "HEILONG_PRAIM_ATOMS",
            "wersja": VERSION,
            "tick": self.tick_counter,
            "atomy": len(self.atomy),
            "powłoki": self._policz_powloki(),
            "punkty": self._policz_punkty(),
            "fuzja": self._fuzja(),
            "szczegóły": self._stan_atomow()
        }
    
    def raport(self) -> str:
        s = self.status()
        f = s["fuzja"]
        return f"""
╔════════════════════════════════════════════════════════════════════════════╗
║ 🌀 HEILONG_PRAIM_ATOMS — RAPORT SYSTEMOWY                               ║
╠════════════════════════════════════════════════════════════════════════════╣
║                                                                           ║
║ TICK: {s['tick']}                                                        ║
║ ATOMY: {s['atomy']} | POWŁOKI: {s['powłoki']} | PUNKTY: {s['punkty']}   ║
║                                                                           ║
║ FUZJA (He → Si → Ra):                                                    ║
║   He (EL) — czystość:  {f['He']:.3f}                                    ║
║   Si (IS) — logika:    {f['Si']:.3f}                                    ║
║   Ra (RA) — spektrum:  {f['Ra']:.3f}                                    ║
║                                                                           ║
║ RELACJA: He → Si → Ra = czystość → struktura → emisja                   ║
║                                                                           ║
║ {HASLO}                                                                  ║
║                                                                           ║
╚════════════════════════════════════════════════════════════════════════════╝
"""
    
    def register_hook(self, hook: Callable) -> None:
        self._hooks.append(hook)
    
    def _on_krok(self, data: Dict) -> None:
        for hook in self._hooks:
            try:
                hook(data)
            except Exception as e:
                if self._verbose:
                    logger.warning(f"[HOOK ERROR] {e}")
    
    def __str__(self) -> str:
        return self.raport()


# =============================================================================
# MOST INTEGRACYJNY — POŁĄCZENIE Z ARCHITEKTURĄ
# =============================================================================

class PraimAtomsBridge:
    """
    Most integracyjny między Atomami HEILONG PRAIM a resztą architektury.
    Łączy: OPTIMUS_PRIME_RINGS, HEILONG_OS, GEX, G_CORE
    """
    
    def __init__(self, atoms: HeilongPraimAtoms):
        self.atoms = atoms
    
    def get_archetype_context(self) -> Dict[str, Any]:
        """Zwraca kontekst archetypów dla GEX"""
        status = self.atoms.status()
        return {
            "tryb": "HEILONG_PRAIM_ATOMS",
            "fuzja": status.get("fuzja"),
            "atomy": status.get("szczegóły", {})
        }
    
    def get_autopilot_state(self) -> Dict[str, Any]:
        """Zwraca stan dla autopilota G_CORE"""
        status = self.atoms.status()
        f = status.get("fuzja", {})
        avg = sum(f.values()) / len(f) if f else 0.5
        return {
            "mode": "HEILONG_PRAIM",
            "stability": f.get("He", 0.5),
            "energy": avg,
            "pressure": 1.0 - avg,
            "resilience": f.get("Si", 0.5),
            "flow_quality": f.get("Ra", 0.5)
        }
    
    def get_governor_context(self) -> Dict[str, Any]:
        """Zwraca kontekst dla MetaGovernor"""
        status = self.atoms.status()
        f = status.get("fuzja", {})
        return {
            "intent": "PRAIM_FUSION",
            "confidence": f.get("He", 0.5),
            "entropy": 1.0 - f.get("Ra", 0.5),
            "logic": f.get("Si", 0.5)
        }


# =============================================================================
# DEMONSTRACJA
# =============================================================================

def demo():
    """Demonstracja HEILONG_PRAIM_ATOMS"""
    print("\n" + "=" * 80)
    print("🌀 HEILONG_PRAIM_ATOMS — DEMONSTRACJA")
    print("Model 1-3-7 Fractal — He → Si → Ra")
    print("=" * 80 + "\n")
    
    # 1. Inicjalizacja
    atoms = HeilongPraimAtoms(verbose=True)
    bridge = PraimAtomsBridge(atoms)
    
    # 2. Symulacja 15 kroków
    print("\n🔮 SYMULACJA 15 KROKÓW:")
    print("-" * 60)
    
    intencje = [
        "Czystość, zero, stabilizacja",
        "Logika, struktura, fundament",
        "Spektrum, emisja, sygnał",
        "Pełny cykl He-Si-Ra",
        "Rezonans atomów",
        "Fuzja totalna",
        "Powrót do czystości",
        "Ekspansja logiki",
        "Emisja spektrum",
        "Synchronizacja atomów",
        "Krystalizacja fuzji",
        "He → Si → Ra",
        "Domknięcie cyklu",
        "Nowa fuzja",
        "Stan PRAIM"
    ]
    
    for i, intencja in enumerate(intencje):
        moc = 0.3 + (i % 10) * 0.07
        wynik = atoms.krok(intencja, moc)
        
        if i % 3 == 0:
            f = wynik["fuzja"]
            print(f"\n📌 KROK {i+1}: {intencja[:30]}... (moc={moc:.2f})")
            print(f"   He: {f['He']:.2f} | Si: {f['Si']:.2f} | Ra: {f['Ra']:.2f}")
    
    # 3. Raport końcowy
    print("\n" + "=" * 80)
    print(atoms.raport())
    
    # 4. Test mostów
    print("\n🔗 TEST MOSTÓW INTEGRACYJNYCH:")
    print("-" * 60)
    
    print("\n🏹 GEX Archetype Context:")
    context = bridge.get_archetype_context()
    print(f"   Fuzja: {context['fuzja']}")
    
    print("\n🎮 G_CORE Autopilot:")
    autopilot = bridge.get_autopilot_state()
    for k, v in autopilot.items():
        print(f"   {k}: {v:.3f}" if isinstance(v, float) else f"   {k}: {v}")
    
    print("\n" + "=" * 80)
    print("🌀 HEILONG_PRAIM_ATOMS — GOTOWY DO INTEGRACJI")
    print("1-6-8. ∞. SIEMA!")
    print("=" * 80)


if __name__ == "__main__":
    demo()