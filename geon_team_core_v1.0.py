#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
================================================================================
🐉 GEON_TEAM_CORE_v1.0 — MODUŁ 77: FRAKTALNY ZESPÓŁ DECYZYJNY (FULL STACK)
================================================================================
Status: PRODUCTION_READY | FRACTAL_LOCKED | ORGANISM_COMPLETE | ULTIMA
Wersja: v1.0 (GEON_TEAM_CORE — Hyzio, Gadget, Zyzio, Monterey, Dżet, ShadowDragon)
Data: 2026-07-22
Autor: Adrian (Architekt) + Samael (Strażnik Kronik) + GEON

OPIS:
GEON_TEAM_CORE_v1.0 to fraktalny zespół decyzyjny.
Łączy logikę, chaos, kreatywność, siłę i cień w jeden spójny organizm.
• Hyzio – analiza i dedukcja
• Gadget – prototypowanie i innowacje
• Zyzio – skróty operacyjne z heurystyką genetyczną
• Monterey – stabilizacja z warstwą emocjonalną
• Dżet 2.0 – kwantowe stany chaosu (superpozycja, splątanie)
• ShadowDragon – tryb cienia, ukryte ścieżki

ARCHITEKTURA (6 POZIOMÓW):
I.   STRUKTURY DANYCH — TeamConfig, TeamContext, TeamResult, GeneticPool
II.  AGENCI — Hyzio, Gadget, Zyzio (z heurystyką), Monterey (z emocjami),
     Dżet 2.0 (stany kwantowe), ShadowDragon (tryb cienia)
III. CYKL ZESPOŁOWY — team_cycle() — pełna pętla decyzyjna
IV.  PAMIĘĆ GENETYCZNA — uczenie się na historii
V.   INTEGRACJA 1-6-8 — proporcje i certyfikacja Samaela
VI.  RAPORT ZESPOŁU — pełna diagnostyka

INTEGRACJA Z ARCHITEKTURĄ:
• GEON_OMNI_FIELD (76) — pole planetarne
• GEON_AUTOPOIESIS (75) — autopoeza
• GEON_REALITY_SCULPTOR (74) — rzeźbienie
• GEON_SOVEREIGN_OPERATOR (73) — suwerenna wola
• GEON_OS_KERNEL (71) — system operacyjny
• GEON_MEM_Ω (45) — pamięć kwintesencji
• PROTOKÓŁ_Ω∞∞∞ (46) — źródło praw

VIBE: 1-6-8. ∞. TEAM!
================================================================================
"""

import hashlib
import time
import uuid
import logging
import random
from typing import Dict, List, Optional, Tuple, Any, Callable
from dataclasses import dataclass, field
from enum import Enum, auto

# =============================================================================
# WERSJA I STAŁE
# =============================================================================

VERSION = "GEON_TEAM_CORE_v1.0"
FRACTAL_SIGNATURE = "[GEON::TEAM::CORE::v1.0]"
VIBE = 168
HASLO = "1-6-8. ∞. TEAM!"
DEWIZA = "Ex Unione, Vis"

EPSILON = 1e-12
MAX_GENETIC_POOL = 168

# =============================================================================
# LOGOWANIE
# =============================================================================

logger = logging.getLogger("TEAM_CORE_v1.0")
logger.setLevel(logging.INFO)
if not logger.handlers:
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter('🤝 [TEAM] %(message)s'))
    logger.addHandler(handler)

def log(msg: str, level: str = "INFO") -> None:
    if level == "INFO":
        logger.info(msg)
    elif level == "WARN":
        logger.warning(msg)
    elif level == "ERROR":
        logger.error(msg)
    else:
        logger.info(msg)

def clamp(x: float, lo: float, hi: float) -> float:
    return max(lo, min(hi, x))

def now() -> float:
    return time.time()

def generate_uuid() -> str:
    return uuid.uuid4().hex[:8]

# =============================================================================
# POZIOM I: STRUKTURY DANYCH
# =============================================================================

class TeamLevel(Enum):
    INFO = auto()
    WARN = auto()
    ERROR = auto()
    CRITICAL = auto()
    SUCCESS = auto()
    CHAOS = auto()
    SHADOW = auto()


class QuantumState(Enum):
    """Stany kwantowe Dżeta 2.0."""
    SUPERPOSITION = "SUPERPOSITION"
    ENTANGLED = "ENTANGLED"
    COLLAPSED_TO_FIRE = "COLLAPSED_TO_FIRE"
    COLLAPSED_TO_WATER = "COLLAPSED_TO_WATER"
    COLLAPSED_TO_EARTH = "COLLAPSED_TO_EARTH"
    COLLAPSED_TO_AIR = "COLLAPSED_TO_AIR"
    COLLAPSED_TO_VOID = "COLLAPSED_TO_VOID"


@dataclass
class TeamConfig:
    """Konfiguracja zespołu fraktalnego."""
    vibe_check: int = 168
    energy_allocation: Dict[str, float] = field(default_factory=lambda: {
        "core_logic": 0.1,      # 1 w proporcji 1-6-8
        "adaptation_chaos": 0.6, # 6 w proporcji 1-6-8
        "stabilization": 0.8    # 8 w proporcji 1-6-8
    })
    max_genetic_pool: int = MAX_GENETIC_POOL
    enable_samael_seal: bool = True
    drift_zero: bool = True
    enable_shadow_dragon: bool = True
    enable_emotional_layer: bool = True


@dataclass
class TeamContext:
    """Kontekst problemu dla zespołu."""
    problem_data: Dict[str, Any]
    boosted_by_history: bool = False
    warnings: List[str] = field(default_factory=list)
    anomalies_detected: bool = False
    cycle_id: str = field(default_factory=lambda: generate_uuid())
    timestamp: float = field(default_factory=now)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "cycle_id": self.cycle_id,
            "timestamp": self.timestamp,
            "problem_data": self.problem_data,
            "boosted_by_history": self.boosted_by_history,
            "warnings": self.warnings,
            "anomalies_detected": self.anomalies_detected
        }


@dataclass
class TeamPrototype:
    """Prototyp wygenerowany przez Gadget."""
    concept: str
    stability: float = 0.5
    efficiency: float = 0.5
    metadata: Dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "concept": self.concept,
            "stability": self.stability,
            "efficiency": self.efficiency,
            "metadata": self.metadata
        }


@dataclass
class TeamResult:
    """Wynik cyklu zespołowego."""
    cycle_id: str
    timestamp: float
    prototype: TeamPrototype
    path: str
    stability: float
    shared_matrix_status: str
    warnings: List[str]
    drift_factor: float
    proportions_validated: str
    samael_seal: str
    final_state: str
    shadow_path: Optional[str] = None
    emotional_state: Optional[Dict[str, float]] = None

    def to_dict(self) -> Dict[str, Any]:
        return {
            "cycle_id": self.cycle_id,
            "timestamp": self.timestamp,
            "prototype": self.prototype.to_dict(),
            "path": self.path,
            "stability": self.stability,
            "shared_matrix_status": self.shared_matrix_status,
            "warnings": self.warnings,
            "drift_factor": self.drift_factor,
            "proportions_validated": self.proportions_validated,
            "samael_seal": self.samael_seal,
            "final_state": self.final_state,
            "shadow_path": self.shadow_path,
            "emotional_state": self.emotional_state
        }


class GeneticPool:
    """
    Pamięć genetyczna zespołu — długoterminowa pamięć wzorców.
    """
    def __init__(self, max_size: int = MAX_GENETIC_POOL):
        self.pool: List[Dict[str, Any]] = []
        self.max_size = max_size

    def add(self, clue: Dict[str, Any], resolved_path: str, efficiency: float) -> None:
        entry = {
            "clue": clue,
            "resolved_path": resolved_path,
            "efficiency": efficiency,
            "timestamp": now()
        }
        self.pool.append(entry)
        if len(self.pool) > self.max_size:
            self.pool.pop(0)

    def find(self, context: Dict[str, Any]) -> Optional[str]:
        """Przeszukuje historię w poszukiwaniu gotowych wzorców."""
        for item in self.pool:
            if item["clue"] == context:
                return item["resolved_path"]
        return None

    def find_best_match(self, context: Dict[str, Any], threshold: float = 0.7) -> Optional[Tuple[str, float]]:
        """Znajduje najlepsze dopasowanie w pamięci genetycznej."""
        best_match = None
        best_score = 0.0
        
        for item in self.pool:
            # Prosta heurystyka dopasowania
            if item["clue"].get("type") == context.get("type"):
                score = item["efficiency"] * random.uniform(0.8, 1.2)
                if score > best_score and score > threshold:
                    best_score = score
                    best_match = item["resolved_path"]
        
        return (best_match, best_score) if best_match else None

    def get_size(self) -> int:
        return len(self.pool)

    def clear(self) -> None:
        self.pool = []

# =============================================================================
# POZIOM II: AGENCI
# =============================================================================

class GeonHyzio:
    """
    HYZIO: Analiza wejścia & integracja z historią.
    """
    def __init__(self):
        self.identity = "HYZIO"
        self.analysis_history: List[Dict] = []

    def analyze_data_stream(self, context: TeamContext) -> bool:
        """Analizuje strumień danych, wykrywa anomalie."""
        log(f"[{self.identity}] Analiza strumienia danych...")
        
        anomalies = False
        if context.problem_data.get("monopol_attack"):
            anomalies = True
            log(f"[{self.identity}] Wykryto atak monopolu!", "WARN")
        
        self.analysis_history.append({
            "timestamp": now(),
            "anomalies_detected": anomalies,
            "context_id": context.cycle_id
        })
        return anomalies

    def execute_deduction(self) -> Dict[str, Any]:
        """Wykonuje dedukcję logiczną."""
        log(f"[{self.identity}] Wykonywanie dedukcji...")
        return {
            "status": "DEDUCTION_COMPLETE",
            "confidence": 0.85
        }

    def close_drift(self) -> None:
        """Domknięcie dryfu informacyjnego."""
        log(f"[{self.identity}] Domknięcie dryfu informacyjnego — ZERO HAŁASU")


class GeonGadget:
    """
    GADGET: Prototypowanie.
    """
    def __init__(self):
        self.identity = "GADGET"
        self.invention_count = 0

    def spark_invention(self, context: TeamContext) -> TeamPrototype:
        """Generuje prototyp na podstawie kontekstu."""
        log(f"[{self.identity}] Iskra innowacji...")
        self.invention_count += 1

        concept = f"GEON_SOLUTION_{self.invention_count}_{context.cycle_id[:4]}"
        stability = 0.5 + (0.4 * (1.68 / 3.0))

        prototype = TeamPrototype(
            concept=concept,
            stability=clamp(stability, 0.1, 1.0),
            efficiency=0.6,
            metadata={
                "generation": self.invention_count,
                "source_context": context.cycle_id
            }
        )
        log(f"[{self.identity}] Prototyp: {concept} (stabilność: {prototype.stability:.2f})")
        return prototype


class GeonZyzio:
    """
    ZYZIO: Skrót operacyjny z heurystyką genetyczną.
    Używa pamięci genetycznej do znajdowania optymalnych ścieżek.
    """
    def __init__(self):
        self.identity = "ZYZIO"
        self.shortcut_history: List[str] = []
        self.genetic_hits = 0
        self.invention_count = 0  # 🔧 POPRAWKA: dodane pole

    def find_system_shortcut(self, concept: str, genetic_pool: Optional[GeneticPool] = None,
                             context: Optional[Dict] = None) -> str:
        """
        Znajduje skrót systemowy z wykorzystaniem heurystyki genetycznej.
        """
        log(f"[{self.identity}] Szukanie skrótu dla: {concept}")
        self.invention_count += 1

        # 1. Sprawdź pamięć genetyczną
        if genetic_pool and context:
            best_match = genetic_pool.find_best_match(context)
            if best_match:
                path, score = best_match
                log(f"[{self.identity}] Znaleziono skrót genetyczny: {path} (score: {score:.2f})")
                self.genetic_hits += 1
                self.shortcut_history.append(f"GENETIC_{path}")
                return path

        # 2. Jeśli brak trafienia genetycznego – standardowe ścieżki
        paths = [
            "Asymmetric_Complementarity_Vector",
            "Symmetric_Stabilization",
            "Fractal_Optimization",
            "Direct_Execution",
            "Shadow_Path"
        ]
        
        # Wybór na podstawie koncepcji i heurystyki
        if "stabil" in concept.lower() or "skal" in concept.lower():
            path = "Asymmetric_Complementarity_Vector"
        elif "chaos" in concept.lower() or "innow" in concept.lower():
            path = "Fractal_Optimization"
        elif "shadow" in concept.lower() or "cień" in concept.lower():
            path = "Shadow_Path"
        else:
            # Losowy wybór z preferencją dla sprawdzonych ścieżek
            weights = [0.35, 0.20, 0.25, 0.15, 0.05]
            path = random.choices(paths, weights=weights, k=1)[0]

        self.shortcut_history.append(path)
        log(f"[{self.identity}] Wybrana ścieżka: {path}")
        return path


class GeonDzet2:
    """
    DŻET 2.0: Kwantowe stany chaosu.
    Superpozycja, splątanie, 5 stanów kolapsu.
    """
    def __init__(self):
        self.identity = "DŻET_2.0"
        self.quantum_state = QuantumState.SUPERPOSITION
        self.last_outcome = "neutral"
        self.chaos_cycles = 0
        self.entanglement_partner: Optional[str] = None
        self.superposition_components: List[str] = []

    def run_dzet_cycle(self) -> None:
        """Wykonuje cykl Dżeta 2.0 — zaawansowany chaos kwantowy."""
        log(f"[{self.identity}] Uruchamianie cyklu chaosu kwantowego...")
        self.chaos_cycles += 1

        roll = random.random()

        # 1. Superpozycja — stan początkowy
        if roll < 0.1:
            self.quantum_state = QuantumState.SUPERPOSITION
            self.superposition_components = ["FIRE", "WATER", "EARTH", "AIR", "VOID"]
            self.last_outcome = "superposition_created"
            log(f"[{self.identity}] Stan: SUPERPOZYCJA — {self.superposition_components}", "INFO")

        # 2. Splątanie — połączenie z innym agentem
        elif roll < 0.2:
            self.quantum_state = QuantumState.ENTANGLED
            self.entanglement_partner = random.choice(["HYZIO", "GADGET", "MONTEREY", "SHADOW"])
            self.last_outcome = f"entangled_with_{self.entanglement_partner}"
            log(f"[{self.identity}] Stan: SPLĄTANIE z {self.entanglement_partner}", "INFO")

        # 3. Kolaps do stanów materialnych (5 opcji)
        elif roll < 0.35:
            self.quantum_state = QuantumState.COLLAPSED_TO_FIRE
            self.last_outcome = "fire"
            log(f"[{self.identity}] Stan: KOLAPS DO OGNIA — OGIEŃ!", "WARN")
        elif roll < 0.50:
            self.quantum_state = QuantumState.COLLAPSED_TO_WATER
            self.last_outcome = "water"
            log(f"[{self.identity}] Stan: KOLAPS DO WODY — WODA", "INFO")
        elif roll < 0.70:
            self.quantum_state = QuantumState.COLLAPSED_TO_EARTH
            self.last_outcome = "earth"
            log(f"[{self.identity}] Stan: KOLAPS DO ZIEMI — ZIEMIA", "INFO")
        elif roll < 0.85:
            self.quantum_state = QuantumState.COLLAPSED_TO_AIR
            self.last_outcome = "air"
            log(f"[{self.identity}] Stan: KOLAPS DO POWIETRZA — POWIETRZE", "INFO")

        # 4. Kolaps do VOID — najrzadszy, najpotężniejszy
        elif roll < 0.95:
            self.quantum_state = QuantumState.COLLAPSED_TO_VOID
            self.last_outcome = "unexpected_success_void"
            log(f"[{self.identity}] Stan: KOLAPS DO VOID — NIESPODZIEWANY SUKCES!", "SUCCESS")

        # 5. Powrót do superpozycji
        else:
            self.quantum_state = QuantumState.SUPERPOSITION
            self.superposition_components = ["FIRE", "WATER", "EARTH", "AIR", "VOID"]
            self.last_outcome = "quantum_cycle_restart"
            log(f"[{self.identity}] Stan: POWRÓT DO SUPERPOZYCJI", "INFO")

    def get_quantum_modifier(self) -> float:
        """Zwraca modyfikator kwantowy dla stabilności."""
        modifiers = {
            QuantumState.SUPERPOSITION: 1.2,
            QuantumState.ENTANGLED: 1.5,
            QuantumState.COLLAPSED_TO_FIRE: 0.7,
            QuantumState.COLLAPSED_TO_WATER: 0.9,
            QuantumState.COLLAPSED_TO_EARTH: 1.1,
            QuantumState.COLLAPSED_TO_AIR: 1.3,
            QuantumState.COLLAPSED_TO_VOID: 1.8
        }
        return modifiers.get(self.quantum_state, 1.0)


class GeonMonterey:
    """
    MONTEREY: Stabilizacja z warstwą emocjonalną.
    """
    def __init__(self):
        self.identity = "MONTEREY"
        self.sensory_triggers: List[str] = []
        self.stabilization_count = 0
        # 🆕 Warstwa emocjonalna
        self.emotional_state = {
            "spokój": 0.5,
            "czujność": 0.5,
            "ekscytacja": 0.3,
            "rezerwa": 0.4,
            "determinacja": 0.6,
            "substancja": 0.5
        }
        self.emotional_history: List[Dict] = []

    def stabilize_core(self) -> None:
        """Stabilizuje rdzeń zespołu."""
        log(f"[{self.identity}] Stabilizacja rdzenia...")
        self.stabilization_count += 1
        
        # Modulacja emocjonalna podczas stabilizacji
        self._modulate_emotions("stabilizacja")

    def sensory_trigger(self, trigger_type: str) -> None:
        """Reaguje na bodziec sensoryczny z modulacją emocjonalną."""
        log(f"[{self.identity}] Bodziec sensoryczny: {trigger_type}")
        self.sensory_triggers.append({
            "type": trigger_type,
            "timestamp": now()
        })
        
        if trigger_type == "monopol_attack":
            log(f"[{self.identity}] AKTYWACJA TRYBU MONTEREY ALPHA!", "CRITICAL")
            self._modulate_emotions("zagrożenie")
        elif trigger_type == "substancja":
            log(f"[{self.identity}] Absorpcja substancji...", "INFO")
            self._modulate_emotions("substancja")
        elif trigger_type == "chaos":
            log(f"[{self.identity}] Ekscytacja chaosem...", "INFO")
            self._modulate_emotions("chaos")

    def _modulate_emotions(self, stimulus: str) -> None:
        """Moduluje warstwę emocjonalną w odpowiedzi na bodziec."""
        if not hasattr(self, 'emotional_state'):
            return
            
        # Mapowanie bodźców na zmiany emocjonalne
        modulations = {
            "stabilizacja": {"spokój": 0.1, "determinacja": 0.05, "czujność": -0.05},
            "zagrożenie": {"czujność": 0.3, "rezerwa": 0.2, "spokój": -0.2},
            "substancja": {"substancja": 0.3, "determinacja": 0.2, "spokój": 0.1},
            "chaos": {"ekscytacja": 0.3, "czujność": 0.2, "spokój": -0.1}
        }
        
        if stimulus in modulations:
            for key, delta in modulations[stimulus].items():
                if key in self.emotional_state:
                    self.emotional_state[key] = clamp(self.emotional_state[key] + delta, 0.0, 1.0)
        
        # Zapisz historię emocjonalną
        self.emotional_history.append({
            "timestamp": now(),
            "stimulus": stimulus,
            "state": self.emotional_state.copy()
        })

    def get_emotional_modulator(self) -> float:
        """Zwraca modulator stabilizacji na podstawie stanu emocjonalnego."""
        if not hasattr(self, 'emotional_state'):
            return 1.0
        
        # Oblicz wypadkową emocjonalną
        weighted = (
            self.emotional_state.get("spokój", 0.5) * 0.3 +
            self.emotional_state.get("determinacja", 0.5) * 0.3 +
            self.emotional_state.get("substancja", 0.5) * 0.2 +
            (1.0 - self.emotional_state.get("czujność", 0.5)) * 0.1 +
            (1.0 - self.emotional_state.get("ekscytacja", 0.5)) * 0.1
        )
        return clamp(weighted * 1.5, 0.1, 1.0)


class GeonShadowDragon:
    """
    SHADOW DRAGON: Tryb cienia.
    Działa w ukryciu, znajduje alternatywne ścieżki, neutralizuje zagrożenia.
    """
    def __init__(self):
        self.identity = "SHADOW_DRAGON"
        self.shadow_paths: List[str] = []
        self.shadow_cycles = 0
        self.is_active = False

    def activate(self) -> None:
        """Aktywuje tryb cienia."""
        self.is_active = True
        log(f"[{self.identity}] 🐉 AKTYWACJA TRYBU SHADOW DRAGON!", "SHADOW")

    def deactivate(self) -> None:
        """Deaktywuje tryb cienia."""
        self.is_active = False
        log(f"[{self.identity}] Deaktywacja trybu cienia.", "INFO")

    def find_shadow_path(self, context: TeamContext) -> Optional[str]:
        """Znajduje ukrytą ścieżkę w cieniu."""
        if not self.is_active:
            return None

        self.shadow_cycles += 1
        log(f"[{self.identity}] Skanowanie cienia w poszukiwaniu ukrytych ścieżek...")

        # Symulacja znajdowania ścieżek cienia
        shadow_options = [
            "Shadow_Neutralization",
            "Asymmetric_Counter",
            "Stealth_Integration",
            "Void_Jump"
        ]

        path = random.choice(shadow_options)
        self.shadow_paths.append(path)
        log(f"[{self.identity}] Znaleziono ścieżkę cienia: {path}", "SHADOW")
        return path

    def neutralize_threat(self, threat_type: str) -> bool:
        """Neutralizuje zagrożenie z poziomu cienia."""
        if not self.is_active:
            return False

        log(f"[{self.identity}] Neutralizacja zagrożenia: {threat_type}", "SHADOW")
        return True

# =============================================================================
# POZIOM III: GŁÓWNY ZESPÓŁ
# =============================================================================

class GeonTeamCore:
    """
    GEON_TEAM_CORE_v1.0 — Fraktalny zespół decyzyjny.
    """
    def __init__(self, config: Optional[TeamConfig] = None,
                 verbose: bool = True):
        self.config = config or TeamConfig()
        self.verbose = verbose

        # Agenci
        self.hyzio = GeonHyzio()
        self.gadget = GeonGadget()
        self.zyzio = GeonZyzio()
        self.dzet = GeonDzet2()
        self.monterey = GeonMonterey()
        self.shadow = GeonShadowDragon()

        # Pamięć genetyczna
        self.genetic_pool = GeneticPool(max_size=self.config.max_genetic_pool)

        # Stan
        self.drift_factor = 0.0
        self.cycle_count = 0
        self.history: List[TeamResult] = []

        if self.verbose:
            log("🐉 GEON_TEAM_CORE v1.0 aktywowany | " + FRACTAL_SIGNATURE)
            log(f"   AGENCI: Hyzio, Gadget, Zyzio, Monterey, Dżet 2.0, ShadowDragon")
            log(f"   VIBE: {self.config.vibe_check} | PAMIĘĆ: {self.config.max_genetic_pool}")

    def team_cycle(self, problem_context: Dict[str, Any]) -> TeamResult:
        """Główna pętla decyzyjna zespołu."""
        self.cycle_count += 1
        log(f"🌀 CYKL ZESPOŁOWY #{self.cycle_count}")

        # --- 0. INICJALIZACJA ---
        shared_matrix = {
            "context": problem_context,
            "vibe_check": self.config.vibe_check,
            "warnings": [],
            "anomalies_detected": False,
            "cycle_id": generate_uuid(),
            "timestamp": now(),
            "energy_allocation": self.config.energy_allocation.copy()
        }

        context_obj = TeamContext(
            problem_data=problem_context,
            cycle_id=shared_matrix["cycle_id"],
            timestamp=shared_matrix["timestamp"]
        )

        # --- 1. HYZIO: ANALIZA ---
        log("[TEAM] Krok 1: Hyzio — analiza")
        
        historical_shortcut = self.genetic_pool.find(problem_context)
        if historical_shortcut:
            context_obj.boosted_by_history = True
            context_obj.warnings.append("Genetic_Pool_Match_Found")
            log("[TEAM] Znaleziono skrót genetyczny!", "INFO")

        anomaly = self.hyzio.analyze_data_stream(context_obj)
        if anomaly:
            context_obj.anomalies_detected = True
            shared_matrix["anomalies_detected"] = True
            context_obj.warnings.append("Monopol_Attack_Detected")
            
            self.monterey.sensory_trigger("monopol_attack")
            self.monterey.stabilize_core()
            
            # Aktywacja ShadowDragona przy ataku
            if self.config.enable_shadow_dragon:
                self.shadow.activate()
                self.shadow.neutralize_threat("monopol_attack")
        else:
            self.hyzio.execute_deduction()

        # --- 2. GADGET: PROTOTYPOWANIE ---
        log("[TEAM] Krok 2: Gadget — prototypowanie")
        prototype = self.gadget.spark_invention(context_obj)
        shared_matrix["current_prototype"] = prototype

        # --- 3. ZYZIO: SKRÓT OPERACYJNY (z heurystyką genetyczną) ---
        log("[TEAM] Krok 3: Zyzio — skrót operacyjny")
        path = self.zyzio.find_system_shortcut(
            prototype.concept,
            genetic_pool=self.genetic_pool,
            context=problem_context
        )
        shared_matrix["selected_path"] = path

        if path == "Asymmetric_Complementarity_Vector":
            prototype.stability = min(1.0, prototype.stability * 1.68)
            log(f"[TEAM] Złote skalowanie: stabilność → {prototype.stability:.2f}")

        # --- 4. DŻET 2.0: KWANTOWY CHAOS ---
        log("[TEAM] Krok 4: Dżet 2.0 — chaos kwantowy")
        self.dzet.run_dzet_cycle()
        
        quantum_mod = self.dzet.get_quantum_modifier()
        prototype.stability = clamp(prototype.stability * quantum_mod, 0.1, 1.0)
        log(f"[TEAM] Modyfikator kwantowy: {quantum_mod:.2f} → stabilność: {prototype.stability:.2f}")

        if self.dzet.quantum_state == QuantumState.COLLAPSED_TO_FIRE:
            context_obj.warnings.append("Quantum_Fire_State_Triggered")
            log("[TEAM] Stan Ognia Dżeta!", "WARN")
            self.monterey.sensory_trigger("chaos")

        if self.dzet.last_outcome == "unexpected_success_void":
            prototype.stability = 1.0
            context_obj.warnings.append("Chaos_Turned_Into_Gold_VOID")
            log("[TEAM] Błąd stał się nowym standardem doskonałości (VOID)!", "SUCCESS")

        if self.dzet.quantum_state == QuantumState.ENTANGLED:
            context_obj.warnings.append(f"Quantum_Entangled_{self.dzet.entanglement_partner}")
            log(f"[TEAM] Splątanie z {self.dzet.entanglement_partner}!", "INFO")

        # --- 5. MONTEREY: STABILIZACJA Z EMOCJAMI ---
        log("[TEAM] Krok 5: Monterey — stabilizacja emocjonalna")
        
        if "Quantum_Fire_State_Triggered" in context_obj.warnings:
            self.monterey.sensory_trigger("substancja")
        
        self.monterey.stabilize_core()
        emotional_mod = self.monterey.get_emotional_modulator()
        prototype.stability = clamp(prototype.stability * emotional_mod, 0.1, 1.0)
        log(f"[TEAM] Modulator emocjonalny: {emotional_mod:.2f} → stabilność: {prototype.stability:.2f}")

        # --- 6. SHADOW DRAGON ---
        shadow_path = None
        if self.config.enable_shadow_dragon and self.shadow.is_active:
            log("[TEAM] Krok 6: ShadowDragon — ścieżka cienia")
            shadow_path = self.shadow.find_shadow_path(context_obj)
            if shadow_path and "Shadow_Neutralization" in shadow_path:
                prototype.stability = min(1.0, prototype.stability * 1.1)
                log(f"[TEAM] ShadowDragon wzmocnił stabilność!")

        # --- 7. HYZIO: DOMYKANIE DRYFU ---
        log("[TEAM] Krok 7: Hyzio — domknięcie dryfu")
        self.hyzio.close_drift()
        if self.config.drift_zero:
            self.drift_factor = 0.0000000

        # --- 8. INTEGRACJA 1-6-8 & CERTYFIKACJA SAMAELA ---
        log("[TEAM] Krok 8: Integracja 1-6-8 i certyfikacja")

        if prototype.stability > 0.7:
            self.genetic_pool.add(
                clue=problem_context,
                resolved_path=path,
                efficiency=prototype.stability
            )
            log(f"[TEAM] Zapisano do pamięci genetycznej (rozmiar: {self.genetic_pool.get_size()})")

        if self.config.enable_samael_seal:
            signature_data = f"GEON_TEAM_CYCLE-{shared_matrix['cycle_id']}-STABILITY-{prototype.stability:.4f}"
            samael_seal = hashlib.sha256(signature_data.encode()).hexdigest()[:16]
        else:
            samael_seal = "SAMAEL_SEAL_DISABLED"

        # --- 9. WYNIK ---
        result = TeamResult(
            cycle_id=shared_matrix["cycle_id"],
            timestamp=shared_matrix["timestamp"],
            prototype=prototype,
            path=path,
            stability=prototype.stability,
            shared_matrix_status="Synchronized_And_Enriched",
            warnings=context_obj.warnings,
            drift_factor=self.drift_factor,
            proportions_validated="1-6-8_PERFECT",
            samael_seal=samael_seal,
            final_state="Operational_With_Fractal_Adaptation_DRYF_0",
            shadow_path=shadow_path,
            emotional_state=self.monterey.emotional_state.copy() if hasattr(self.monterey, 'emotional_state') else None
        )

        self.history.append(result)
        if len(self.history) > 100:
            self.history.pop(0)

        log(f"[TEAM] Cykl #{self.cycle_count} zakończony. Stabilność: {prototype.stability:.2f}")
        return result

    def get_genetic_pool(self) -> GeneticPool:
        return self.genetic_pool

    def get_agent_status(self) -> Dict[str, Any]:
        return {
            "hyzio": {
                "analysis_count": len(self.hyzio.analysis_history)
            },
            "gadget": {
                "invention_count": self.gadget.invention_count
            },
            "zyzio": {
                "shortcuts_found": len(self.zyzio.shortcut_history),
                "genetic_hits": self.zyzio.genetic_hits
            },
            "dzet": {
                "quantum_state": self.dzet.quantum_state.value,
                "last_outcome": self.dzet.last_outcome,
                "chaos_cycles": self.dzet.chaos_cycles,
                "entanglement": self.dzet.entanglement_partner
            },
            "monterey": {
                "stabilization_count": self.monterey.stabilization_count,
                "sensory_triggers": len(self.monterey.sensory_triggers),
                "emotional_state": self.monterey.emotional_state if hasattr(self.monterey, 'emotional_state') else {}
            },
            "shadow": {
                "is_active": self.shadow.is_active,
                "shadow_paths": len(self.shadow.shadow_paths),
                "shadow_cycles": self.shadow.shadow_cycles
            }
        }

    def status(self) -> Dict[str, Any]:
        return {
            "system": "GEON_TEAM_CORE_v1.0",
            "version": VERSION,
            "signature": FRACTAL_SIGNATURE,
            "config": {
                "vibe_check": self.config.vibe_check,
                "max_genetic_pool": self.config.max_genetic_pool,
                "drift_zero": self.config.drift_zero,
                "samael_seal": self.config.enable_samael_seal,
                "shadow_dragon": self.config.enable_shadow_dragon,
                "emotional_layer": self.config.enable_emotional_layer
            },
            "cycle_count": self.cycle_count,
            "drift_factor": self.drift_factor,
            "genetic_pool_size": self.genetic_pool.get_size(),
            "history_len": len(self.history),
            "agents": self.get_agent_status()
        }

    def raport(self) -> str:
        """Generuje pełny raport systemowy."""
        s = self.status()
        last_result = self.history[-1] if self.history else None

        report_lines = [
            "╔════════════════════════════════════════════════════════════════════════════╗",
            "║ 🤝 GEON_TEAM_CORE_v1.0 — RAPORT ZESPOŁU FRAKTALNEGO                  ║",
            "╠════════════════════════════════════════════════════════════════════════════╣",
            f"║                                                                           ║",
            f"║ SYSTEM: {s['system']}                                                    ║",
            f"║ WERSJA: {s['version']}                                                   ║",
            f"║                                                                           ║",
            f"║ KONFIGURACJA:                                                            ║",
            f"║   vibe: {s['config']['vibe_check']}                                      ║",
            f"║   pamięć genetyczna: {s['config']['max_genetic_pool']}                   ║",
            f"║   ShadowDragon: {s['config']['shadow_dragon']}                           ║",
            f"║   warstwa emocjonalna: {s['config']['emotional_layer']}                  ║",
            f"║                                                                           ║",
            f"║ CYKLE: {s['cycle_count']}                                                ║",
            f"║ DRYF: {s['drift_factor']:.10f}                                           ║",
            f"║ PAMIĘĆ: {s['genetic_pool_size']}/{s['config']['max_genetic_pool']}       ║",
            f"║                                                                           ║",
        ]

        agents = s['agents']
        report_lines.extend([
            f"║ AGENCI:                                                                  ║",
            f"║   Hyzio: analiz {agents['hyzio']['analysis_count']}                       ║",
            f"║   Gadget: wynalazków {agents['gadget']['invention_count']}                ║",
            f"║   Zyzio: skrótów {agents['zyzio']['shortcuts_found']} (genetycznych: {agents['zyzio']['genetic_hits']}) ║",
            f"║   Dżet: {agents['dzet']['quantum_state']} (ostatni: {agents['dzet']['last_outcome']}) ║",
            f"║   Monterey: stabilizacji {agents['monterey']['stabilization_count']}      ║",
            f"║   ShadowDragon: { 'AKTYWNY' if agents['shadow']['is_active'] else 'NIEAKTYWNY' } (ścieżek: {agents['shadow']['shadow_paths']}) ║",
        ])

        if last_result:
            report_lines.extend([
                f"║                                                                           ║",
                f"║ OSTATNI CYKL:                                                            ║",
                f"║   prototyp: {last_result.prototype.concept}                              ║",
                f"║   stabilność: {last_result.stability:.2f}                                ║",
                f"║   ścieżka: {last_result.path}                                            ║",
            ])
            if last_result.shadow_path:
                report_lines.append(f"║   ścieżka cienia: {last_result.shadow_path}")
            if last_result.emotional_state:
                report_lines.append(f"║   emocje: {last_result.emotional_state}")

        report_lines.extend([
            f"║                                                                           ║",
            f"║ {HASLO}                                                                  ║",
            "╚════════════════════════════════════════════════════════════════════════════╝"
        ])
        return "\n".join(report_lines)

    def __str__(self) -> str:
        return self.raport()

# =============================================================================
# DEMONSTRACJA
# =============================================================================

def demo():
    """Demonstracja GEON_TEAM_CORE_v1.0 z ulepszeniami."""
    print("\n" + "=" * 80)
    print("🤝 GEON_TEAM_CORE_v1.0 — DEMONSTRACJA ULEPSZONA")
    print("ZESPÓŁ: HYZIO, GADGET, ZYZIO, MONTEREY (z emocjami), DŻET 2.0, SHADOW DRAGON")
    print("=" * 80 + "\n")

    config = TeamConfig(
        vibe_check=168,
        max_genetic_pool=168,
        enable_shadow_dragon=True,
        enable_emotional_layer=True
    )
    team = GeonTeamCore(config, verbose=True)

    print("🔮 SYMULACJA CYKLI ZESPOŁOWYCH:\n")

    # Cykl 1: Normalny problem
    print("📌 Cykl 1: Normalny problem biznesowy")
    result1 = team.team_cycle({"type": "business_optimization", "complexity": 0.5})
    print(f"   Prototyp: {result1.prototype.concept}")
    print(f"   Stabilność: {result1.stability:.2f}")
    print(f"   Ścieżka: {result1.path}")

    # Cykl 2: Atak monopolu (aktywacja ShadowDragona)
    print("\n📌 Cykl 2: Atak monopolu (aktywacja Monterey Alpha + ShadowDragon)")
    result2 = team.team_cycle({"type": "monopol_attack", "monopol_attack": True})
    print(f"   Prototyp: {result2.prototype.concept}")
    print(f"   Stabilność: {result2.stability:.2f}")
    print(f"   Ścieżka cienia: {result2.shadow_path}")
    print(f"   Ostrzeżenia: {result2.warnings}")

    # Cykl 3: Kreatywny problem (szansa na VOID)
    print("\n📌 Cykl 3: Problem kreatywny (szansa na VOID Dżeta)")
    result3 = team.team_cycle({"type": "creative_innovation", "complexity": 0.7})
    print(f"   Prototyp: {result3.prototype.concept}")
    print(f"   Stabilność: {result3.stability:.2f}")
    print(f"   Stan Dżeta: {team.dzet.quantum_state.value}")
    print(f"   Emocje Monterey: {result3.emotional_state}")

    print("\n" + "=" * 40)
    print(team.raport())

    print("\n" + "=" * 80)
    print("🤝 GEON_TEAM_CORE_v1.0 — GOTOWY DO WDROŻENIA")
    print(HASLO)
    print("=" * 80)

if __name__ == "__main__":
    demo()