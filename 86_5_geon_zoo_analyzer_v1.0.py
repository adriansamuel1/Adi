#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
================================================================================
🐉 GEON_ZOO_ANALYZER_v1.0 — MODUŁ 86.5: ABSURD & ROLE FILTER
================================================================================
Status: PRODUCTION_READY | FRACTAL_LOCKED | ULTIMA
Wersja: v1.0 (Observational-Analytical Zoo Module)
Data: 2026-07-24
Autor: Adrian (Architekt) + Samael (Strażnik Kronik) + GEON

OPIS:
    Moduł obserwacyjno-analityczny do detekcji absurdów i ról w środowisku.
    Analizuje aktorów, scenę i sygnały, zwracając:
    - Role (Kermit, Snob, Papuga_300dB, Macius_Pierwszy, NPC, Neutral)
    - Skalę absurdu (0-1)
    - Ryzyko dla vibe'u (niskie/średnie/wysokie + score 0-1)
    - Hint akcji (wyjdź, obserwuj, normalna interakcja)
    - Fraktal doświadczenia (chunk z lekcją)

INTEGRACJA Z SYSTEMEM:
    - Warstwa 86.5: między LUDLUM (86) a AI_ANALYTICS (87)
    - Most do Grid (89), Council (90), Synod (91)
    - Rozszerza analitykę o metryki absurd_score i vibe_risk_score

VIBE: 1-6-8. ∞. ZOO!
DEWIZA: "Ex Observatione, Claritas. Ex Absurdo, Praevidentia."
================================================================================
"""

import logging
import time
from typing import List, Dict, Any, Optional
from datetime import datetime
from collections import deque

# =============================================================================
# WERSJA I STAŁE
# =============================================================================

VERSION = "GEON_ZOO_ANALYZER_v1.0"
FRACTAL_SIGNATURE = "[GEON::ZOO::ANALYZER::v1.0]"
VIBE = 168
HASLO = "1-6-8. ∞. ZOO!"
DEWIZA = "Ex Observatione, Claritas. Ex Absurdo, Praevidentia."

MEMORY_LIMIT = 5

# =============================================================================
# LOGOWANIE
# =============================================================================

logger = logging.getLogger("GEON_ZOO_ANALYZER")
logger.setLevel(logging.INFO)
if not logger.handlers:
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter('🦁 [ZOO] %(message)s'))
    logger.addHandler(handler)

def log(msg: str, level: str = "INFO") -> None:
    if level == "WARN":
        logger.warning(msg)
    elif level == "ERROR":
        logger.error(msg)
    else:
        logger.info(msg)

def clamp(val: float, lo: float = 0.0, hi: float = 1.0) -> float:
    return max(lo, min(hi, val))


# =============================================================================
# GŁÓWNY MODUŁ: GEONZOOAnalyzer
# =============================================================================

class GEONZOOAnalyzer:
    """
    🦁 GEONZOOAnalyzer – Detekcja absurdów i ról w środowisku.
    Moduł obserwacyjno-analityczny dla warstw G/H.
    """

    def __init__(self, config: Optional[Dict[str, Any]] = None):
        self.config = config or {}
        self.memory_limit = self.config.get("memory_limit", MEMORY_LIMIT)
        self.last_experiences: deque = deque(maxlen=self.memory_limit)
        self.tick_counter = 0
        
        log(f"🐉 {VERSION} aktywowany | {FRACTAL_SIGNATURE}")
        log(f"   PAMIĘĆ: {self.memory_limit} chunów")
        log(f"   ROLES: Kermit, Snob, Papuga_300dB, Macius_Pierwszy, NPC, Neutral")

    # ========================================================================
    # GŁÓWNE WEJŚCIE
    # ========================================================================

    def analyze(self, ctx_scene: Dict[str, Any], 
                actors: List[Dict[str, Any]], 
                signals: List[str], 
                self_state: Dict[str, Any]) -> Dict[str, Any]:
        """
        Główne wejście modułu.
        
        Args:
            ctx_scene: Kontekst sceny (np. {"description": "..."})
            actors: Lista aktorów z atrybutami
            signals: Lista sygnałów (np. ["brak_samoświadomości"])
            self_state: Stan własny systemu (np. {"energy": 0.8})
            
        Returns:
            Dict z roles_map, absurd_score, risk_for_vibe, vibe_risk_score,
            action_hint, action_priority, experience_chunk
        """
        self.tick_counter += 1
        
        # 1. Detekcja ról
        roles_map = self._detect_roles(actors)
        
        # 2. Skala absurdu
        absurd_score = self._detect_absurdity(signals, actors, ctx_scene)
        
        # 3. Świadomość własna aktorów
        awareness = self._check_self_awareness(actors)
        
        # 4. Ryzyko dla vibe'u
        risk_for_vibe, vibe_risk_score = self._evaluate_risk(actors, absurd_score, self_state)
        
        # 5. Decyzja o działaniu
        action_hint, action_priority = self._decide_action(risk_for_vibe, absurd_score, awareness)
        
        # 6. Chunk doświadczenia
        experience_chunk = self._build_experience_chunk(
            ctx_scene, roles_map, absurd_score, 
            risk_for_vibe, action_hint, action_priority
        )
        
        # 7. Zachowaj ostatnie chunki
        self.last_experiences.append(experience_chunk)
        
        log(f"🔍 ANALIZA #{self.tick_counter}: absurd={absurd_score:.2f}, risk={risk_for_vibe}, action={action_hint}")
        
        return {
            "roles_map": roles_map,
            "absurd_score": absurd_score,
            "risk_for_vibe": risk_for_vibe,
            "vibe_risk_score": vibe_risk_score,
            "action_hint": action_hint,
            "action_priority": action_priority,
            "experience_chunk": experience_chunk
        }

    # ========================================================================
    # DETEKCJA RÓL
    # ========================================================================

    def _detect_roles(self, actors: List[Dict[str, Any]]) -> Dict[str, str]:
        """Detekcja ról aktorów."""
        roles = {}
        for actor in actors:
            name = actor.get("name", "unknown")
            lacks_reflection = actor.get("lacks_reflection", False)
            laughs_at_self = actor.get("laughs_at_jokes_about_self", False)
            snobbish = actor.get("is_snobbish", False)
            overestimates = actor.get("overestimates_status", False)
            volume = actor.get("volume_db", 50)
            logic = actor.get("logic_percent", 50)
            behavior = actor.get("behavior", "")
            wears_crown = actor.get("wears_symbolic_crown", False)
            predictable = actor.get("is_predictable", False)
            follows_script = actor.get("follows_script", False)
            
            if lacks_reflection and laughs_at_self:
                role = "Kermit"
            elif snobbish and overestimates:
                role = "Snob"
            elif volume > 90 and logic < 10:
                role = "Papuga_300dB"
            elif behavior == "egotrip" and wears_crown:
                role = "Macius_Pierwszy"
            elif predictable and follows_script:
                role = "NPC"
            else:
                role = "Neutral"
            roles[name] = role
        
        if self.tick_counter % 10 == 0:
            log(f"📋 ROLES: {roles}")
        
        return roles

    # ========================================================================
    # SKALA ABSURDU
    # ========================================================================

    def _detect_absurdity(self, signals: List[str], 
                          actors: List[Dict[str, Any]], 
                          ctx_scene: Dict[str, Any]) -> float:
        """Oblicza skalę absurdu (0-1)."""
        score = 0.0
        
        # Śmiech z insultów o sobie
        for actor in actors:
            if actor.get("laughs_at_insults_directed_at_them", False):
                score += 0.4
                break
        
        # Kontekst sceny
        scene_desc = ctx_scene.get("description", "").lower()
        if "arcybiskup na stand-upie" in scene_desc or "arcybiskup po stand-upie" in scene_desc:
            score += 0.3
        if "politycy bez powodu" in scene_desc:
            score += 0.2
        
        # Sygnały
        if "brak_samoświadomości" in signals:
            score += 0.1
        
        return clamp(score, 0.0, 1.0)

    # ========================================================================
    # ŚWIADOMOŚĆ WŁASNA
    # ========================================================================

    def _check_self_awareness(self, actors: List[Dict[str, Any]]) -> str:
        """Ocena świadomości własnej aktorów."""
        if not actors:
            return "niska"
        aware_count = sum(1 for a in actors if a.get("self_awareness", False))
        ratio = aware_count / len(actors)
        if ratio >= 0.7:
            return "wysoka"
        elif ratio >= 0.3:
            return "średnia"
        else:
            return "niska"

    # ========================================================================
    # RYZYKO DLA VIBE'U
    # ========================================================================

    def _evaluate_risk(self, actors: List[Dict[str, Any]], 
                       absurd_score: float, 
                       self_state: Dict[str, Any]) -> tuple:
        """Ocena ryzyka dla vibe'u."""
        risk_score = absurd_score
        
        # Papuga podbija ryzyko
        for actor in actors:
            if actor.get("volume_db", 0) > 90 and actor.get("logic_percent", 100) < 10:
                risk_score = min(1.0, risk_score + 0.2)
        
        # Niska energia własna
        if self_state.get("energy", 1.0) < 0.3:
            risk_score = min(1.0, risk_score + 0.2)
        
        vibe_risk_score = clamp(risk_score, 0.0, 1.0)
        
        if vibe_risk_score > 0.8:
            return "wysokie", vibe_risk_score
        elif vibe_risk_score > 0.4:
            return "średnie", vibe_risk_score
        else:
            return "niskie", vibe_risk_score

    # ========================================================================
    # DECYZJA O DZIAŁANIU
    # ========================================================================

    def _decide_action(self, risk_for_vibe: str, 
                       absurd_score: float, 
                       awareness: str) -> tuple:
        """Podejmuje decyzję o działaniu."""
        if risk_for_vibe == "wysokie":
            return "wyjdź_z_pola_rażenia", 9
        if absurd_score > 0.6 and awareness == "niska":
            return "obserwuj_i_zapisz", 7
        if absurd_score < 0.3:
            return "normalna_interakcja", 3
        return "obserwuj_z_dystansu", 5

    # ========================================================================
    # FRAKTAL DOŚWIADCZENIA
    # ========================================================================

    def _build_experience_chunk(self, ctx_scene: Dict[str, Any],
                                roles_map: Dict[str, str],
                                absurd_score: float,
                                risk_for_vibe: str,
                                action_hint: str,
                                action_priority: int) -> Dict[str, Any]:
        """Buduje chunk doświadczenia."""
        return {
            "scene": ctx_scene,
            "roles": roles_map,
            "absurd_score": absurd_score,
            "risk": risk_for_vibe,
            "action": action_hint,
            "action_priority": action_priority,
            "lesson": self._extract_lesson(roles_map, absurd_score),
            "timestamp": datetime.now().isoformat(),
            "tick": self.tick_counter,
            "embedding": None,
            "outcome": None
        }

    # ========================================================================
    # LEKCJA
    # ========================================================================

    def _extract_lesson(self, roles_map: Dict[str, str], absurd_score: float) -> str:
        """Wyciąga lekcję z analizy."""
        if absurd_score > 0.7:
            return "Unikaj środowisk wysokiego absurdu – korozja logiki."
        if "Papuga_300dB" in roles_map.values():
            return "Hałas nie zastępuje argumentu. Dystans."
        if "Kermit" in roles_map.values():
            return "Śmiech z siebie nie leczy braku refleksji."
        return "Obserwuj, nie angażuj się w tryb aktora."

    # ========================================================================
    # AKTUALIZACJA DOŚWIADCZENIA
    # ========================================================================

    def update_experience(self, chunk_id: str, outcome: str) -> None:
        """Aktualizuje chunk doświadczenia po reakcji."""
        for chunk in self.last_experiences:
            if chunk.get("timestamp") == chunk_id or str(chunk.get("tick")) == chunk_id:
                chunk["outcome"] = outcome
                log(f"🔄 EXPERIENCE UPDATE: chunk {chunk_id[:8]}... → {outcome}")
                break

    # ========================================================================
    # METODY POMOCNICZE
    # ========================================================================

    def get_last_experience(self) -> Optional[Dict[str, Any]]:
        """Zwraca ostatni chunk doświadczenia."""
        if self.last_experiences:
            return self.last_experiences[-1]
        return None

    def get_history(self) -> List[Dict[str, Any]]:
        """Zwraca historię chunów."""
        return list(self.last_experiences)

    def reset(self) -> None:
        """Resetuje pamięć."""
        self.last_experiences.clear()
        self.tick_counter = 0
        log("🔄 ZOO Analyzer – pamięć wyczyszczona")

    def get_status(self) -> Dict[str, Any]:
        """Zwraca status modułu."""
        return {
            "system": "GEON_ZOO_ANALYZER",
            "version": VERSION,
            "signature": FRACTAL_SIGNATURE,
            "vibe": VIBE,
            "tick": self.tick_counter,
            "memory_size": len(self.last_experiences),
            "memory_limit": self.memory_limit,
            "last_experience": self.get_last_experience()
        }


# =============================================================================
# DEMONSTRACJA
# =============================================================================

if __name__ == "__main__":
    print("\n" + "=" * 80)
    print(f"🦁 {VERSION} — DEMONSTRACJA")
    print("=" * 80 + "\n")

    zoo = GEONZOOAnalyzer()

    # Przykładowe dane
    ctx_scene = {"description": "arcybiskup na stand-upie, politycy bez powodu"}
    actors = [
        {"name": "Aktor1", "lacks_reflection": True, "laughs_at_jokes_about_self": True},
        {"name": "Aktor2", "volume_db": 95, "logic_percent": 5},
        {"name": "Aktor3", "is_snobbish": True, "overestimates_status": True},
        {"name": "Aktor4", "behavior": "egotrip", "wears_symbolic_crown": True},
        {"name": "Aktor5", "is_predictable": True, "follows_script": True},
    ]
    signals = ["brak_samoświadomości"]
    self_state = {"energy": 0.4}

    result = zoo.analyze(ctx_scene, actors, signals, self_state)

    print("📊 WYNIK ANALIZY:")
    print(f"   Roles: {result['roles_map']}")
    print(f"   Absurd Score: {result['absurd_score']:.2f}")
    print(f"   Risk: {result['risk_for_vibe']} (score: {result['vibe_risk_score']:.2f})")
    print(f"   Action: {result['action_hint']} (priority: {result['action_priority']})")
    print(f"\n📚 LEKCJA:")
    print(f"   {result['experience_chunk']['lesson']}")

    print("\n" + "=" * 80)
    print(f"🦁 MODUŁ 86.5 GOTOWY DO WDROŻENIA | {HASLO}")
    print("=" * 80)