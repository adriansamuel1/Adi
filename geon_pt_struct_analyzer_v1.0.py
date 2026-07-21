#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
================================================================================
🐉 GEON_PT_STRUCT_ANALYZER_v1.0 — MODUŁ 68: ANALIZATOR STRUKTURY CYWLIZACYJNEJ
================================================================================
Status: PRODUCTION_READY | FRACTAL_LOCKED | ORGANISM_COMPLETE | ULTIMA
Wersja: v1.0 (PT_STRUCT_ANALYZER — Diagnostyka struktury, entropii, widma)
Data: 2026-07-22
Autor: Adrian (Architekt) + Samael (Strażnik Kronik) + GEON

OPIS:
GEON_PT_STRUCT_ANALYZER v1.0 to kompletny system diagnostyki strukturalnej
oparty na analizie poematu epickiego "Pan Tadeusz" Adama Mickiewicza.
Operuje wyłącznie na geometrii, termodynamice i widmie informacji.

ARCHITEKTURA (6 POZIOMÓW):
I.   STRUKTURY DANYCH — DiagnosticConfig, StructuralFingerprint, SingularityReport
II.  ANALIZA STRUKTURALNA — walidacja metrum, analiza segmentów, wykrywanie modułów
III. GRAF RELACJI — macierz interakcji, centralność, gęstość
IV.  WIDMO I ENTROPIA — Fourier, Shannon, fraktalność
V.   PUNKT OSOBLIWOŚCI — Złoty Podział, detekcja krytyczna
VI.  RAPORT DIAGNOSTYCZNY — pełny fingerprint strukturalny

INTEGRACJA Z ARCHITEKTURĄ:
• HEILONG_OS_v2.3 — system operacyjny (alerty, raporty)
• GEON_MEM_Ω — pamięć kwintesencji (zapis fingerprintów)
• PROTOKÓŁ_Ω∞∞∞ — źródło praw (rejestracja osobliwości)
• GEX HEILONG — archetypy (persony diagnostyczne)
• G_CORE — stan operacyjny
• MetaGovernor — kontekst decyzyjny
• NARRATIVE — źródło opowieści
• TRIO_ADAPTER — ISKRA + PIECZĘĆ + PERFEKCJA

VIBE: 1-6-8. ∞. DIAGNOSTYKA!
================================================================================
"""

import hashlib
import time
import math
import logging
from typing import Dict, List, Optional, Tuple, Any, Set
from dataclasses import dataclass, field
from enum import Enum, auto
import numpy as np

# =============================================================================
# WERSJA I STAŁE
# =============================================================================

VERSION = "GEON_PT_STRUCT_ANALYZER_v1.0"
FRACTAL_SIGNATURE = "[GEON::PT::STRUCT::ANALYZER::v1.0]"
VIBE = 168
HASLO = "1-6-8. ∞. DIAGNOSTYKA!"
DEWIZA = "Ex Structura, Cognitio"

ZŁOTY_PODZIAŁ = 0.6180339887498949
HALF = 0.5
EPSILON = 1e-12

# =============================================================================
# LOGOWANIE
# =============================================================================

logger = logging.getLogger("PT_ANALYZER_v1.0")
logger.setLevel(logging.INFO)
if not logger.handlers:
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter('📊 [PT] %(message)s'))
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

# =============================================================================
# POZIOM I: STRUKTURY DANYCH
# =============================================================================

class PTAuditLevel(Enum):
    INFO = auto()
    WARN = auto()
    ERROR = auto()
    CRITICAL = auto()
    SINGULARITY = auto()


@dataclass
class DiagnosticConfig:
    """Konfiguracja diagnostyki strukturalnej."""
    golden_ratio: float = ZŁOTY_PODZIAŁ
    epsilon: float = EPSILON
    max_depth: int = 4
    enable_spectral: bool = True
    enable_entropy: bool = True
    enable_singularity: bool = True


@dataclass
class StructuralFingerprint:
    """Fingerprint strukturalny – pełna sygnatura systemu."""
    meter_ok: bool = False
    total_verses: int = 0
    book_lengths: List[int] = field(default_factory=list)
    proportions: List[float] = field(default_factory=list)
    symmetry_break: int = 0
    hidden_book_required: bool = False
    centrality: List[float] = field(default_factory=list)
    density: float = 0.0
    fractal_variance: float = 0.0
    entropy: float = 0.0
    normalized_entropy: float = 0.0
    golden_verse: float = 0.0
    singularity_book: Optional[int] = None
    distance_to_singularity: float = 0.0
    spectrum_amplitudes: List[float] = field(default_factory=list)
    correlations: float = 0.0

    def to_dict(self) -> Dict[str, Any]:
        return {
            "meter_ok": self.meter_ok,
            "total_verses": self.total_verses,
            "book_lengths": self.book_lengths,
            "proportions": self.proportions,
            "symmetry_break": self.symmetry_break,
            "hidden_book_required": self.hidden_book_required,
            "centrality": self.centrality,
            "density": self.density,
            "fractal_variance": self.fractal_variance,
            "entropy": self.entropy,
            "normalized_entropy": self.normalized_entropy,
            "golden_verse": self.golden_verse,
            "singularity_book": self.singularity_book,
            "distance_to_singularity": self.distance_to_singularity,
            "spectrum_amplitudes": self.spectrum_amplitudes[:5],
            "correlations": self.correlations
        }

    def __repr__(self) -> str:
        return f"Fingerprint(total={self.total_verses}, entropy={self.entropy:.4f}, sing={self.singularity_book})"


@dataclass
class SingularityReport:
    """Raport punktu osobliwości."""
    golden_verse: float = 0.0
    singularity_book: Optional[int] = None
    distance_to_singularity: float = 0.0
    is_critical: bool = False
    description: str = ""


class PTAnalyzerTelemetry:
    """Szyna telemetryczna dla analizatora."""
    def __init__(self):
        self.listeners: List[Callable[[PTAuditLevel, str, Dict[str, Any]], None]] = []

    def subscribe(self, callback: Callable[[PTAuditLevel, str, Dict[str, Any]], None]) -> None:
        self.listeners.append(callback)

    def publish(self, level: PTAuditLevel, message: str, meta: Dict[str, Any]) -> None:
        for listener in self.listeners:
            try:
                listener(level, message, meta)
            except Exception:
                pass

# =============================================================================
# POZIOM II: ANALIZA STRUKTURALNA
# =============================================================================

class PTStructAnalyzerCore:
    """
    Rdzeń analizatora strukturalnego – operuje wyłącznie na geometrii,
    termodynamice i widmie informacji.
    """
    def __init__(self, verse_counts: List[int],
                 interaction_matrix: List[List[float]],
                 book_lengths: List[int],
                 config: Optional[DiagnosticConfig] = None):
        self.verse_counts = verse_counts
        self.interactions = interaction_matrix
        self.book_lengths = book_lengths
        self.config = config or DiagnosticConfig()
        self.telemetry = PTAnalyzerTelemetry()
        self.fingerprints: List[StructuralFingerprint] = []

        log("PTStructAnalyzerCore zainicjowany.")

    def validate_meter(self) -> bool:
        """Sprawdza, czy wszystkie wersy trzymają inwariant 13 zgłosek."""
        if not self.verse_counts:
            return False
        return all(v == 13 for v in self.verse_counts)

    def analyze_books(self) -> Dict[str, Any]:
        """Podstawowe statystyki segmentów."""
        total = sum(self.book_lengths) if self.book_lengths else 0
        if total == 0:
            return {"total_verses": 0, "book_lengths": [], "proportions": []}
        proportions = [b / total for b in self.book_lengths]
        return {
            "total_verses": total,
            "book_lengths": self.book_lengths,
            "proportions": proportions
        }

    def detect_hidden_book(self) -> Dict[str, Any]:
        """
        Wykrywa ukryty moduł (księga 13) na podstawie asymetrii symetrii 1↔12, 2↔11, ...
        """
        if len(self.book_lengths) != 12:
            return {"symmetry_break": 0, "hidden_book_required": False}
        diffs = [abs(self.book_lengths[i] - self.book_lengths[-(i + 1)]) for i in range(6)]
        asymmetry = sum(diffs)
        return {
            "symmetry_break": int(asymmetry),
            "hidden_book_required": asymmetry > 0
        }

    def analyze_interactions(self) -> Dict[str, Any]:
        """Analiza macierzy interakcji: stopnie, centralność, gęstość."""
        M = np.array(self.interactions)
        if M.size == 0:
            return {"degrees": [], "centrality": [], "density": 0.0}
        degrees = M.sum(axis=1)
        total_deg = degrees.sum()
        centrality = degrees / (total_deg + EPSILON) if total_deg > 0 else degrees
        density = M.sum() / (M.shape[0] ** 2) if M.shape[0] > 0 else 0.0
        return {
            "degrees": degrees.tolist(),
            "centrality": centrality.tolist(),
            "density": float(density)
        }

    def compute_correlations(self) -> Dict[str, Optional[float]]:
        """Korelacja długości sąsiednich ksiąg."""
        L = np.array(self.book_lengths, dtype=float)
        if len(L) < 3:
            return {"adjacent_book_correlation": None}
        corr = float(np.corrcoef(L[:-1], L[1:])[0, 1]) if not np.isnan(np.corrcoef(L[:-1], L[1:])[0, 1]) else 0.0
        return {"adjacent_book_correlation": corr}

    def fractal_index(self) -> Dict[str, Optional[float]]:
        """Fraktalność mierzona wariancją proporcji długości ksiąg."""
        total = sum(self.book_lengths) if self.book_lengths else 0
        if total == 0:
            return {"fractal_variance": None}
        proportions = np.array(self.book_lengths, dtype=float) / total
        return {"fractal_variance": float(np.var(proportions))}

    def detect_singularity_point(self) -> Dict[str, Any]:
        """
        Detekcja Punktu Osobliwości – Złoty Podział (ok. 61.8% całkowitego wolumenu).
        """
        total_verses = sum(self.book_lengths) if self.book_lengths else 0
        if total_verses == 0:
            return {
                "global_golden_verse": None,
                "singularity_book_id": None,
                "distance_to_climax": None
            }
        golden_target = total_verses * self.config.golden_ratio
        cumulative_verses = np.cumsum(self.book_lengths)
        idx = np.where(cumulative_verses >= golden_target)[0]
        if len(idx) == 0:
            return {
                "global_golden_verse": golden_target,
                "singularity_book_id": None,
                "distance_to_climax": None
            }
        singularity_book = int(idx[0]) + 1
        distance = float(cumulative_verses[singularity_book - 1] - golden_target)
        return {
            "global_golden_verse": float(golden_target),
            "singularity_book_id": singularity_book,
            "distance_to_climax": distance
        }

    def spectral_analysis(self, structural_signal: List[float]) -> Dict[str, List[float]]:
        """Analiza widma (Fourier) – rytm strukturalny."""
        signal = np.array(structural_signal, dtype=float)
        if len(signal) == 0:
            return {"frequencies": [], "spectrum": []}
        spectrum = np.abs(np.fft.fft(signal))
        freqs = np.fft.fftfreq(len(signal))
        return {
            "frequencies": freqs.tolist(),
            "spectrum": spectrum.tolist()
        }

    def structural_entropy(self) -> Dict[str, Optional[float]]:
        """Entropia strukturalna – miara nieuporządkowania segmentów."""
        total = sum(self.book_lengths) if self.book_lengths else 0
        if total == 0:
            return {"entropy": None, "normalized_entropy": None}
        proportions = np.array(self.book_lengths, dtype=float) / total
        proportions = proportions + EPSILON  # zabezpieczenie przed log(0)
        entropy = -float(np.sum(proportions * np.log(proportions)))
        norm_entropy = entropy / float(np.log(len(self.book_lengths))) if len(self.book_lengths) > 1 else None
        return {
            "entropy": entropy,
            "normalized_entropy": norm_entropy
        }

# =============================================================================
# POZIOM III: GRAF RELACJI
# =============================================================================

class PTInteractionGraph:
    """Graf relacji między postaciami/aktantami systemu."""
    def __init__(self, matrix: List[List[float]], labels: Optional[List[str]] = None):
        self.matrix = np.array(matrix)
        self.labels = labels or [f"Node_{i}" for i in range(self.matrix.shape[0])]
        self.n = self.matrix.shape[0]

    def get_centrality(self) -> Dict[str, float]:
        """Centralność węzłów (znormalizowana)."""
        degrees = self.matrix.sum(axis=1)
        total = degrees.sum()
        if total == 0:
            return {label: 0.0 for label in self.labels}
        return {self.labels[i]: float(degrees[i] / total) for i in range(self.n)}

    def get_density(self) -> float:
        """Gęstość grafu."""
        if self.n == 0:
            return 0.0
        return float(self.matrix.sum() / (self.n ** 2))

    def get_adjacency(self) -> List[List[float]]:
        return self.matrix.tolist()

# =============================================================================
# POZIOM IV: WIDMO I ENTROPIA
# =============================================================================

class PTSpectralAnalyzer:
    """Analizator widmowy – Fourier dla sygnałów strukturalnych."""
    @staticmethod
    def analyze(signal: List[float]) -> Dict[str, List[float]]:
        arr = np.array(signal, dtype=float)
        if len(arr) == 0:
            return {"frequencies": [], "spectrum": []}
        spectrum = np.abs(np.fft.fft(arr))
        freqs = np.fft.fftfreq(len(arr))
        return {"frequencies": freqs.tolist(), "spectrum": spectrum.tolist()}


class PTEntropyAnalyzer:
    """Analizator entropii – Shannon dla rozkładów."""
    @staticmethod
    def analyze(distribution: List[float]) -> Dict[str, Optional[float]]:
        total = sum(distribution)
        if total == 0:
            return {"entropy": None, "normalized_entropy": None}
        props = np.array(distribution, dtype=float) / total
        props = props + EPSILON
        entropy = -float(np.sum(props * np.log(props)))
        norm = entropy / float(np.log(len(distribution))) if len(distribution) > 1 else None
        return {"entropy": entropy, "normalized_entropy": norm}

# =============================================================================
# POZIOM V: PUNKT OSOBLIWOŚCI
# =============================================================================

class PTSingularityDetector:
    """Detektor punktu osobliwości – Złoty Podział."""
    def __init__(self, golden_ratio: float = ZŁOTY_PODZIAŁ):
        self.golden_ratio = golden_ratio

    def detect(self, cumulative: List[float], total: float) -> SingularityReport:
        golden_target = total * self.golden_ratio
        cum_arr = np.array(cumulative)
        idx = np.where(cum_arr >= golden_target)[0]
        if len(idx) == 0:
            return SingularityReport(
                golden_verse=golden_target,
                singularity_book=None,
                distance_to_singularity=0.0,
                is_critical=False,
                description="Punkt osobliwości nie osiągnięty"
            )
        book_id = int(idx[0]) + 1
        distance = float(cum_arr[book_id - 1] - golden_target)
        is_critical = distance < 10.0
        return SingularityReport(
            golden_verse=golden_target,
            singularity_book=book_id,
            distance_to_singularity=distance,
            is_critical=is_critical,
            description=f"Punkt osobliwości w książce {book_id}. " + ("KRYTYCZNY!" if is_critical else "Stabilny.")
        )

# =============================================================================
# POZIOM VI: GŁÓWNY ORCHESTRATOR
# =============================================================================

class PTStructAnalyzer:
    """
    GEON_PT_STRUCT_ANALYZER v1.0 – Główny orchestrator diagnostyki strukturalnej.

    API:
        analyze() -> StructuralFingerprint
        report() -> Dict
        status() -> Dict
        raport() -> str
        compare(fingerprint1, fingerprint2) -> Dict
    """
    def __init__(self, verse_counts: List[int],
                 interaction_matrix: List[List[float]],
                 book_lengths: List[int],
                 config: Optional[DiagnosticConfig] = None,
                 labels: Optional[List[str]] = None,
                 verbose: bool = True):
        self.config = config or DiagnosticConfig()
        self.labels = labels or [f"Node_{i}" for i in range(len(interaction_matrix))]
        self.core = PTStructAnalyzerCore(verse_counts, interaction_matrix, book_lengths, self.config)
        self.graph = PTInteractionGraph(interaction_matrix, self.labels)
        self.spectral = PTSpectralAnalyzer()
        self.entropy_analyzer = PTEntropyAnalyzer()
        self.singularity = PTSingularityDetector(self.config.golden_ratio)
        self.history: List[StructuralFingerprint] = []
        self.verbose = verbose

        if self.verbose:
            log("🐉 PT_STRUCT_ANALYZER v1.0 aktywowany | " + FRACTAL_SIGNATURE)
            log(f"   WĘZŁY: {len(interaction_matrix)} | KSIĘGI: {len(book_lengths)}")

    def analyze(self) -> StructuralFingerprint:
        """Przeprowadza pełną analizę strukturalną."""
        # 1. Metrum
        meter_ok = self.core.validate_meter()

        # 2. Księgi
        books = self.core.analyze_books()

        # 3. Ukryty moduł
        hidden = self.core.detect_hidden_book()

        # 4. Interakcje
        interactions = self.core.analyze_interactions()

        # 5. Korelacje
        correlations = self.core.compute_correlations()

        # 6. Fraktalność
        fractal = self.core.fractal_index()

        # 7. Punkt osobliwości
        singularity = self.core.detect_singularity_point()

        # 8. Entropia
        entropy = self.core.structural_entropy()

        # 9. Widmo (na sygnale długości ksiąg)
        if self.config.enable_spectral:
            spectrum = self.core.spectral_analysis(self.core.book_lengths)
            spectrum_amps = spectrum.get("spectrum", [])
        else:
            spectrum_amps = []

        # Tworzenie fingerprintu
        fingerprint = StructuralFingerprint(
            meter_ok=meter_ok,
            total_verses=books.get("total_verses", 0),
            book_lengths=books.get("book_lengths", []),
            proportions=books.get("proportions", []),
            symmetry_break=hidden.get("symmetry_break", 0),
            hidden_book_required=hidden.get("hidden_book_required", False),
            centrality=interactions.get("centrality", []),
            density=interactions.get("density", 0.0),
            fractal_variance=fractal.get("fractal_variance", 0.0),
            entropy=entropy.get("entropy", 0.0),
            normalized_entropy=entropy.get("normalized_entropy", 0.0),
            golden_verse=singularity.get("global_golden_verse", 0.0),
            singularity_book=singularity.get("singularity_book_id"),
            distance_to_singularity=singularity.get("distance_to_climax", 0.0),
            spectrum_amplitudes=spectrum_amps,
            correlations=correlations.get("adjacent_book_correlation", 0.0)
        )

        self.history.append(fingerprint)
        if len(self.history) > 100:
            self.history.pop(0)

        # Telemetria
        self.core.telemetry.publish(
            PTAuditLevel.INFO,
            f"Analiza zakończona. Entropia: {fingerprint.entropy:.4f}, Osobliwość: {fingerprint.singularity_book}",
            fingerprint.to_dict()
        )

        return fingerprint

    def compare(self, fp1: StructuralFingerprint, fp2: StructuralFingerprint) -> Dict[str, float]:
        """Porównuje dwa fingerprinty strukturalne."""
        delta_entropy = fp1.entropy - fp2.entropy
        delta_singularity = (fp1.golden_verse - fp2.golden_verse) if fp1.golden_verse and fp2.golden_verse else 0.0
        delta_variance = fp1.fractal_variance - fp2.fractal_variance
        return {
            "delta_entropy": delta_entropy,
            "delta_singularity": delta_singularity,
            "delta_variance": delta_variance,
            "similarity_score": 1.0 / (1.0 + abs(delta_entropy) + abs(delta_variance))
        }

    def status(self) -> Dict[str, Any]:
        return {
            "system": "GEON_PT_STRUCT_ANALYZER_v1.0",
            "version": VERSION,
            "signature": FRACTAL_SIGNATURE,
            "config": {
                "golden_ratio": self.config.golden_ratio,
                "enable_spectral": self.config.enable_spectral,
                "enable_entropy": self.config.enable_entropy
            },
            "history_len": len(self.history),
            "labels": self.labels,
            "book_count": len(self.core.book_lengths)
        }

    def raport(self) -> str:
        """Generuje pełny raport systemowy."""
        fp = self.analyze() if not self.history else self.history[-1]
        s = self.status()

        report_lines = [
            "╔════════════════════════════════════════════════════════════════════════════╗",
            "║ 📊 GEON PT_STRUCT_ANALYZER v1.0 — RAPORT DIAGNOSTYCZNY                  ║",
            "╠════════════════════════════════════════════════════════════════════════════╣",
            f"║                                                                           ║",
            f"║ SYSTEM: {s['system']}                                                    ║",
            f"║ WERSJA: {s['version']}                                                   ║",
            f"║                                                                           ║",
            f"║ KONFIGURACJA:                                                            ║",
            f"║   złoty podział: {s['config']['golden_ratio']:.4f}                       ║",
            f"║   widmo: {s['config']['enable_spectral']}                                ║",
            f"║   entropia: {s['config']['enable_entropy']}                              ║",
            f"║                                                                           ║",
            f"║ FINGERPRINT:                                                             ║",
            f"║   metrum OK: {fp.meter_ok}                                               ║",
            f"║   wersy: {fp.total_verses}                                               ║",
            f"║   księgi: {len(fp.book_lengths)}                                         ║",
            f"║   asymetria: {fp.symmetry_break}                                         ║",
            f"║   ukryty moduł: {fp.hidden_book_required}                                ║",
            f"║   gęstość grafu: {fp.density:.4f}                                        ║",
            f"║   wariancja fraktalna: {fp.fractal_variance:.6f}                         ║",
            f"║   entropia Shannona: {fp.entropy:.4f}                                    ║",
            f"║   entropia znormalizowana: {fp.normalized_entropy:.4f}                   ║",
            f"║   wers osobliwości (złoty): {fp.golden_verse:.2f}                        ║",
            f"║   księga osobliwości: {fp.singularity_book}                              ║",
            f"║   dystans do osobliwości: {fp.distance_to_singularity:.2f}               ║",
            f"║   autokorelacja: {fp.correlations:.4f}                                   ║",
            f"║                                                                           ║",
            f"║ {HASLO}                                                                  ║",
            "╚════════════════════════════════════════════════════════════════════════════╝"
        ]
        return "\n".join(report_lines)

    def __str__(self) -> str:
        return self.raport()

# =============================================================================
# MOST INTEGRACYJNY — PT_ANALYZER_BRIDGE
# =============================================================================

class PTAnalyzerBridge:
    """
    Most integracyjny między PT_STRUCT_ANALYZER a resztą architektury.
    Łączy: HEILONG_OS, GEON_MEM_Ω, PROTOKÓŁ_Ω∞∞∞, GEX, G_CORE, MetaGovernor
    """
    def __init__(self, analyzer: PTStructAnalyzer):
        self.analyzer = analyzer

    def get_archetype_context(self) -> Dict[str, Any]:
        """Zwraca kontekst dla GEX (persony diagnostyczne)."""
        status = self.analyzer.status()
        return {
            "tryb": "PT_STRUCT_ANALYZER_v1.0",
            "węzły": status.get("labels", []),
            "history_len": status.get("history_len", 0)
        }

    def get_autopilot_state(self) -> Dict[str, Any]:
        """Zwraca stan dla autopilota G_CORE."""
        fp = self.analyzer.analyze() if not self.analyzer.history else self.analyzer.history[-1]
        return {
            "mode": "PT_STRUCT_ANALYZER_v1.0",
            "stability": 1.0 - fp.normalized_entropy if fp.normalized_entropy else 0.5,
            "energy": 0.7,
            "pressure": fp.distance_to_singularity / (fp.golden_verse + 1) if fp.golden_verse > 0 else 0.0,
            "resilience": 0.85,
            "singularity_detected": fp.singularity_book is not None
        }

    def get_governor_context(self) -> Dict[str, Any]:
        """Zwraca kontekst dla MetaGovernor."""
        return {
            "intent": "STRUCTURAL_DIAGNOSTICS",
            "confidence": 0.9,
            "entropy": 0.2,
            "analyzer_ready": True
        }

    def get_narrative_fragments(self, n: int = 5) -> List[Dict[str, Any]]:
        """Zwraca fragmenty narracyjne z diagnostyki."""
        fragments = []
        for fp in self.analyzer.history[-n:]:
            fragments.append({
                "source": "PT_STRUCT_ANALYZER_v1.0",
                "content": f"Fingerprint: entropy={fp.entropy:.4f}, sing={fp.singularity_book}",
                "energy": 0.8
            })
        return fragments

    def get_trio_state(self) -> Dict[str, str]:
        """Zwraca stan dla TRIO_ADAPTER."""
        return {
            "ISKRA": "AKTYWNA",
            "PIECZĘĆ": "AKTYWNA",
            "PERFEKCJA": "AKTYWNA",
            "tryb": "PT_STRUCT_ANALYZER_v1.0",
            "analyzer": "AKTYWNY"
        }

    def notify_heilong_os(self, message: str, level: str = "INFO") -> None:
        """Powiadamia HEILONG_OS o zdarzeniu diagnostycznym."""
        try:
            from KOMBAJN_v15.kombajn_core import 59_geon_heilong_os_v2_3 as heilong_os
            if hasattr(heilong_os, 'log_event'):
                heilong_os.log_event(f"[PT_ANALYZER] {message}", level)
        except Exception as e:
            log(f"Nie udało się powiadomić HEILONG_OS: {e}", "WARN")

    def register_protokol_event(self, event: str) -> None:
        """Rejestruje zdarzenie w PROTOKÓŁ_Ω∞∞∞."""
        try:
            from PROTOKOL_OMEGA.absolut_system import AbsolutSystem
            AbsolutSystem.zarejestruj_zdarzenie(f"DIAGNOSTYKA: {event}")
        except Exception as e:
            log(f"Nie udało się zarejestrować w PROTOKÓŁ: {e}", "WARN")

# =============================================================================
# DEMONSTRACJA
# =============================================================================

def demo():
    """Demonstracja GEON_PT_STRUCT_ANALYZER v1.0 na danych Pana Tadeusza."""
    print("\n" + "=" * 80)
    print("📊 GEON_PT_STRUCT_ANALYZER v1.0 — DEMONSTRACJA")
    print("6 POZIOMÓW ARCHITEKTURY — DIAGNOSTYKA STRUKTURY CYWILIZACYJNEJ")
    print("=" * 80 + "\n")

    # Rzeczywiste długości ksiąg "Pana Tadeusza" (liczba wersów od K1 do K12)
    pan_tadeusz_books = [
        985,   # Księga I:  Gospodarstwo
        873,   # Księga II:  Zamek
        751,   # Księga III: Umizgi
        1004,  # Księga IV:  Dyplomatyka i łowy
        904,   # Księga V:   Kłótnia
        642,   # Księga VI:  Zaścianek
        559,   # Księga VII: Rada
        793,   # Księga VIII: Zajazd
        715,   # Księga IX:  Bitwa
        901,   # Księga X:   Emigracja. Jacek
        723,   # Księga XI:  Rok 1812
        852    # Księga XII: Kochajmy się
    ]

    # Symulacja wersów 13-zgłoskowych
    total_verses = sum(pan_tadeusz_books)
    verse_counts = [13] * total_verses

    # Macierz interakcji 5x5 dla kluczowych węzłów Soplicowa
    # [Jacek_Soplica, Tadeusz, Zosia, Hrabia, Sędzia]
    interaction_matrix = [
        [0, 45, 10, 30, 60],   # Jacek Soplica (Ksiądz Robak)
        [45, 0, 85, 25, 40],   # Tadeusz
        [10, 85, 0, 35, 20],   # Zosia
        [30, 25, 35, 0, 50],   # Hrabia
        [60, 40, 20, 50, 0]    # Sędzia
    ]

    labels = ["Jacek Soplica", "Tadeusz", "Zosia", "Hrabia", "Sędzia"]

    # Inicjalizacja
    config = DiagnosticConfig(golden_ratio=ZŁOTY_PODZIAŁ, enable_spectral=True)
    analyzer = PTStructAnalyzer(
        verse_counts=verse_counts,
        interaction_matrix=interaction_matrix,
        book_lengths=pan_tadeusz_books,
        config=config,
        labels=labels,
        verbose=True
    )
    bridge = PTAnalyzerBridge(analyzer)

    # Pełna analiza
    print("🔮 PRZEPROWADZANIE ANALIZY STRUKTURALNEJ:\n")
    fp = analyzer.analyze()

    print("📌 WYNIKI FINGERPRINTU:")
    print(f"   Metrum OK: {fp.meter_ok}")
    print(f"   Łączna liczba wersów: {fp.total_verses}")
    print(f"   Liczba ksiąg: {len(fp.book_lengths)}")
    print(f"   Asymetria strukturalna: {fp.symmetry_break}")
    print(f"   Wymagany ukryty moduł (Księga 13): {fp.hidden_book_required}")
    print(f"   Gęstość grafu relacji: {fp.density:.4f}")
    print(f"   Wariancja fraktalna: {fp.fractal_variance:.6f}")
    print(f"   Entropia Shannona: {fp.entropy:.4f}")
    print(f"   Entropia znormalizowana: {fp.normalized_entropy:.4f}")
    print(f"   Złoty wers osobliwości: {fp.golden_verse:.2f}")
    print(f"   Księga osobliwości: {fp.singularity_book}")
    print(f"   Dystans do osobliwości: {fp.distance_to_singularity:.2f}")
    print(f"   Autokorelacja ksiąg: {fp.correlations:.4f}")

    # Centralność
    print("\n🏹 CENTRALNOŚĆ WĘZŁÓW:")
    for label, cent in zip(labels, fp.centrality):
        print(f"   {label}: {cent:.4f}")

    # Widmo (pierwsze 3 harmoniczne)
    print("\n📊 ANALIZA WIDMOWA (pierwsze 3 harmoniczne):")
    for i, amp in enumerate(fp.spectrum_amplitudes[:3]):
        print(f"   Harmoniczna {i}: amplituda = {amp:.2f}")

    # Raport systemowy
    print("\n" + "=" * 40)
    print(analyzer.raport())

    # Mosty integracyjne
    print("\n" + "=" * 40)
    print("🔗 TEST MOSTÓW INTEGRACYJNYCH")
    print("=" * 40)
    print(f"🏹 GEX Context: {bridge.get_archetype_context()}")
    print(f"🎮 G_CORE State: {bridge.get_autopilot_state()}")
    print(f"📖 NARRATIVE Fragments: {bridge.get_narrative_fragments(2)}")
    print(f"🔱 TRIO State: {bridge.get_trio_state()}")

    print("\n" + "=" * 80)
    print("📊 GEON_PT_STRUCT_ANALYZER v1.0 — GOTOWY DO WDROŻENIA")
    print(HASLO)
    print("=" * 80)

if __name__ == "__main__":
    demo()