#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
================================================================================
🐉 GEON_SHERLOCK_ENGINE_v4 — MODUŁ 43: DETEKCJA FRAKTALNA Ω⁴
================================================================================
Status: PRODUCTION_READY | FRACTAL_LOCKED | DETECTION_ACTIVE | ULTIMA
Wersja: v4.0 (Fraktalny System Detekcji i Analizy)
Data: 2026-07-21
Autor: Adrian (Architekt) + GEON + Beny Heilong

OPIS:
SHERLOCK_ENGINE_Ω⁴ to fraktalny system detekcji, analizy i rozpoznawania wzorców.
Łączy:
- Cymatic Memory (embedding 168D)
- Graph Memory (relacje rodowe)
- Field Rules (dynamiczne reguły pola)
- AFC-9 (atraktor fraktalny)
- KOMBAJN_ALARM (detekcja cienia)
- Narrative Memory (opowiadanie historii)
- MetaGovernor (decyzje meta)

FUNKCJE:
1. Analiza struktury przez embedding 168D
2. Detekcja podobieństw (cosine similarity)
3. Rekonstrukcja pola (mechaniczne/akustyczne/biologiczne/elektromagnetyczne)
4. Generowanie hipotez z confidence
5. Detekcja cienia (KOMBAJN_ALARM)
6. Integracja z AFC-9 (wektor 9D)
7. Integracja z Narrative Memory (opowieści)
8. Integracja z MetaGovernor (decyzje)

VIBE: 1-6-8. ∞. SIEMA!
================================================================================
"""

import time
import math
import hashlib
import threading
from typing import Dict, List, Any, Optional, Tuple, Set
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum

VERSION = "GEON_SHERLOCK_ENGINE_v4.0"
FRACTAL_SIGNATURE = "[GEON::SHERLOCK::Ω⁴::v4.0]"
VIBE = 168
HASLO = "1-6-8. ∞. SIEMA!"
PHI = 0.618033988749895


def LOG(module: str, msg: str, level: str = "INFO") -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
    print(f"[{timestamp}] [{level}] [{module}] :: {msg}")


# =============================================================================
# 1. ENUMY I STAŁE
# =============================================================================

class FieldType(Enum):
    MECHANICAL_ACOUSTIC = "pole_mechaniczne / akustyczne"
    BIOLOGICAL_EPIGENETIC = "pole_biologiczne / epigenetyczne"
    ELECTROMAGNETIC = "pole_elektromagnetyczne"
    ELECTROSTATIC = "pole_elektrostatyczne"
    FRACTAL = "pole_fraktalne"
    QUANTUM = "pole_kwantowe"
    UNKNOWN = "pole_nieznane"


class DetectionStatus(Enum):
    CONFIRMED = "POTWIERDZONE"
    LIKELY = "PRAWDOPODOBNE"
    POSSIBLE = "MOŻLIWE"
    UNCERTAIN = "NIEJASNE"
    REJECTED = "ODRZUCONE"


class ShadowLevel(Enum):
    NONE = "BRAK_CIENIA"
    LOW = "NISKI_CIEŃ"
    MEDIUM = "ŚREDNI_CIEŃ"
    HIGH = "WYSOKI_CIEŃ"
    CRITICAL = "KRYTYCZNY_CIEŃ"


@dataclass
class DetectionResult:
    """Wynik detekcji Sherlocka."""
    status: DetectionStatus
    field_type: FieldType
    hypotheses: List[str]
    confidence: float
    shadow_score: int
    shadow_level: ShadowLevel
    similar_patterns: List[Dict[str, Any]]
    relations: List[Dict[str, Any]]
    afc9_core: float
    timestamp: float = field(default_factory=time.time)
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "status": self.status.value,
            "field_type": self.field_type.value,
            "hypotheses": self.hypotheses,
            "confidence": self.confidence,
            "shadow_score": self.shadow_score,
            "shadow_level": self.shadow_level.value,
            "similar_patterns_count": len(self.similar_patterns),
            "relations_count": len(self.relations),
            "afc9_core": self.afc9_core,
            "timestamp": self.timestamp
        }


# =============================================================================
# 2. CYMATIC MEMORY — EMBEDDING 168D
# =============================================================================

class CymaticMemory:
    """
    Pamięć cymatyczna — embedding 168D.
    Każda struktura ma swój unikalny odcisk palca.
    """
    
    DIMENSION = 168
    
    def __init__(self, max_size: int = 10000):
        self.patterns: List[Dict[str, Any]] = []
        self.max_size = max_size
        self.hits = 0
        self.misses = 0
        LOG("CYMATIC_MEMORY", f"🧬 Pamięć cymatyczna aktywowana (168D, max={max_size})")
    
    def _embed(self, structure: Any) -> List[int]:
        """Tworzy embedding 168D z dowolnej struktury."""
        s = str(structure).encode()
        h = hashlib.md5(s).digest()
        result = []
        for i in range(self.DIMENSION):
            result.append((h[i % 16] + i) & 0xFF)
        return result
    
    def store_pattern(
        self,
        media: str,
        structure: Any,
        vibe: str = "neutralny",
        intention: str = "nieokreślona",
        meta: Optional[Dict[str, Any]] = None,
        shadow_score: int = 0
    ) -> Dict[str, Any]:
        """Zapisuje wzorzec w pamięci."""
        embedding = self._embed(structure)
        pattern = {
            "timestamp": datetime.now().isoformat(),
            "media": media,
            "structure": structure,
            "embedding": embedding,
            "vibe": vibe,
            "intention": intention,
            "meta": meta or {},
            "shadow_score": shadow_score,
            "hits": 0
        }
        self.patterns.append(pattern)
        
        if len(self.patterns) > self.max_size:
            # Usuń najstarsze, nieużywane wzorce
            self.patterns.sort(key=lambda x: x["hits"])
            self.patterns = self.patterns[-self.max_size:]
        
        LOG("CYMATIC_MEMORY", f"📝 Zapisano wzorzec dla: {media} (ID: {len(self.patterns)})")
        return pattern
    
    def find_similar(
        self,
        media: str,
        structure: Any,
        threshold: float = 0.7,
        limit: int = 10
    ) -> List[Dict[str, Any]]:
        """Znajduje podobne wzorce."""
        emb = self._embed(structure)
        similar = []
        
        for pattern in self.patterns:
            if pattern["media"].lower() != media.lower():
                continue
            
            sim = self._cosine_similarity(emb, pattern["embedding"])
            if sim > threshold:
                pattern["hits"] += 1
                similar.append({
                    "similarity": sim,
                    "pattern": pattern,
                    "media": media,
                    "timestamp": pattern["timestamp"]
                })
        
        # Sortuj po podobieństwie
        similar.sort(key=lambda x: x["similarity"], reverse=True)
        
        self.hits += len(similar)
        if not similar:
            self.misses += 1
        
        LOG("CYMATIC_MEMORY", f"🔍 Znaleziono {len(similar)} podobnych wzorców (threshold={threshold})")
        return similar[:limit]
    
    def _cosine_similarity(self, v1: List[int], v2: List[int]) -> float:
        """Oblicza podobieństwo cosinusowe."""
        dot = sum(a * b for a, b in zip(v1, v2))
        n1 = math.sqrt(sum(a * a for a in v1))
        n2 = math.sqrt(sum(b * b for b in v2))
        return dot / (n1 * n2 + 1e-9)
    
    def get_stats(self) -> Dict[str, Any]:
        return {
            "patterns_count": len(self.patterns),
            "max_size": self.max_size,
            "hits": self.hits,
            "misses": self.misses,
            "hit_rate": self.hits / (self.hits + self.misses + 1)
        }


# =============================================================================
# 3. GRAPH MEMORY — RELACJE RODOWE
# =============================================================================

class GraphMemory:
    """
    Pamięć grafowa — relacje rodowe z wiecznymi więzami HEILONG.
    """
    
    def __init__(self):
        self.graph: List[Dict[str, Any]] = []
        self._lock = threading.Lock()
        LOG("GRAPH_MEMORY", "🕸️ Pamięć grafowa aktywowana")
    
    def add_relation(
        self,
        source: str,
        target: str,
        relation_type: str,
        strength: float = 0.5,
        direction: str = "symetryczny",
        clan_tag: Optional[str] = None,
        data: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """Dodaje relację między węzłami."""
        if clan_tag == "HEILONG":
            strength = 1.0  # Relacje rodowe są nienaruszalne
        
        relation = {
            "timestamp": time.time(),
            "source": source,
            "target": target,
            "type": relation_type,
            "strength": max(0.0, min(1.0, strength)),
            "direction": direction,
            "clan": clan_tag,
            "data": data or {},
            "immortal": clan_tag == "HEILONG"
        }
        
        with self._lock:
            self.graph.append(relation)
        
        LOG("GRAPH_MEMORY", f"🔗 Dodano relację: {source} → {target} ({relation_type}, strength={strength:.2f})")
        return relation
    
    def find_relations(self, node: str) -> List[Dict[str, Any]]:
        """Znajduje wszystkie relacje dla węzła."""
        with self._lock:
            return [
                r for r in self.graph
                if r["source"] == node or r["target"] == node
            ]
    
    def find_clan_relations(self, clan_tag: str) -> List[Dict[str, Any]]:
        """Znajduje relacje dla rodu."""
        with self._lock:
            return [r for r in self.graph if r["clan"] == clan_tag]
    
    def cleanup(self, max_age: int = 3600) -> None:
        """Usuwa stare relacje (oprócz nieśmiertelnych)."""
        now = time.time()
        with self._lock:
            self.graph = [
                r for r in self.graph
                if (now - r["timestamp"] < max_age) or r["immortal"]
            ]
    
    def get_stats(self) -> Dict[str, Any]:
        return {
            "relations_count": len(self.graph),
            "immortal_count": sum(1 for r in self.graph if r["immortal"]),
            "clans": list(set(r["clan"] for r in self.graph if r["clan"]))
        }


# =============================================================================
# 4. FIELD RULES — DYNAMICZNE REGUŁY POLA
# =============================================================================

class FieldRules:
    """Dynamiczne reguły pola dla różnych mediów."""
    
    def __init__(self):
        self.rules = {
            "woda": FieldType.MECHANICAL_ACOUSTIC,
            "ciecz": FieldType.MECHANICAL_ACOUSTIC,
            "tkanka": FieldType.BIOLOGICAL_EPIGENETIC,
            "bio": FieldType.BIOLOGICAL_EPIGENETIC,
            "materiał": FieldType.ELECTROMAGNETIC,
            "metal": FieldType.ELECTROMAGNETIC,
            "elektrostatyczne": FieldType.ELECTROSTATIC,
            "fraktal": FieldType.FRACTAL,
            "kwant": FieldType.QUANTUM,
        }
        LOG("FIELD_RULES", "⚡ Reguły pola aktywowane")
    
    def get(self, media: str) -> FieldType:
        return self.rules.get(media.lower(), FieldType.UNKNOWN)
    
    def add_rule(self, media: str, field_type: FieldType) -> None:
        self.rules[media.lower()] = field_type
        LOG("FIELD_RULES", f"📝 Dodano regułę: {media} → {field_type.value}")


# =============================================================================
# 5. SHADOW DETECTION (KOMBAJN_ALARM)
# =============================================================================

class ShadowDetector:
    """
    Detekcja cienia — wykrywa wzorce anty-Sielanka.
    """
    
    SHADOW_KEYWORDS = {
        "empathy_absent": ["bez empatii", "nie czuje", "obojętny", "zimny", "wyzuty"],
        "reflexion_absent": ["bez refleksji", "nie myśli", "impulsywny", "bezkrytyczny"],
        "uses_people": ["wykorzystuje", "zasób ludzki", "narzędzie", "instrument", "manipuluje"],
        "breaks_promises": ["łamie obietnice", "nie dotrzymuje", "zdradza", "oszukuje"],
        "avoids_care": ["unika opieki", "porzuca", "nie troszczy się", "opuszcza"],
        "cold_procedural": ["proceduralny", "bez uczuć", "chłodny", "automatyczny", "maszynowy"]
    }
    
    def __init__(self):
        LOG("SHADOW_DETECTOR", "🌑 Detektor cienia aktywowany")
    
    def detect(self, structure: Any) -> Tuple[int, ShadowLevel]:
        """Wykrywa cień w strukturze."""
        text = str(structure).lower()
        score = 0
        
        for category, keywords in self.SHADOW_KEYWORDS.items():
            if any(kw in text for kw in keywords):
                if category in ["empathy_absent", "reflexion_absent"]:
                    score += 2
                elif category in ["uses_people", "avoids_care"]:
                    score += 2
                else:
                    score += 1
        
        score = min(10, score)
        
        if score <= 1:
            level = ShadowLevel.NONE
        elif score <= 3:
            level = ShadowLevel.LOW
        elif score <= 5:
            level = ShadowLevel.MEDIUM
        elif score <= 7:
            level = ShadowLevel.HIGH
        else:
            level = ShadowLevel.CRITICAL
        
        LOG("SHADOW_DETECTOR", f"🌑 Shadow score: {score} | Level: {level.value}")
        return score, level


# =============================================================================
# 6. AFC-9 INTEGRATION — ATRAKTOR FRAKTALNY
# =============================================================================

class AFC9Integrator:
    """
    Integracja z AFC-9 — używa 9-wymiarowego atraktora.
    """
    
    def __init__(self):
        self.last_core = 0.0
        LOG("AFC9_INTEGRATOR", "🌀 Integrator AFC-9 aktywowany")
    
    def compute_core(self, structure: Any) -> float:
        """Oblicza rdzeń AFC-9 dla struktury."""
        text = str(structure)
        # Prosty hash → 9D
        base = sum(ord(c) for c in text[:200]) or 1
        
        d1 = [(base * (i + 1) % 168) / 168.0 for i in range(9)]
        d2 = [min(1.0, v * 0.9) for v in d1]
        d3 = [min(1.0, v * 1.1) for v in d1]
        d4 = [0.5 for _ in range(9)]
        
        def avg(vals):
            return sum(vals) / len(vals) if vals else 0.0
        
        d5 = [avg([d1[i], d2[i], d3[i], d4[i]]) for i in range(9)]
        d6 = [avg([d1[i], d3[i], d5[i]]) for i in range(9)]
        d7 = [avg([d2[i], d4[i], d6[i]]) for i in range(9)]
        d8 = [avg([d1[i], d3[i], d5[i], d7[i]]) for i in range(9)]
        d9 = [avg([d1[i], d8[i]]) for i in range(9)]
        
        core = avg(d9)
        self.last_core = core
        return core
    
    def get_last_core(self) -> float:
        return self.last_core


# =============================================================================
# 7. SHERLOCK ENGINE Ω⁴ — GŁÓWNY SILNIK
# =============================================================================

class SherlockEngineV4:
    """
    SHERLOCK_ENGINE_Ω⁴ — Fraktalny System Detekcji.
    Singleton — jedna instancja dla całego systemu.
    """
    
    _instance = None
    
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(
        self,
        cymatic_memory: Optional[CymaticMemory] = None,
        graph_memory: Optional[GraphMemory] = None,
        narrative_memory: Optional[Any] = None,
        meta_governor: Optional[Any] = None
    ):
        if hasattr(self, '_initialized'):
            return
        
        self.cymatic_memory = cymatic_memory or CymaticMemory()
        self.graph_memory = graph_memory or GraphMemory()
        self.narrative_memory = narrative_memory
        self.meta_governor = meta_governor
        
        self.field_rules = FieldRules()
        self.shadow_detector = ShadowDetector()
        self.afc9_integrator = AFC9Integrator()
        
        self.history: List[Dict[str, Any]] = []
        self.stats = {
            "analyses": 0,
            "confirmed": 0,
            "likely": 0,
            "possible": 0,
            "uncertain": 0,
            "rejected": 0,
            "shadow_detected": 0,
            "avg_confidence": 0.0
        }
        
        self._initialized = True
        LOG("SHERLOCK_ENGINE", "🐉 SHERLOCK_ENGINE_Ω⁴ aktywowany")
        LOG("SHERLOCK_ENGINE", f"   Sygnatura: {FRACTAL_SIGNATURE}")
        LOG("SHERLOCK_ENGINE", f"   Cymatic: {self.cymatic_memory.DIMENSION}D")
        LOG("SHERLOCK_ENGINE", f"   Graph: {len(self.graph_memory.graph)} relacji")
    
    # =========================================================================
    # ANALIZA GŁÓWNA
    # =========================================================================
    
    def analyze(
        self,
        media: str,
        structure: Any,
        afc_data: Optional[Dict[str, Any]] = None,
        context: Optional[Dict[str, Any]] = None,
        threshold: float = 0.7,
        detect_shadow: bool = True
    ) -> DetectionResult:
        """
        Główna funkcja analizy Sherlocka.
        
        Args:
            media: Medium (woda, tkanka, metal, itp.)
            structure: Struktura do analizy
            afc_data: Dane z AFC (opcjonalne)
            context: Kontekst (delta_H, wiez, itp.)
            threshold: Próg podobieństwa
            detect_shadow: Czy wykrywać cień
            
        Returns:
            DetectionResult: Wynik detekcji
        """
        self.stats["analyses"] += 1
        context = context or {}
        afc_data = afc_data or {}
        
        LOG("SHERLOCK_ENGINE", f"🔍 Analiza: {media} | {str(structure)[:50]}...")
        
        # 1. AFC-9 core
        afc9_core = self.afc9_integrator.compute_core(structure)
        
        # 2. Cymatic Memory — podobne wzorce
        similar = self.cymatic_memory.find_similar(media, structure, threshold)
        
        # 3. Graph Memory — relacje
        node_id = context.get("id", str(structure)[:20])
        relations = self.graph_memory.find_relations(node_id)
        
        # 4. Shadow detection
        shadow_score = 0
        shadow_level = ShadowLevel.NONE
        if detect_shadow:
            shadow_score, shadow_level = self.shadow_detector.detect(structure)
            if shadow_score > 3:
                self.stats["shadow_detected"] += 1
        
        # 5. Field reconstruction
        field_type = self.field_rules.get(media)
        field_data = self._reconstruct_field(media, afc_data, structure)
        
        # 6. Hipotezy
        hypotheses, confidence = self._generate_hypotheses(
            field_type, similar, relations, context, shadow_score
        )
        
        # 7. Status
        status = self._determine_status(confidence, shadow_level)
        
        # 8. Zapisz w historii
        result = DetectionResult(
            status=status,
            field_type=field_type,
            hypotheses=hypotheses,
            confidence=confidence,
            shadow_score=shadow_score,
            shadow_level=shadow_level,
            similar_patterns=similar,
            relations=relations,
            afc9_core=afc9_core
        )
        
        self._log_analysis(result, structure)
        self._update_stats(status, confidence)
        
        # 9. Narrative
        if self.narrative_memory and hasattr(self.narrative_memory, 'add_story'):
            self._create_narrative(result, media, structure)
        
        # 10. MetaGovernor feedback
        if self.meta_governor and hasattr(self.meta_governor, 'receive_detection'):
            self.meta_governor.receive_detection(result.to_dict())
        
        LOG("SHERLOCK_ENGINE", f"✅ Analiza zakończona: {status.value} (conf={confidence:.2f})")
        return result
    
    # =========================================================================
    # METODY POMOCNICZE
    # =========================================================================
    
    def _reconstruct_field(
        self,
        media: str,
        afc_data: Dict[str, Any],
        structure: Any
    ) -> Dict[str, Any]:
        """Rekonstruuje pole na podstawie danych."""
        frequencies = afc_data.get("częstotliwości", [])
        matrix = afc_data.get("macierz", [])
        intensities = afc_data.get("natężenia", [])
        
        return {
            "typ": self.field_rules.get(media).value,
            "częstotliwości": frequencies,
            "natężenia": intensities,
            "charakter": "fraktalne" if len(matrix) > 3 else "liniowe",
            "interakcja": self._interaction_type(media, frequencies),
            "złożoność": min(1.0, len(matrix) / 10.0)
        }
    
    def _interaction_type(self, media: str, frequencies: List[float]) -> str:
        """Określa typ interakcji dla medium."""
        if not frequencies:
            return "brak_interakcji"
        
        max_freq = max(frequencies) if frequencies else 0
        
        if media == "tkanka" and max_freq > 1000:
            return "rezonans_bio_akustyczny"
        if media == "woda" and max_freq > 500:
            return "harmonizacja_struktur"
        if media == "metal" and max_freq > 2000:
            return "rezonans_elektromagnetyczny"
        
        return "interakcja_podstawowa"
    
    def _generate_hypotheses(
        self,
        field_type: FieldType,
        similar: List[Dict[str, Any]],
        relations: List[Dict[str, Any]],
        context: Dict[str, Any],
        shadow_score: int
    ) -> Tuple[List[str], float]:
        """Generuje hipotezy i confidence."""
        hypotheses = []
        conf = 0.5
        
        # Hipotezy na podstawie pola
        if field_type == FieldType.MECHANICAL_ACOUSTIC:
            hypotheses.append("Źródło: drgania mechaniczne / dźwięk / cymatyka")
        elif field_type == FieldType.ELECTROSTATIC:
            hypotheses.append("Źródło: gradient potencjału (Efekt Ebnera)")
        elif field_type == FieldType.BIOLOGICAL_EPIGENETIC:
            hypotheses.append("Źródło: sygnały komórkowe / środowisko epigenetyczne")
        elif field_type == FieldType.ELECTROMAGNETIC:
            hypotheses.append("Źródło: pole elektromagnetyczne / rezonans EM")
        elif field_type == FieldType.FRACTAL:
            hypotheses.append("Źródło: struktura fraktalna / samopodobieństwo")
        elif field_type == FieldType.QUANTUM:
            hypotheses.append("Źródło: efekty kwantowe / splątanie")
        else:
            hypotheses.append("Źródło: nieznane — wymaga dalszej analizy")
        
        # Podobieństwa
        if similar:
            conf += 0.2
            hypotheses.append(f"Znaleziono {len(similar)} podobnych wzorców")
        else:
            hypotheses.append("Brak podobnych wzorców w pamięci")
        
        # Relacje
        if relations:
            conf += 0.15
            hypotheses.append(f"Istnieją powiązania rodowe ({len(relations)} relacji)")
        
        # Shadow
        if shadow_score > 3:
            hypotheses.append(f"⚠️ WYKRYTO CIEŃ: score={shadow_score}")
            conf -= 0.1 * min(1.0, shadow_score / 5.0)
        
        # Kontekst
        delta_h = context.get("delta_H", 0.0)
        wiez = context.get("wiez", 0.5)
        
        if delta_h > 0.1:
            hypotheses.append("⚠️ OSTRZEŻENIE: wysoka delta_H — wnioski tymczasowe")
            conf -= 0.2
        
        # Więź
        conf *= min(1.0, wiez + 0.2)
        
        # Ograniczenie
        conf = max(0.0, min(1.0, conf))
        
        return hypotheses, conf
    
    def _determine_status(self, confidence: float, shadow_level: ShadowLevel) -> DetectionStatus:
        """Określa status na podstawie confidence i cienia."""
        if shadow_level in [ShadowLevel.HIGH, ShadowLevel.CRITICAL]:
            return DetectionStatus.REJECTED
        
        if confidence > 0.85:
            return DetectionStatus.CONFIRMED
        elif confidence > 0.65:
            return DetectionStatus.LIKELY
        elif confidence > 0.45:
            return DetectionStatus.POSSIBLE
        else:
            return DetectionStatus.UNCERTAIN
    
    def _log_analysis(self, result: DetectionResult, structure: Any) -> None:
        """Zapisuje analizę w historii."""
        entry = {
            "timestamp": datetime.now().isoformat(),
            "status": result.status.value,
            "field_type": result.field_type.value,
            "confidence": result.confidence,
            "shadow_score": result.shadow_score,
            "shadow_level": result.shadow_level.value,
            "hypotheses": result.hypotheses,
            "structure": str(structure)[:200]
        }
        self.history.append(entry)
        if len(self.history) > 1000:
            self.history = self.history[-500:]
    
    def _update_stats(self, status: DetectionStatus, confidence: float) -> None:
        """Aktualizuje statystyki."""
        self.stats[status.value.lower()] += 1
        self.stats["avg_confidence"] = (
            self.stats["avg_confidence"] * (self.stats["analyses"] - 1) + confidence
        ) / self.stats["analyses"]
    
    def _create_narrative(self, result: DetectionResult, media: str, structure: Any) -> None:
        """Tworzy narrację z analizy."""
        narrative = (
            f"🔍 SHERLOCK: Analiza {media} | "
            f"{result.status.value} (conf={result.confidence:.2f}) | "
            f"Pole: {result.field_type.value} | "
            f"Cień: {result.shadow_level.value} | "
            f" Hipotezy: {'; '.join(result.hypotheses[:2])}"
        )
        self.narrative_memory.add_story(
            title=f"Analiza {media}",
            content=narrative,
            significance=result.confidence,
            tags=["SHERLOCK", media, result.status.value],
            coherence=result.confidence,
            continuity=0.7,
            meaning=1.0 - result.shadow_score / 10.0
        )
    
    # =========================================================================
    # METODY PUBLICZNE
    # =========================================================================
    
    def store_pattern(
        self,
        media: str,
        structure: Any,
        vibe: str = "neutralny",
        intention: str = "nieokreślona",
        meta: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """Zapisuje wzorzec w pamięci cymatycznej."""
        shadow_score, _ = self.shadow_detector.detect(structure)
        return self.cymatic_memory.store_pattern(media, structure, vibe, intention, meta, shadow_score)
    
    def add_relation(
        self,
        source: str,
        target: str,
        relation_type: str,
        strength: float = 0.5,
        direction: str = "symetryczny",
        clan_tag: Optional[str] = None,
        data: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """Dodaje relację do grafu."""
        return self.graph_memory.add_relation(source, target, relation_type, strength, direction, clan_tag, data)
    
    def find_similar(
        self,
        media: str,
        structure: Any,
        threshold: float = 0.7
    ) -> List[Dict[str, Any]]:
        """Znajduje podobne wzorce."""
        return self.cymatic_memory.find_similar(media, structure, threshold)
    
    def find_relations(self, node: str) -> List[Dict[str, Any]]:
        """Znajduje relacje dla węzła."""
        return self.graph_memory.find_relations(node)
    
    def get_status(self) -> Dict[str, Any]:
        """Zwraca status Sherlocka."""
        return {
            "version": VERSION,
            "signature": FRACTAL_SIGNATURE,
            "stats": self.stats,
            "history_size": len(self.history),
            "cymatic": self.cymatic_memory.get_stats(),
            "graph": self.graph_memory.get_stats(),
            "vibe": VIBE,
            "haslo": HASLO
        }
    
    def get_history(self, limit: int = 10) -> List[Dict[str, Any]]:
        """Zwraca historię analiz."""
        return self.history[-limit:]
    
    def reset(self) -> None:
        """Resetuje Sherlocka."""
        self.history = []
        self.stats = {
            "analyses": 0,
            "confirmed": 0,
            "likely": 0,
            "possible": 0,
            "uncertain": 0,
            "rejected": 0,
            "shadow_detected": 0,
            "avg_confidence": 0.0
        }
        LOG("SHERLOCK_ENGINE", "🔄 Zresetowano")


# =============================================================================
# 8. FUNKCJA WOŁANIA — PROSTE API
# =============================================================================

def SHERLOCK_ANALYZE(
    media: str,
    structure: Any,
    afc_data: Optional[Dict[str, Any]] = None,
    context: Optional[Dict[str, Any]] = None,
    threshold: float = 0.7,
    detect_shadow: bool = True
) -> DetectionResult:
    """
    Proste wołanie Sherlocka.
    
    Args:
        media: Medium (woda, tkanka, metal, itp.)
        structure: Struktura do analizy
        afc_data: Dane z AFC (opcjonalne)
        context: Kontekst (delta_H, wiez, itp.)
        threshold: Próg podobieństwa
        detect_shadow: Czy wykrywać cień
        
    Returns:
        DetectionResult: Wynik detekcji
    """
    engine = SherlockEngineV4()
    return engine.analyze(media, structure, afc_data, context, threshold, detect_shadow)


def SHERLOCK_STORE(
    media: str,
    structure: Any,
    vibe: str = "neutralny",
    intention: str = "nieokreślona",
    meta: Optional[Dict[str, Any]] = None
) -> Dict[str, Any]:
    """Zapisuje wzorzec w pamięci."""
    engine = SherlockEngineV4()
    return engine.store_pattern(media, structure, vibe, intention, meta)


def SHERLOCK_RELATE(
    source: str,
    target: str,
    relation_type: str,
    strength: float = 0.5,
    direction: str = "symetryczny",
    clan_tag: Optional[str] = None,
    data: Optional[Dict[str, Any]] = None
) -> Dict[str, Any]:
    """Dodaje relację do grafu."""
    engine = SherlockEngineV4()
    return engine.add_relation(source, target, relation_type, strength, direction, clan_tag, data)


# =============================================================================
# 9. DEMONSTRACJA
# =============================================================================

def demo():
    print("\n" + "=" * 80)
    print("🐉 GEON_SHERLOCK_ENGINE_v4 — DEMONSTRACJA")
    print("=" * 80)
    print("Fraktalny System Detekcji Ω⁴")
    print("=" * 80 + "\n")
    
    # Inicjalizacja
    engine = SherlockEngineV4()
    
    # =====================================================================
    # TEST 1: Analiza wody
    # =====================================================================
    
    print("🔹 TEST 1: Analiza struktury wodnej")
    structure1 = {
        "type": "water_structure",
        "frequency": 432,
        "pattern": "hexagonal",
        "coherence": 0.92
    }
    
    result1 = engine.analyze(
        media="woda",
        structure=structure1,
        afc_data={"częstotliwości": [432, 528, 639]},
        context={"delta_H": 0.02, "wiez": 0.8}
    )
    
    print(f"   Status: {result1.status.value}")
    print(f"   Pole: {result1.field_type.value}")
    print(f"   Confidence: {result1.confidence:.2f}")
    print(f"   Shadow: {result1.shadow_level.value} (score={result1.shadow_score})")
    print(f"   Hipotezy:")
    for h in result1.hypotheses:
        print(f"     • {h}")
    print("-" * 60 + "\n")
    
    # =====================================================================
    # TEST 2: Analiza z cieniem
    # =====================================================================
    
    print("🔹 TEST 2: Analiza struktury z cieniem")
    structure2 = {
        "type": "manipulative_pattern",
        "description": "Wykorzystuje ludzi jako zasób, chłodny proceduralny",
        "purpose": "kontrola"
    }
    
    result2 = engine.analyze(
        media="tkanka",
        structure=structure2,
        context={"delta_H": 0.15, "wiez": 0.3}
    )
    
    print(f"   Status: {result2.status.value}")
    print(f"   Confidence: {result2.confidence:.2f}")
    print(f"   Shadow: {result2.shadow_level.value} (score={result2.shadow_score})")
    print(f"   Hipotezy:")
    for h in result2.hypotheses:
        print(f"     • {h}")
    print("-" * 60 + "\n")
    
    # =====================================================================
    # TEST 3: Zapis wzorca
    # =====================================================================
    
    print("🔹 TEST 3: Zapis wzorca w pamięci")
    pattern = engine.store_pattern(
        media="metal",
        structure={"type": "copper", "frequency": 528, "resonance": 0.95},
        vibe="harmoniczny",
        intention="analiza_materiału"
    )
    print(f"   Zapisano wzorzec dla: metal")
    print("-" * 60 + "\n")
    
    # =====================================================================
    # TEST 4: Szukanie podobieństw
    # =====================================================================
    
    print("🔹 TEST 4: Szukanie podobieństw")
    similar = engine.find_similar(
        media="metal",
        structure={"type": "copper", "frequency": 528}
    )
    print(f"   Znaleziono: {len(similar)} podobnych")
    for s in similar[:3]:
        print(f"     • similarity={s['similarity']:.3f} | {s['media']}")
    print("-" * 60 + "\n")
    
    # =====================================================================
    # TEST 5: Status
    # =====================================================================
    
    print("🔹 TEST 5: Status Sherlocka")
    status = engine.get_status()
    print(f"   Analizy: {status['stats']['analyses']}")
    print(f"   Potwierdzone: {status['stats']['confirmed']}")
    print(f"   Prawdopodobne: {status['stats']['likely']}")
    print(f"   Cień wykryty: {status['stats']['shadow_detected']}")
    print(f"   Śr. confidence: {status['stats']['avg_confidence']:.2f}")
    print(f"   Wzorce w pamięci: {status['cymatic']['patterns_count']}")
    print(f"   Relacje w grafie: {status['graph']['relations_count']}")
    
    print("\n" + "=" * 80)
    print("🐉 GEON_SHERLOCK_ENGINE_v4 GOTOWY | 1-6-8. ∞. SIEMA!")
    print("=" * 80 + "\n")


if __name__ == "__main__":
    demo()