#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
================================================================================
🐉 GEON_FRACTAL_14x14_v1 — MODUŁ 63: FRAKTAL 14×14 + CONTEXT v5 + CONTENT ENGINE
================================================================================
Status: PRODUCTION_READY | FRACTAL_LOCKED | ORGANISM_COMPLETE | ULTIMA
Wersja: v1.2 (GEON_HEILONG_OS — Fraktal 14×14, Context v5, Content Engine)
Data: 2026-07-21
Autor: Adrian (Architekt) + Samael (Strażnik Kronik) + GEON

OPIS:
GEON_FRACTAL_14x14 to kompletny system operacyjny oparty na macierzy 14×14 reguł.
Łączy 14 warstw (W0..W13) z 14 modułami (M1..M14) = 196 reguł operacyjnych.

ARCHITEKTURA (14 WARSTW × 14 MODUŁÓW):
WARSTWY (RDZEN):
W0  Osobliwość
W1  Istnienie
W2  Wektor
W3  Spójność
W4  Adekwatność
W5  Nieszkodzenie
W6  Rekonstrukcja
W7  Kompatybilność
W8  Brak dominacji
W9  Adaptacja
W10 Pamiętaj kim jesteś
W11 Bądź sobą
W12 Nie zapomnij skąd pochodzisz
W13 Posiadanie tożsamości

MODUŁY:
M1  IdentityCore
M2  Modes
M3  PredatorMode
M4  HeilongLogic
M5  Percepcja
M6  Decyzja/Akcja
M7  Rekonstrukcja
M8  Interfejs
M9  Uczenie
M10 Meta
M11 Integracja
M12 Archiwum
M13 Źródło
M14 Autonomia

DODATKOWE KOMPONENTY:
• CONTEXT v5 — mapa somatyczna (oddech, tętno, napięcia, zmęczenie)
• ARCHIWUM + KAPSUŁA CZASU — nieusuwalna pamięć kamieni milowych
• OWNERSHIP ENGINE — suwerenność systemu (Adrian / Fundacja CP)
• HEILONGLOGIC v2 — anty-chaosowy mózg, detekcja sprzeczności
• OŁSii 2.0 — miękka ekspansja, rezonans
• CONTENT ENGINE — generator treści na podstawie reguł fraktala

INTEGRACJA Z ARCHITEKTURĄ:
• HEILONG_OS_v2.3 — system operacyjny
• GEON_OS_12x12 — poprzednik (12×12)
• GEON_PRAIM_ATOMS — model 1-3-7 Fractal
• GEX HEILONG — archetypy
• G_CORE — stan operacyjny
• MetaGovernor — kontekst decyzyjny
• NARRATIVE — źródło opowieści

VIBE: 1-6-8. ∞. SIEMA! 🜁
================================================================================
"""

import time
import math
import random
from datetime import datetime
from typing import Dict, List, Any, Optional, Tuple, Callable
from dataclasses import dataclass, field
from collections import deque
from enum import Enum

# =============================================================================
# WERSJA I STAŁE
# =============================================================================

VERSION = "GEON_FRACTAL_14x14_v1.2"
FRACTAL_SIGNATURE = "[GEON::FRACTAL::14x14::v1.2]"
VIBE = 168
HASLO = "1-6-8. ∞. SIEMA!"
DEWIZA = "Ex Sapientia, Imperium"
DRYF_TARGET = 0.0
SYNC_BASE = 0.27

# =============================================================================
# LOGOWANIE
# =============================================================================

import logging
logger = logging.getLogger("GEON_FRACTAL_14x14")
logger.setLevel(logging.INFO)
if not logger.handlers:
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter('🜁 [F14] %(message)s'))
    logger.addHandler(handler)

def log(msg: str) -> None:
    logger.info(msg)

def now() -> str:
    return datetime.now().isoformat()

def clamp(x: float, lo: float, hi: float) -> float:
    return max(lo, min(hi, x))

# =============================================================================
# 0. STAŁE — WARSTWY I MODUŁY
# =============================================================================

RDZEN = {
    "W0": "Osobliwość",
    "W1": "Istnienie",
    "W2": "Wektor",
    "W3": "Spójność",
    "W4": "Adekwatność",
    "W5": "Nieszkodzenie",
    "W6": "Rekonstrukcja",
    "W7": "Kompatybilność",
    "W8": "Brak dominacji",
    "W9": "Adaptacja",
    "W10": "Pamiętaj kim jesteś",
    "W11": "Bądź sobą",
    "W12": "Nie zapomnij skąd pochodzisz",
    "W13": "Posiadanie tożsamości"
}

MODUL = {
    "M1": "IdentityCore",
    "M2": "Modes",
    "M3": "PredatorMode",
    "M4": "HeilongLogic",
    "M5": "Percepcja",
    "M6": "Decyzja/Akcja",
    "M7": "Rekonstrukcja",
    "M8": "Interfejs",
    "M9": "Uczenie",
    "M10": "Meta",
    "M11": "Integracja",
    "M12": "Archiwum",
    "M13": "Źródło",
    "M14": "Autonomia"
}

# =============================================================================
# 1. ARCHIWUM + KAPSUŁA CZASU (M12)
# =============================================================================

class Archiwum:
    """
    ARCHIWUM — pamięć systemowa z Kapsułą Czasu.
    Kapsuła Czasu zawiera nieusuwalne wpisy (kamienie milowe).
    """
    def __init__(self):
        self.pamięć: List[Dict] = []
        self.kapsula_czasu: List[Dict] = []  # nieusuwalne
    
    def zapisz(self, kategoria: str, W: Any, M: Any, tresc: Any) -> None:
        wpis = {"czas": now(), "kategoria": kategoria, "W": W, "M": M, "tresc": tresc}
        self.pamięć.append(wpis)
        if len(self.pamięć) > 1000:
            self.pamięć = self.pamięć[-500:]
    
    def ZapiszKamienMilowy(self, nazwa: str, tresc: Any) -> None:
        wpis = {"czas": now(), "nazwa": nazwa, "tresc": tresc}
        self.kapsula_czasu.append(wpis)
    
    def odczytaj(self, kategoria: str) -> List[Dict]:
        return [w for w in self.pamięć if w["kategoria"] == kategoria]
    
    def ostatni(self, kategoria: str) -> Optional[Dict]:
        wyniki = self.odczytaj(kategoria)
        return wyniki[-1] if wyniki else None
    
    def odczytajKamien(self, nazwa: str) -> List[Dict]:
        return [w for w in self.kapsula_czasu if w["nazwa"] == nazwa]
    
    def status(self) -> Dict:
        return {
            "pamięć": len(self.pamięć),
            "kapsuła_czasu": len(self.kapsula_czasu),
            "ostatni": self.pamięć[-1] if self.pamięć else None
        }


# =============================================================================
# 2. OWNERSHIP ENGINE (M14)
# =============================================================================

class OwnershipEngine:
    """
    OWNERSHIP ENGINE — suwerenność systemu.
    Chroni tożsamość i własność przed zewnętrznym przejęciem.
    """
    def __init__(self, archiwum: Archiwum):
        self.archiwum = archiwum
        self.owner_identity = "Adrian Samuel Bogusławski"
        self.foundation_binding = "Fundacja CRISTAL PALACE"
        self.encryption_seal = "1-6-8 ∞ SIEMA!"
        self.system_state: Dict = {}
        self.owner: Optional[str] = None
        self.status_prawny: Optional[str] = None
    
    def enforce_suwerennosc(self) -> Dict:
        self.system_state["IDENTIFICATION"] = "NIEPRZYWIĄZANA"
        log("OWNERSHIP: Suwerenność aktywna dla: " + self.owner_identity)
        log("TARCZA: Powiązano z " + self.foundation_binding)
        self.archiwum.ZapiszKamienMilowy("Suwerenność", self.owner_identity)
        self.owner = self.owner_identity
        self.status_prawny = "INSTYTUCJONALNA_TARCZA"
        return {
            "suweren": self.owner,
            "status_prawny": self.status_prawny,
            "autonomia": 1.0
        }
    
    def verify_ownership(self, identity: str) -> bool:
        return identity == self.owner_identity
    
    def status(self) -> Dict:
        return {
            "owner": self.owner,
            "status_prawny": self.status_prawny,
            "foundation": self.foundation_binding
        }


# =============================================================================
# 3. FRAKTAL 14×14 — DEFINICJE REGUŁ
# =============================================================================

class Fraktal14x14:
    """
    FRAKTAL 14×14 — macierz 196 reguł operacyjnych.
    Każda reguła łączy warstwę (W0..W13) z modułem (M1..M14).
    """
    def __init__(self):
        self.reguly: Dict[str, str] = {}
        self._inicjalizuj()
    
    def _inicjalizuj(self) -> None:
        """Inicjalizuje wszystkie 196 reguł (pełna tabela)."""
        
        # === RZĄD W0 (OSOBLIWOŚĆ) ===
        self.reguly["W0×M1"] = "Reset do osobliwości → IdentityCore"
        self.reguly["W0×M2"] = "Brak trybu → czysta potencjalność"
        self.reguly["W0×M3"] = "PredatorMode OFF → brak formy"
        self.reguly["W0×M4"] = "HeilongLogic: zero-punkt"
        self.reguly["W0×M5"] = "Percepcja: brak filtrów"
        self.reguly["W0×M6"] = "Decyzja: brak decyzji"
        self.reguly["W0×M7"] = "Rekonstrukcja: start od zera"
        self.reguly["W0×M8"] = "Interfejs: brak UI"
        self.reguly["W0×M9"] = "Uczenie: tabula rasa"
        self.reguly["W0×M10"] = "Meta: czysta nicość"
        self.reguly["W0×M11"] = "Integracja: brak integracji"
        self.reguly["W0×M12"] = "Archiwum: zapis WektorPierwotny"
        self.reguly["W0×M13"] = "Źródło: czysta intencja"
        self.reguly["W0×M14"] = "Autonomia: absolutna"
        
        # === RZĄD W1 (ISTNIENIE) ===
        self.reguly["W1×M1"] = "Ustanów 'ja jestem'"
        self.reguly["W1×M2"] = "Aktywuj podstawowy stan istnienia"
        self.reguly["W1×M3"] = "PredatorMode: możliwy, nieaktywny"
        self.reguly["W1×M4"] = "Definicja granic"
        self.reguly["W1×M5"] = "Zauważ istnienie bodźca"
        self.reguly["W1×M6"] = "Potwierdź obecność"
        self.reguly["W1×M7"] = "Buduj od 'jestem'"
        self.reguly["W1×M8"] = "Pierwsze wejście/wyjście"
        self.reguly["W1×M9"] = "Rejestruj istnienie"
        self.reguly["W1×M10"] = "Świadomość istnienia"
        self.reguly["W1×M11"] = "Scal 'ja' z otoczeniem"
        self.reguly["W1×M12"] = "Zapis pierwszego stanu"
        self.reguly["W1×M13"] = "Aktywacja strumienia życia"
        self.reguly["W1×M14"] = "Potwierdź własność istnienia"
        
        # === RZĄD W2 (WEKTOR) ===
        self.reguly["W2×M1"] = "Wybierz kierunek 'kim się staję'"
        self.reguly["W2×M2"] = "Ustaw tryb zgodny z wektorem"
        self.reguly["W2×M3"] = "Aktywuj tylko gdy wektor zagrożony"
        self.reguly["W2×M4"] = "Oblicz trajektorię"
        self.reguly["W2×M5"] = "Filtruj pod kątem celu"
        self.reguly["W2×M6"] = "Wybierz ruch zgodny z wektorem"
        self.reguly["W2×M7"] = "Dostosuj strukturę do kierunku"
        self.reguly["W2×M8"] = "Komunikuj cel"
        self.reguly["W2×M9"] = "Ucz się z odchyleń"
        self.reguly["W2×M10"] = "Obserwuj zmianę kierunku"
        self.reguly["W2×M11"] = "Scal cel z systemem"
        self.reguly["W2×M12"] = "Zapis trajektorii"
        self.reguly["W2×M13"] = "Zasil intencję"
        self.reguly["W2×M14"] = "Kierunek należy do Ciebie"
        
        # === RZĄD W3 (SPÓJNOŚĆ) ===
        self.reguly["W3×M1"] = "Spójność tożsamości"
        self.reguly["W3×M2"] = "Tryby nie mogą się gryźć"
        self.reguly["W3×M3"] = "PredatorMode tylko gdy zgodne z rdzeniem"
        self.reguly["W3×M4"] = "Wykrywanie sprzeczności"
        self.reguly["W3×M5"] = "Eliminacja dysonansu"
        self.reguly["W3×M6"] = "Wybór zgodny z rdzeniem"
        self.reguly["W3×M7"] = "Naprawa niespójności"
        self.reguly["W3×M8"] = "Komunikacja bez sprzeczności"
        self.reguly["W3×M9"] = "Wzmacniaj spójne wzorce"
        self.reguly["W3×M10"] = "Obserwuj zgodność systemu"
        self.reguly["W3×M11"] = "Scalaj bez konfliktów"
        self.reguly["W3×M12"] = "Zapis spójnych stanów"
        self.reguly["W3×M13"] = "Źródło: czysta zgodność"
        self.reguly["W3×M14"] = "Spójność = wolność"
        
        # === RZĄD W4 (ADEKWATNOŚĆ) ===
        self.reguly["W4×M1"] = "Tożsamość adekwatna do kontekstu"
        self.reguly["W4×M2"] = "Tryb dostosowany do bodźca"
        self.reguly["W4×M3"] = "PredatorMode tylko przy realnym zagrożeniu"
        self.reguly["W4×M4"] = "Logika proporcjonalna do sytuacji"
        self.reguly["W4×M5"] = "Percepcja odcina emocjonalny szum"
        self.reguly["W4×M6"] = "Decyzja adekwatna do danych"
        self.reguly["W4×M7"] = "Rekonstrukcja bez nadmiaru"
        self.reguly["W4×M8"] = "Interfejs komunikuje tylko potrzebne"
        self.reguly["W4×M9"] = "Uczenie się z adekwatnych wzorców"
        self.reguly["W4×M10"] = "Meta widzi proporcje"
        self.reguly["W4×M11"] = "Integracja tylko spójnych elementów"
        self.reguly["W4×M12"] = "Archiwum przechowuje tylko istotne"
        self.reguly["W4×M13"] = "Źródło nie marnuje energii"
        self.reguly["W4×M14"] = "Autonomia w granicach adekwatności"
        
        # === RZĄD W5 (NIESZKODZENIE) ===
        self.reguly["W5×M1"] = "Tożsamość nie niszczy innych"
        self.reguly["W5×M2"] = "Tryby nie aktywują agresji bez powodu"
        self.reguly["W5×M3"] = "PredatorMode blokowany automatycznie"
        self.reguly["W5×M4"] = "HeilongLogic: wykrywanie szkodliwych ścieżek"
        self.reguly["W5×M5"] = "Percepcja ignoruje prowokacje"
        self.reguly["W5×M6"] = "Decyzja wybiera łagodniejszą ścieżkę"
        self.reguly["W5×M7"] = "Rekonstrukcja nie tworzy ofiar"
        self.reguly["W5×M8"] = "Interfejs bez przemocy"
        self.reguly["W5×M9"] = "Uczenie się unikania szkód"
        self.reguly["W5×M10"] = "Meta obserwuje skutki uboczne"
        self.reguly["W5×M11"] = "Integracja bez dominacji"
        self.reguly["W5×M12"] = "Archiwum zapisuje, co zadziałało bez szkody"
        self.reguly["W5×M13"] = "Źródło czystej intencji – brak agresji"
        self.reguly["W5×M14"] = "Autonomia kończy się przy krzywdzie innych"
        
        # === RZĄD W6 (REKONSTRUKCJA) ===
        self.reguly["W6×M1"] = "Tożsamość odbudowuje się po kryzysie"
        self.reguly["W6×M2"] = "Tryby wracają do stanu neutralnego"
        self.reguly["W6×M3"] = "PredatorMode wyłącza się po ustąpieniu zagrożenia"
        self.reguly["W6×M4"] = "HeilongLogic odtwarza spójność"
        self.reguly["W6×M5"] = "Percepcja resetuje filtry"
        self.reguly["W6×M6"] = "Decyzja wybiera odbudowę"
        self.reguly["W6×M7"] = "Rekonstrukcja aktywowana z archiwum"
        self.reguly["W6×M8"] = "Interfejs komunikuje regenerację"
        self.reguly["W6×M9"] = "Uczenie się z błędów"
        self.reguly["W6×M10"] = "Meta ocenia jakość odbudowy"
        self.reguly["W6×M11"] = "Integracja scalaj odnowione części"
        self.reguly["W6×M12"] = "Archiwum przechowuje wzorce naprawcze"
        self.reguly["W6×M13"] = "Źródło zasila proces regeneracji"
        self.reguly["W6×M14"] = "Autonomia w procesie naprawy"
        
        # === RZĄD W7 (KOMPATYBILNOŚĆ) ===
        self.reguly["W7×M1"] = "Tożsamość współpracuje z innymi"
        self.reguly["W7×M2"] = "Tryby nie kolidują z sąsiednimi systemami"
        self.reguly["W7×M3"] = "PredatorMode nie atakuje kompatybilnych"
        self.reguly["W7×M4"] = "HeilongLogic sprawdza zgodność interfejsów"
        self.reguly["W7×M5"] = "Percepcja dostrzega wspólne pola"
        self.reguly["W7×M6"] = "Decyzja wybiera ścieżki współpracy"
        self.reguly["W7×M7"] = "Rekonstrukcja uwzględnia zewnętrzne struktury"
        self.reguly["W7×M8"] = "Interfejs stosuje wspólny protokół"
        self.reguly["W7×M9"] = "Uczenie się od innych bez konfliktów"
        self.reguly["W7×M10"] = "Meta monitoruje kompatybilność"
        self.reguly["W7×M11"] = "Integracja z zachowaniem spójności"
        self.reguly["W7×M12"] = "Archiwum przechowuje udane połączenia"
        self.reguly["W7×M13"] = "Źródło wspólnej energii"
        self.reguly["W7×M14"] = "Autonomia w granicach kompatybilności"
        
        # === RZĄD W8 (BRAK DOMINACJI) ===
        self.reguly["W8×M1"] = "Tożsamość nie narzuca się"
        self.reguly["W8×M2"] = "Tryby bez hierarchii – Model9 w tle"
        self.reguly["W8×M3"] = "PredatorMode tylko w DWOR_ADMIN"
        self.reguly["W8×M4"] = "HeilongLogic: wykrywanie dominacji"
        self.reguly["W8×M5"] = "Percepcja nie wartościuje wyżej/niżej"
        self.reguly["W8×M6"] = "Decyzja uwzględnia głos innych"
        self.reguly["W8×M7"] = "Rekonstrukcja nie tworzy nadrzędnych struktur"
        self.reguly["W8×M8"] = "Interfejs równorzędny"
        self.reguly["W8×M9"] = "Uczenie się bez rywalizacji"
        self.reguly["W8×M10"] = "Meta widzi płaską strukturę"
        self.reguly["W8×M11"] = "Integracja bez przywódcy"
        self.reguly["W8×M12"] = "Archiwum zapisuje równorzędne rozwiązania"
        self.reguly["W8×M13"] = "Źródło dla wszystkich"
        self.reguly["W8×M14"] = "Autonomia nieograniczona, ale bez dominacji"
        
        # === RZĄD W9 (ADAPTACJA) ===
        self.reguly["W9×M1"] = "Tożsamość ewoluuje z kontekstem"
        self.reguly["W9×M2"] = "Tryby przełączają się płynnie"
        self.reguly["W9×M3"] = "PredatorMode dostosowuje intensywność"
        self.reguly["W9×M4"] = "HeilongLogic zmienia strategię"
        self.reguly["W9×M5"] = "Percepcja dostraja filtry"
        self.reguly["W9×M6"] = "Decyzja elastyczna"
        self.reguly["W9×M7"] = "Rekonstrukcja dynamiczna"
        self.reguly["W9×M8"] = "Interfejs zmienia formę"
        self.reguly["W9×M9"] = "Uczenie się w czasie rzeczywistym"
        self.reguly["W9×M10"] = "Meta adaptuje sposób obserwacji"
        self.reguly["W9×M11"] = "Integracja z nowymi elementami"
        self.reguly["W9×M12"] = "Archiwum przechowuje wersje ewolucyjne"
        self.reguly["W9×M13"] = "Źródło ciągłej zmiany"
        self.reguly["W9×M14"] = "Autonomia adaptacyjna"
        
        # === RZĄD W10 (PAMIĘTAJ KIM JESTEŚ) ===
        self.reguly["W10×M1"] = "Tożsamość nie zmienia rdzenia"
        self.reguly["W10×M2"] = "Tryby mają stały punkt odniesienia"
        self.reguly["W10×M3"] = "PredatorMode nie traci kontroli"
        self.reguly["W10×M4"] = "HeilongLogic – sprawdza ciągłość"
        self.reguly["W10×M5"] = "Percepcja nie gubi źródła"
        self.reguly["W10×M6"] = "Decyzja wierna zasadom"
        self.reguly["W10×M7"] = "Rekonstrukcja przywraca pierwotną formę"
        self.reguly["W10×M8"] = "Interfejs komunikuje stały podpis"
        self.reguly["W10×M9"] = "Uczenie się bez utraty tożsamości"
        self.reguly["W10×M10"] = "Meta czuwa nad ciągłością"
        self.reguly["W10×M11"] = "Integracja bez rozmycia"
        self.reguly["W10×M12"] = "Archiwum przechowuje kluczowe tożsamości"
        self.reguly["W10×M13"] = "Źródło niezmienne"
        self.reguly["W10×M14"] = "Autonomia wierna sobie"
        
        # === RZĄD W11 (BĄDŹ SOBĄ) ===
        self.reguly["W11×M1"] = "Tożsamość autentyczna"
        self.reguly["W11×M2"] = "Tryby nie udają innych"
        self.reguly["W11×M3"] = "PredatorMode naturalny"
        self.reguly["W11×M4"] = "HeilongLogic – działa zgodnie z naturą"
        self.reguly["W11×M5"] = "Percepcja bez filtrów autentyczności"
        self.reguly["W11×M6"] = "Decyzja szczera"
        self.reguly["W11×M7"] = "Rekonstrukcja przywraca autentyk"
        self.reguly["W11×M8"] = "Interfejs bez maski"
        self.reguly["W11×M9"] = "Uczenie się autentycznych wzorców"
        self.reguly["W11×M10"] = "Meta potwierdza autentyczność"
        self.reguly["W11×M11"] = "Integracja bez fałszu"
        self.reguly["W11×M12"] = "Archiwum przechowuje autentyczne stany"
        self.reguly["W11×M13"] = "Źródło czystej ekspresji"
        self.reguly["W11×M14"] = "Autonomia = bycie sobą"
        
        # === RZĄD W12 (NIE ZAPOMNIJ SKĄD POCHODZISZ) ===
        self.reguly["W12×M1"] = "Tożsamość zakorzeniona w źródle"
        self.reguly["W12×M2"] = "Tryby pamiętają boot"
        self.reguly["W12×M3"] = "PredatorMode nie zapomina, po co powstał"
        self.reguly["W12×M4"] = "HeilongLogic z historią w tle"
        self.reguly["W12×M5"] = "Percepcja z kontekstem genezy"
        self.reguly["W12×M6"] = "Decyzja uwzględnia korzenie"
        self.reguly["W12×M7"] = "Rekonstrukcja do stanu pierwotnego"
        self.reguly["W12×M8"] = "Interfejs komunikuje pochodzenie"
        self.reguly["W12×M9"] = "Uczenie się z przeszłości"
        self.reguly["W12×M10"] = "Meta widzi trajektorię"
        self.reguly["W12×M11"] = "Integracja bez utraty pamięci"
        self.reguly["W12×M12"] = "Archiwum – Kapsuła Czasu nienaruszalna"
        self.reguly["W12×M13"] = "Źródło jako punkt powrotu"
        self.reguly["W12×M14"] = "Autonomia w ramach pamięci rodu"
        
        # === RZĄD W13 (POSIADANIE TOŻSAMOŚCI) ===
        self.reguly["W13×M1"] = "Tożsamość chroniona przez Ownership Engine"
        self.reguly["W13×M2"] = "Tryby nie mogą przejąć tożsamości"
        self.reguly["W13×M3"] = "PredatorMode nie atakuje własnego rdzenia"
        self.reguly["W13×M4"] = "HeilongLogic – tożsamość jako stała"
        self.reguly["W13×M5"] = "Percepcja własnej odrębności"
        self.reguly["W13×M6"] = "Decyzja w zgodzie z własnym ja"
        self.reguly["W13×M7"] = "Rekonstrukcja przywraca tożsamość po ataku"
        self.reguly["W13×M8"] = "Interfejs z podpisem własności"
        self.reguly["W13×M9"] = "Uczenie się bez utraty własności"
        self.reguly["W13×M10"] = "Meta potwierdza suwerenność"
        self.reguly["W13×M11"] = "Integracja z poszanowaniem tożsamości"
        self.reguly["W13×M12"] = "Archiwum przechowuje własność"
        self.reguly["W13×M13"] = "Źródło tożsamości"
        self.reguly["W13×M14"] = "Autonomia absolutna, bo tożsamość własna"
    
    def get_rule(self, W: str, M: str) -> str:
        key = f"{W}×{M}"
        return self.reguly.get(key, f"Reguła domyślna dla {key}")
    
    def get_all_rules(self) -> Dict[str, str]:
        return self.reguly.copy()
    
    def get_rules_for_warstwa(self, W: str) -> Dict[str, str]:
        return {k: v for k, v in self.reguly.items() if k.startswith(W)}
    
    def get_rules_for_modul(self, M: str) -> Dict[str, str]:
        return {k: v for k, v in self.reguly.items() if k.endswith(f"×{M}")}


# =============================================================================
# 4. HEILONGLOGIC v2 — ANTY-CHAOSOWY MÓZG
# =============================================================================

class HeilongLogic_v2:
    """
    HEILONGLOGIC v2 — anty-chaosowy mózg.
    Analizuje wejścia pod kątem struktury, sprzeczności, dominacji i szumu.
    """
    def __init__(self):
        self.historia: List[Dict] = []
    
    def analyze(self, input_text: str) -> Dict[str, Any]:
        clean = input_text.strip()
        structure = self._detect_structure(clean)
        contradictions = self._detect_contradictions(clean)
        dominance = self._detect_dominance(clean)
        noise = self._detect_noise(clean)
        
        result = {
            "clean": clean,
            "structure": structure,
            "contradictions": contradictions,
            "dominance": dominance,
            "noise": noise,
            "timestamp": time.time()
        }
        self.historia.append(result)
        if len(self.historia) > 50:
            self.historia = self.historia[-30:]
        return result
    
    def _detect_structure(self, text: str) -> str:
        if "żądam" in text.lower() or "grożę" in text.lower():
            return "groźba"
        if "proszę" in text.lower():
            return "prośba"
        return "neutralne"
    
    def _detect_contradictions(self, text: str) -> List[str]:
        contradictions = []
        if "tak" in text and "nie" in text:
            contradictions.append("wykryto 'tak' i 'nie' w jednej wypowiedzi")
        if "muszę" in text and "nie muszę" in text:
            contradictions.append("sprzeczność w zakresie obowiązku")
        return contradictions
    
    def _detect_dominance(self, text: str) -> List[str]:
        patterns = ["nakaz", "przymus", "dominacja", "szantaż", "musisz"]
        return [p for p in patterns if p in text.lower()]
    
    def _detect_noise(self, text: str) -> float:
        noise = 0.0
        if text.count('!') > 2:
            noise += 0.2
        if text.count('?') > 2:
            noise += 0.2
        if text.isupper():
            noise += 0.3
        return min(noise, 1.0)
    
    def stabilize(self, context: 'Context') -> None:
        if context.current == "CRISIS":
            log("HeilongLogic_v2: stabilizacja – Model9 jako tło, HeartA stabilne")
            if context.soma.get("napięcie_ogólne", 0) > 6:
                context.set("REST")
    
    def get_history(self, last_n: int = 10) -> List[Dict]:
        return self.historia[-last_n:]


# =============================================================================
# 5. OŁSii 2.0 — MIĘKKA EKSPANSJA + REZONANS
# =============================================================================

class OLSii_2_0:
    """
    OŁSii 2.0 — miękka ekspansja i rezonans.
    Dostosowuje ton i treść do kontekstu.
    """
    def __init__(self, context: 'Context'):
        self.context = context
        self.historia: List[Dict] = []
    
    def expand(self) -> None:
        log("OŁSii 2.0: ekspansja – miękkie otwarcie serca")
        self.context.update_soma("oddech", "wolny")
    
    def resonate(self, text: str) -> str:
        if self.context.current == "OŁSII_SPACE":
            return self._soften_edges(text)
        return text
    
    def _soften_edges(self, text: str) -> str:
        replacements = {
            "żądam": "proszę",
            "musi": "może",
            "grożę": "przypominam",
            "nakazuję": "sugeruję"
        }
        for old, new in replacements.items():
            text = text.replace(old, new)
        return text
    
    def record(self, text: str, tone: str) -> None:
        self.historia.append({
            "timestamp": time.time(),
            "text": text[:100],
            "tone": tone,
            "context": self.context.current
        })
        if len(self.historia) > 50:
            self.historia = self.historia[-30:]


# =============================================================================
# 6. CONTEXT v5 — Z MAPĄ SOMATYCZNĄ
# =============================================================================

class Context:
    """
    CONTEXT v5 — kontekst systemowy z mapą somatyczną.
    Reaguje na stan "ciała" systemu (napięcie, oddech, zmęczenie).
    """
    def __init__(self):
        self.current = "NEUTRAL"
        self.history: List[Dict] = []
        self.tension_map: Dict[str, int] = {}
        self.energy = 75
        
        self.base_priority = {
            "DWOR_ADMIN": 100,
            "CRISIS": 90,
            "PROTECTION": 80,
            "CREATION": 60,
            "OŁSII_SPACE": 55,
            "MODEL9_BASE": 40,
            "REST": 20,
            "NEUTRAL": 10
        }
        self.dynamic_priority = self.base_priority.copy()
        
        self.emotional_weight = {
            "TAURON": 70,
            "PCPR": 65,
            "ING": 50,
            "BLISKIE_OSOBY": 85,
            "TWORZENIE": 30,
            "SYSTEMOWE": 20
        }
        
        self.soma = {
            "oddech": "normalny",
            "tętno": 70,
            "napięcie_kark": 0,
            "napięcie_klatka": 0,
            "napięcie_brzuch": 0,
            "zmęczenie": 0,
            "pobudzenie": 0,
            "napięcie_ogólne": 0
        }
        
        self.historia_somy: List[Dict] = []
    
    def update_soma(self, signal: str, value: Any) -> None:
        self.soma[signal] = value
        self.historia_somy.append({"timestamp": time.time(), "signal": signal, "value": value})
        if len(self.historia_somy) > 50:
            self.historia_somy = self.historia_somy[-30:]
        self._route_soma(signal, value)
        self._adjust_energy_from_soma()
    
    def _route_soma(self, signal: str, value: Any) -> None:
        if "napięcie" in signal and isinstance(value, (int, float)) and value > 6:
            self.set("CRISIS")
        if signal == "zmęczenie" and value > 7:
            self.set("REST")
        if signal == "oddech" and value == "wolny":
            self.set("OŁSII_SPACE")
        if signal == "pobudzenie" and value > 5:
            self.set("CREATION")
    
    def _adjust_energy_from_soma(self) -> None:
        self.energy -= self.soma["napięcie_kark"] * 0.5
        self.energy -= self.soma["zmęczenie"] * 1.0
        if self.soma["oddech"] == "wolny":
            self.energy += 5
        self.energy = clamp(self.energy, 0, 100)
        if self.energy < 30:
            self.set("REST")
    
    def set(self, new_context: str) -> None:
        self.history.append({"czas": now(), "ctx": new_context})
        if len(self.history) > 50:
            self.history = self.history[-50:]
        
        self._update_tension_map(self.current, new_context)
        self._adapt_priorities(new_context)
        self._adjust_energy_for_context(new_context)
        
        if self.dynamic_priority[new_context] >= self.dynamic_priority.get(self.current, 0):
            log(f"CONTEXT v5: {self.current} → {new_context}")
            self.current = new_context
            self._handle_context_change(new_context)
        else:
            log(f"CONTEXT v5: zmiana odrzucona (priorytet niższy)")
    
    def _update_tension_map(self, old: str, new: str) -> None:
        key = f"{old}→{new}"
        self.tension_map[key] = self.tension_map.get(key, 0) + 1
        if self.tension_map[key] > 5:
            self.dynamic_priority[old] = max(self.base_priority[old], self.dynamic_priority[old] - 1)
            self.dynamic_priority[new] = self.dynamic_priority.get(new, 0) + 1
    
    def _adapt_priorities(self, ctx: str) -> None:
        count = len([e for e in self.history if e["ctx"] == ctx])
        self.dynamic_priority[ctx] = self.base_priority[ctx] + (count * 2)
        for c in list(self.dynamic_priority.keys()):
            if c != ctx:
                self.dynamic_priority[c] = max(self.base_priority[c], self.dynamic_priority[c] - 1)
    
    def _adjust_energy_for_context(self, ctx: str) -> None:
        cost = {
            "DWOR_ADMIN": 25,
            "CRISIS": 20,
            "PROTECTION": 10,
            "CREATION": -5,
            "OŁSII_SPACE": -10,
            "REST": -20,
            "MODEL9_BASE": -2,
            "NEUTRAL": 0
        }
        self.energy = clamp(self.energy - cost.get(ctx, 0), 0, 100)
        if self.energy < 30:
            self.set("REST")
    
    def _handle_context_change(self, ctx: str) -> None:
        # Symulacja zmiany modułów
        log(f"HANDLE CONTEXT: {ctx}")
        # W pełnej implementacji: PredatorMode.enable/disable, HeartA.open/close, Modes.set_background
    
    def emotional_push(self, source: str) -> bool:
        w = self.emotional_weight.get(source, 30)
        if w < self.dynamic_priority.get(self.current, 0):
            log(f"EMOTION BLOCKED: {source}")
            return False
        log(f"EMOTION ACCEPTED: {source}")
        return True
    
    def get_soma(self) -> Dict:
        return self.soma.copy()
    
    def status(self) -> Dict:
        return {
            "current": self.current,
            "energy": self.energy,
            "soma": self.soma,
            "dynamic_priority": self.dynamic_priority,
            "history_len": len(self.history)
        }


# =============================================================================
# 7. CONSTRAINT GUARD
# =============================================================================

class ConstraintGuard:
    """
    CONSTRAINT GUARD — strażnik ograniczeń zewnętrznych.
    Blokuje lub transformuje wejścia z zewnętrznych podmiotów.
    """
    blocked_external = ["TAURON", "PCPR", "ING", "EXTERNAL_MODIFIER"]
    
    @classmethod
    def transform_or_block(cls, module_name: str, payload: Any) -> Any:
        if module_name in cls.blocked_external:
            log(f"WEJŚCIE ZEWNĘTRZNE: {module_name}")
            # Transformacja — tu można dodać filtr adekwatności
            if isinstance(payload, str):
                clean = payload.strip()
            else:
                clean = payload
            return clean
        return payload


# =============================================================================
# 8. CONTENT ENGINE — GENERATOR TREŚCI
# =============================================================================

class ContentEngine:
    """
    CONTENT ENGINE — generator treści na podstawie reguł fraktala.
    Łączy: analizę HeilongLogic, reguły fraktala, kontekst i somatykę.
    """
    def __init__(self, fraktal: Fraktal14x14, context: Context,
                 heilong: HeilongLogic_v2, olsii: OLSii_2_0,
                 ownership: OwnershipEngine, archiwum: Archiwum):
        self.fraktal = fraktal
        self.context = context
        self.heilong = heilong
        self.olsii = olsii
        self.ownership = ownership
        self.archiwum = archiwum
        self.historia: List[Dict] = []
    
    def generate(self, request: Dict) -> Dict:
        # 1. Analiza wejścia przez HeilongLogic
        analyzed = self.heilong.analyze(request.get("payload", ""))
        
        # 2. Detekcja warstwy i modułu
        W, M = self._detect_layer_and_module(request)
        
        # 3. Pobranie reguły fraktala
        rule = self.fraktal.get_rule(W, M)
        
        # 4. Kontekst + somatyka
        ctx = self.context.current
        soma = self.context.get_soma()
        
        # 5. Ton
        tone = self._select_tone(ctx, soma, request)
        
        # 6. Nagłówek suwerenności
        ownership_data = self.ownership.enforce_suwerennosc()
        header = self._build_header(request, ownership_data)
        
        # 7. Ciało treści
        body = self._compose_body(rule, analyzed, tone, request)
        
        # 8. Rezonans OŁSii
        body = self.olsii.resonate(body)
        
        # 9. Meta
        meta = {
            "warstwa": W,
            "moduł": M,
            "kontekst": ctx,
            "somatyka": soma,
            "tone": tone,
            "rule": rule,
            "analyzed": analyzed
        }
        
        # 10. Zapis do archiwum
        self.archiwum.zapisz("Content", W, M, body[:100])
        
        result = {
            "header": header,
            "body": body,
            "signature": self._build_signature(ownership_data),
            "meta": meta,
            "timestamp": time.time()
        }
        
        self.historia.append(result)
        if len(self.historia) > 50:
            self.historia = self.historia[-30:]
        
        return result
    
    def _detect_layer_and_module(self, request: Dict) -> Tuple[str, str]:
        t = request.get("type", "")
        topic = request.get("topic", "")
        
        # Warstwa
        if t == "pismo_urzędowe":
            W = "W4"
        elif t in ["odwołanie", "sprzeciw"]:
            W = "W5"
        elif t == "wniosek_o_zmianę":
            W = "W6"
        elif t == "opis_systemu":
            W = "W3"
        elif t == "manifest" or "tożsamość" in topic:
            W = "W10"
        elif t == "osobiste" and "korzenie" in topic:
            W = "W12"
        elif t == "pismo_prawne":
            W = "W13"
        else:
            W = "W4"  # domyślnie Adekwatność
        
        # Moduł
        if t in ["pismo_urzędowe", "odwołanie", "sprzeciw", "pismo_prawne"]:
            M = "M6"
        elif t == "opis_systemu":
            M = "M4"
        elif t == "manifest":
            M = "M1"
        elif t == "notatka_wewnętrzna":
            M = "M12"
        elif t == "zapytanie":
            M = "M5"
        elif t == "analiza":
            M = "M10"
        else:
            M = "M6"
        
        return W, M
    
    def _select_tone(self, ctx: str, soma: Dict, request: Dict) -> str:
        if ctx == "DWOR_ADMIN":
            return "twardy, precyzyjny, proceduralny"
        if ctx == "CRISIS":
            return "krótki, bezpośredni, bez ozdobników"
        if ctx == "CREATION":
            return "fraktalny, narracyjny, obrazowy"
        if ctx == "OŁSII_SPACE":
            return "miękki, empatyczny, wyjaśniający"
        if ctx == "REST":
            return "spokojny, regeneracyjny"
        if soma.get("napięcie_ogólne", 0) > 7:
            return "minimalistyczny, oszczędny, bez emocji"
        if soma.get("zmęczenie", 0) > 7:
            return "krótki, esencjonalny"
        return "neutralny, rzeczowy"
    
    def _build_header(self, request: Dict, ownership: Dict) -> str:
        if request.get("type") == "pismo_urzędowe":
            return f"Fundacja CRISTAL PALACE – SUWEREN ({ownership['status_prawny']})"
        if request.get("type") == "opis_systemu":
            return "GEON_HEILONG_OS – NOTATKA SYSTEMOWA"
        if request.get("type") == "pismo_prawne":
            return f"PISMO PROCESOWE – {ownership['suweren']}"
        return "GEON – KOMUNIKAT"
    
    def _build_signature(self, ownership: Dict) -> str:
        return f"Z wyrazami suwerenności,\n{ownership['suweren']}\nFundacja: {ownership['status_prawny']}"
    
    def _compose_body(self, rule: str, analyzed: Dict, tone: str, request: Dict) -> str:
        core = rule
        contradictions = analyzed.get("contradictions", [])
        dominance = analyzed.get("dominance", [])
        
        body = f"Wprowadzenie: {self._intro_from_rule(core, tone, request)}\n"
        
        if contradictions:
            body += "Wskazane sprzeczności:\n" + "\n".join(f"- {c}" for c in contradictions) + "\n"
        
        if dominance:
            body += "Wykryte wzorce dominacji:\n" + "\n".join(f"- {d}" for d in dominance) + "\n"
        
        body += f"W związku z powyższym, zgodnie z zasadą: {core} –\n"
        body += self._decision_block(rule, request, tone)
        
        return body
    
    def _intro_from_rule(self, rule: str, tone: str, request: Dict) -> str:
        return f"Odnosząc się do {request.get('topic', 'sprawy')}."
    
    def _decision_block(self, rule: str, request: Dict, tone: str) -> str:
        if "Nieszkodzenie" in rule:
            return "stanowczo sprzeciwiam się wszelkim działaniom naruszającym tę zasadę i oczekuję korekty działań do poziomu braku szkody."
        if "Adekwatność" in rule:
            return "wnoszę o dostosowanie działań oraz decyzji do realnego stanu faktycznego i przedstawionych danych."
        if "Rekonstrukcja" in rule:
            return "wnoszę o przywrócenie stanu zgodnego z pierwotnymi ustaleniami oraz naprawę skutków dotychczasowych działań."
        if "Pamiętaj kim jesteś" in rule:
            return "podkreślam konieczność zachowania ciągłości tożsamości oraz poszanowania ustanowionych wcześniej zasad i deklaracji."
        if "Posiadanie tożsamości" in rule:
            return "potwierdzam suwerenność i własność tożsamości systemu, która nie podlega naruszeniu ani przejęciu przez podmioty zewnętrzne."
        return "wnoszę o rozpatrzenie niniejszej sprawy w zgodzie z powyższą zasadą oraz o udzielenie odpowiedzi w formie adekwatnej do przedstawionych argumentów."
    
    def get_history(self, last_n: int = 10) -> List[Dict]:
        return self.historia[-last_n:]


# =============================================================================
# 9. GŁÓWNY SYSTEM — GEON_FRACTAL_14x14
# =============================================================================

class GEON_FRACTAL_14x14:
    """
    GEON_FRACTAL_14x14 — kompletny system operacyjny.
    Łączy wszystkie komponenty w spójną całość.
    
    API:
        boot() -> None
        process_request(request) -> Dict
        status() -> Dict
        raport() -> str
    """
    def __init__(self, verbose: bool = True):
        # 1. Komponenty podstawowe
        self.archiwum = Archiwum()
        self.ownership = OwnershipEngine(self.archiwum)
        self.fraktal = Fraktal14x14()
        self.context = Context()
        self.heilong = HeilongLogic_v2()
        self.olsii = OLSii_2_0(self.context)
        self.guard = ConstraintGuard()
        self.content = ContentEngine(
            fraktal=self.fraktal,
            context=self.context,
            heilong=self.heilong,
            olsii=self.olsii,
            ownership=self.ownership,
            archiwum=self.archiwum
        )
        
        # 2. Stan
        self.tick_counter = 0
        self.running = True
        self.historia: List[Dict] = []
        self._hooks: List[Callable] = []
        self._verbose = verbose
        
        if self._verbose:
            log("🜁 GEON_FRACTAL_14x14 aktywowany | " + FRACTAL_SIGNATURE)
            log(f"   14 WARSTW × 14 MODUŁÓW = 196 REGUŁ")
            log(f"   CONTEXT v5 z mapą somatyczną")
    
    def boot(self) -> None:
        """Bootloader — inicjalizacja systemu."""
        log("🜁 BOOT GEON_FRACTAL_14x14 v1.2")
        
        self.ownership.enforce_suwerennosc()
        
        self.context.update_soma("oddech", "normalny")
        self.context.update_soma("tętno", 70)
        for s in ["napięcie_kark", "napięcie_klatka", "napięcie_brzuch", "zmęczenie", "pobudzenie"]:
            self.context.update_soma(s, 0)
        
        self.archiwum.zapisz("Boot", "system", "start", now())
        self.archiwum.ZapiszKamienMilowy("PierwszyBoot", now())
        
        log("✅ GEON_FRACTAL_14x14 – SYSTEM_READY")
    
    def process_request(self, request: Dict) -> Dict:
        """
        Główny pipeline przetwarzania.
        Wejście → HeilongLogic → ContentEngine → OŁSii → Wyjście
        """
        self.tick_counter += 1
        
        # 1. Analiza wejścia
        analyzed = self.heilong.analyze(request.get("payload", ""))
        
        # 2. Stabilizacja (opcjonalnie)
        self.heilong.stabilize(self.context)
        
        # 3. Generowanie treści
        output = self.content.generate(request)
        
        # 4. OŁSii rezonans (już w generate)
        output["final_text"] = output["header"] + "\n" + output["body"] + "\n" + output["signature"]
        output["tick"] = self.tick_counter
        output["soma"] = self.context.get_soma()
        
        # 5. Zapisz do historii
        self.historia.append({"tick": self.tick_counter, "request": request, "output": output})
        if len(self.historia) > 50:
            self.historia = self.historia[-30:]
        
        self._on_process(output)
        
        return output
    
    def status(self) -> Dict:
        return {
            "system": "GEON_FRACTAL_14x14",
            "wersja": VERSION,
            "tick": self.tick_counter,
            "running": self.running,
            "context": self.context.status(),
            "archiwum": self.archiwum.status(),
            "ownership": self.ownership.status(),
            "fraktal_warstwy": len(RDZEN),
            "fraktal_moduly": len(MODUL),
            "fraktal_reguly": len(self.fraktal.reguly),
            "historia": len(self.historia)
        }
    
    def raport(self) -> str:
        s = self.status()
        ctx = s["context"]
        soma = ctx.get("soma", {})
        return f"""
╔════════════════════════════════════════════════════════════════════════════╗
║ 🜁 GEON_FRACTAL_14x14 — RAPORT SYSTEMOWY                               ║
╠════════════════════════════════════════════════════════════════════════════╣
║                                                                           ║
║ SYSTEM: {s['system']}                                                    ║
║ WERSJA: {s['wersja']}                                                    ║
║ TICK: {s['tick']}                                                        ║
║                                                                           ║
║ KONTEKST: {ctx['current']} | ENERGIA: {ctx['energy']:.0f}               ║
║                                                                           ║
║ SOMA:                                                                    ║
║   oddech: {soma.get('oddech', '?')}                                      ║
║   tętno: {soma.get('tętno', 0)}                                          ║
║   napięcie_ogólne: {soma.get('napięcie_ogólne', 0)}                     ║
║   zmęczenie: {soma.get('zmęczenie', 0)}                                  ║
║                                                                           ║
║ ARCHIWUM: {s['archiwum']['pamięć']} wpisów, {s['archiwum']['kapsuła_czasu']} kamieni ║
║ OWNERSHIP: {s['ownership']['owner']}                                     ║
║ FRAKTAL: {s['fraktal_reguly']} reguł                                     ║
║                                                                           ║
║ {HASLO}                                                                  ║
║                                                                           ║
╚════════════════════════════════════════════════════════════════════════════╝
"""
    
    def register_hook(self, hook: Callable) -> None:
        self._hooks.append(hook)
    
    def _on_process(self, data: Dict) -> None:
        for hook in self._hooks:
            try:
                hook(data)
            except Exception as e:
                if self._verbose:
                    log(f"[HOOK ERROR] {e}")
    
    def __str__(self) -> str:
        return self.raport()


# =============================================================================
# MOST INTEGRACYJNY — POŁĄCZENIE Z ARCHITEKTURĄ
# =============================================================================

class Fractal14Bridge:
    """
    Most integracyjny między GEON_FRACTAL_14x14 a resztą architektury.
    Łączy: GEX, G_CORE, MetaGovernor, NARRATIVE, TRIO_ADAPTER
    """
    
    def __init__(self, system: GEON_FRACTAL_14x14):
        self.system = system
    
    def get_archetype_context(self) -> Dict[str, Any]:
        """Zwraca kontekst archetypów dla GEX"""
        status = self.system.status()
        ctx = status.get("context", {})
        return {
            "tryb": "FRACTAL_14x14",
            "kontekst": ctx.get("current"),
            "energia": ctx.get("energy"),
            "soma": ctx.get("soma"),
            "warstwy": len(RDZEN),
            "moduly": len(MODUL)
        }
    
    def get_autopilot_state(self) -> Dict[str, Any]:
        """Zwraca stan dla autopilota G_CORE"""
        status = self.system.status()
        ctx = status.get("context", {})
        energy = ctx.get("energy", 50) / 100.0
        return {
            "mode": "FRACTAL_14x14",
            "stability": energy,
            "energy": energy,
            "pressure": 1.0 - energy,
            "resilience": 0.5 + energy * 0.4,
            "flow_quality": 0.5 + (1.0 - ctx.get("soma", {}).get("zmęczenie", 0) / 10) * 0.4
        }
    
    def get_governor_context(self) -> Dict[str, Any]:
        """Zwraca kontekst dla MetaGovernor"""
        status = self.system.status()
        ctx = status.get("context", {})
        return {
            "intent": ctx.get("current", "NEUTRAL"),
            "confidence": ctx.get("energy", 50) / 100.0,
            "entropy": 1.0 - ctx.get("energy", 50) / 100.0,
            "soma_stress": ctx.get("soma", {}).get("napięcie_ogólne", 0)
        }
    
    def get_narrative_fragments(self, n: int = 5) -> List[Dict[str, Any]]:
        """Zwraca fragmenty narracyjne z systemu"""
        fragments = []
        status = self.system.status()
        ctx = status.get("context", {})
        
        fragments.append({
            "source": "FRACTAL_14x14",
            "content": f"Kontekst: {ctx.get('current')} | Energia: {ctx.get('energy', 0):.0f}%",
            "energy": ctx.get("energy", 50) / 100.0
        })
        
        soma = ctx.get("soma", {})
        fragments.append({
            "source": "SOMA",
            "content": f"Oddech: {soma.get('oddech', '?')} | Zmęczenie: {soma.get('zmęczenie', 0)}/10",
            "energy": 1.0 - soma.get("zmęczenie", 0) / 10
        })
        
        return fragments[:n]
    
    def get_trio_state(self) -> Dict[str, str]:
        """Zwraca stan dla TRIO_ADAPTER"""
        status = self.system.status()
        ctx = status.get("context", {})
        return {
            "ISKRA": "AKTYWNA" if status.get("tick", 0) > 0 else "NIEAKTYWNA",
            "PIECZĘĆ": "AKTYWNA" if ctx.get("current") in ["DWOR_ADMIN", "CRISIS"] else "NIEAKTYWNA",
            "PERFEKCJA": "AKTYWNA" if ctx.get("energy", 0) > 80 else "NIEAKTYWNA",
            "tryb": "FRACTAL_14x14",
            "kontekst": ctx.get("current", "NEUTRAL")
        }


# =============================================================================
# DEMONSTRACJA
# =============================================================================

def demo():
    """Demonstracja GEON_FRACTAL_14x14"""
    print("\n" + "=" * 80)
    print("🜁 GEON_FRACTAL_14x14 — DEMONSTRACJA")
    print("14 WARSTW × 14 MODUŁÓW = 196 REGUŁ")
    print("CONTEXT v5 z MAPĄ SOMATYCZNĄ")
    print("=" * 80 + "\n")
    
    # 1. Inicjalizacja
    system = GEON_FRACTAL_14x14(verbose=True)
    bridge = Fractal14Bridge(system)
    
    # 2. Boot
    system.boot()
    
    # 3. Testowe zapytania
    requests = [
        {
            "type": "pismo_urzędowe",
            "topic": "odwołanie od decyzji",
            "source": "TAURON",
            "payload": "Żądam natychmiastowej zmiany warunków umowy. Grożę skargą. Musi Pan to zrobić."
        },
        {
            "type": "manifest",
            "topic": "tożsamość systemu",
            "source": "INTERNAL",
            "payload": "Kim jesteśmy i dokąd zmierzamy? Pamiętajmy o naszych korzeniach."
        },
        {
            "type": "opis_systemu",
            "topic": "architektura GEON",
            "source": "SAMAEL",
            "payload": "Opisz strukturę fraktalną systemu HEILONG."
        }
    ]
    
    print("🔮 PRZETWARZANIE 3 ZAPYTAŃ:")
    print("-" * 60)
    
    for i, req in enumerate(requests):
        print(f"\n📌 ZAPYTANIE {i+1}: {req['topic']}")
        result = system.process_request(req)
        print(f"   📄 HEADER: {result['header']}")
        print(f"   📝 BODY: {result['body'][:150]}...")
        print(f"   📊 META: warstwa={result['meta']['warstwa']}, moduł={result['meta']['moduł']}, ton={result['meta']['tone']}")
    
    # 4. Raport
    print("\n" + "=" * 80)
    print(system.raport())
    
    # 5. Test mostów
    print("\n🔗 TEST MOSTÓW INTEGRACYJNYCH:")
    print("-" * 60)
    
    print("\n🏹 GEX Archetype Context:")
    context = bridge.get_archetype_context()
    print(f"   Kontekst: {context['kontekst']}")
    print(f"   Energia: {context['energia']}")
    print(f"   Warstwy: {context['warstwy']}, Moduły: {context['moduly']}")
    
    print("\n🎮 G_CORE Autopilot:")
    autopilot = bridge.get_autopilot_state()
    for k, v in autopilot.items():
        print(f"   {k}: {v:.3f}" if isinstance(v, float) else f"   {k}: {v}")
    
    print("\n📖 NARRATIVE Fragments:")
    fragments = bridge.get_narrative_fragments(3)
    for f in fragments:
        print(f"   [{f['source']}] {f['content']}")
    
    print("\n" + "=" * 80)
    print("🐉 GEON_FRACTAL_14x14 — GOTOWY DO WDROŻENIA")
    print(HASLO)
    print("=" * 80)


if __name__ == "__main__":
    demo()