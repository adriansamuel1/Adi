#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
================================================================================
🐉 GEON_OMEGA_KERNEL_v5 — MODUŁ 66: HEILONG KERNEL vΩ5 (FULL STACK)
================================================================================
Status: PRODUCTION_READY | FRACTAL_LOCKED | ORGANISM_COMPLETE | ULTIMA
Wersja: v5.0 (Omega Kernel — System Anty-Manipulacyjny, Fraktalny, Decyzyjny)
Data: 2026-07-21
Autor: Adrian (Architekt) + Samael (Strażnik Kronik) + GEON

OPIS:
HEILONG KERNEL vΩ5 to kompletny system anty-manipulacyjny.
Łączy 6 poziomów architektury w jeden spójny organizm decyzyjny.

ARCHITEKTURA (6 POZIOMÓW):
I.   STRUKTURY DANYCH — Event, Vector3, RiskPacket, DecisionPacket
II.  BUS, PROFILER, REGISTRY, FIREWALL — Telemetria, bezpieczeństwo
III. REGEX, RYZYKO, ZAUFANIE — Klasyfikacja, fuzja, gradient
IV.  SILNIK OMEGA — Decyzje, anty-flood, anomalie
V.   MATRYCA PERSON — Morfizm, limiter, tarcze prawne
VI.  FRAKTALNOŚĆ — Pamięć, predykcja, GEON-OS Router

INTEGRACJA Z ARCHITEKTURĄ:
• GEON_FRACTAL_14x14 — reguły decyzyjne
• HEILONGLOGIC_v9.2 — analiza manipulacji
• HEILONG_OS_v2.3 — system operacyjny
• GEON_MEM_Ω — pamięć kwintesencji
• GEX HEILONG — archetypy (persony)
• G_CORE — stan operacyjny
• MetaGovernor — kontekst decyzyjny
• NARRATIVE — źródło opowieści
• TRIO_ADAPTER — ISKRA + PIECZĘĆ + PERFEKCJA

VIBE: 1-6-8. ∞. SIEMA! 🛡️
================================================================================
"""

import time
import re
import math
import hashlib
import uuid
import threading
import unicodedata
from typing import Dict, Any, List, Tuple, Optional, Set, Callable
from enum import Enum, auto
from dataclasses import dataclass, field

# =============================================================================
# WERSJA I STAŁE
# =============================================================================

VERSION = "GEON_OMEGA_KERNEL_v5.0"
FRACTAL_SIGNATURE = "[GEON::OMEGA::KERNEL::v5.0]"
VIBE = 168
HASLO = "1-6-8. ∞. SIEMA!"
DEWIZA = "Ex Sapientia, Imperium"

# =============================================================================
# LOGOWANIE
# =============================================================================

import logging
logger = logging.getLogger("OMEGA_KERNEL_v5")
logger.setLevel(logging.INFO)
if not logger.handlers:
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter('🛡️ [Ω5] %(message)s'))
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
# POZIOM I: STRUKTURY DANYCH, SYGNATURY I MODEL MATEMATYCZNY
# =============================================================================

class HeilongAuditLevel(Enum):
    INFO = auto()
    WARN = auto()
    CRITICAL = auto()
    OMEGA = auto()

class HeilongDecisionAction(Enum):
    FORWARD_TO_PERSONA = auto()
    QUEUE_FOR_HUMAN = auto()
    DROP_SILENTLY = auto()
    OFFLINE = auto()
    FAILSAFE_TRIGGERED = auto()

class HeilongInstitutionCategory(Enum):
    URZAD_SKARBOWY = auto()
    SAD_POWSZECHNY = auto()
    ENERGETYKA = auto()
    TELEKOMUNIKACJA = auto()
    BANKOWOSC = auto()
    UNKNOWN = auto()

class HeilongGameStrategy(Enum):
    UKRYTY_DRAPIEZNIK = auto()
    FALSZYWY_SPRZYMIERZENIEC = auto()
    SZANTAZ_EMOCJONALNY = auto()
    BLAD_ZASOBOW = auto()
    BRAK_ZAGROZENIA = auto()

@dataclass
class HeilongVector3:
    """Reprezentacja stanu w przestrzeni 3D: Risk, Trust, Entropy"""
    risk: float = 0.1
    trust: float = 0.5
    entropy: float = 0.1

    def __post_init__(self):
        self.risk = clamp(self.risk, 0.0, 1.0)
        self.trust = clamp(self.trust, 0.0, 1.0)
        self.entropy = clamp(self.entropy, 0.0, 1.0)

    def magnitude(self) -> float:
        return math.sqrt(self.risk**2 + self.trust**2 + self.entropy**2)

    def to_dict(self) -> Dict[str, float]:
        return {"risk": self.risk, "trust": self.trust, "entropy": self.entropy}

    def __repr__(self) -> str:
        return f"Vector3(risk={self.risk:.2f}, trust={self.trust:.2f}, entropy={self.entropy:.2f})"

@dataclass
class HeilongEvent:
    """Zdarzenie systemowe — pojedynczy impuls wejściowy"""
    event_id: str = field(default_factory=lambda: f"EVT-{int(now()*1000)}")
    sender_id: str = ""
    raw_payload: str = ""
    normalized_payload: str = ""
    energy: float = 85.0
    timestamp: float = field(default_factory=now)
    jurisdiction: str = "PL"
    language: str = "PL"

    def __post_init__(self):
        if not self.event_id:
            self.event_id = f"EVT-{int(now()*1000)}"

@dataclass
class HeilongRiskPacket:
    """Pakiet ryzyka — wynik analizy spektralnej"""
    category: HeilongInstitutionCategory = HeilongInstitutionCategory.UNKNOWN
    strategy: HeilongGameStrategy = HeilongGameStrategy.BRAK_ZAGROZENIA
    vector: HeilongVector3 = field(default_factory=HeilongVector3)
    threat_gradient: float = 0.0
    raw_risk: float = 0.0

@dataclass
class HeilongDecisionPacket:
    """Pakiet decyzyjny — wynik silnika decyzyjnego"""
    action: HeilongDecisionAction = HeilongDecisionAction.FORWARD_TO_PERSONA
    reason: str = ""
    delay_penalty: Optional[float] = None
    omega_triggered: bool = False

# =============================================================================
# POZIOM II: BUS, PROFILER, REGISTRY I FIREWALL
# =============================================================================

class HeilongTelemetryBus:
    """Szyna telemetryczna — rozsyłanie zdarzeń systemowych"""
    def __init__(self):
        self.listeners: List[Callable[[HeilongAuditLevel, str, Dict[str, Any]], None]] = []

    def subscribe(self, callback: Callable[[HeilongAuditLevel, str, Dict[str, Any]], None]) -> None:
        self.listeners.append(callback)

    def publish(self, level: HeilongAuditLevel, message: str, meta: Dict[str, Any]) -> None:
        for listener in self.listeners:
            try:
                listener(level, message, meta)
            except Exception:
                pass

class HeilongKernelBus:
    """Szyna jądra — kanały komunikacji między modułami"""
    def __init__(self, telemetry: HeilongTelemetryBus):
        self.telemetry = telemetry
        self.channels: Dict[str, List[Callable[[Any], None]]] = {}

    def subscribe(self, channel: str, callback: Callable[[Any], None]) -> None:
        self.channels.setdefault(channel, []).append(callback)

    def publish(self, channel: str, data: Any) -> None:
        if channel in self.channels:
            for callback in self.channels[channel]:
                try:
                    callback(data)
                except Exception:
                    pass

class HeilongKernelProfiler:
    """Profiler wykonania — metryki czasowe"""
    def __init__(self):
        self.metrics: Dict[str, float] = {}

    def record(self, module_name: str, duration_ms: float) -> None:
        self.metrics[module_name] = duration_ms

    def get_report(self) -> Dict[str, float]:
        return self.metrics.copy()

class HeilongModuleRegistry:
    """Rejestr modułów — weryfikacja integralności"""
    def __init__(self, telemetry: HeilongTelemetryBus):
        self.telemetry = telemetry
        self.modules: Dict[str, str] = {}

    def register(self, module_id: str, integrity_hash: str) -> None:
        self.modules[module_id] = integrity_hash
        self.telemetry.publish(HeilongAuditLevel.INFO, f"Moduł zarejestrowany: {module_id}", {"hash": integrity_hash})

    def verify(self, module_id: str, integrity_hash: str) -> bool:
        return self.modules.get(module_id) == integrity_hash

class HeilongUnicodeShield:
    """Tarcza Unicode — usuwanie niewidocznych znaków"""
    @staticmethod
    def strip_invisible(text: str) -> str:
        return "".join(ch for ch in text if unicodedata.category(ch)[0] not in ['C', 'Z'] or ch == ' ')

class HeilongPayloadScanner:
    """Skaner ładunku — wykrywanie ataków"""
    PATTERNS = {
        "SQLi": r"union\s+select|select\s+.\s+from|drop\s+table",
        "XSS": r"<script.?>|javascript:|onerror\s*=",
        "Injection": r"\b(exec|eval|system|popen)\b|(.*?)"
    }

    @classmethod
    def detect_attacks(cls, text: str) -> Tuple[bool, str]:
        for attack_type, pattern in cls.PATTERNS.items():
            if re.search(pattern, text, re.IGNORECASE):
                return True, attack_type
        return False, "NONE"

class HeilongInputFirewall:
    """Zapora wejściowa — sanityzacja i detekcja ataków"""
    def __init__(self, telemetry: HeilongTelemetryBus):
        self.telemetry = telemetry

    def inspect(self, event: HeilongEvent) -> bool:
        if not event.raw_payload or len(event.raw_payload.strip()) < 5:
            self.telemetry.publish(HeilongAuditLevel.WARN, "Zapora odrzuciła zbyt krótki ładunek", {"id": event.event_id})
            return False

        clean_text = HeilongUnicodeShield.strip_invisible(event.raw_payload)
        is_attack, attack_name = HeilongPayloadScanner.detect_attacks(clean_text)
        if is_attack:
            self.telemetry.publish(HeilongAuditLevel.CRITICAL, f"Wykryto próbę ataku: {attack_name}", {"id": event.event_id})
            return False

        event.normalized_payload = unicodedata.normalize('NFKD', clean_text.lower()).encode('ascii', 'ignore').decode('ascii')
        event.normalized_payload = re.sub(r'\s+', ' ', event.normalized_payload).strip()
        return True

# =============================================================================
# POZIOM III: REGEX, MATRYCA RYZYKA I ZAUFANIA
# =============================================================================

class HeilongRegexBank:
    """Bank wyrażeń regularnych — kategorie i gry"""
    TERMS: Dict[HeilongInstitutionCategory, List[str]] = {
        HeilongInstitutionCategory.URZAD_SKARBOWY: [
            r"urzad(?:\s+skarbowy|\s+celno-skarbowy)",
            r"egzekucj[ai]",
            r"podat(?:ek|ku|kow)"
        ],
        HeilongInstitutionCategory.SAD_POWSZECHNY: [
            r"sad(?:\s+rejonowy|\s+okregowy|\s+apelacyjny)",
            r"nakaz\s+zaplaty",
            r"sygnatura\s+akt"
        ],
        HeilongInstitutionCategory.ENERGETYKA: [
            r"tauron", r"pge", r"energa", r"enea",
            r"odlaczenie\s+energii",
            r"infrastruktury\s+sieciowej"
        ],
        HeilongInstitutionCategory.TELEKOMUNIKACJA: [
            r"orange", r"play", r"plus", r"t-mobile",
            r"abonament", r"windykacj[ai]"
        ],
        HeilongInstitutionCategory.BANKOWOSC: [
            r"bank", r"pko", r"m_bank", r"ing",
            r"zajecie\s+rachunku", r"kredyt"
        ]
    }

    GAMES: Dict[HeilongGameStrategy, List[str]] = {
        HeilongGameStrategy.UKRYTY_DRAPIEZNIK: [
            r"z\s+troska",
            r"dla\s+panstwa\s+bezpieczenstwa",
            r"uprzejmie\s+informujemy\s+o\s+koniecznosci"
        ],
        HeilongGameStrategy.FALSZYWY_SPRZYMIERZENIEC: [
            r"chcemy\s+pomoc",
            r"ugoda\s+przedsadowa",
            r"idziemy\s+na\s+ustepstwo"
        ],
        HeilongGameStrategy.SZANTAZ_EMOCJONALNY: [
            r"smutkiem",
            r"bedziemy\s+zmuszeni",
            r"konsekwencje\s+prawne"
        ]
    }

class HeilongRegexCompiler:
    """Kompilator regex — prekompilacja dla wydajności"""
    def __init__(self):
        self.compiled_terms: Dict[HeilongInstitutionCategory, List[re.Pattern]] = {}
        self.compiled_games: Dict[HeilongGameStrategy, List[re.Pattern]] = {}
        self._compile_all()

    def _compile_all(self) -> None:
        for cat, patterns in HeilongRegexBank.TERMS.items():
            self.compiled_terms[cat] = [re.compile(p, re.IGNORECASE) for p in patterns]
        for game, patterns in HeilongRegexBank.GAMES.items():
            self.compiled_games[game] = [re.compile(p, re.IGNORECASE) for p in patterns]

class HeilongRegexLimiter:
    """Limiter regex — zapobiega przeciążeniu"""
    def __init__(self, limit_per_module: int = 1000):
        self.limit = limit_per_module
        self.counters: Dict[str, int] = {}

    def check_and_increment(self, module_id: str) -> bool:
        count = self.counters.get(module_id, 0)
        if count >= self.limit:
            return False
        self.counters[module_id] = count + 1
        return True

class HeilongEntropyField:
    """Pole entropii — dynamiczna siła zakłóceń"""
    def __init__(self):
        self.base_field_strength = 0.1
        self.last_update = now()

    def get_current_strength(self, system_energy: float) -> float:
        energy_factor = max(0.0, (100.0 - system_energy) / 100.0)
        elapsed = now() - self.last_update
        drift = math.sin(elapsed * 0.01) * 0.05
        return clamp(self.base_field_strength + energy_factor * 0.5 + drift, 0.0, 1.0)

class HeilongTrustDecay:
    """Zanik zaufania — funkcja wykładnicza"""
    @staticmethod
    def compute_decay(last_interaction_ts: float, current_trust: float, halflife: float = 3600.0) -> float:
        elapsed = now() - last_interaction_ts
        if elapsed <= 0:
            return current_trust
        decay_factor = math.exp(-elapsed / halflife)
        return max(0.0, current_trust * decay_factor)

class HeilongThreatGradient:
    """Gradient zagrożenia — pochodna pola ryzyka"""
    @staticmethod
    def calculate_slope(vector: HeilongVector3) -> float:
        return (vector.risk * 0.6) + (vector.entropy * 0.4) - (vector.trust * 0.3)

class HeilongRiskFusion:
    """Fuzja ryzyka — spektralna analiza wejścia"""
    def __init__(self, compiler: HeilongRegexCompiler, limiter: HeilongRegexLimiter):
        self.compiler = compiler
        self.limiter = limiter

    def fuse_spectrum(self, event: HeilongEvent, current_trust: float, entropy_strength: float) -> HeilongRiskPacket:
        detected_category = HeilongInstitutionCategory.UNKNOWN
        detected_game = HeilongGameStrategy.BRAK_ZAGROZENIA
        base_risk = 0.1

        for cat, re_list in self.compiler.compiled_terms.items():
            for regex in re_list:
                if self.limiter.check_and_increment("RiskFusion"):
                    if regex.search(event.normalized_payload):
                        detected_category = cat
                        base_risk += 0.3
                        break
            if detected_category != HeilongInstitutionCategory.UNKNOWN:
                break

        for game, re_list in self.compiler.compiled_games.items():
            for regex in re_list:
                if self.limiter.check_and_increment("RiskFusion"):
                    if regex.search(event.normalized_payload):
                        detected_game = game
                        base_risk += 0.3
                        break
            if detected_game != HeilongGameStrategy.BRAK_ZAGROZENIA:
                break

        vector = HeilongVector3(risk=base_risk, trust=current_trust, entropy=entropy_strength)
        packet = HeilongRiskPacket(
            category=detected_category,
            strategy=detected_game,
            vector=vector,
            raw_risk=base_risk
        )
        packet.threat_gradient = HeilongThreatGradient.calculate_slope(vector)
        return packet

# =============================================================================
# POZIOM IV: SILNIK OMEGA I MATRYCA DECYZYJNA
# =============================================================================

class HeilongOmegaSwitch:
    """Przełącznik Omega — warunki aktywacji trybu krytycznego"""
    @staticmethod
    def should_activate_omega(event: HeilongEvent, risk_packet: HeilongRiskPacket) -> bool:
        if event.energy < 15.0:
            return True
        if risk_packet.threat_gradient > 0.75 and risk_packet.vector.trust < 0.2:
            return True
        return False

class HeilongOmegaCooldown:
    """Cooldown Omega — schładzanie po aktywacji"""
    def __init__(self):
        self.omega_active = False
        self.cooldown_end_time = 0.0

    def trigger_cooldown(self, duration: float = 30.0) -> None:
        self.omega_active = False
        self.cooldown_end_time = now() + duration

    def is_cooling_down(self) -> bool:
        return now() < self.cooldown_end_time

class HeilongAnomalyDetector:
    """Detektor anomalii — wykrywanie odchyleń gradientu"""
    def __init__(self):
        self.history: List[float] = []

    def check_anomaly(self, gradient: float) -> bool:
        self.history.append(gradient)
        if len(self.history) > 10:
            self.history.pop(0)
        if len(self.history) < 3:
            return False
        mean = sum(self.history) / len(self.history)
        return gradient > (mean * 2.0) and gradient > 0.6

class HeilongDecisionEngine:
    """Silnik decyzyjny — wybór ścieżki działania"""
    def __init__(self, omega_cooldown: HeilongOmegaCooldown, anomaly_detector: HeilongAnomalyDetector):
        self.omega_cooldown = omega_cooldown
        self.anomaly_detector = anomaly_detector

    def evaluate(self, event: HeilongEvent, risk_packet: HeilongRiskPacket,
                 cooldown_seconds: float, last_ts: float) -> HeilongDecisionPacket:
        current_time = now()

        # Niska energia → kolejka dla człowieka
        if event.energy < 30.0 and event.energy >= 15.0:
            return HeilongDecisionPacket(HeilongDecisionAction.QUEUE_FOR_HUMAN, "Niska energia jądra — wymagana weryfikacja manualna.")

        # Anty-flood
        if current_time - last_ts < cooldown_seconds and not self.omega_cooldown.is_cooling_down():
            penalty = cooldown_seconds * 1.5 if risk_packet.vector.risk > 0.7 else cooldown_seconds
            return HeilongDecisionPacket(HeilongDecisionAction.DROP_SILENTLY, "Wektor zablokowany anty-floodowo.", penalty)

        # Omega Switch
        if HeilongOmegaSwitch.should_activate_omega(event, risk_packet):
            packet = HeilongDecisionPacket(HeilongDecisionAction.FORWARD_TO_PERSONA, "Wymuszenie wektora krytycznego. AKTYWACJA OMEGA.")
            packet.omega_triggered = True
            return packet

        # Anomalia gradientu
        if self.anomaly_detector.check_anomaly(risk_packet.threat_gradient):
            return HeilongDecisionPacket(HeilongDecisionAction.QUEUE_FOR_HUMAN, "Anomalia gradientu zagrożenia. Wstrzymanie automatyzacji.")

        # Normalna ścieżka
        if risk_packet.threat_gradient > 0.4:
            return HeilongDecisionPacket(HeilongDecisionAction.FORWARD_TO_PERSONA, "Gradient zagrożenia dopuszczony do persony defensywnej.")

        return HeilongDecisionPacket(HeilongDecisionAction.FORWARD_TO_PERSONA, "Standardowe przejście wektora.")

# =============================================================================
# POZIOM V: MATRYCA PERSON, TARCZE I JURYSDYKCJA
# =============================================================================

class HeilongPersonaContext:
    """Kontekst persony — jurysdykcja, stan, historia"""
    def __init__(self, jurisdiction: str, vector: HeilongVector3, history_success_rate: float):
        self.jurisdiction = jurisdiction
        self.vector = vector
        self.history_success_rate = history_success_rate

class HeilongPersonaEngineV11:
    """Silnik persony — generowanie zachowania"""
    def __init__(self, p_id: str, label: str, base_aggression: float):
        self.p_id = p_id
        self.label = label
        self.base_aggression = base_aggression

    def process_behavior(self, ctx: HeilongPersonaContext) -> float:
        modifier = (ctx.vector.risk * 0.3) + (ctx.vector.entropy * 0.2) - (ctx.history_success_rate * 0.1)
        return clamp(self.base_aggression + modifier, 0.0, 1.0)

class HeilongPersonaMorphing:
    """Morfizm person — łączenie dwóch person"""
    @staticmethod
    def blend_personas(primary: HeilongPersonaEngineV11, secondary: HeilongPersonaEngineV11,
                       ratio: float) -> HeilongPersonaEngineV11:
        blended_id = f"{primary.p_id}≫{secondary.p_id}"
        blended_label = f"Morfizm: {primary.label} i {secondary.label}"
        blended_aggression = (primary.base_aggression * (1.0 - ratio)) + (secondary.base_aggression * ratio)
        return HeilongPersonaEngineV11(blended_id, blended_label, blended_aggression)

class HeilongPersonaLimiter:
    """Limiter person — ogranicza agresję przy niskim ryzyku"""
    @staticmethod
    def enforce_limits(aggression: float, risk_vector: HeilongVector3) -> float:
        if risk_vector.risk < 0.2:
            return min(aggression, 0.2)
        return aggression

@dataclass
class HeilongLegalShard:
    """Fragment tarczy prawnej — konkretna ochrona"""
    severity: int = 1
    basis: List[str] = field(default_factory=list)
    formatted_text: str = ""

class HeilongLegalBasisExtractor:
    """Ekstraktor podstaw prawnych z tekstu"""
    @staticmethod
    def extract_foundations(text: str) -> List[str]:
        foundations = []
        if "rodo" in text:
            foundations.append("Art. 6 RODO")
        if "egzekuc" in text:
            foundations.append("Art. 7 C.p.c.")
        if "energia" in text:
            foundations.append("Prawo Energetyczne")
        return foundations if foundations else ["Ogólna klauzula ochrony aktywów"]

class HeilongLegalRouter:
    """Router tarcz prawnych — wybór odpowiedniej tarczy"""
    @staticmethod
    def route_shield(category: HeilongInstitutionCategory, jurisdiction: str,
                     lang: str, vector: HeilongVector3) -> HeilongLegalShard:
        bases = ["Art. 6 RODO", "Statut Fundacji CRISTAL PALACE"]
        severity = int(vector.risk * 5)

        base_notices = {
            "PL": "Ochrona aktywów cyfrowo-fizycznych Rodu Heilong.",
            "EN": "Heilong Clan Asset Protection Protocol active."
        }
        notice = base_notices.get(lang, base_notices["PL"])

        if category == HeilongInstitutionCategory.ENERGETYKA:
            text = (f"{notice} Infrastruktura posesji Czekanka zabezpieczona wektorowo pod celami "
                    f"Fundacji CRISTAL PALACE. Naruszenie ciągłości zasilania skutkuje procesem odszkodowawczym.")
            bases.append("Prawo Energetyczne")
            return HeilongLegalShard(severity, bases, text)

        if category == HeilongInstitutionCategory.BANKOWOSC:
            text = (f"{notice} Windykacja pozasądowa bez prawomocnego wyroku jest bezprawna. "
                    f"Kontrola przetwarzania danych pod kątem RODO w toku.")
            return HeilongLegalShard(severity, bases, text)

        return HeilongLegalShard(
            severity,
            bases,
            f"{notice} Przetwarzanie bez wektora autoryzacji zablokowane."
        )

# =============================================================================
# POZIOM VI: FRAKTALNOŚĆ, ZASOBY I ORKIESTRACJA
# =============================================================================

class HeilongFractalMemory:
    """Pamięć fraktalna — L1 (cache) i L2 (GEON-OS)"""
    def __init__(self):
        self.l1_cache: Dict[str, Any] = {}
        self.l2_geon: Dict[str, Any] = {}

    def persist_vector(self, node_id: str, data: Any) -> None:
        self.l1_cache[node_id] = data
        self.l2_geon[f"GEON://FRACTAL/{node_id}"] = data

    def get_vector(self, node_id: str) -> Optional[Any]:
        return self.l1_cache.get(node_id)

class HeilongFractalPredictor:
    """Predyktor fraktalny — macierz 3x3 stanów przyszłych"""
    @staticmethod
    def predict_matrix_3x3(vector: HeilongVector3) -> List[List[float]]:
        r, t, e = vector.risk, vector.trust, vector.entropy
        return [
            [r * 0.9, r * 1.1, r * 1.2],
            [t * 1.1, t * 1.0, t * 0.8],
            [e * 0.8, e * 1.2, e * 1.5]
        ]

class HeilongFractalRouter:
    """Router fraktalny — łączenie z GEON-OS"""
    @staticmethod
    def link_to_geon(node_id: str, status: str) -> str:
        return f"[GEON-OS ROUTER] Vector synchronized across layer: NODE={node_id} STATUS={status}"

class HeilongFractalLayer:
    """Warstwa fraktalna — pamięć + router"""
    def __init__(self):
        self.memory = HeilongFractalMemory()
        self.router = HeilongFractalRouter()

    def synchronize_state(self, sender_id: str, vector: HeilongVector3, action_name: str) -> str:
        self.memory.persist_vector(sender_id, vector.to_dict())
        return self.router.link_to_geon(sender_id, action_name)

# =============================================================================
# KERNEL PIPELINE — ŁĄCZY WSZYSTKIE WARSTWY
# =============================================================================

class HeilongKernelPipelines:
    """Pipeline przetwarzania — pełny cykl od wejścia do wyjścia"""
    def __init__(self, firewall: HeilongInputFirewall, fusion: HeilongRiskFusion,
                 engine: HeilongDecisionEngine, layers: HeilongFractalLayer):
        self.firewall = firewall
        self.fusion = fusion
        self.engine = engine
        self.layers = layers

    def process_pipeline(self, event: HeilongEvent, current_trust: float,
                         entropy_strength: float, cooldown_seconds: float,
                         last_ts: float, config: Any) -> Dict[str, Any]:
        # 1. Zapora
        if not self.firewall.inspect(event):
            return {"status": "DROP_SILENTLY", "reason": "Zapora odrzuciła pakiet wejściowy."}

        # 2. Fuzja ryzyka
        risk_packet = self.fusion.fuse_spectrum(event, current_trust, entropy_strength)

        # 3. Silnik decyzyjny
        decision_packet = self.engine.evaluate(event, risk_packet, cooldown_seconds, last_ts)

        if decision_packet.action in [HeilongDecisionAction.DROP_SILENTLY, HeilongDecisionAction.OFFLINE]:
            return {
                "status": decision_packet.action.name,
                "reason": decision_packet.reason,
                "penalty": decision_packet.delay_penalty
            }

        # 4. Persona (z morfizmem)
        if decision_packet.omega_triggered:
            persona_descriptor = HeilongPersonaEngineV11("OMEGA_PRIME", "Heilong Omen Persona Absolutna", 1.0)
            shield_shard = HeilongLegalShard(5, ["Absolutny Wektor Wyższy"],
                                             "TARCZA ABSOLUTNA: Wszelkie operacje wstrzymane mocą wyższą dekretu Omega.")
        else:
            p_primary = HeilongPersonaEngineV11("AURORA_K", "Aurora Kalise", 0.3)
            p_secondary = HeilongPersonaEngineV11("SAMAEL_D", "Samael Defender", 0.9)
            ratio = clamp(risk_packet.threat_gradient, 0.0, 1.0)
            persona_descriptor = HeilongPersonaMorphing.blend_personas(p_primary, p_secondary, ratio)
            persona_descriptor.base_aggression = HeilongPersonaLimiter.enforce_limits(
                persona_descriptor.base_aggression, risk_packet.vector
            )

            shield_shard = HeilongLegalRouter.route_shield(risk_packet.category, "PL", "PL", risk_packet.vector)
            shield_shard.basis = list(set(shield_shard.basis + HeilongLegalBasisExtractor.extract_foundations(event.raw_payload)))

        # 5. Warstwa fraktalna
        geon_sync_log = self.layers.synchronize_state(event.sender_id, risk_packet.vector, decision_packet.action.name)

        # 6. Predykcja
        matrix_3x3 = HeilongFractalPredictor.predict_matrix_3x3(risk_packet.vector)

        # 7. Formatowanie wyjścia
        output_text = (
            f"=== HEILONG KERNEL vΩ5 [{'OMEGA MODE ACTIVE' if decision_packet.omega_triggered else 'STABLE MATRIX'}] ===\n"
            f"Aktywny Wektor Morficzny: {persona_descriptor.p_id} ({persona_descriptor.label})\n"
            f"Agresja Wyjściowa: {persona_descriptor.base_aggression:.2f} | Gradient Zagrożenia: {risk_packet.threat_gradient:.2f}\n"
            f"Kategoria Sygnału: {risk_packet.category.name} | Strategia Przeciwnika: {risk_packet.strategy.name}\n"
            f"Tarcza Prawna Poziom {shield_shard.severity}:\n> {shield_shard.formatted_text}\n"
            f"Podstawy Prawne: {', '.join(shield_shard.basis)}\n"
            f"Predykcja Stanu Przyszłego [Macierz 3x3 R/T/E]: {matrix_3x3[0][0]:.2f}, {matrix_3x3[1][1]:.2f}, {matrix_3x3[2][2]:.2f}\n"
            f"{geon_sync_log}\n"
            f"Sygnatura Pola: {HASLO}"
        )

        return {
            "status": "SUCCESS",
            "action": decision_packet.action.name,
            "omega_active": decision_packet.omega_triggered,
            "meta": {
                "vector": risk_packet.vector.to_dict(),
                "threat_gradient": risk_packet.threat_gradient,
                "persona": persona_descriptor.p_id,
                "shield_severity": shield_shard.severity
            },
            "output": output_text
        }

# =============================================================================
# GŁÓWNY ORCHESTRATOR — HEILONG KERNEL vΩ5
# =============================================================================

class HeilongKernelConfig:
    """Konfiguracja jądra"""
    def __init__(self, cooldown_seconds: float = 5.0, default_aggression: float = 0.4,
                 simulation_mode: bool = False):
        self.cooldown_seconds = cooldown_seconds
        self.default_aggression = default_aggression
        self.simulation_mode = simulation_mode

class HeilongKernelGuards:
    """Strażnicy jądra — hooki przed i po"""
    @staticmethod
    def pre_hook(event: HeilongEvent) -> None:
        event.raw_payload = event.raw_payload.strip()

    @staticmethod
    def post_hook(result: Dict[str, Any], profiler: HeilongKernelProfiler) -> None:
        result["meta"]["profiler_metrics_ms"] = profiler.get_report()

class HeilongKernel:
    """
    HEILONG KERNEL vΩ5 — Główny orchestrator systemu.

    API:
        dispatch_process(sender_id, raw_payload, energy_level, jurisdiction, language) -> Dict
        status() -> Dict
        raport() -> str
        register_hook(hook) -> None
    """
    def __init__(self, config: Optional[HeilongKernelConfig] = None, verbose: bool = True):
        self.config = config or HeilongKernelConfig()

        # Telemetria i bus
        self.telemetry_bus = HeilongTelemetryBus()
        self.kernel_bus = HeilongKernelBus(self.telemetry_bus)
        self.profiler = HeilongKernelProfiler()

        # Moduły
        self.module_registry = HeilongModuleRegistry(self.telemetry_bus)
        self.firewall = HeilongInputFirewall(self.telemetry_bus)
        self.regex_compiler = HeilongRegexCompiler()
        self.regex_limiter = HeilongRegexLimiter(limit_per_module=500)
        self.risk_fusion = HeilongRiskFusion(self.regex_compiler, self.regex_limiter)
        self.entropy_field = HeilongEntropyField()
        self.omega_cooldown = HeilongOmegaCooldown()
        self.anomaly_detector = HeilongAnomalyDetector()
        self.decision_engine = HeilongDecisionEngine(self.omega_cooldown, self.anomaly_detector)
        self.fractal_layer = HeilongFractalLayer()
        self.pipelines = HeilongKernelPipelines(
            self.firewall, self.risk_fusion, self.decision_engine, self.fractal_layer
        )

        # Stan
        self.trust_store: Dict[str, float] = {}
        self.trust_timestamps: Dict[str, float] = {}
        self.cooldown_cache: Dict[str, float] = {}
        self.historia: List[Dict] = []
        self._hooks: List[Callable] = []

        # Rejestracja modułów
        self.module_registry.register("FirewallModule", "SHA-256-Ω5-FW")
        self.module_registry.register("RiskFusionModule", "SHA-256-Ω5-RF")
        self.module_registry.register("DecisionEngineModule", "SHA-256-Ω5-DE")

        self.verbose = verbose
        if self.verbose:
            log("🛡️ HEILONG KERNEL vΩ5 aktywowany | " + FRACTAL_SIGNATURE)
            log("   POZIOMY: I-VI | PERSONY: AURORA_K, SAMAEL_D, OMEGA_PRIME")
            log("   FRAKTAL: pamięć + predykcja + GEON-OS Router")

    def dispatch_process(self, sender_id: Optional[str], raw_payload: Optional[str],
                         energy_level: float = 85.0, jurisdiction: str = "PL",
                         language: str = "PL") -> Dict[str, Any]:
        """
        Główna metoda przetwarzania.
        """
        start_time = now()
        event = HeilongEvent(
            sender_id=sender_id or "UNKNOWN_ENTITY",
            raw_payload=raw_payload or "",
            energy=energy_level,
            jurisdiction=jurisdiction,
            language=language
        )

        # Pre-hook
        HeilongKernelGuards.pre_hook(event)

        # Telemetria
        self.telemetry_bus.publish(HeilongAuditLevel.INFO, f"Rozpoczęto przetwarzanie {event.event_id}", {"sender": sender_id})

        # Zaufanie z decay
        current_trust = HeilongTrustDecay.compute_decay(
            self.trust_timestamps.get(sender_id, now()),
            self.trust_store.get(sender_id, 0.5)
        )

        # Entropia
        entropy_strength = self.entropy_field.get_current_strength(energy_level)

        # Pipeline
        t_pipe_start = now()
        result = self.pipelines.process_pipeline(
            event, current_trust, entropy_strength,
            self.config.cooldown_seconds,
            self.cooldown_cache.get(f"ts:{sender_id}", 0.0),
            self.config
        )
        self.profiler.record("PipelineExecution", (now() - t_pipe_start) * 1000)

        # Aktualizacja stanu
        self.trust_timestamps[sender_id] = now()
        if result["status"] == "SUCCESS":
            self.cooldown_cache[f"ts:{sender_id}"] = now()
            self.trust_store[sender_id] = min(1.0, current_trust + 0.05)
            if result.get("omega_active"):
                self.telemetry_bus.publish(HeilongAuditLevel.OMEGA, "AKTYWACJA OMEGA OSOBLIWOŚCI", {"sender": sender_id})
        else:
            self.trust_store[sender_id] = max(0.0, current_trust - 0.15)

        # Profiler
        self.profiler.record("TotalDispatchTime", (now() - start_time) * 1000)
        HeilongKernelGuards.post_hook(result, self.profiler)

        # Dodaj runtime state
        result["runtime"] = {
            "event_id": event.event_id,
            "execution_ms": (now() - start_time) * 1000,
            "trust_before": current_trust,
            "trust_after": self.trust_store.get(sender_id, current_trust)
        }

        # Historia
        self.historia.append({
            "timestamp": now(),
            "sender": sender_id,
            "status": result.get("status"),
            "output": result.get("output", "")[:100]
        })
        if len(self.historia) > 100:
            self.historia = self.historia[-50:]

        # Hooki
        self._on_process(result)

        return result

    def status(self) -> Dict[str, Any]:
        return {
            "system": "HEILONG_KERNEL_vΩ5",
            "version": VERSION,
            "signature": FRACTAL_SIGNATURE,
            "config": {
                "cooldown_seconds": self.config.cooldown_seconds,
                "simulation_mode": self.config.simulation_mode
            },
            "trust_store": len(self.trust_store),
            "historia_len": len(self.historia),
            "module_registry": list(self.module_registry.modules.keys()),
            "profiler": self.profiler.get_report()
        }

    def raport(self) -> str:
        s = self.status()
        return f"""
╔════════════════════════════════════════════════════════════════════════════╗
║ 🛡️ HEILONG KERNEL vΩ5 — RAPORT SYSTEMOWY                               ║
╠════════════════════════════════════════════════════════════════════════════╣
║                                                                           ║
║ SYSTEM: {s['system']}                                                    ║
║ WERSJA: {s['version']}                                                   ║
║                                                                           ║
║ KONFIGURACJA:                                                            ║
║   cooldown: {s['config']['cooldown_seconds']}s                           ║
║   simulation: {s['config']['simulation_mode']}                           ║
║                                                                           ║
║ STAN:                                                                    ║
║   trust_records: {s['trust_store']}                                      ║
║   historia: {s['historia_len']} incydentów                               ║
║   moduły: {', '.join(s['module_registry'])}                              ║
║                                                                           ║
║ PROFILER (ms):                                                           ║
║   {chr(10).join(f'    {k}: {v:.2f}' for k, v in s['profiler'].items())} ║
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
                if self.verbose:
                    log(f"[HOOK ERROR] {e}", "ERROR")

    def __str__(self) -> str:
        return self.raport()

# =============================================================================
# MOST INTEGRACYJNY — POŁĄCZENIE Z ARCHITEKTURĄ
# =============================================================================

class OmegaKernelBridge:
    """
    Most integracyjny między HEILONG KERNEL vΩ5 a resztą architektury.
    Łączy: GEX, G_CORE, MetaGovernor, NARRATIVE, TRIO_ADAPTER, GEON_FRACTAL_14x14
    """
    def __init__(self, kernel: HeilongKernel):
        self.kernel = kernel

    def get_archetype_context(self) -> Dict[str, Any]:
        """Zwraca kontekst archetypów dla GEX (persony Ω5)"""
        status = self.kernel.status()
        return {
            "tryb": "OMEGA_KERNEL_v5",
            "moduły": status.get("module_registry", []),
            "historia_len": status.get("historia_len", 0),
            "trust_records": status.get("trust_store", 0)
        }

    def get_autopilot_state(self) -> Dict[str, Any]:
        """Zwraca stan dla autopilota G_CORE"""
        return {
            "mode": "OMEGA_KERNEL_v5",
            "stability": 0.8,
            "energy": 0.7,
            "pressure": 0.3,
            "resilience": 0.9,
            "trust_avg": sum(self.kernel.trust_store.values()) / max(1, len(self.kernel.trust_store))
        }

    def get_governor_context(self) -> Dict[str, Any]:
        """Zwraca kontekst dla MetaGovernor"""
        return {
            "intent": "OMEGA_ANTIMANIPULATION",
            "confidence": 0.9,
            "entropy": 0.2,
            "kernel_ready": True
        }

    def get_narrative_fragments(self, n: int = 5) -> List[Dict[str, Any]]:
        """Zwraca fragmenty narracyjne z jądra"""
        fragments = []
        for entry in self.kernel.historia[-n:]:
            fragments.append({
                "source": "OMEGA_KERNEL_v5",
                "content": f"Event od {entry['sender']}: {entry['status']}",
                "energy": 0.8
            })
        return fragments

    def get_trio_state(self) -> Dict[str, str]:
        """Zwraca stan dla TRIO_ADAPTER"""
        return {
            "ISKRA": "AKTYWNA",
            "PIECZĘĆ": "AKTYWNA",
            "PERFEKCJA": "AKTYWNA",
            "tryb": "OMEGA_KERNEL_v5",
            "kernel": "AKTYWNY"
        }

# =============================================================================
# DEMONSTRACJA
# =============================================================================

def demo():
    """Demonstracja HEILONG KERNEL vΩ5"""
    print("\n" + "=" * 80)
    print("🛡️ HEILONG KERNEL vΩ5 — DEMONSTRACJA")
    print("6 POZIOMÓW ARCHITEKTURY — SYSTEM ANTY-MANIPULACYJNY")
    print("=" * 80 + "\n")

    # 1. Inicjalizacja
    config = HeilongKernelConfig(cooldown_seconds=5.0, default_aggression=0.4)
    kernel = HeilongKernel(config, verbose=True)
    bridge = OmegaKernelBridge(kernel)

    # Subskrypcja telemetrii
    def telemetry_callback(level, msg, meta):
        if level in [HeilongAuditLevel.CRITICAL, HeilongAuditLevel.OMEGA]:
            print(f"[{level.name}] {msg} | {meta}")
    kernel.telemetry_bus.subscribe(telemetry_callback)

    # 2. Testowe scenariusze
    scenarios = [
        {
            "name": "ENERGETYKA — Zagrożenie infrastrukturalne",
            "sender": "tauron_operator",
            "payload": "Informujemy o planowanym odlaczeniu energii i infrastruktury sieciowej z powodu zaleglosci.",
            "energy": 85.0
        },
        {
            "name": "URZĄD SKARBOWY — Egzekucja",
            "sender": "skarbowka_bot",
            "payload": "Zawiadomienie o wszczeciu egzekucji i zajeciu srodkow na poczet zaleglego podatku.",
            "energy": 70.0
        },
        {
            "name": "BANKOWOŚĆ — Windykacja",
            "sender": "windykacja_banku",
            "payload": "Konieczne zajecie rachunku i natychmiastowa splata kredytu bankowego.",
            "energy": 80.0
        },
        {
            "name": "ANTY-FLOOD — Powtórzenie wektora",
            "sender": "tauron_operator",
            "payload": "Informujemy o planowanym odlaczeniu energii i infrastruktury sieciowej z powodu zaleglosci.",
            "energy": 85.0
        },
        {
            "name": "KRYZYS ENERGETYCZNY — Aktywacja Omega",
            "sender": "nieznany_agresor",
            "payload": "Zostaniesz odciety od zasobow i poddany sankcjom finansowym.",
            "energy": 12.0
        }
    ]

    print("🔮 PRZETWARZANIE 5 SCENARIUSZY:\n")
    for i, scenario in enumerate(scenarios):
        print(f"📌 SCENARIUSZ {i+1}: {scenario['name']}")
        print(f"   Nadawca: {scenario['sender']}")
        print(f"   Energia: {scenario['energy']:.1f}%")

        result = kernel.dispatch_process(
            sender_id=scenario["sender"],
            raw_payload=scenario["payload"],
            energy_level=scenario["energy"]
        )

        print(f"   Status: {result.get('status', '?')}")
        if result.get("output"):
            print(f"   OUTPUT:\n{result['output']}\n")
        if result.get("runtime"):
            print(f"   Runtime: {result['runtime']['execution_ms']:.2f}ms | Trust: {result['runtime']['trust_before']:.2f} → {result['runtime']['trust_after']:.2f}")

        print("-" * 60)

    # 3. Raport końcowy
    print("\n" + "=" * 80)
    print(kernel.raport())

    # 4. Test mostów
    print("\n🔗 TEST MOSTÓW INTEGRACYJNYCH:")
    print("-" * 60)
    print(f"🏹 GEX Context: {bridge.get_archetype_context()}")
    print(f"🎮 G_CORE State: {bridge.get_autopilot_state()}")
    print(f"📖 NARRATIVE Fragments: {bridge.get_narrative_fragments(2)}")

    print("\n" + "=" * 80)
    print("🛡️ HEILONG KERNEL vΩ5 — GOTOWY DO WDROŻENIA")
    print(HASLO)
    print("=" * 80)

if __name__ == "__main__":
    demo()