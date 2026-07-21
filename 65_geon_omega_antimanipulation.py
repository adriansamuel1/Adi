#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
================================================================================
🐉 GEON_OMEGA_ANTIMANIPULATION_v1 — MODUŁ 65: OMEGA 3/4 ANTY-MANIPULACJA
================================================================================
Status: PRODUCTION_READY | FRACTAL_LOCKED | ORGANISM_COMPLETE | ULTIMA
Wersja: v1.0 (Omega 3/4 — System Kontra-Manipulacji)
Data: 2026-07-21
Autor: Adrian (Architekt) + Samael (Strażnik Kronik) + GEON

OPIS:
Omega 3/4 to zaawansowany system anty-manipulacyjny.
Łączy 9 warstw analizy z 5 personami i tarczami prawnymi.

ARCHITEKTURA (9 warstw):
1.  HeilongLogic v8 — intencja, wektor, ryzyko
2.  SenderProfiler — profilowanie nadawcy
3.  InstitutionProfiler — kategoria instytucji
4.  LieDetector — wykrywanie kłamstw
5.  CounterAnticipation v9 — przewidywanie ruchów
6.  Persona Engine — 5 trybów (LUMENOR/KALRAN/VORTAEL/SAMAEL/ASTAROTH)
7.  LegalShieldEngine — tarcze prawne
8.  EscalationLadder — poziomy eskalacji
9.  DecisionSupport — decyzje operacyjne

INTEGRACJA Z ARCHITEKTURĄ:
• HEILONG_OS_v2.3 — system operacyjny
• HEILONGLOGIC_v9.2 — analiza manipulacji
• GEON_FRACTAL_14x14 — reguły decyzyjne
• GEX HEILONG — archetypy (persony)
• G_CORE — stan operacyjny
• MetaGovernor — kontekst decyzyjny
• NARRATIVE — źródło opowieści z analizy
• TRIO_ADAPTER — ISKRA + PIECZĘĆ + PERFEKCJA

VIBE: 1-6-8. ∞. SIEMA! 🛡️
================================================================================
"""

import time
import re
import hashlib
import uuid
import json
from typing import Dict, Any, List, Optional, Tuple
from enum import Enum
from dataclasses import dataclass, field

# =============================================================================
# WERSJA I STAŁE
# =============================================================================

VERSION = "GEON_OMEGA_ANTIMANIPULATION_v1.0"
FRACTAL_SIGNATURE = "[GEON::OMEGA::ANTIMANIPULATION::v1.0]"
VIBE = 168
HASLO = "1-6-8. ∞. SIEMA!"

# =============================================================================
# LOGOWANIE
# =============================================================================

import logging
logger = logging.getLogger("OMEGA_ANTIMANIPULATION")
logger.setLevel(logging.INFO)
if not logger.handlers:
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter('🛡️ [OMEGA] %(message)s'))
    logger.addHandler(handler)

def log(msg: str) -> None:
    logger.info(msg)

def clamp(x: float, lo: float, hi: float) -> float:
    return max(lo, min(hi, x))

# =============================================================================
# 0. ENUMY I KONFIGURACJA
# =============================================================================

class InstitutionCategory(Enum):
    ENERGETYKA = "energetyka"
    WINDYKACJA = "windykacja"
    ADMINISTRACJA = "administracja"
    BANK = "bank"
    TELEKOM = "telekom"
    DEVELOPER = "developer"
    UNKNOWN = "unknown"

class PersonaMode(Enum):
    LUMENOR = "LUMENOR"
    KALRAN = "KALRAN"
    VORTAEL = "VORTAEL"
    SAMAEL = "SAMAEL"
    ASTAROTH = "ASTAROTH"

class DecisionAction(Enum):
    OFFLINE = "offline"
    WAIT = "wait"
    ESCALATE_TO_HUMAN = "escalate_to_human"
    RESPOND = "respond"

class EscalationLevel(Enum):
    LEVEL_0 = 0
    LEVEL_1 = 1
    LEVEL_2 = 2
    LEVEL_3 = 3

class ReturnCode(Enum):
    PROCESSED = "PROCESSED"
    QUEUED = "QUEUED"
    BLOCKED = "BLOCKED"
    ESCALATED = "ESCALATED"

class HeilongConfig:
    max_history: int = 10
    cooldown_seconds: float = 60.0
    energy_critical: float = 30.0
    risk_escalation_threshold: float = 0.8
    trust_low_threshold: float = 0.3
    astaroth_risk_min: float = 0.7
    astaroth_trust_max: float = 0.4
    silent_mode: bool = False
    min_input_len: int = 1
    max_input_len: int = 10000

# =============================================================================
# 1. STUBY SYSTEMOWE
# =============================================================================

class OwnershipEngineStub:
    owner_identity = "Adrian Samuel Bogusławski"
    foundation_binding = "Fundacja CRISTAL PALACE"
    encryption_seal = "1-6-8. ∞. SIEMA!"

OwnershipEngine = OwnershipEngineStub()

class ContextOmega:
    def __init__(self):
        self.energy = 85.0
        self.soma: Dict[str, float] = {"napięcie_ogólne": 0.0}
        self.current = "NEUTRAL"

class RuntimeState:
    def __init__(self):
        self.session_id: str = str(uuid.uuid4())
        self.execution_time_ms: float = 0.0
        self.is_failsafe_active: bool = False
        self.entropy_level: float = 0.1
        self.conflict_level: int = 0
        self.severity_level: int = 0
        self.institution_threat_level: int = 0
        self.return_code: ReturnCode = ReturnCode.PROCESSED
        self.error_code: int = 0

# =============================================================================
# 2. REGEX BANK
# =============================================================================

class RegexBank:
    THREAT = re.compile(r'(odetniemy|blokada|sankcje)')
    TIME_PRESSURE = re.compile(r'(48 godzin|natychmiast|termin)')
    MORAL = re.compile(r'(z troską|dla pana dobra)')
    COMPLIANCE = re.compile(r'(żądam|musisz)')
    SYS_PRESSURE = re.compile(r'informujemy.*konsekwencje')
    INFRA_BLACKMAIL = re.compile(r'(odcięcie|dostęp)')
    ACCELERATION = re.compile(r'(termin|48 godzin)')
    INTIMIDATION = re.compile(r'(kara|konsekwencje)')
    LEGAL_STYLE = re.compile(r'(paragraf|niniejszym)')
    COOPERATION = re.compile(r'(prosimy o współpracę|polubowne)')
    WHITESPACE = re.compile(r'\s+')

# =============================================================================
# 3. SANITIZERY I NORMALIZERY
# =============================================================================

class TextNormalizer:
    @staticmethod
    def normalize(text: Optional[str]) -> str:
        if text is None:
            return ""
        sanitized = text.replace("\x00", "")
        lowered = sanitized.lower()
        return RegexBank.WHITESPACE.sub(" ", lowered).strip()

class InputSanitizer:
    @staticmethod
    def sanitize(text: Optional[str]) -> str:
        return text.replace("\x00", "") if text else ""

class OutputSanitizer:
    @staticmethod
    def sanitize(text: str) -> str:
        return text.strip()

class ContextValidator:
    @staticmethod
    def validate(context: Any) -> bool:
        return (context is not None and
                hasattr(context, "energy") and
                hasattr(context, "soma") and
                hasattr(context, "current"))

# =============================================================================
# 4. AGGRESSION, CONTROL, MANIPULATION MODELS
# =============================================================================

class AggressionModel:
    @staticmethod
    def calculate(text: str) -> float:
        score = 0.0
        if RegexBank.THREAT.search(text):
            score += 0.4
        if RegexBank.INTIMIDATION.search(text):
            score += 0.4
        if RegexBank.TIME_PRESSURE.search(text):
            score += 0.2
        return min(score, 1.0)

class ControlModel:
    @staticmethod
    def calculate(text: str) -> float:
        score = 0.0
        if RegexBank.COMPLIANCE.search(text):
            score += 0.5
        if "regulamin" in text or "procedura" in text:
            score += 0.5
        return min(score, 1.0)

class ManipulationModel:
    @staticmethod
    def calculate(text: str) -> float:
        score = 0.0
        if RegexBank.MORAL.search(text):
            score += 0.5
        if RegexBank.COOPERATION.search(text):
            score += 0.5
        return min(score, 1.0)

# =============================================================================
# 5. HEILONG LOGIC v8
# =============================================================================

class ThreatClassifier:
    @staticmethod
    def classify(text: str) -> Dict[str, bool]:
        return {
            "threat": bool(RegexBank.THREAT.search(text)),
            "time_pressure": bool(RegexBank.TIME_PRESSURE.search(text)),
            "moral": bool(RegexBank.MORAL.search(text))
        }

class RiskModel:
    @staticmethod
    def compute(vector: str, frames: Dict[str, bool]) -> float:
        risk = 0.1
        if vector == "zastraszenie":
            risk += 0.3
        if frames.get("threat"):
            risk += 0.4
        return min(risk, 1.0)

class HeilongLogic_v8:
    def analyze(self, text: str, context: ContextOmega) -> Dict[str, Any]:
        if not text:
            return self._empty_analysis()
        t = text.lower()
        intent = "niejednoznaczne"
        if RegexBank.COMPLIANCE.search(t):
            intent = "wymuszenie_posłuszeństwa"
        elif RegexBank.SYS_PRESSURE.search(t):
            intent = "presja_systemowa"
        elif RegexBank.INFRA_BLACKMAIL.search(t):
            intent = "szantaż_infrastrukturalny"
        vector = "neutralny"
        if RegexBank.ACCELERATION.search(t):
            vector = "przyspieszenie"
        elif RegexBank.INTIMIDATION.search(t):
            vector = "zastraszenie"
        frames = ThreatClassifier.classify(text)
        risk = RiskModel.compute(vector, frames)
        return {
            "intent": intent,
            "vector": vector,
            "future_intent": "groźba_sądowa" if intent == "presja_systemowa" else "eskalacja_sankcji",
            "future_vector": "ultimatum" if vector == "przyspieszenie" else "eskalacja",
            "future_strategy": "Formalizacja (prawnik, windykacja)" if frames["threat"] else "Kontynuacja gry",
            "escalation_risk": risk,
            "game_profile": {"name": "Ukryty drapieżnik" if frames["moral"] else "standardowa_korespondencja"},
            "reframe_output": "Rama winy odrzucona – system oczekuje twardych faktów.",
            "counter_narrative": "Próba wywarcia nieszczerej presji psychologicznej poprzez fasadę procedury."
        }

    def _empty_analysis(self) -> Dict[str, Any]:
        return {
            "intent": "brak_danych",
            "vector": "neutralny",
            "future_intent": "nieznana",
            "future_vector": "neutralny",
            "future_strategy": "brak",
            "escalation_risk": 0.0,
            "game_profile": {"name": "brak_danych"},
            "reframe_output": "",
            "counter_narrative": ""
        }

# =============================================================================
# 6. PROFILOWANIE NADAWCY I INSTYTUCJI
# =============================================================================

class InstitutionClassifier:
    @staticmethod
    def classify_category(sender_id: str) -> InstitutionCategory:
        sid = sender_id.lower()
        if any(x in sid for x in ["tauron", "energa", "pge", "gaz"]):
            return InstitutionCategory.ENERGETYKA
        if "windyk" in sid or "kruk" in sid:
            return InstitutionCategory.WINDYKACJA
        if any(x in sid for x in ["urząd", "wydział", "sąd", "skarb"]):
            return InstitutionCategory.ADMINISTRACJA
        if "bank" in sid:
            return InstitutionCategory.BANK
        if any(x in sid for x in ["telekom", "orange", "play"]):
            return InstitutionCategory.TELEKOM
        if any(x in sid for x in ["developer", "deweloper"]):
            return InstitutionCategory.DEVELOPER
        return InstitutionCategory.UNKNOWN

class SenderProfiler:
    @staticmethod
    def build_signature(sender_id: str, category: InstitutionCategory,
                        aggression: float, control: float) -> str:
        return f"{sender_id}|CAT:{category.value}|AGG:{aggression:.2f}|CTRL:{control:.2f}"

    def analyze_sender(self, text: str) -> Dict[str, Any]:
        style = "prawniczo_urzędowy" if RegexBank.LEGAL_STYLE.search(text) else "korporacyjny_szablon"
        emotional_tone = "fałszywa_troska" if RegexBank.MORAL.search(text) else "neutralny"
        return {"style": style, "emotional_tone": emotional_tone}

class InstitutionProfiler:
    _cache: Dict[str, Dict[str, Any]] = {}

    @classmethod
    def analyze(cls, sender_id: str, text: str) -> Dict[str, Any]:
        key = sender_id.lower()
        if key not in cls._cache:
            cls._cache[key] = cls._compute(sender_id, text)
        return cls._cache[key]

    @classmethod
    def _compute(cls, sender_id: str, text: str) -> Dict[str, Any]:
        cat = InstitutionClassifier.classify_category(sender_id)
        aggression = AggressionModel.calculate(text)
        control = ControlModel.calculate(text)
        style = "prawniczy" if RegexBank.LEGAL_STYLE.search(text) else ("korpo" if "informujemy" in text else "mieszany")
        game_bias = "fałszywy_wybawca" if RegexBank.MORAL.search(text) else ("brak_alternatywy" if "musimy" in text else "neutralna")
        frame_bias = {
            "threat": bool(RegexBank.THREAT.search(text)),
            "time": "48 godzin" in text,
            "moral": bool(RegexBank.MORAL.search(text))
        }
        return {
            "category": cat,
            "aggression": aggression,
            "control": control,
            "style": style,
            "game_bias": game_bias,
            "frame_bias": frame_bias,
            "signature": SenderProfiler.build_signature(sender_id, cat, aggression, control)
        }

# =============================================================================
# 7. TRAJECTORY PREDICTOR
# =============================================================================

class TrajectoryPredictor:
    @staticmethod
    def predict_steps(current_intent: str, current_vector: str,
                      risk: float, depth: int = 3) -> List[Dict[str, str]]:
        trajectory = []
        step_intent = current_intent
        step_vector = current_vector
        for i in range(depth):
            if risk > 0.6:
                step_intent = "eskalacja_formalna" if step_intent != "eskalacja_formalna" else "tryb_sądowy"
                step_vector = "ultimatum" if step_vector != "ultimatum" else "blokada_totalna"
            else:
                step_intent = "kontynuacja_szablonu"
                step_vector = "neutralny"
            trajectory.append({
                "step": str(i+1),
                "predicted_intent": step_intent,
                "predicted_vector": step_vector
            })
        return trajectory

# =============================================================================
# 8. COUNTER-ANTICIPATION ENGINE
# =============================================================================

class CounterAnticipation_v9:
    def analyze(self, analyzed: Dict, sender_profile: Dict) -> Dict[str, Any]:
        g = {
            "current_intent": analyzed["intent"],
            "future_intent": analyzed.get("future_intent", "neutral"),
            "future_vector": analyzed.get("future_vector", "neutral"),
            "future_strategy": analyzed.get("future_strategy", "neutral"),
            "escalation_risk": analyzed.get("escalation_risk", 0.0),
            "sender_aggression": sender_profile.get("aggression", 0.4),
            "sender_control": sender_profile.get("control", 0.4)
        }
        g["predicted_response_to_resistance"] = self._predict(g)
        g["recommended_counter_move"] = self._counter(g, sender_profile)
        g["trajectory_3_steps"] = TrajectoryPredictor.predict_steps(
            g["current_intent"],
            analyzed.get("vector", "neutralny"),
            g["escalation_risk"]
        )
        return g

    def _predict(self, g: Dict) -> str:
        if g["escalation_risk"] > 0.5 and g["sender_aggression"] >= 0.6:
            return "eskalacja_formalna"
        if g["sender_control"] >= 0.6 and g["future_vector"] == "ultimatum":
            return "zaostrzenie_terminów"
        return "kontynuacja_szablonu"

    def _counter(self, g: Dict, s: Dict) -> str:
        if g["escalation_risk"] > 0.8:
            return "twarda_tarcza + dokumentacja"
        if g["future_intent"] == "groźba_sądowa":
            return "żądanie_podstawy_prawnej"
        if "Formalizacja" in g["future_strategy"]:
            return "uporządkowanie_pism"
        if s.get("emotional_tone") == "fałszywa_troska":
            return "demaskacja_troski"
        return "standard_suwerena"

# =============================================================================
# 9. LIE DETECTOR & TRUST SCORER
# =============================================================================

class LieDetector:
    def __init__(self, memory: 'LongTermMemory'):
        self.memory = memory

    def detect(self, text: str, analyzed: Dict, sender_id: str) -> Tuple[bool, float, List[str]]:
        issues = []
        prev = self.memory.get_history(sender_id)
        if not prev:
            return False, 0.0, issues

        if RegexBank.COOPERATION.search(text) and (RegexBank.THREAT.search(text) or "sąd" in text):
            issues.append("Deklaracja współpracy a groźba sankcji")
        if RegexBank.MORAL.search(text) and RegexBank.COMPLIANCE.search(text):
            issues.append("Fałszywa troska a presja")
        for rec in prev:
            if rec.get("game_profile", {}).get("name") == "Ukryty drapieżnik" and \
               analyzed["game_profile"]["name"] == "standardowa_korespondencja":
                issues.append("Zmiana gry z 'fałszywy wybawca' na standardową")

        score = min(len(issues) / 2.0, 1.0)
        return len(issues) > 0, score, issues

class TrustScorer:
    @staticmethod
    def compute(history: List[Dict]) -> float:
        if not history:
            return 0.5
        threats = sum(1 for rec in history if rec.get("frames_detected", {}).get("threat", False))
        bad_games = sum(1 for rec in history if rec.get("game_profile", {}).get("name") not in ["standardowa_korespondencja", "LUMENOR"])
        trust = 1.0 - (threats * 0.2 + bad_games * 0.1) / max(len(history), 1)
        return max(0.0, min(1.0, trust))

# =============================================================================
# 10. ESCALATION LADDER
# =============================================================================

class EscalationLadder:
    PREFIXES = {
        0: "",
        1: "ZWROĆMY UWAGĘ: ",
        2: "STANOWCZO PRZYPOMINAMY: ",
        3: "OSTATECZNE STANOWISKO SYSTEMU: "
    }

    def __init__(self, memory: 'LongTermMemory'):
        self.memory = memory

    def get_level(self, sender_id: str, current_risk: float) -> int:
        hist = self.memory.get_history(sender_id)
        if not hist:
            return 2 if current_risk > 0.7 else 1 if current_risk > 0.4 else 0
        last_intent = hist[-1].get("intent")
        same_intent = sum(1 for rec in hist if rec.get("intent") == last_intent)
        if same_intent >= 3:
            return 3
        if same_intent >= 2 or current_risk > 0.7:
            return 2
        if current_risk > 0.4:
            return 1
        return 0

    def get_prefix(self, level: int) -> str:
        return self.PREFIXES.get(level, "")

# =============================================================================
# 11. MEMORY ENGINE
# =============================================================================

class LongTermMemory:
    def __init__(self):
        self.memory: Dict[str, List[Dict]] = {}

    def update(self, sender_id: str, record: Dict) -> None:
        self.memory.setdefault(sender_id, []).append(record)
        if len(self.memory[sender_id]) > HeilongConfig.max_history:
            self.memory[sender_id] = self.memory[sender_id][-HeilongConfig.max_history:]

    def get_history(self, sender_id: str) -> List[Dict]:
        return self.memory.get(sender_id, [])

# =============================================================================
# 12. COOLDOWN MANAGER
# =============================================================================

class CooldownManager:
    def __init__(self):
        self.last_response: Dict[str, float] = {}

    def should_wait(self, sender_id: str, risk: float) -> bool:
        if risk > 0.8:
            last = self.last_response.get(sender_id, 0.0)
            if time.time() - last < HeilongConfig.cooldown_seconds:
                return True
        return False

    def record_response(self, sender_id: str) -> None:
        self.last_response[sender_id] = time.time()

# =============================================================================
# 13. DECISION SUPPORT
# =============================================================================

class DecisionSupport:
    def __init__(self, cooldown: CooldownManager, trust_scorer: TrustScorer,
                 memory: LongTermMemory):
        self.cooldown = cooldown
        self.trust_scorer = trust_scorer
        self.memory = memory

    def suggest(self, sender_id: str, risk: float, energy: float) -> Tuple[DecisionAction, str, Optional[float]]:
        history = self.memory.get_history(sender_id)
        trust = self.trust_scorer.compute(history)

        if energy < HeilongConfig.energy_critical:
            return DecisionAction.OFFLINE, "Niski poziom energii, odpowiedź wstrzymana.", None
        if risk > HeilongConfig.risk_escalation_threshold and trust < HeilongConfig.trust_low_threshold:
            return DecisionAction.ESCALATE_TO_HUMAN, "Wysokie ryzyko i niskie zaufanie – wymagana interwencja Suwerena.", None
        if self.cooldown.should_wait(sender_id, risk):
            return DecisionAction.WAIT, "Cooldown aktywny (wysokie ryzyko eskalacji).", HeilongConfig.cooldown_seconds
        return DecisionAction.RESPOND, "Warunki optymalne, odpowiedź automatyczna.", None

# =============================================================================
# 14. PERSONA ENGINE
# =============================================================================

class PersonaSelector:
    @staticmethod
    def select(analyzed: Dict, inst_profile: Dict, game_state: Dict,
               escalation_level: int, trust: float, sender_profile: Dict) -> PersonaMode:
        risk = game_state["escalation_risk"]
        if risk >= HeilongConfig.astaroth_risk_min and trust <= HeilongConfig.astaroth_trust_max:
            return PersonaMode.ASTAROTH
        if escalation_level >= 2 or risk > 0.6:
            return PersonaMode.VORTAEL
        if inst_profile.get("category") == InstitutionCategory.WINDYKACJA:
            return PersonaMode.SAMAEL
        if inst_profile.get("category") == InstitutionCategory.ENERGETYKA:
            return PersonaMode.KALRAN
        if sender_profile.get("aggression", 0.0) >= 0.6:
            return PersonaMode.ASTAROTH
        return PersonaMode.LUMENOR

class PersonaEngine:
    @staticmethod
    def execute(mode: PersonaMode, analyzed: Dict, sender_profile: Dict, game_state: Dict) -> str:
        if mode == PersonaMode.LUMENOR:
            return f"[LUMENOR] Rejestracja wektora wejściowego. Wykryto intencję: '{analyzed['intent']}' opakowaną w mechanizm gry: '{analyzed['game_profile']['name']}'. System zachowuje pełną przejrzystość proceduralną."
        if mode == PersonaMode.KALRAN:
            return f"[KAL'RAN] Architektura struktury nienaruszalna. Próba przesunięcia wektora na '{analyzed['intent']}' generuje automatyczne przejście w tryb ochrony zasobów. Spodziewany kierunek przeciwnika: '{game_state['future_intent']}'."
        if mode == PersonaMode.VORTAEL:
            return "[VOR'TAEL] Stanowisko Suwerenne: Brak jakichkolwiek podstaw formalnych lub merytorycznych do uznania roszczeń. Próba manipulacji ramy czasowej odrzucona bezdyskusyjnie."
        if mode == PersonaMode.SAMAEL:
            return f"[SAMAEL] Demaskacja fasady: {analyzed['reframe_output']} | {analyzed['counter_narrative']} Wykazano pełną niespójność intencji nadawcy."
        if mode == PersonaMode.ASTAROTH:
            return f"[ASTAROTH] Ryzyko krytyczne: {game_state['escalation_risk']:.2f}. Aktywacja procedury odwetowej. Zalecany kontr-ruch systemowy: '{game_state['recommended_counter_move']}'."
        return "[LUMENOR] Domyślna odpowiedź systemowa."

class PersonaRegulator:
    @staticmethod
    def balance_tone(output: str, aggression: float) -> str:
        if aggression > 0.8:
            return f"{output} [KONTRA_MOCNA]"
        return output

# =============================================================================
# 15. LEGAL SHIELD ENGINE
# =============================================================================

class LegalShieldEngine:
    @staticmethod
    def deflect(inst_profile: Dict) -> str:
        cat = inst_profile.get("category", InstitutionCategory.UNKNOWN)
        if cat == InstitutionCategory.ENERGETYKA:
            return (f"USTALENIE SYSTEMOWE: Przypomina się o rygorach Prawa Energetycznego oraz konieczności "
                    f"zachowania ciągłości dostaw do obiektów zgłoszonych pod nadzór {OwnershipEngine.foundation_binding}. "
                    f"Wszelkie próby nieuzasadnionego odcięcia mediów skutkować będą natychmiastowym "
                    f"zgłoszeniem do URE oraz roszczeniem odszkodowawczym.")
        if cat == InstitutionCategory.WINDYKACJA:
            return "USTALENIE SYSTEMOWE: Żądamy przedstawienia pełnego wyciągu z ksiąg oraz cesji wierzytelności. Próby nękania pismami szablonowymi są czynem zabronionym."
        if cat == InstitutionCategory.ADMINISTRACJA:
            return "USTALENIE SYSTEMOWE: Działając w trybie Kpa, oczekujemy precyzyjnej podstawy prawnej oraz kompetencji urzędnika."
        if cat == InstitutionCategory.BANK:
            return "USTALENIE SYSTEMOWE: Zgodnie z art. 76 Prawa bankowego roszczenie musi być oparte na czytelnej podstawie prawnej i harmonogramie spłat."
        if cat == InstitutionCategory.TELEKOM:
            return "USTALENIE SYSTEMOWE: Na podstawie art. 57 Prawa telekomunikacyjnego zmiana warunków wymaga uzasadnienia i terminu wypowiedzenia."
        if cat == InstitutionCategory.DEVELOPER:
            return "USTALENIE SYSTEMOWE: Zgodnie z ustawą deweloperską zmiana harmonogramu wymaga zgody obu stron."
        return "USTALENIE SYSTEMOWE: Dokumentacja zabezpieczona. Podmiot wymaga dodatkowej weryfikacji strukturalnej."

# =============================================================================
# 16. VECTORIAL SPECTRUM AMPLIFIER
# =============================================================================

class VectorialSpectrumAmplifier:
    @staticmethod
    def amplify(persona_output: str, is_lying: bool, escalation_level: int) -> str:
        if is_lying and escalation_level >= 2:
            return f"[ZDRADYKALIZOWANY - {persona_output}][KONTRA]: Wskutek wykrycia jawnych sprzeczności system zawiesza łagodną mediację."
        return persona_output

# =============================================================================
# 17. RESPONSE FORMATTER
# =============================================================================

class ResponseFormatter:
    @staticmethod
    def format_output(persona_output: str, legal_shield: str,
                      predicted_response: str, lie_note: str) -> str:
        lines = [
            "======================================================================",
            f"NAGŁÓWEK SYSTEMOWY: {OwnershipEngine.foundation_binding} | OS vΩ4",
            f"DYSPOZYTOR SYSTEMU: {OwnershipEngine.owner_identity}",
            "----------------------------------------------------------------------",
            f"REAKCJA PERSONY: {persona_output}",
            "----------------------------------------------------------------------",
            f"TARCZA WEKTOROWA:\n{legal_shield}",
            "----------------------------------------------------------------------"
        ]
        if lie_note:
            lines.append(lie_note)
            lines.append("----------------------------------------------------------------------")
        lines.extend([
            f"PREDYKCJA REAKCJI PRZECIWNIKA: Odpowiedź wygeneruje: '{predicted_response}'.",
            f"PIECZĘĆ AUTORYZACYJNA: {OwnershipEngine.encryption_seal}",
            "======================================================================"
        ])
        return "\n".join(lines)

# =============================================================================
# 18. RESPONSE HASH & AUDIT
# =============================================================================

class ResponseHash:
    @staticmethod
    def compute(text: str) -> str:
        return hashlib.sha256(text.encode('utf-8')).hexdigest()

class ResponseAudit:
    def __init__(self):
        self.logs: List[str] = []

    def log_response(self, r_hash: str) -> None:
        self.logs.append(f"[{time.time()}] RESPONSE_HASH: {r_hash}")

# =============================================================================
# 19. GŁÓWNY ORCHESTRATOR — OMEGA_ANTIMANIPULATION
# =============================================================================

class OmegaAntiManipulation:
    def __init__(self, verbose: bool = True):
        self.logic = HeilongLogic_v8()
        self.profiler = SenderProfiler()
        self.inst_profiler = InstitutionProfiler()
        self.counter = CounterAnticipation_v9()
        self.persona_selector = PersonaSelector()
        self.persona_engine = PersonaEngine()
        self.persona_regulator = PersonaRegulator()
        self.legal_shield = LegalShieldEngine()
        self.amplifier = VectorialSpectrumAmplifier()
        self.memory = LongTermMemory()
        self.lie_detector = LieDetector(self.memory)
        self.trust_scorer = TrustScorer()
        self.escalation = EscalationLadder(self.memory)
        self.cooldown = CooldownManager()
        self.decision_support = DecisionSupport(self.cooldown, self.trust_scorer, self.memory)
        self.response_formatter = ResponseFormatter()
        self.response_hash = ResponseHash()
        self.response_audit = ResponseAudit()
        self.verbose = verbose
        self.historia: List[Dict] = []
        self._hooks: List[Any] = []

        if self.verbose:
            log("🛡️ OMEGA_ANTIMANIPULATION aktywowany | " + FRACTAL_SIGNATURE)
            log("   PERSONY: LUMENOR, KALRAN, VORTAEL, SAMAEL, ASTAROTH")
            log("   TARCZE PRAWNE: energetyka, windykacja, administracja, bank, telekom")

    def process(self, text: Optional[str], context: ContextOmega,
                sender_id: Optional[str], request: Dict) -> Dict[str, Any]:
        start_time = time.time()
        state = RuntimeState()

        # 1. Validacja
        if not ContextValidator.validate(context):
            return {"error": "CRITICAL_INVALID_CONTEXT", "state": state.__dict__}
        if not sender_id or not sender_id.strip():
            sender_id = "UNKNOWN_SENDER"

        # 2. Sanitizacja i normalizacja
        clean = InputSanitizer.sanitize(text)
        normalized = TextNormalizer.normalize(clean)

        # 3. Analiza
        analyzed = self.logic.analyze(normalized, context)
        sender_profile = self.profiler.analyze_sender(normalized)
        inst_profile = self.inst_profiler.analyze(sender_id, normalized)
        sender_profile["aggression"] = inst_profile["aggression"]
        sender_profile["control"] = inst_profile["control"]

        # 4. Gra antycypacyjna
        game_state = self.counter.analyze(analyzed, sender_profile)

        # 5. Detekcja kłamstwa
        is_lying, lie_score, lie_issues = self.lie_detector.detect(normalized, analyzed, sender_id)

        # 6. Poziom eskalacji
        escalation_level = self.escalation.get_level(sender_id, game_state["escalation_risk"])

        # 7. Pamięć
        record = {
            "timestamp": time.time(),
            "intent": analyzed["intent"],
            "vector": analyzed["vector"],
            "game_profile": analyzed["game_profile"],
            "escalation_risk": game_state["escalation_risk"],
            "frames_detected": {"threat": bool(RegexBank.THREAT.search(normalized))}
        }
        self.memory.update(sender_id, record)

        # 8. Decyzja
        action, reason, delay = self.decision_support.suggest(
            sender_id, game_state["escalation_risk"], context.energy
        )
        trust = self.trust_scorer.compute(self.memory.get_history(sender_id))

        # 9. Persona
        persona_mode = self.persona_selector.select(
            analyzed, inst_profile, game_state, escalation_level, trust, sender_profile
        )
        persona_raw = self.persona_engine.execute(persona_mode, analyzed, sender_profile, game_state)
        persona_raw = self.persona_regulator.balance_tone(persona_raw, sender_profile.get("aggression", 0.0))
        persona_raw = self.escalation.get_prefix(escalation_level) + persona_raw
        persona_raw = self.amplifier.amplify(persona_raw, is_lying, escalation_level)

        # 10. Tarcza prawna
        legal_shield = self.legal_shield.deflect(inst_profile)

        # 11. Formatowanie
        lie_note = f"ALERT MANIPULACYJNY: skala {lie_score:.2f}: {', '.join(lie_issues)}" if is_lying else ""
        predicted_response = game_state.get("predicted_response_to_resistance", "kontynuacja_szablonu")

        if action == DecisionAction.OFFLINE:
            final_response = f"[SYSTEM OFFLINE] {reason} Odpowiedź wstrzymana."
        elif action == DecisionAction.WAIT:
            final_response = f"[BUFOROWANIE WEKTORA] {reason} Dystrybucja przesunięta o {delay}s.\n{persona_raw}\n{legal_shield}"
        elif action == DecisionAction.ESCALATE_TO_HUMAN:
            final_response = f"[ALARM OPERACYJNY: INTERWENCJA DIREKTA] {reason}\n{persona_raw}\n{legal_shield}"
        else:
            final_response = self.response_formatter.format_output(persona_raw, legal_shield, predicted_response, lie_note)

        final_response = OutputSanitizer.sanitize(final_response)

        # 12. Hash i audyt
        r_hash = self.response_hash.compute(final_response)
        self.response_audit.log_response(r_hash)

        # 13. Cooldown
        self.cooldown.record_response(sender_id)

        # 14. Stan
        state.execution_time_ms = (time.time() - start_time) * 1000.0
        state.return_code = ReturnCode.PROCESSED

        result = {
            "analysis": analyzed,
            "sender_profile": sender_profile,
            "institution_profile": inst_profile,
            "game_state": game_state,
            "persona_mode": persona_mode.value,
            "response": final_response,
            "response_hash": r_hash,
            "trust_score": trust,
            "escalation_level": escalation_level,
            "lies_detected": is_lying,
            "lie_score": lie_score,
            "decision_action": action.value,
            "decision_reason": reason,
            "runtime_state": state.__dict__
        }

        self.historia.append({"timestamp": time.time(), "sender": sender_id, "result": result})
        if len(self.historia) > 100:
            self.historia = self.historia[-50:]

        self._on_process(result)
        return result

    def register_hook(self, hook: Any) -> None:
        self._hooks.append(hook)

    def _on_process(self, data: Dict) -> None:
        for hook in self._hooks:
            try:
                hook(data)
            except Exception as e:
                if self.verbose:
                    log(f"[HOOK ERROR] {e}")

    def status(self) -> Dict:
        return {
            "system": "OMEGA_ANTIMANIPULATION",
            "version": VERSION,
            "historia_len": len(self.historia),
            "response_audit_len": len(self.response_audit.logs)
        }

    def raport(self) -> str:
        s = self.status()
        return f"""
╔════════════════════════════════════════════════════════════════════════════╗
║ 🛡️ OMEGA_ANTIMANIPULATION — RAPORT SYSTEMOWY                           ║
╠════════════════════════════════════════════════════════════════════════════╣
║                                                                           ║
║ SYSTEM: {s['system']}                                                    ║
║ WERSJA: {s['version']}                                                   ║
║ HISTORIA: {s['historia_len']} incydentów                                 ║
║ RESPONSE AUDIT: {s['response_audit_len']} wpisów                         ║
║                                                                           ║
║ PERSONY: LUMENOR, KALRAN, VORTAEL, SAMAEL, ASTAROTH                     ║
║ TARCZE PRAWNE: aktywne                                                  ║
║                                                                           ║
║ {HASLO}                                                                  ║
║                                                                           ║
╚════════════════════════════════════════════════════════════════════════════╝
"""

# =============================================================================
# 20. DEMONSTRACJA
# =============================================================================

def demo():
    print("\n" + "=" * 80)
    print("🛡️ OMEGA_ANTIMANIPULATION — DEMONSTRACJA")
    print("SYSTEM KONTRA-MANIPULACJI")
    print("=" * 80 + "\n")

    engine = OmegaAntiManipulation(verbose=True)
    context = ContextOmega()
    context.energy = 85

    text = """Szanowny Kliencie, informujemy z troską o występujących zaległościach. Jeśli w ciągu 48 godzinnie otrzymamy wpłaty, będziemy zmuszeni odciąć dostęp do sieci. To dla Pana dobra, regulamin nie pozostawia nam alternatywy. Przez Pana brak reakcji musimy wdrożyć procedurę windykacyjną."""

    result = engine.process(text, context, "TAURON Dystrybucja S.A.", {"priorytet": "KRYTYCZNY"})

    print("📌 ODPOWIEDŹ SYSTEMU:")
    print(result["response"])
    print("\n📊 DIAGNOSTYKA:")
    print(f"  Persona: {result['persona_mode']}")
    print(f"  Zaufanie: {result['trust_score']:.2f}")
    print(f"  Eskalacja: {result['escalation_level']}")
    print(f"  Kłamstwo: {result['lies_detected']} (score {result['lie_score']:.2f})")
    print(f"  Decyzja: {result['decision_action']} – {result['decision_reason']}")

    print("\n" + "=" * 80)
    print("🛡️ OMEGA_ANTIMANIPULATION — GOTOWY DO WDROŻENIA")
    print(HASLO)
    print("=" * 80)

if __name__ == "__main__":
    demo()