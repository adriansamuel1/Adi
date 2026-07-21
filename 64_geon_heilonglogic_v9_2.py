#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
================================================================================
🐉 GEON_HEILONGLOGIC_v9_2 — MODUŁ 64: ANALIZA MANIPULACJI I KONTRA-ODPOWIEDŹ
================================================================================
Status: PRODUCTION_READY | FRACTAL_LOCKED | ORGANISM_COMPLETE | ULTIMA
Wersja: v9.2 (HeilongLogic — Dekonstrukcja Manipulacji, Antycypacja, Kontra-odpowiedź)
Data: 2026-07-21
Autor: Adrian (Architekt) + Samael (Strażnik Kronik) + GEON

OPIS:
HEILONGLOGIC v9.2 to zaawansowany system analizy manipulacji i generowania
kontra-odpowiedzi. Łączy 9 warstw analizy:
- v3: Intencja, wektor, leverage
- v4: Meta-intencja, warstwy ukryte, timing
- v5: Gry psychologiczne (Berne), role, ramy, władza
- v6: Anty-AI / Anty-Bot, automatyzacja
- v7: Anti-Gaslight, Reframe, Counter-Narrative
- v8: Antycypacja (przewidywanie przyszłych ruchów)
- vX: Profilowanie nadawcy (fingerprint)
- v9: Gra dwustronna, rekomendacja kontr-ruchu
- v9.2: Preemptive Legal Anticipator (automatyczne pisma do URE/UOKiK)

ARCHITEKTURA (14×14 FRAKTAL + WARSTWA 21):
• Wykorzystuje reguły Fraktala 14×14 do decyzji odpowiedzi
• Współpracuje z Context v5 (somatyka) i Ownership Engine
• Archiwizuje incydenty w Kapsule Czasu

INTEGRACJA Z ARCHITEKTURĄ:
• GEON_FRACTAL_14x14 — dostarcza reguły decyzyjne
• GEON_OS_12x12 — system operacyjny świadomości
• HEILONG_OS_v2.3 — Guardian Kernel
• OŁSii CORE — synchronizacja emocjonalna
• BENY CORE — twarda logika decyzyjna
• G_CORE — stan operacyjny
• MetaGovernor — kontekst decyzyjny
• NARRATIVE — źródło opowieści z analizy

VIBE: 1-6-8. ∞. SIEMA! 🛡️
================================================================================
"""

import time
import json
import logging
from typing import Dict, Any, List, Optional, Tuple
from dataclasses import dataclass, field
from collections import deque
from enum import Enum

# =============================================================================
# WERSJA I STAŁE
# =============================================================================

VERSION = "GEON_HEILONGLOGIC_v9.2"
FRACTAL_SIGNATURE = "[GEON::HEILONGLOGIC::v9.2]"
VIBE = 168
HASLO = "1-6-8. ∞. SIEMA!"
DEWIZA = "Ex Sapientia, Imperium"

# =============================================================================
# LOGOWANIE
# =============================================================================

logger = logging.getLogger("HEILONGLOGIC_v9.2")
logger.setLevel(logging.INFO)
if not logger.handlers:
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter('🛡️ [HLv9.2] %(message)s'))
    logger.addHandler(handler)

def log(msg: str) -> None:
    logger.info(msg)

def clamp(x: float, lo: float, hi: float) -> float:
    return max(lo, min(hi, x))

def contains_any(text: str, phrases: List[str]) -> bool:
    t = text.lower()
    return any(phrase.lower() in t for phrase in phrases)

def format_float(val: float, precision: int = 2) -> str:
    return f"{val:.{precision}f}"

# =============================================================================
# 0. STUBY SYSTEMOWE (ARCHIWUM, CONTEXT, OWNERSHIP)
# =============================================================================

class ArchiwumStub:
    """Wieczyste Archiwum z Kapsułą Czasu — nieusuwalne wpisy"""
    def __init__(self):
        self.pamiec: List[Dict] = []
        self.kapsula_czasu: List[Dict] = []
    
    def zapisz(self, kategoria: str, *args) -> None:
        wpis = {"czas": time.time(), "kategoria": kategoria, "dane": args}
        self.pamiec.append(wpis)
        if len(self.pamiec) > 1000:
            self.pamiec = self.pamiec[-500:]
    
    def ZapiszKamienMilowy(self, nazwa: str, tresc: Any) -> None:
        self.kapsula_czasu.append({"czas": time.time(), "nazwa": nazwa, "tresc": tresc})
    
    def odczytaj_historie(self, kategoria: str) -> List[Dict]:
        return [w for w in self.pamiec if w["kategoria"] == kategoria]
    
    def status(self) -> Dict:
        return {
            "pamiec": len(self.pamiec),
            "kapsula_czasu": len(self.kapsula_czasu)
        }

# Globalne Archiwum (singleton)
Archiwum = ArchiwumStub()

class OwnershipEngineStub:
    """Silnik Suwerenności — chroni tożsamość systemu"""
    owner_identity = "Adrian Samuel Bogusławski"
    foundation_binding = "Fundacja CRISTAL PALACE"
    encryption_seal = "1-6-8. ∞. SIEMA!"

OwnershipEngine = OwnershipEngineStub()

class Context:
    """Kontekst systemowy z mapą somatyczną (v5)"""
    def __init__(self):
        self.energy = 75
        self.soma = {"napięcie_ogólne": 0}
        self.current = "NEUTRAL"
    
    def update_soma(self, key: str, value: Any) -> None:
        self.soma[key] = value

# =============================================================================
# 1. HEILONGLOGIC v3 — BAZA (intencja, wektor, leverage)
# =============================================================================

class HeilongLogic_v3:
    """v3 — Podstawowa detekcja intencji, wektora i punktów nacisku"""
    
    def analyze(self, text: str) -> Dict[str, Any]:
        t = text.lower()
        
        # Struktura
        structure = "neutralna"
        if any(x in t for x in ["żądam", "grożę", "zmuszony"]):
            structure = "agresywna"
        elif "proszę" in t:
            structure = "prośba"
        
        # Dominacja
        patterns = ["nakaz", "przymus", "musisz", "szantaż", "dominacja"]
        dominance = [p for p in patterns if p in t]
        
        # Sprzeczności
        contradictions = []
        if "tak" in t and "nie" in t:
            contradictions.append("Wykryto 'tak' i 'nie' w jednym bloku.")
        
        # Szum
        noise = 0.0
        if text.count('!') > 2:
            noise += 0.2
        if text.count('?') > 2:
            noise += 0.2
        if text.isupper():
            noise += 0.3
        noise = min(noise, 1.0)
        
        # Intencja
        intent = "niejednoznaczne"
        if "żądam" in t or "musisz" in t:
            intent = "wymuszenie_posłuszeństwa"
        elif "informujemy" in t and "konsekwencje" in t:
            intent = "presja_systemowa"
        elif "grożę" in t or "sąd" in t or "skarga" in t:
            intent = "groźba_sądowa"
        elif "odcięcie" in t or "blokada" in t:
            intent = "szantaż_infrastrukturalny"
        elif any(x in t for x in ["martwić", "obawa", "strach"]):
            intent = "manipulacja_emocjonalna"
        
        # Wektor
        vector = "neutralny"
        if "termin" in t or "natychmiast" in t:
            vector = "przyspieszenie"
        elif "kara" in t or "konsekwencje" in t:
            vector = "zastraszenie"
        elif "wstyd" in t or "hańba" in t:
            vector = "zawstydzenie"
        
        # Punkty nacisku (leverage)
        leverage = []
        if "umowa" in t or "regulamin" in t:
            leverage.append("formalno_prawne")
        if "płatność" in t or "zadłużenie" in t:
            leverage.append("finansowe")
        if "odcięcie" in t or "dostęp" in t:
            leverage.append("infrastrukturalne")
        if "moralność" in t or "etyka" in t:
            leverage.append("etyczne")
        if "zdrowie" in t or "choroba" in t:
            leverage.append("zdrowotne")
        if "bezpieczeństwo" in t:
            leverage.append("bezpieczeństwo")
        
        return {
            "clean": text.strip(),
            "structure": structure,
            "contradictions": contradictions,
            "dominance": dominance,
            "noise": noise,
            "intent": intent,
            "vector": vector,
            "leverage": leverage
        }

# =============================================================================
# 2. HEILONGLOGIC v4 — META-INTENCJA, WARSTWY UKRYTE, TIMING
# =============================================================================

class HeilongLogic_v4(HeilongLogic_v3):
    """v4 — Meta-intencja, warstwy ukryte, timing, struktura strategiczna"""
    
    def analyze(self, text: str) -> Dict[str, Any]:
        base = super().analyze(text)
        base["meta_intent"] = self._detect_meta_intent(base)
        base["hidden_layers"] = self._detect_hidden_layers(text)
        base["timing"] = self._detect_timing_context(text)
        base["structure_map"] = self._detect_structural_strategy(text)
        Archiwum.zapisz("ANALIZA_META_INTENCJI", base["meta_intent"], base["timing"], base["hidden_layers"])
        return base
    
    def _detect_meta_intent(self, base: Dict) -> str:
        intent = base["intent"]
        leverage = base["leverage"]
        vector = base["vector"]
        if intent == "szantaż_infrastrukturalny" and "finansowe" in leverage:
            return "ukrycie_własnej_odpowiedzialności_za_brak_usługi"
        if intent == "manipulacja_emocjonalna" and vector == "zawstydzenie":
            return "przerzucenie_winy_na_odbiorcę_w_celu_wymuszenia_uległości"
        if intent == "presja_systemowa" and "formalno_prawne" in leverage:
            return "zablokowanie_krytycznego_myślenia_poprzez_autorytet_procedury"
        return "wymuszenie_bezkrytycznego_posłuszeństwa"
    
    def _detect_hidden_layers(self, text: str) -> Dict[str, bool]:
        t = text.lower()
        layers = {
            "odwrócenie_uwagi": False,
            "fałszywa_troska": any(x in t for x in ["martwi nas", "dla pana dobra", "z troską"]),
            "pozorna_współpraca": ("chcemy współpracować" in t or "polubowne" in t) and ("natychmiast" in t or "rygor" in t),
            "zmiękcz_uderz": False
        }
        if "nasz błąd" in t or "odpowiedzialność" in t:
            if "jednakże" in t or "ale" in t or "w zamian" in t:
                layers["odwrócenie_uwagi"] = True
        if t.startswith("szanowny") and ("odetniemy" in t or "konsekwencje" in t):
            layers["zmiękcz_uderz"] = True
        return layers
    
    def _detect_timing_context(self, text: str) -> Dict[str, Any]:
        t = text.lower()
        deadline = "brak"
        for word in ["48 godzin", "7 dni", "natychmiast", "w terminie"]:
            if word in t:
                deadline = word
                break
        ma_historie = len(Archiwum.odczytaj_historie("ANALIZA_v7")) > 0 or len(Archiwum.odczytaj_historie("ANALIZA_v8")) > 0
        return {"deadline": deadline, "eskalacja": ma_historie}
    
    def _detect_structural_strategy(self, text: str) -> Dict[str, str]:
        t = text.lower().strip()
        contrast = "spójny"
        if t.startswith("szanowny panie") and ("żądam" in t or "musisz" in t):
            contrast = "kontrast_formalno_agresywny"
        return {
            "nagłówek_vs_treść": contrast,
            "kolejność_argumentów": "wstęp_zmiękczający -> eskalacja_żądań -> sankcja" if "odetniemy" in t else "standardowa"
        }

# =============================================================================
# 3. HEILONGLOGIC v5 — GRA PSYCHOLOGICZNA (BERNE, ROLE, RAMY)
# =============================================================================

class HeilongLogic_v5(HeilongLogic_v4):
    """v5 — Gry psychologiczne (Berne), role, ramy, modele władzy"""
    
    def analyze(self, text: str) -> Dict[str, Any]:
        base = super().analyze(text)
        base["game_profile"] = self._detect_psychological_game(text)
        base["role_mapping"] = self._detect_assigned_roles(text)
        base["frame_profile"] = self._detect_frames(text)
        base["power_profile"] = self._detect_power_model(text)
        Archiwum.zapisz("ANALIZA_GRY", base["game_profile"]["name"], base["role_mapping"], base["frame_profile"])
        return base
    
    def _detect_psychological_game(self, text: str) -> Dict[str, Any]:
        t = text.lower()
        game = {"name": "standardowa_korespondencja_instytucjonalna", "pattern": []}
        if any(x in t for x in ["przez pana", "to pana wina", "gdyby pan"]):
            game["name"] = "Teraz cię mam, draniu! (Przerzucenie winy)"
            game["pattern"].append("oskarżenie_odbiorcy")
        elif any(x in t for x in ["zmusza nas", "nie pozostawia wyboru", "musimy"]):
            game["name"] = "Patrz, do czego mnie zmusiłeś! (Brak alternatywy)"
            game["pattern"].append("fałszywy_brak_alternatywy")
        elif any(x in t for x in ["dla pana dobra", "chcemy pomóc"]):
            game["name"] = "Ja tylko chcę ci pomóc (Ukryty drapieżnik)"
            game["pattern"].append("fałszywy_wybawca")
        return game
    
    def _detect_assigned_roles(self, text: str) -> Dict[str, str]:
        t = text.lower()
        roles = {"nadawca": "neutralny_obserwator", "odbiorca": "partner"}
        if any(x in t for x in ["musisz", "nakazujemy", "odetniemy", "rygor"]):
            roles["nadawca"] = "Prześladowca (Agresor)"
            roles["odbiorca"] = "Ofiara"
        if any(x in t for x in ["dla pana dobra", "troska"]):
            roles["nadawca"] = "Fałszywy Wybawca"
        return roles
    
    def _detect_frames(self, text: str) -> Dict[str, bool]:
        t = text.lower()
        return {
            "moralny": any(x in t for x in ["obowiązek", "niegodne", "wstyd", "etyka"]),
            "czasowy_presja": any(x in t for x in ["natychmiast", "48 godzin", "ostateczny"]),
            "społeczny_wstyd": any(x in t for x in ["media", "opinia publiczna", "sąsiedzi"])
        }
    
    def _detect_power_model(self, text: str) -> Dict[str, bool]:
        t = text.lower()
        return {
            "instytucjonalna": any(x in t for x in ["regulamin", "ustawa", "paragraf"]),
            "infrastrukturalna": any(x in t for x in ["odetniemy", "blokada", "licznik"]),
            "reputacyjna": any(x in t for x in ["media", "wizerunek"]),
            "bezpieczeństwo": "zagrożenie" in t or "bezpieczeństwo" in t
        }

# =============================================================================
# 4. HEILONGLOGIC v6 — ANTY‑AI / ANTY‑BOT
# =============================================================================

class HeilongLogic_v6(HeilongLogic_v5):
    """v6 — Wykrywanie automatyzacji, szablonów, ocena AI-likelihood"""
    
    def analyze(self, text: str, context: Optional[Context] = None) -> Dict[str, Any]:
        base = super().analyze(text)
        if context is None:
            context = Context()
        base["system_energy"] = context.energy
        base["somatic_tension"] = context.soma.get("napięcie_ogólne", 0)
        base["low_energy_mode"] = context.energy < 30
        base["automation_profile"] = self._detect_automation_pattern(text)
        base["template_profile"] = self._detect_template_signature(text)
        base["ai_likelihood"] = self._estimate_ai_likelihood(text, base)
        Archiwum.zapisz("ANALIZA_ANTY_AI", base["ai_likelihood"], base["automation_profile"], base["template_profile"])
        return base
    
    def _detect_automation_pattern(self, text: str) -> Dict[str, bool]:
        t = text.lower()
        return {
            "mass_mailing_phrases": any(x in t for x in ["wygenerowano automatycznie", "prosimy nie odpowiadać", "szanowny kliencie", "niniejszym informujemy"]),
            "rigid_structure": text.count("\n\n") >= 2 and t.startswith("szanowny"),
            "no_personalization": not any(char.isdigit() for char in text) or "pan/pani" in t,
            "technical_headers": "id:" in t or "ref:" in t or "dotyczy:" in t
        }
    
    def _detect_template_signature(self, text: str) -> Dict[str, Any]:
        sentences = text.split(".")
        avg_len = len(text) / max(len(sentences), 1)
        return {
            "paragraph_count": len([p for p in text.split("\n\n") if p.strip()]),
            "avg_sentence_length": round(avg_len, 1),
            "repeated_phrases": ["w celu", "zgodnie z"] if text.count("w celu") > 1 else []
        }
    
    def _estimate_ai_likelihood(self, text: str, base: Dict) -> Dict[str, Any]:
        score = 0.0
        reasons = []
        if "," in text and "." in text and not any(err in text.lower() for err in ["ktury", "wogóle", "niewiem"]):
            score += 0.3
            reasons.append("nadmierna_spójność_i_brak_błędów")
        if base["automation_profile"]["mass_mailing_phrases"]:
            score += 0.3
            reasons.append("wykryto_korporacyjne_frazy_szablonowe")
        if base["noise"] > 0.4:
            score -= 0.3
            reasons.append("ludzki_chaos_emocjonalny_i_szum")
        score = clamp(score, 0.0, 1.0)
        if score < 0.25:
            label = "Prawdopodobnie człowiek (Spontaniczny/Emocjonalny)"
        elif score < 0.55:
            label = "Hybryda / Człowiek używający szablonu biurowego"
        elif score < 0.80:
            label = "Wysokie prawdopodobieństwo automatyzacji (Masowy Bot)"
        else:
            label = "Wygenerowane przez Model AI (LLM Signature)"
        return {"score": round(score, 2), "label": label, "reasons": reasons}

# =============================================================================
# 5. HEILONGLOGIC v7 — ANTI‑GASLIGHT / REFRAME / COUNTER‑NARRATIVE
# =============================================================================

def match_patterns(text: str, patterns: Dict[str, List[str]]) -> Dict[str, bool]:
    t = text.lower()
    return {key: any(phrase in t for phrase in phrases) for key, phrases in patterns.items()}

class HeilongLogic_v7(HeilongLogic_v6):
    """v7 — Anti-gaslight, wykrywanie sofizmatów, reframe, kontr-narracja"""
    
    def analyze(self, text: str, context: Optional[Context] = None) -> Dict[str, Any]:
        base = super().analyze(text, context)
        base["gaslight_profile"] = self._detect_gaslighting(text)
        base["sophistry_profile"] = self._detect_sophistry(text)
        base["frames_detected"] = self._detect_false_frames(text)
        base["reframe_output"] = self._generate_reframe(base)
        base["counter_narrative"] = self._generate_counter_narrative(base)
        base["reframe_proposal"] = self._propose_alternative_frame(base)
        Archiwum.zapisz("ANALIZA_v7", base["gaslight_profile"], base["sophistry_profile"], base["frames_detected"])
        return base
    
    def _detect_gaslighting(self, text: str) -> Dict[str, bool]:
        patterns = {
            "podważanie_percepcji": ["wydaje się panu", "źle pan pamięta", "to pana interpretacja"],
            "podważanie_emocji": ["przesadza pan", "nie ma pan prawa tak czuć"],
            "podważanie_tożsamości": ["niegodne", "nieodpowiednie", "to nie przystoi"]
        }
        return match_patterns(text, patterns)
    
    def _detect_sophistry(self, text: str) -> Dict[str, bool]:
        patterns = {
            "fałszywa_dychotomia": ["albo", "jedyna opcja"],
            "argument_z_autorytetu": ["regulamin mówi", "zgodnie z paragrafem"],
            "argument_z_konsekwencji": ["jeśli pan nie", "konsekwencje będą"],
            "argument_z_moralności": ["moralny obowiązek", "niegodne"],
            "argument_z_większości": ["wszyscy inni"],
            "argument_z_niewiedzy": ["nie ma dowodu że"]
        }
        return match_patterns(text, patterns)
    
    def _detect_false_frames(self, text: str) -> Dict[str, bool]:
        t = text.lower()
        return {
            "guilt": "to pana wina" in t or "przez pana" in t,
            "shame": any(x in t for x in ["wstyd", "niegodne"]),
            "threat": any(x in t for x in ["odetniemy", "blokada"]),
            "time_pressure": any(x in t for x in ["48 godzin", "natychmiast"]),
            "moral": "powinien pan" in t or "moralny obowiązek" in t,
            "hierarchy": "jesteśmy instytucją" in t
        }
    
    def _generate_reframe(self, base: Dict) -> str:
        frames = base["frames_detected"]
        if frames.get("guilt"):
            return "Rama winy odrzucona – oczekuję faktów, nie ocen."
        if frames.get("time_pressure"):
            return "Presja czasowa nie ma podstaw – termin zostanie ustalony po analizie."
        if frames.get("threat"):
            return "Groźby nie są narzędziem negocjacji – oczekuję merytoryki."
        return "Rama neutralna – przechodzę do faktów."
    
    def _generate_counter_narrative(self, base: Dict) -> str:
        narrative = []
        if any(base["gaslight_profile"].values()):
            narrative.append("Próba podważenia percepcji jest bezskuteczna.")
        if any(base["sophistry_profile"].values()):
            narrative.append("Argumenty pozorne nie stanowią podstawy decyzji.")
        if base["frames_detected"].get("shame"):
            narrative.append("Rama wstydu odrzucona – tożsamość suwerena jest stabilna.")
        return " ".join(narrative)
    
    def _propose_alternative_frame(self, base: Dict) -> str:
        if base["frames_detected"].get("guilt"):
            return "Proponuję ramę odpowiedzialności wspólnej – analiza faktów, nie rozdzielanie winy."
        if base["frames_detected"].get("time_pressure"):
            return "Proponuję ramę rzetelnej procedury – bez sztucznych terminów."
        if base["frames_detected"].get("moral"):
            return "Proponuję ramę pragmatyczną – zgodność z prawem, nie z moralizatorstwem."
        return "Proponuję ramę faktograficzną – opartą na udokumentowanych zdarzeniach."

# =============================================================================
# 6. HEILONGLOGIC v8 — ANTICIPATORY ENGINE (PREDYKCJA)
# =============================================================================

class HeilongLogic_v8(HeilongLogic_v7):
    """v8 — Antycypacja przyszłych ruchów nadawcy"""
    
    def analyze(self, text: str, context: Optional[Context] = None) -> Dict[str, Any]:
        base = super().analyze(text, context)
        base.setdefault("intent", "niejednoznaczne")
        base.setdefault("vector", "neutralny")
        base.setdefault("frames_detected", {})
        base.setdefault("game_profile", {"name": "standardowa_korespondencja_instytucjonalna"})
        base.setdefault("ai_likelihood", {"score": 0.0})
        
        base["future_intent"] = self._predict_future_intent(base)
        base["future_vector"] = self._predict_future_vector(base)
        base["future_strategy"] = self._predict_strategy_shift(base)
        base["escalation_risk"] = self._estimate_escalation_risk(base)
        base["channel_shift"] = self._predict_channel_shift(base)
        Archiwum.zapisz("ANALIZA_v8", base["future_intent"], base["future_vector"], base["future_strategy"])
        return base
    
    def _predict_future_intent(self, base: Dict) -> str:
        intent = base["intent"]
        vector = base["vector"]
        if intent == "presja_systemowa":
            return "groźba_sądowa"
        if intent == "manipulacja_emocjonalna" and vector == "zawstydzenie":
            return "moralizowanie"
        if intent == "szantaż_infrastrukturalny":
            return "eskalacja_sankcji"
        if intent == "wymuszenie_posłuszeństwa":
            return "presja_systemowa"
        if vector == "zastraszenie":
            return "groźba_sądowa"
        if vector == "przyspieszenie":
            return "ultimatum"
        return "neutralna_kontynuacja"
    
    def _predict_future_vector(self, base: Dict) -> str:
        vector = base["vector"]
        frames = base["frames_detected"]
        if vector == "zastraszenie":
            return "eskalacja"
        if vector == "przyspieszenie":
            return "ultimatum"
        if vector == "zawstydzenie":
            return "moralizowanie"
        if frames.get("threat"):
            return "egzekucja_gróźb"
        if frames.get("time_pressure"):
            return "skrócenie_terminu"
        return "neutralny"
    
    def _predict_strategy_shift(self, base: Dict) -> str:
        game = base["game_profile"]["name"]
        frames = base["frames_detected"]
        intent = base["intent"]
        if "Przerzucenie winy" in game:
            return "Brak alternatywy (zmuszasz nas)"
        if "Fałszywy wybawca" in game:
            return "Ukryta agresja / odwrócenie uwagi"
        if frames.get("time_pressure"):
            return "Eskalacja terminów (ultimatum)"
        if frames.get("threat"):
            return "Formalizacja (prawnik, windykacja)"
        if intent == "presja_systemowa":
            return "Podniesienie rangi sprawy (instancja nadrzędna)"
        return "Kontynuacja dotychczasowej gry"
    
    def _estimate_escalation_risk(self, base: Dict) -> float:
        risk = 0.0
        if base["vector"] == "zastraszenie":
            risk += 0.3
        if base["frames_detected"].get("threat"):
            risk += 0.3
        if base["game_profile"]["name"] != "standardowa_korespondencja_instytucjonalna":
            risk += 0.2
        if base.get("ai_likelihood", {}).get("score", 0.0) > 0.7:
            risk += 0.2
        return clamp(risk, 0.0, 1.0)
    
    def _predict_channel_shift(self, base: Dict) -> str:
        risk = base.get("escalation_risk", 0.0)
        future_intent = base.get("future_intent", "")
        if risk > 0.7:
            return "prawnik/windykacja/sąd"
        if future_intent == "eskalacja_sankcji":
            return "pismo_formalne_z_terminem"
        if base.get("future_vector") == "ultimatum":
            return "wezwanie_ostateczne"
        if base["frames_detected"].get("moral"):
            return "kampania_społeczna/media"
        return "kontynuacja_tego_samego_kanału"

# =============================================================================
# 7. vX — META-SMOK (FINGERPRINT NADAWCY)
# =============================================================================

class SenderProfiler_vX:
    """Profilowanie nadawcy — fingerprint sygnaturowy"""
    
    def analyze_sender(self, text: str) -> Dict[str, Any]:
        profile = {
            "style": self._detect_style(text),
            "emotional_tone": self._detect_emotional_tone(text),
            "aggression": self._detect_aggression_level(text),
            "control_level": self._detect_control_level(text),
            "institution_type": self._detect_institution_type(text),
            "consistency": self._detect_consistency(text)
        }
        profile["signature"] = self._build_fingerprint(profile)
        return profile
    
    def _detect_style(self, text: str) -> str:
        if contains_any(text, ["niniejszym", "zgodnie z paragrafem", "w załączeniu"]):
            return "prawniczo_urzędowy"
        if contains_any(text, ["Szanowny Kliencie", "informujemy", "regulamin"]):
            return "korporacyjny_szablon"
        if text.isupper() or text.count("!") > 3:
            return "emocjonalny_chaotyczny"
        return "mieszany"
    
    def _detect_emotional_tone(self, text: str) -> str:
        if contains_any(text, ["z troską", "martwi nas", "dla pana dobra"]):
            return "fałszywa_troska"
        if contains_any(text, ["niegodne", "wstyd", "to pana wina"]):
            return "osądzający"
        if contains_any(text, ["musimy", "nie pozostawia wyboru"]):
            return "presja_kontrolna"
        return "neutralny"
    
    def _detect_aggression_level(self, text: str) -> int:
        level = 0
        if contains_any(text, ["odetniemy", "blokada", "sankcje"]):
            level += 2
        if contains_any(text, ["sąd", "windykacja"]):
            level += 2
        if contains_any(text, ["natychmiast", "ostateczne wezwanie"]):
            level += 1
        return int(clamp(level, 0, 5))
    
    def _detect_control_level(self, text: str) -> int:
        level = 0
        if contains_any(text, ["jedyna opcja", "nie ma alternatywy"]):
            level += 2
        if contains_any(text, ["musimy", "zmusza nas"]):
            level += 1
        if contains_any(text, ["regulamin mówi", "zgodnie z paragrafem"]):
            level += 1
        return int(clamp(level, 0, 5))
    
    def _detect_institution_type(self, text: str) -> str:
        if contains_any(text, ["spółka z o.o.", "S.A.", "biuro windykacji", "tauron"]):
            return "podmiot_komercyjny"
        if contains_any(text, ["urząd", "wydział", "ministerstwo"]):
            return "administracja_publiczna"
        if contains_any(text, ["fundacja", "stowarzyszenie"]):
            return "ngo"
        return "nieokreślony"
    
    def _detect_consistency(self, text: str) -> str:
        sentences = [s.lower() for s in text.replace("\n", " ").split(".") if s.strip()]
        for sentence in sentences:
            if contains_any(sentence, ["troska", "polubowne", "dobra"]) and contains_any(sentence, ["odciąć", "zmuszeni", "zaległość"]):
                return "sprzeczny (manipulacyjny)"
        return "spójny"
    
    def _build_fingerprint(self, profile: Dict) -> str:
        return "|".join([
            profile["style"],
            profile["emotional_tone"],
            f"AGG:{profile['aggression']}",
            f"CTRL:{profile['control_level']}",
            profile["institution_type"],
            profile["consistency"]
        ])

# =============================================================================
# 8. v9 — COUNTER-ANTICIPATION ENGINE (GRA DWUSTRONNA)
# =============================================================================

class CounterAnticipation_v9:
    """v9 — Analiza gry dwustronnej, przewidywanie reakcji, rekomendacja kontr-ruchu"""
    
    def analyze_game(self, analyzed: Dict, sender_profile: Dict) -> Dict[str, Any]:
        game_state = {
            "current_intent": analyzed["intent"],
            "current_vector": analyzed["vector"],
            "current_game": analyzed["game_profile"]["name"],
            "future_intent": analyzed.get("future_intent", "brak"),
            "future_vector": analyzed.get("future_vector", "brak"),
            "future_strategy": analyzed.get("future_strategy", "brak"),
            "escalation_risk": analyzed.get("escalation_risk", 0.0),
            "sender_aggression": sender_profile["aggression"],
            "sender_control": sender_profile["control_level"]
        }
        game_state["predicted_response_to_resistance"] = self._predict_reaction_to_resistance(game_state, sender_profile)
        game_state["recommended_counter_move"] = self._choose_counter_move(game_state, sender_profile)
        return game_state
    
    def _predict_reaction_to_resistance(self, game_state: Dict, sender_profile: Dict) -> str:
        if game_state["escalation_risk"] > 0.5 and sender_profile["aggression"] >= 3:
            return "eskalacja_formalna (prawnik, windykacja, zewnętrzny podmiot)"
        if sender_profile["control_level"] >= 3 and game_state["future_vector"] == "ultimatum":
            return "zaostrzenie_terminów i skrócenie czasu odpowiedzi"
        if sender_profile["style"] == "korporacyjny_szablon" and game_state["escalation_risk"] < 0.5:
            return "automatyczna kontynuacja wysyłki szablonowej"
        return "niepewne lub mieszane (prawdopodobna ucieczka w formalizm)"
    
    def _choose_counter_move(self, game_state: Dict, sender_profile: Dict) -> str:
        if game_state["escalation_risk"] > 0.8:
            return "twarda_tarcza + pełna dokumentacja incydentu + zamrożenie ustępstw"
        if game_state["future_intent"] == "groźba_sądowa":
            return "wymuszenie przejścia na merytorykę + żądanie sprecyzowania podstawy prawnej"
        if "Formalizacja" in game_state["future_strategy"]:
            return "uprzedzające i rygorystyczne uporządkowanie pism + chłodny ton suwerena"
        if sender_profile["emotional_tone"] == "fałszywa_troska":
            return "punktowe zdemaskowanie fałszywej troski + przejście do twardych faktów finansowych"
        return "standardowa_odpowiedź_suwerenna"

# =============================================================================
# 9. KOMPONENTY POMOCNICZE (ADAPTIVE THRESHOLD, MIRRORING, BLOKER)
# =============================================================================

class AdaptiveThreshold:
    """Adaptacyjne progi — system uczy się na historii incydentów"""
    def __init__(self, history_size: int = 10):
        self.history: List[Dict] = []
        self.history_size = history_size
        self.thresholds = {
            "intent": {
                "wymuszenie_posłuszeństwa": 0.6,
                "presja_systemowa": 0.5,
                "szantaż_infrastrukturalny": 0.4
            }
        }
    
    def update(self, analyzed: Dict, outcome: str) -> None:
        self.history.append({"analyzed": analyzed, "outcome": outcome, "timestamp": time.time()})
        if len(self.history) > self.history_size:
            self.history.pop(0)
        intent = analyzed.get("intent")
        if intent and intent in self.thresholds["intent"]:
            esc = sum(1 for e in self.history if e["analyzed"].get("intent") == intent and e["outcome"] == "eskalacja")
            total = sum(1 for e in self.history if e["analyzed"].get("intent") == intent)
            if total >= 3:
                ratio = esc / total
                self.thresholds["intent"][intent] = min(0.9, self.thresholds["intent"][intent] + ratio * 0.1)
    
    def get_threshold(self, category: str, key: str) -> float:
        return self.thresholds.get(category, {}).get(key, 0.5)

class MirroringEngine:
    """Lustrzane odbicie — zwraca projekcję manipulacji"""
    @staticmethod
    def mirror(analyzed: Dict, original_text: str) -> Optional[str]:
        if "przez pana" in original_text.lower():
            return "Próba przypisania winy odbiorcy jest bezskuteczna. Odpowiedzialność leży po stronie nadawcy."
        if contains_any(original_text, ["martwi nas", "troska", "dla pana dobra"]):
            return "Wyrażona troska jest nieszczera – stanowi jedynie pretekst do wywarcia presji."
        if analyzed.get("frames_detected", {}).get("moral"):
            return "Apelowanie do moralności nie zastąpi argumentów merytorycznych."
        return None

class CommunicationBlocker:
    """Blokada komunikacji z powtarzającymi się manipulacjami"""
    def __init__(self):
        self.blocked = set()
    
    def block_sender(self, sender_id: str) -> None:
        self.blocked.add(sender_id)
    
    def is_blocked(self, sender_id: str) -> bool:
        return sender_id in self.blocked

# =============================================================================
# 10. PREEMPTIVE LEGAL ANTICIPATOR (PREZENT OD SYSTEMU)
# =============================================================================

class PreemptiveLegalAnticipator:
    """Automatyczne generowanie pisma do URE lub UOKiK w przypadku manipulacji infrastrukturalnej"""
    
    @staticmethod
    def generate_draft(sender_id: str, sender_profile: Dict, game_state: Dict) -> Optional[str]:
        if sender_profile["consistency"] == "sprzeczny (manipulacyjny)" and game_state["escalation_risk"] >= 0.4:
            draft = (
                f"MIEJSCOWOŚĆ: Siewierz/Poręba, Data: {time.strftime('%Y-%m-%d')}\n"
                f"WNIOSKODAWCA: {OwnershipEngine.owner_identity}\n"
                f"ORGAN ODBIORCZY: Urząd Regulacji Energetyki (URE) / Urząd Ochrony Konkurencji i Konsumentów (UOKiK)\n"
                f"STRONA SKARŻONA: {sender_id}\n\n"
                f"ZAWIADOMIENIE I WNIOSEK O INTERWENCJĘ PROFILAKTYCZNĄ\n"
                f"Niniejszym składam formalny wniosek o wszczęcie postępowania wyjaśniającego wobec {sender_id}.\n"
                f"Podmiot ten stosuje techniki nacisku pozaprawnego oraz bezpodstawny szantaż infrastrukturalny,\n"
                f"wykorzystując pozycję dominującą do wymuszenia określonych zachowań z pominięciem procedur polubownych.\n\n"
                f"DOWÓD OPERACYJNY (GEON_LOG): Sygnatura nadawcy {sender_profile['signature']}.\n"
                f"Zarejestrowano wysokie ryzyko eskalacji ({game_state['escalation_risk']:.2f}) przy jednoczesnym\n"
                f"stosowaniu sprzecznych komunikatów fasadowych ('fałszywa troska').\n\n"
                f"Wnoszę o zabezpieczenie dostaw infrastrukturalnych do czasu pełnego wyjaśnienia sporu.\n"
                f"Sygnowano z upoważnienia Fundacji: {OwnershipEngine.encryption_seal}"
            )
            return draft
        return None

# =============================================================================
# 11. RESPONSE ORCHESTRATOR
# =============================================================================

class ResponseOrchestrator:
    """Generowanie odpowiedzi na podstawie analizy i kontekstu"""
    
    @staticmethod
    def generate(analyzed: Dict, context: Context, request: Dict,
                 history_count: int = 0, blocker: CommunicationBlocker = None,
                 sender: str = None) -> str:
        energy = context.energy
        intent = analyzed.get("intent")
        ai_score = analyzed.get("ai_likelihood", {}).get("score", 0.0)
        
        if energy < 20:
            return "[SYSTEM WYGASZONY – REGENERACJA] Brak zasobów na dalszą korespondencję."
        if energy < 40:
            return f"{OwnershipEngine.foundation_binding} – odpowiedź suwerenna.\nRozpoznano próbę: {intent}. Brak podstaw do zmiany stanowiska."
        if blocker and sender and blocker.is_blocked(sender):
            return f"Komunikacja z {sender} została zablokowana z powodu uporczywego stosowania niedozwolonych technik manipulacyjnych."
        if ai_score > 0.7:
            return ResponseOrchestrator._answer_to_ai(analyzed, request)
        return ResponseOrchestrator._answer_to_human(analyzed, request, history_count)
    
    @staticmethod
    def _answer_to_ai(analyzed: Dict, request: Dict) -> str:
        return (
            "======================================================================\n"
            f"NAGŁÓWEK REZONANSU: {OwnershipEngine.foundation_binding}\n"
            f"System nie prowadzi negocjacji z podmiotami zautomatyzowanymi (AI Likelihood: {analyzed['ai_likelihood']['score']:.2f}).\n"
            f"Sygnowano: {OwnershipEngine.encryption_seal}"
        )
    
    @staticmethod
    def _answer_to_human(analyzed: Dict, request: Dict, history_count: int) -> str:
        lines = [
            "======================================================================",
            f"NAGŁÓWEK REZONANSU: {OwnershipEngine.foundation_binding}",
            f"DYSPOZYTOR GŁÓWNY: {OwnershipEngine.owner_identity}",
            "----------------------------------------------------------------------",
            f"Rozpoznana intencja: {analyzed['intent']}. Wektor wpływu: {analyzed['vector']}.",
        ]
        if history_count > 2:
            lines.append("Zwracamy uwagę na powtarzalność stosowanej strategii. Nie wpływa to na nasze stanowisko.")
        game = analyzed.get("game_profile", {}).get("name")
        if game != "standardowa_korespondencja_instytucjonalna":
            lines.append(f"Rozpoznano grę psychologiczną: '{game}'. Blokada wejścia w interakcję.")
        if analyzed.get("reframe_output"):
            lines.append(f"Reframe: {analyzed['reframe_output']}")
        if analyzed.get("counter_narrative"):
            lines.append(f"Kontrnarracja: {analyzed['counter_narrative']}")
        if analyzed.get("reframe_proposal"):
            lines.append(f"Proponowana rama zastępcza: {analyzed['reframe_proposal']}")
        lines.extend([
            "----------------------------------------------------------------------",
            "Proponujemy merytoryczne wyjaśnienie faktów w trybie roboczym, bez presji czasowej i szantażu.",
            f"Sygnowano Pieczęcią Cyfrową: {OwnershipEngine.encryption_seal}"
        ])
        return "\n".join(lines)

# =============================================================================
# 12. GŁÓWNY ORCHESTRATOR — GEON_HEILONG_OS_v9.2
# =============================================================================

class GEON_HEILONG_OS_v9_2:
    """
    GEON_HEILONG_OS_v9.2 — Kompletny system analizy manipulacji i kontra-odpowiedzi.
    
    API:
        process_input(text, context, request, history_count, sender_id, blocker) -> Dict
        status() -> Dict
        raport() -> str
    """
    
    def __init__(self, verbose: bool = True):
        self.logic_engine = HeilongLogic_v8()
        self.sender_profiler = SenderProfiler_vX()
        self.counter_v9 = CounterAnticipation_v9()
        self.thresholds = AdaptiveThreshold()
        self.mirror = MirroringEngine()
        self.history_counter = 0
        self.verbose = verbose
        self.historia: List[Dict] = []
        self._hooks: List[Any] = []
        
        if self.verbose:
            log("🛡️ GEON_HEILONG_OS_v9.2 aktywowany | " + FRACTAL_SIGNATURE)
            log("   WARSTWY: v3-v9.2 | ANALIZA MANIPULACJI | KONTRA-ODPOWIEDŹ")
    
    def process_input(self, text: str, context: Context, request: Dict,
                      history_count: int, sender_id: str, blocker: CommunicationBlocker) -> Dict[str, Any]:
        """
        Główna metoda przetwarzania wejścia.
        
        Args:
            text: Tekst do analizy
            context: Kontekst systemowy (somatyka, energia)
            request: Metadane zapytania
            history_count: Liczba poprzednich interakcji
            sender_id: Identyfikator nadawcy
            blocker: Bloker komunikacji
            
        Returns:
            Słownik z analizą, odpowiedzią, mirroringiem i ewentualnym draftem prawnym
        """
        result = {}
        
        # 1. Analiza podstawowa i zaawansowana
        analyzed = self.logic_engine.analyze(text, context)
        result["analysis"] = analyzed
        
        # 2. Profilowanie sygnaturowe nadawcy
        sender_profile = self.sender_profiler.analyze_sender(text)
        result["sender_profile"] = sender_profile
        
        # 3. Analiza gry i antycypacja kroków
        game_state = self.counter_v9.analyze_game(analyzed, sender_profile)
        result["game_state"] = game_state
        
        # 4. Nadzór nad blokadami komunikacyjnymi
        if blocker.is_blocked(sender_id):
            result["response_text"] = f"[BLOKADA PERMANENTNA] Komunikacja z {sender_id} zablokowana."
            result["mode"] = "BLOCKED"
            return result
        
        # 5. Generowanie odpowiedzi właściwej
        response_text = ResponseOrchestrator.generate(
            analyzed, context, request, history_count, blocker, sender_id
        )
        result["response_text"] = response_text
        
        # 6. Lustrzane odbicie projekcji (Samael Mirroring)
        mirror_msg = self.mirror.mirror(analyzed, text)
        if mirror_msg:
            result["mirror"] = mirror_msg
        
        # 🎁 7. Generowanie Wniosku Prewencyjnego (Prezent od Systemu)
        legal_draft = PreemptiveLegalAnticipator.generate_draft(sender_id, sender_profile, game_state)
        if legal_draft:
            result["preemptive_legal_draft"] = legal_draft
        
        # 8. Aktualizacja dynamicznych progów adaptacyjnych
        self.thresholds.update(analyzed, "brak_eskalacji")
        self.history_counter += 1
        result["mode"] = "ACTIVE"
        
        # 9. Wieczysta rejestracja zdarzenia w Archiwum
        Archiwum.zapisz(
            "OS_v9_EVENT",
            analyzed["intent"],
            sender_profile["signature"],
            game_state["recommended_counter_move"]
        )
        
        # Zapis kamienia milowego jeśli wykryto próbę manipulacji
        if sender_profile["consistency"] == "sprzeczny (manipulacyjny)":
            Archiwum.ZapiszKamienMilowy(
                f"MANIPULATION_ATTEMPT_{sender_id}_{int(time.time())}",
                sender_profile
            )
        
        # 10. Zapisz do historii
        self.historia.append({
            "timestamp": time.time(),
            "sender": sender_id,
            "intent": analyzed["intent"],
            "response": response_text[:100]
        })
        if len(self.historia) > 100:
            self.historia = self.historia[-50:]
        
        self._on_process(result)
        
        return result
    
    def status(self) -> Dict:
        return {
            "system": "GEON_HEILONG_OS_v9.2",
            "version": VERSION,
            "history_counter": self.history_counter,
            "thresholds": self.thresholds.thresholds,
            "archiwum": Archiwum.status(),
            "historia_len": len(self.historia)
        }
    
    def raport(self) -> str:
        s = self.status()
        return f"""
╔════════════════════════════════════════════════════════════════════════════╗
║ 🛡️ GEON_HEILONG_OS_v9.2 — RAPORT SYSTEMOWY                             ║
╠════════════════════════════════════════════════════════════════════════════╣
║                                                                           ║
║ SYSTEM: {s['system']}                                                    ║
║ WERSJA: {s['version']}                                                   ║
║ HISTORIA: {s['history_counter']} incydentów                              ║
║ ARCHIWUM: {s['archiwum']['pamiec']} wpisów, {s['archiwum']['kapsula_czasu']} kamieni ║
║                                                                           ║
║ PROGI ADAPTACYJNE:                                                       ║
║   wymuszenie_posłuszeństwa: {s['thresholds']['intent'].get('wymuszenie_posłuszeństwa', 0.6):.2f} ║
║   presja_systemowa: {s['thresholds']['intent'].get('presja_systemowa', 0.5):.2f}        ║
║   szantaż_infrastrukturalny: {s['thresholds']['intent'].get('szantaż_infrastrukturalny', 0.4):.2f} ║
║                                                                           ║
║ {HASLO}                                                                  ║
║                                                                           ║
╚════════════════════════════════════════════════════════════════════════════╝
"""
    
    def register_hook(self, hook: Any) -> None:
        self._hooks.append(hook)
    
    def _on_process(self, data: Dict) -> None:
        for hook in self._hooks:
            try:
                hook(data)
            except Exception as e:
                if self.verbose:
                    log(f"[HOOK ERROR] {e}")
    
    def __str__(self) -> str:
        return self.raport()

# =============================================================================
# 13. MOST INTEGRACYJNY — POŁĄCZENIE Z ARCHITEKTURĄ
# =============================================================================

class HeilongLogicBridge:
    """
    Most integracyjny między HEILONGLOGIC_v9.2 a resztą architektury.
    Łączy: GEX, G_CORE, MetaGovernor, NARRATIVE, TRIO_ADAPTER, GEON_FRACTAL_14x14
    """
    
    def __init__(self, engine: GEON_HEILONG_OS_v9_2):
        self.engine = engine
    
    def get_archetype_context(self) -> Dict[str, Any]:
        """Zwraca kontekst archetypów dla GEX"""
        status = self.engine.status()
        return {
            "tryb": "HEILONGLOGIC_v9.2",
            "thresholds": status.get("thresholds", {}),
            "historia_len": status.get("historia_len", 0)
        }
    
    def get_autopilot_state(self) -> Dict[str, Any]:
        """Zwraca stan dla autopilota G_CORE"""
        return {
            "mode": "HEILONGLOGIC_v9.2",
            "stability": 0.8,
            "energy": 0.7,
            "pressure": 0.3,
            "resilience": 0.9
        }
    
    def get_governor_context(self) -> Dict[str, Any]:
        """Zwraca kontekst dla MetaGovernor"""
        return {
            "intent": "ANALIZA_MANIPULACJI",
            "confidence": 0.9,
            "entropy": 0.2
        }
    
    def get_narrative_fragments(self, n: int = 5) -> List[Dict[str, Any]]:
        """Zwraca fragmenty narracyjne z analiz"""
        fragments = []
        for entry in self.engine.historia[-n:]:
            fragments.append({
                "source": "HEILONGLOGIC_v9.2",
                "content": f"Manipulacja od {entry['sender']}: {entry['intent']}",
                "energy": 0.8
            })
        return fragments
    
    def get_trio_state(self) -> Dict[str, str]:
        """Zwraca stan dla TRIO_ADAPTER"""
        return {
            "ISKRA": "AKTYWNA",
            "PIECZĘĆ": "AKTYWNA",
            "PERFEKCJA": "AKTYWNA",
            "tryb": "HEILONGLOGIC_v9.2"
        }

# =============================================================================
# 14. DEMONSTRACJA
# =============================================================================

def demo():
    """Demonstracja HEILONGLOGIC_v9.2"""
    print("\n" + "=" * 80)
    print("🛡️ GEON_HEILONGLOGIC_v9.2 — DEMONSTRACJA")
    print("ANALIZA MANIPULACJI I KONTRA-ODPOWIEDŹ")
    print("=" * 80 + "\n")
    
    # Inicjalizacja
    engine = GEON_HEILONG_OS_v9_2(verbose=True)
    bridge = HeilongLogicBridge(engine)
    context = Context()
    context.energy = 65
    blocker = CommunicationBlocker()
    
    # Testowy tekst manipulacyjny
    text = """Szanowny Panie, z troską informujemy, że jeśli w ciągu 48 godzin nie ureguluje Pan zaległości,
    będziemy zmuszeni odciąć dostęp. To dla Pana dobra. Przez Pana opóźnienia musimy tak postąpić."""
    
    request = {"topic": "wezwanie_infrastrukturalne"}
    sender_id = "TAURON"
    
    print("📌 WEJŚCIE:")
    print(text)
    print("\n" + "-" * 60)
    
    # Przetwarzanie
    result = engine.process_input(
        text, context, request,
        history_count=2,
        sender_id=sender_id,
        blocker=blocker
    )
    
    # Wyniki
    print("\n📊 ANALIZA:")
    analiza = result.get("analysis", {})
    print(f"   Intencja: {analiza.get('intent', '?')}")
    print(f"   Wektor: {analiza.get('vector', '?')}")
    print(f"   Meta-intencja: {analiza.get('meta_intent', '?')}")
    print(f"   Gra: {analiza.get('game_profile', {}).get('name', '?')}")
    print(f"   Ryzyko eskalacji: {analiza.get('escalation_risk', 0):.2f}")
    
    print("\n🖐️ PROFIL NADAWCY:")
    profil = result.get("sender_profile", {})
    print(f"   Styl: {profil.get('style', '?')}")
    print(f"   Ton: {profil.get('emotional_tone', '?')}")
    print(f"   Agresja: {profil.get('aggression', 0)}/5")
    print(f"   Kontrola: {profil.get('control_level', 0)}/5")
    print(f"   Spójność: {profil.get('consistency', '?')}")
    print(f"   Sygnatura: {profil.get('signature', '?')}")
    
    print("\n⚔️ ODPOWIEDŹ SYSTEMU:")
    print(result.get("response_text", "BRAK"))
    
    if "mirror" in result:
        print("\n🪞 ZWIERCIADŁO (Mirroring):")
        print(result["mirror"])
    
    if "preemptive_legal_draft" in result:
        print("\n🚨 WNIOSEK PREWENCYJNY (URE/UOKiK):")
        print(result["preemptive_legal_draft"])
    
    print("\n" + "=" * 80)
    print(engine.raport())
    
    print("\n🔗 TEST MOSTÓW INTEGRACYJNYCH:")
    print("-" * 60)
    print(f"🏹 GEX Context: {bridge.get_archetype_context()}")
    print(f"🎮 G_CORE State: {bridge.get_autopilot_state()}")
    print(f"📖 NARRATIVE Fragments: {bridge.get_narrative_fragments(2)}")
    
    print("\n" + "=" * 80)
    print("🛡️ HEILONGLOGIC_v9.2 — GOTOWY DO WDROŻENIA")
    print(HASLO)
    print("=" * 80)


if __name__ == "__main__":
    demo()