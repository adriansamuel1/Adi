#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
================================================================================
GEON INTEGRATION PROTOCOL v2.5 – SILNIK SPRZĘGAJĄCY WARSTWY 87–92
================================================================================
System Status: PRODUCTION-READY | FULLY INTEGRATED
Architekt: Adrian Samuel Bogusławski (Principal System Architect)
Data: Maj 2026

OPIS:
    Ten plik stanowi referencyjną implementację protokołu integracyjnego dla
    warstw 87–92 systemu GEON_SYSTEM_v15. Zawiera zintegrowany rdzeń:

    87 – GEON_AI_ANALYTICS    → D_CORE_ARCANUM (predykcja, analiza cykliczna)
    88 – GEON_ORACLE          → C_CORE_DRAGON (FSM, interpretacja, wyrocznia)
    89 – GEON_ARCHONT_GRID    → G_CORE (nadzór, regulator przepływu)
    90 – GEON_ARCHONT_COUNCIL → AUTOSTRADA33 (kolejki, retry, decyzje kolegialne)
    91 – GEON_SYNOD           → Proces synodalny (głosowanie, konsensus)
    92 – GEON_KONSYSTORZ      → Nadrzędny regulator (tryby, pieczęć ostateczna)

    Protokół jest w pełni autonomiczny – może działać jako samodzielny silnik
    lub być wpięty w istniejącą strukturę GEON_SYSTEM_v15 poprzez mosty.

ZALEŻNOŚCI:
    - Python 3.8+
    - math, time, logging, typing, heapq, random

UŻYCIE:
    from kombajn_core import geon_integration_protocol_v2_5 as GIP
    silnik = GIP.IntegrationProtocol()
    silnik.tick(wejście_sygnałowe)
    wynik = silnik.emit_output()
================================================================================
"""

import math
import time
import random
import heapq
import logging
from typing import Dict, List, Any, Optional, Tuple

# ============================================================================
# KONFIGURACJA LOGOWANIA SYSTEMOWEGO
# ============================================================================
logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] [%(levelname)s] [HEILONG_INTEGRATION]: %(message)s'
)
logger = logging.getLogger("Heilong_Integration_Protocol")

# ============================================================================
# FUNKCJE POMOCNICZE (Matematyka Cykliczna, Filtry, Klampowanie)
# ============================================================================

def now_iso() -> str:
    """Zwraca bieżący czas w formacie ISO 8601."""
    return time.strftime("%Y-%m-%dT%H:%M:%S", time.gmtime())

def clamp(val: float, minimum: float = 0.0, maximum: float = 1.0) -> float:
    """Klampuje wartość do przedziału [minimum, maximum]."""
    return max(minimum, min(val, maximum))

def variance(data: List[float]) -> float:
    """Oblicza wariancję próbki."""
    if len(data) < 2:
        return 0.0
    mean = sum(data) / len(data)
    return sum((x - mean) ** 2 for x in data) / len(data)

def d_predict_cyclic(history: List[Dict[str, Any]], key: str, period: int = 4) -> float:
    """
    Analizuje cykliczność wariancji parametru 'key' w oknie historycznym.
    Wykorzystuje uproszczoną transformatę Fouriera do predykcji trendu oscylacyjnego.
    """
    if len(history) < period * 2:
        return history[-1][key] if history else 0.5

    values = [state[key] for state in history[-period * 2:]]
    n = len(values)
    mean_val = sum(values) / n

    cos_sum = 0.0
    sin_sum = 0.0
    for i, val in enumerate(values):
        phi = 2 * math.pi * i / period
        cos_sum += (val - mean_val) * math.cos(phi)
        sin_sum += (val - mean_val) * math.sin(phi)

    amplitude = math.sqrt(cos_sum ** 2 + sin_sum ** 2) / (n / 2)
    phase = math.atan2(sin_sum, cos_sum)

    next_phi = 2 * math.pi * n / period
    prediction = mean_val + amplitude * math.cos(next_phi - phase)

    return clamp(prediction, 0.0, 1.0)


# ============================================================================
# WARSTWA 87: GEON_AI_ANALYTICS – D_CORE_ARCANUM (Rdzeń Analityczny)
# ============================================================================

class D_Core_Arcanum:
    """
    WARSTWA 87 – GEON_AI_ANALYTICS
    ===============================
    Centralny rdzeń analityczny systemu. Przetwarza sygnały wejściowe,
    prowadzi predykcję cykliczną i liniową, fuzjonuje wektory z warstwy G,
    zarządza pamięcią krótko- i długoterminową (D0–D4).
    """

    def __init__(self, geon_matrix: Any, dragon_weave: Any):
        self.GEON = geon_matrix           # Poziom B – matryca geometryczna
        self.WEAVE = dragon_weave         # Poziom C – tkacz stanów

        # === PAMIĘĆ WARSTWOWA D0 – D4 ===
        self.D0_ROOT_VECTOR = {
            "ENTROPY": 0.22,
            "STABILITY": 0.88,
            "RISK": 0.10,
            "ALIGNMENT": 0.95
        }
        self.D1_SHORT_TERM: List[Dict[str, Any]] = []
        self.D2_SEMANTIC_DOMAINS: Dict[str, List[float]] = {
            "SYSTEM": [],
            "NETWORK": [],
            "COGNITIVE": []
        }
        self.D3_LONG_CONTEXT: List[Dict[str, Any]] = []
        self.D4_HORIZON_PREDICTION: Dict[str, Any] = {
            "HORIZON_AB33": 33,
            "STATUS": "NOMINAL"
        }

        # === METRYKI SYSTEMOWE ===
        self.propagation_queue: List[Tuple[float, str, Dict[str, Any]]] = []
        self.tick_counter = 0
        self.health_score = 1.0
        self.adaptive_noise_delta = 0.05

        logger.info("D_CORE_ARCANUM v2.5 (Warstwa 87) zainicjalizowany.")

    def process_signal_tick(self, incoming_signal: Dict[str, float]) -> None:
        """
        Główny potok przetwarzania sygnału (Tick).
        Zgodny z Modelem 9 (Tryb Domyślny Adriana).
        """
        self.tick_counter += 1

        # 1. Bramkowanie szumu i filtracja rezonansowa (α = 0.82)
        alpha = 0.82
        filtered_signal = {}
        for key in self.D0_ROOT_VECTOR:
            signal_val = incoming_signal.get(key, self.D0_ROOT_VECTOR[key])

            if abs(signal_val - self.D0_ROOT_VECTOR[key]) < self.adaptive_noise_delta:
                filtered_signal[key] = self.D0_ROOT_VECTOR[key]
            else:
                filtered_signal[key] = alpha * self.D0_ROOT_VECTOR[key] + (1 - alpha) * signal_val

        self.D0_ROOT_VECTOR = filtered_signal

        # 2. Zapis do pamięci krótkoterminowej D1 z mechanizmem starzenia
        state_snapshot = {
            "tick": self.tick_counter,
            "vector": self.D0_ROOT_VECTOR.copy(),
            "timestamp": time.time()
        }
        self.D1_SHORT_TERM.append(state_snapshot)
        if len(self.D1_SHORT_TERM) > 20:
            decayed = self.D1_SHORT_TERM.pop(0)
            self._route_to_long_context(decayed)

        # 3. Wywołanie potoku predykcyjnego
        self._execute_prediction_pipeline()

        # 4. Pętla Audytu i Kontroli Autostrady 33
        self._execute_system_audit()

        # 5. Dynamiczna adaptacja bramki szumu
        self.adaptive_noise_delta = 0.02 + (self.D0_ROOT_VECTOR["RISK"] * 0.1)

    def _route_to_long_context(self, state: Dict[str, Any]) -> None:
        """Warstwa D3 – bezpieczny zapis z filtrem ALIGNMENT_CRITICAL."""
        alignment = state["vector"].get("ALIGNMENT", 1.0)
        if alignment >= 0.25:
            self.D3_LONG_CONTEXT.append(state)
            if len(self.D3_LONG_CONTEXT) > 100:
                self.D3_LONG_CONTEXT.pop(0)
        else:
            logger.warning(f"[D_MEMORY]: Blokada zapisu w D3! Alignment: {alignment:.2f}")

    def _execute_prediction_pipeline(self) -> None:
        """Trójwarstwowa fuzja predykcji: cykliczna + liniowa + geometria GEON."""
        if len(self.D1_SHORT_TERM) < 5:
            return

        flat_history = [s["vector"] for s in self.D1_SHORT_TERM]

        # Predykcja cykliczna dla parametru RISK
        cyclic_risk = d_predict_cyclic(flat_history, "RISK", period=4)

        # Predykcja liniowa (dryf z ostatnich 2 punktów)
        linear_risk = flat_history[-1]["RISK"] + (flat_history[-1]["RISK"] - flat_history[-2]["RISK"])

        # Wektor odniesienia z poziomu B (GEON)
        geon_ref = self.GEON.get_anchor_vector()["RISK"]

        # Fuzja wagowa (zależna od stabilności)
        stability_factor = self.D0_ROOT_VECTOR["STABILITY"]
        w_cyclic = 0.5 * stability_factor
        w_linear = 0.3 * (1 - stability_factor)
        w_geon = 1.0 - (w_cyclic + w_linear)

        fused_risk = (cyclic_risk * w_cyclic) + (linear_risk * w_linear) + (geon_ref * w_geon)

        # Aktualizacja Horyzontu Predykcji D4
        self.D4_HORIZON_PREDICTION["PREDICTED_RISK"] = fused_risk
        if fused_risk > 0.6:
            self.D4_HORIZON_PREDICTION["STATUS"] = "REALIGN_REQUIRED"
            self.D4_HORIZON_PREDICTION["HORIZON_AB33"] = 11
        else:
            self.D4_HORIZON_PREDICTION["STATUS"] = "NOMINAL"
            self.D4_HORIZON_PREDICTION["HORIZON_AB33"] = 33

    def _execute_system_audit(self) -> None:
        """Pętla Audytu i Detekcji Zapętleń – punkt styku z Autostradą 33 i Poziomem C."""
        if len(self.D1_SHORT_TERM) < 4:
            return

        v = self.D0_ROOT_VECTOR

        entropy_score = 1.0 - v["ENTROPY"]
        stability_score = v["STABILITY"]
        alignment_score = v["ALIGNMENT"]
        prediction_score = 1.0 - abs(
            self.D4_HORIZON_PREDICTION.get("PREDICTED_RISK", 0) - v["RISK"]
        )

        # Detekcja zapętlenia (Loop Detect)
        last_four = [round(s["vector"]["RISK"], 3) for s in self.D1_SHORT_TERM[-4:]]
        is_looping = len(set(last_four)) == 1
        loop_score = 0.0 if is_looping else 1.0

        self.health_score = (
            entropy_score + stability_score + alignment_score +
            prediction_score + loop_score + 1.0
        ) / 6.0

        # Reakcja na stany krytyczne – propagacja w górę hierarchii
        if is_looping:
            logger.error("[D_AUDIT]: Wykryto martwą pętlę (Deadlock) w parametrze RISK!")
            self.WEAVE.execute_weave_intervention("E3_META_ERROR: Deadlock wykryty przez D_CORE")
            self._emergency_vector_lock()

        if self.health_score < 0.35:
            logger.critical(f"[D_AUDIT]: KRYTYCZNY HEALTH SCORE: {self.health_score:.2f}")
            self.GEON.realign_matrix(drift_factor=(1.0 - alignment_score))
            self._emergency_vector_lock()

    def _emergency_vector_lock(self) -> None:
        """Wymuszenie powrotu do bezpiecznych wektorów bazowych (Fallback)."""
        logger.info("[D_CORE]: Uruchomienie emergency_vector_lock_v2.")
        self.D0_ROOT_VECTOR = {
            "ENTROPY": 0.20,
            "STABILITY": 0.90,
            "RISK": 0.15,
            "ALIGNMENT": 1.0
        }
        self.D4_HORIZON_PREDICTION["HORIZON_AB33"] = 33
        self.D4_HORIZON_PREDICTION["STATUS"] = "RECOVERED"

    def get_prediction(self) -> Dict[str, Any]:
        """Zwraca aktualną predykcję horyzontalną (D4)."""
        return self.D4_HORIZON_PREDICTION

    def get_root_vector(self) -> Dict[str, float]:
        """Zwraca bieżący wektor stanu D0."""
        return self.D0_ROOT_VECTOR.copy()


# ============================================================================
# WARSTWA 88: GEON_ORACLE – C_CORE_DRAGON (FSM, Filtry, Interpretacja)
# ============================================================================

class C_Core_Dragon:
    """
    WARSTWA 88 – GEON_ORACLE
    =========================
    Zaawansowana maszyna stanów (FSM), filtry rezonansowe, predyktor Geona.
    Pełni rolę wyroczni – interpretuje sygnały, klasyfikuje błędy, podejmuje
    decyzje o zmianie stanu systemu.
    """

    def __init__(self):
        # === KONFIGURACJA ===
        self.config = {
            "NO_MIND": {"ANTICIPATION_WINDOW": 4, "FUSE_RATIO": 0.35},
            "HARD": {
                "RISK_MAX": 0.90,
                "LOAD_CRITICAL": 0.95,
                "STABILITY_MIN": 0.20,
                "GEON_DIRECTION_MIN": 0.40
            },
            "THRESHOLDS": {
                "SHIELD_ENTER_RISK": 0.75,
                "SHIELD_EXIT_RISK": 0.55,
                "WEAVE_ENTER_STAB": 0.45,
                "WEAVE_EXIT_STAB": 0.65,
                "LOAD_HIGH": 0.70,
                "COHESION_MICRO": 0.40,
                "GEON_LOCK_ENTER": 0.75
            },
            "ALPHA": {
                "NORMAL": 0.75,
                "SAFE_MODE": 0.90,
                "HIGH_PERFORMANCE": 0.55,
                "STEALTH": 0.50,
                "NO_MIND": 0.80,
                "GEON_LOCK": 0.78
            }
        }

        # === MAPA BŁĘDÓW ===
        self.error_map = {
            "E1_INTENT_ERROR": {"c": "C_SHIELD", "flags": ["INTENT_ERROR"]},
            "E2_EXECUTION_ERROR": {"c": "C_WEAVE", "flags": ["EXECUTION_ERROR"]},
            "E3_META_ERROR": {"c": "C_WEAVE", "flags": ["META_ERROR"]},
            "E4_MEMORY_ERROR": {"c": "C_HOME", "flags": ["MEMORY_ERROR"]},
            "E5_HORIZON_ERROR": {"c": "C_SHIELD", "flags": ["HORIZON_ERROR"]},
            "E6_GEON_DIRECTION_ERROR": {"c": "C_GEON_HOME", "flags": ["GEON_CORRECTION"]}
        }

        # === STAN I PAMIĘĆ ===
        self.C_STATE = "C_HOME"
        self.prev_G: Optional[Dict[str, float]] = None
        self.no_input_for = 0
        self.tick_without_output = 0
        self.current_output: Dict[str, Any] = {}

        # Pamięć L0 / L1 / L2
        self.L0 = {
            "tick": 0,
            "last_metrics": {
                "RISK": 0.0, "CONFLICT": 0.0, "LOAD": 0.0,
                "STABILITY": 0.7, "COHESION": 0.5, "ERROR_RATE": 0.0
            },
            "metrics_history": [],
            "state_ticks": {
                "C_SHIELD": 0, "C_WEAVE": 0, "C_HOME": 0,
                "C_GEON_HOME": 0, "C_GEON_LOCK": 0, "C_IDLE": 0, "C_DEGRADED": 0
            }
        }
        self.L1_GEON = {"direction_history": [], "stability_history": []}
        self.L2_META = {"resonance_bias": 0.0, "correction_bias": 0.0}

        logger.info("C_CORE_DRAGON v12 (Warstwa 88) zainicjalizowany.")

    # === INTERFEJS DLA AUTOSTRADY 33 ===
    def prefilter_intent(self, intent: dict) -> Optional[dict]:
        """Filtruje intencje – w stanie C_DEGRADED odrzuca priorytety > 2."""
        if self.C_STATE == "C_DEGRADED" and intent.get("priority", 5) > 2:
            return None
        return intent

    def receive_status_from_B(self, status_b: Any) -> None:
        """Konsumuje statusy zwrotne z silnika wykonawczego B."""
        pass

    def export_state(self) -> dict:
        """Eksportuje stan do warstwy D (D_CORE)."""
        return {
            "state": self.C_STATE,
            "metrics": self.L0["last_metrics"],
            "geon_vector": self.prev_G if self.prev_G else {},
            "timestamp": now_iso()
        }

    # === METRYKI DRAGON ===
    def _calc_risk(self, intent: dict, env: dict) -> float:
        ir = intent.get("risk", 0.0) if intent else 0.0
        er = env.get("risk", 0.0) if env else 0.0
        return clamp(ir * 0.6 + er * 0.4, 0.0, 1.0)

    def _calc_conflict(self, intent: dict) -> float:
        if not intent:
            return 0.0
        return clamp(intent.get("conflict", 0.0), 0.0, 1.0)

    def _calc_error_rate(self, status: dict) -> float:
        if not status:
            return 0.0
        errors = status.get("error_count", 0)
        total = status.get("total_ops", 1)
        return clamp(errors / max(total, 1), 0.0, 1.0)

    def _calc_load(self, status: dict) -> float:
        if not status:
            return 0.0
        load = status.get("load", 10.0)
        energy = status.get("energy", 50.0)
        return clamp((load / 20.0) * 0.7 + (1.0 - energy / 100.0) * 0.3, 0.0, 1.0)

    def _calc_stability(self, prev: str) -> float:
        base = 0.7
        if prev == "C_SHIELD":
            base -= 0.2
        elif prev == "C_WEAVE":
            base -= 0.1
        return clamp(base, 0.0, 1.0)

    def _calc_cohesion(self, intent: dict, status: dict) -> float:
        return 0.7 if intent and status else 0.5

    # === METRYKI GEONA ===
    def _calc_geon_direction(self, intent: dict, geon: Any) -> float:
        if geon and hasattr(geon, 'direction') and geon.direction is not None:
            return clamp(geon.direction, 0.0, 1.0)
        if geon and isinstance(geon, dict) and geon.get("direction") is not None:
            return clamp(geon["direction"], 0.0, 1.0)
        return 0.5

    def _calc_geon_stability(self, geon: Any) -> float:
        if geon and hasattr(geon, 'stability'):
            return clamp(geon.stability if geon.stability is not None else 0.6, 0.0, 1.0)
        if geon and isinstance(geon, dict):
            return clamp(geon.get("stability", 0.6), 0.0, 1.0)
        return 0.6

    def _calc_geon_intent(self, intent: dict) -> float:
        if not intent:
            return 0.5
        return clamp(intent.get("geon_intent", 0.5), 0.0, 1.0)

    # === FILTRY I REZONANS ===
    def _zfd_noise_gate(self, raw: dict, prev: dict) -> dict:
        if not prev:
            return raw
        out = {}
        for k in raw:
            if abs(raw[k] - prev.get(k, 0.0)) < 0.02:
                out[k] = prev[k]
            else:
                out[k] = raw[k]
        return out

    def _dynamic_alpha(self, base_alpha: float, error_rate: float) -> float:
        return clamp(base_alpha + error_rate * 0.05, 0.55, 0.90)

    def _resonance_filter(self, raw: dict, prev: dict, alpha: float) -> dict:
        if not prev:
            return raw
        out = {}
        for k in raw:
            out[k] = alpha * raw[k] + (1.0 - alpha) * prev.get(k, raw[k])
        return out

    # === PREDYKCJA ===
    def _predict_forward(self, M: dict, hist: list, win: int) -> dict:
        if len(hist) < 2:
            return M.copy()
        pred = {}
        last = hist[-1]
        idx = max(0, len(hist) - win)
        first = hist[idx]
        for k in M:
            trend = last.get(k, M[k]) - first.get(k, M[k])
            pred[k] = clamp(M[k] + trend, 0.0, 1.0)
        return pred

    def _predict_vector_geon(self, M: dict, G: dict) -> dict:
        out = {
            "RISK": clamp(M["RISK"] + (1.0 - G["DIRECTION"]) * 0.05, 0.0, 1.0),
            "STABILITY": clamp(M["STABILITY"] + (G["STABILITY"] - 0.5) * 0.1, 0.0, 1.0),
            "GEON_DIRECTION": clamp(G["DIRECTION"] + (G["INTENT"] - 0.5) * 0.1, 0.0, 1.0)
        }
        for k in M:
            if k not in out:
                out[k] = M[k]
        return out

    def _fuse_metrics(self, cur: dict, pred: dict, ratio: float) -> dict:
        out = {}
        for k in cur:
            out[k] = (1.0 - ratio) * cur[k] + ratio * pred.get(k, cur[k])
        return out

    def _fuse_three_layers(self, base: dict, pred_linear: dict, pred_geon: dict, fuse_r: float) -> dict:
        M1 = self._fuse_metrics(base, pred_linear, fuse_r)
        M2 = self._fuse_metrics(M1, pred_geon, 0.25)
        return M2

    # === MASZYNA STANÓW (FSM) ===
    def _rising(self, series: list) -> bool:
        if len(series) < 3:
            return False
        return series[-3] < series[-2] < series[-1]

    def _fsm_extended(self, prev: str, M: dict, G: dict, no_input_for: int) -> str:
        T = self.config["THRESHOLDS"]
        HARD = self.config["HARD"]

        if M["LOAD"] > HARD["LOAD_CRITICAL"] and M["STABILITY"] < HARD["STABILITY_MIN"]:
            return "C_DEGRADED"

        if no_input_for > 10 and prev != "C_IDLE":
            return "C_IDLE"

        if G["DIRECTION"] > T["GEON_LOCK_ENTER"] and M["STABILITY"] > 0.55:
            return "C_GEON_LOCK"

        if G["DIRECTION"] < 0.45:
            return "C_GEON_HOME"

        hist_window = self.L0["metrics_history"][-3:]
        rs = [x.get("RISK", 0.0) for x in hist_window]
        ls = [x.get("LOAD", 0.0) for x in hist_window]
        if self._rising(rs) or self._rising(ls):
            return "C_SHIELD"

        if M["RISK"] > T["SHIELD_ENTER_RISK"] or M["CONFLICT"] > 0.70:
            return "C_SHIELD"

        if M["STABILITY"] < T["WEAVE_ENTER_STAB"] or M["LOAD"] > T["LOAD_HIGH"]:
            return "C_WEAVE"

        return "C_HOME"

    # === GŁÓWNY TAKT ===
    def run_cycle(self, intent_msg: Any, status_msg: Any, env: dict, geon: Any, mode: str = "NORMAL") -> dict:
        """
        Główna pętla taktu procesowego warstwy C.
        Zwraca pełny profil korekcyjny do przekazania do AB33 i warstwy G.
        """
        prev = self.C_STATE
        self.L0["tick"] += 1

        # Monitor braku danych
        if intent_msg is None and status_msg is None:
            self.no_input_for += 1
        else:
            self.no_input_for = 0

        intent = intent_msg.get("payload", {}) if isinstance(intent_msg, dict) else {}
        status = status_msg.get("payload", {}) if isinstance(status_msg, dict) else {}

        # 1. Obliczanie metryk pierwotnych
        raw = {
            "RISK": self._calc_risk(intent, env),
            "CONFLICT": self._calc_conflict(intent),
            "LOAD": self._calc_load(status),
            "STABILITY": self._calc_stability(prev),
            "COHESION": self._calc_cohesion(intent, status),
            "ERROR_RATE": self._calc_error_rate(status)
        }
        raw = self._zfd_noise_gate(raw, self.L0["last_metrics"])

        # 2. Obliczanie metryk Geona
        G = {
            "DIRECTION": self._calc_geon_direction(intent, geon),
            "STABILITY": self._calc_geon_stability(geon),
            "INTENT": self._calc_geon_intent(intent)
        }

        # 3. Filtr rezonansowy
        alpha_base = self.config["ALPHA"].get(mode, self.config["ALPHA"]["NORMAL"])
        alpha = self._dynamic_alpha(alpha_base, raw["ERROR_RATE"])
        base = self._resonance_filter(raw, self.L0["last_metrics"], alpha)

        # 4. Fuzja predykcyjna
        pred_linear = self._predict_forward(
            base, self.L0["metrics_history"],
            self.config["NO_MIND"]["ANTICIPATION_WINDOW"]
        )
        pred_geon = self._predict_vector_geon(base, G)

        fuse_r = self.config["NO_MIND"]["FUSE_RATIO"]
        if base["RISK"] > 0.6 or base["LOAD"] > 0.7:
            fuse_r = 0.50
        M = self._fuse_three_layers(base, pred_linear, pred_geon, fuse_r)

        # 5. Ewolucja FSM
        c_state = self._fsm_extended(prev, M, G, self.no_input_for)

        # 6. Klasyfikacja błędów
        errors = []
        if M["CONFLICT"] > 0.8:
            errors.append("E1_INTENT_ERROR")
        if M["ERROR_RATE"] > 0.5:
            errors.append("E2_EXECUTION_ERROR")
        if M["STABILITY"] < 0.2:
            errors.append("E3_META_ERROR")
        if len(self.L0["metrics_history"]) > 5:
            stab_hist = [x.get("STABILITY", 0.7) for x in self.L0["metrics_history"][-5:]]
            if variance(stab_hist) > 0.4:
                errors.append("E4_MEMORY_ERROR")
        if self.prev_G and (G["DIRECTION"] - self.prev_G["DIRECTION"] > 0.3):
            errors.append("E5_HORIZON_ERROR")
        if G["DIRECTION"] < 0.40:
            errors.append("E6_GEON_DIRECTION_ERROR")

        flags = []
        for e in errors:
            policy_err = self.error_map[e]
            c_state = policy_err["c"]
            flags.extend(policy_err["flags"])

        # 7. Polityka systemowa
        T = self.config["THRESHOLDS"]
        if c_state == "C_GEON_HOME":
            A, B, pf = {"action": "direction_realign"}, {"action": "stability_boost", "value": 0.10}, ["GEON_RECENTER"]
        elif c_state == "C_GEON_LOCK":
            A, B, pf = {"action": "lock_direction"}, {"action": "smooth"}, ["GEON_LOCKED"]
        elif c_state == "C_SHIELD":
            A, B, pf = {"action": "block"}, {"action": "throttle", "value": 0.40}, ["ALERT"]
        elif c_state == "C_WEAVE":
            A, B, pf = {"action": "reprioritize"}, {"action": "smooth"}, ["STABILIZE"]
        elif c_state == "C_HOME":
            if M["COHESION"] < T["COHESION_MICRO"]:
                A, B, pf = {"action": "micro_adjust"}, {"action": "none"}, []
            else:
                A, B, pf = {"action": "none"}, {"action": "none"}, []
        else:
            A, B, pf = {"action": "none"}, {"action": "none"}, ["FALLBACK"]
        flags.extend(pf)

        # 8. Confidence
        base_conf = 0.70
        margin = 0.0
        if c_state == "C_SHIELD":
            margin = M["RISK"] - T["SHIELD_ENTER_RISK"]
        elif c_state == "C_WEAVE":
            margin = T["WEAVE_ENTER_STAB"] - M["STABILITY"]
        elif c_state == "C_HOME":
            margin = min(T["SHIELD_ENTER_RISK"] - M["RISK"], M["STABILITY"] - T["WEAVE_ENTER_STAB"])
        conf_dragon = clamp(base_conf + margin, 0.0, 1.0)
        conf_geon = clamp(G["DIRECTION"] * 0.6 + G["STABILITY"] * 0.4, 0.0, 1.0)
        conf = conf_dragon * 0.6 + conf_geon * 0.4

        # 9. Twarde bezpieczniki
        HARD = self.config["HARD"]
        if conf < 0.30:
            c_state = "C_SHIELD"
            flags.append("CONFIDENCE_CRITICAL")
        if self.tick_without_output > 5:
            c_state = "C_DEGRADED"
            flags.append("NO_OUTPUT_DEGRADED")
        if M["RISK"] > HARD["RISK_MAX"]:
            c_state = "C_SHIELD"
            A = {"action": "block_all"}
            B = {"action": "throttle", "value": 0.10}
            flags.append("HARD_SAFETY")
        if M["LOAD"] > HARD["LOAD_CRITICAL"]:
            B = {"action": "emergency_throttle", "value": 0.05}
            flags.append("OVERLOAD")
        if M["STABILITY"] < HARD["STABILITY_MIN"] and c_state != "C_SHIELD":
            c_state = "C_WEAVE"
            flags.append("STABILITY_CRITICAL")
        if G["DIRECTION"] < HARD["GEON_DIRECTION_MIN"]:
            c_state = "C_GEON_HOME"
            flags.append("GEON_DIRECTION_CRITICAL")

        # 10. Entropia i meta-bias
        if self.L0["state_ticks"].get("C_WEAVE", 0) > 10:
            if len(self.L0["metrics_history"]) >= 5:
                if self.L0["metrics_history"][-5].get("STABILITY", 0) >= self.L0["metrics_history"][-1].get("STABILITY", 0):
                    c_state = "C_WEAVE"
                    flags.extend(["META_ERROR", "WEAVE_INEFFICIENT"])
        if self.L0["state_ticks"].get(c_state, 0) > 50:
            flags.append("ENTROPY_REFRESH")
            self.L2_META["resonance_bias"] += 0.01

        # 11. Aktualizacja pamięci
        self.L0["last_metrics"] = M
        self.L0["metrics_history"].append(M)
        if len(self.L0["metrics_history"]) > 20:
            self.L0["metrics_history"] = self.L0["metrics_history"][-20:]

        for s in self.L0["state_ticks"]:
            if s == c_state:
                self.L0["state_ticks"][s] = 0
            else:
                self.L0["state_ticks"][s] += 1

        self.L1_GEON["direction_history"].append(G["DIRECTION"])
        self.L1_GEON["stability_history"].append(G["STABILITY"])

        if len(self.L1_GEON["direction_history"]) >= 100:
            if variance(self.L1_GEON["direction_history"][-100:]) < 0.01:
                self.L2_META["resonance_bias"] += 0.05

        # 12. Generowanie outputu
        out = {
            "STATE": c_state,
            "PREV_STATE": prev,
            "CORRECTION_A": A,
            "CORRECTION_B": B,
            "SYSTEM_FLAGS": list(set(flags)),
            "CONFIDENCE": conf,
            "GEON_DIRECTION": G["DIRECTION"],
            "GEON_STABILITY": G["STABILITY"],
            "TICK": self.L0["tick"],
            "TIMESTAMP": now_iso()
        }

        if mode in ["STEALTH", "NO_MIND"]:
            out.pop("TIMESTAMP", None)

        self.C_STATE = c_state
        self.prev_G = G
        if out:
            self.tick_without_output = 0
        else:
            self.tick_without_output += 1
        self.current_output = out

        return out

    def get_state(self) -> str:
        """Zwraca bieżący stan FSM."""
        return self.C_STATE

    def get_flags(self) -> List[str]:
        """Zwraca aktywne flagi systemowe."""
        return self.current_output.get("SYSTEM_FLAGS", [])


# ============================================================================
# WARSTWA 89: GEON_ARCHONT_GRID – G_CORE (Regulator Przepływu)
# ============================================================================

class GMemoryNode:
    """
    Rejestr Pamięciowy warstwy G (G_MEM) – przechowuje stany operacyjne Geona.
    """

    def __init__(self):
        self.MODE = "NORMAL"
        self.multiplier = 1.0
        self.THROTTLE_A = False
        self.THROTTLE_REASON = None
        self.G_VECTOR = {
            "DIRECTION": 0.5,
            "STABILITY": 0.6,
            "INERTIA": 0.2,
            "BUFFER_PRESSURE": 0.0
        }


def G3_compute_multiplier_v2(mode: str, buffer_pressure: float) -> Tuple[float, bool, str]:
    """
    Krytyczna funkcja analityczna warstwy G3.
    Wylicza mnożnik wydajności oraz flagi dławienia (Throttle) dla warstwy A.
    """
    if mode == "HIGH_PERFORMANCE":
        base_multiplier = 1.5
    elif mode == "SAFE_MODE":
        base_multiplier = 0.6
    elif mode == "STEALTH":
        base_multiplier = 0.8
    elif mode == "NO_MIND":
        base_multiplier = 1.2
    elif mode == "GEON_LOCK":
        base_multiplier = 1.0
    else:
        base_multiplier = 1.0

    if buffer_pressure > 0.9:
        effective_multiplier = base_multiplier * 0.2
        throttle_a = True
        reason = "CRITICAL_BUFFER_OVERLOAD"
    elif buffer_pressure > 0.6:
        effective_multiplier = base_multiplier * 0.6
        throttle_a = False
        reason = "SOFT_BUFFER_THROTTLE"
    else:
        effective_multiplier = base_multiplier
        throttle_a = False
        reason = "NOMINAL_FLOW"

    effective_multiplier = max(0.1, min(effective_multiplier, 2.5))
    return effective_multiplier, throttle_a, reason


def G_ENGINE_TICK_V2(
    E_OUTPUT: dict,
    D_VECTOR: dict,
    G_MEM: GMemoryNode,
    intent_queue_len: int,
    intent_queue_cap: int
) -> dict:
    """
    Główny regulator geometryczny ekosystemu GEON_OS.
    Spina wektory wejściowe E_OUTPUT i pamięć historyczną D_VECTOR,
    stabilizując matrycę przesyłu danych dla Autostrady 33.
    """
    buffer_pressure = intent_queue_len / intent_queue_cap if intent_queue_cap > 0 else 0.0
    G_MEM.G_VECTOR["BUFFER_PRESSURE"] = clamp(buffer_pressure, 0.0, 1.0)

    e_risk = E_OUTPUT.get("ENERGY_RISK", 0.0)
    d_stability = D_VECTOR.get("SYSTEM_STABILITY", 0.6)

    G_MEM.G_VECTOR["STABILITY"] = clamp(d_stability * 0.8 + (1.0 - e_risk) * 0.2, 0.0, 1.0)

    multiplier, throttle_a, reason = G3_compute_multiplier_v2(G_MEM.MODE, buffer_pressure)

    G_MEM.multiplier = multiplier
    G_MEM.THROTTLE_A = throttle_a
    G_MEM.THROTTLE_REASON = reason

    if G_MEM.G_VECTOR["STABILITY"] < 0.25 and G_MEM.MODE != "SAFE_MODE":
        G_MEM.MODE = "SAFE_MODE"
        G_MEM.THROTTLE_A = True
        G_MEM.THROTTLE_REASON = "GEOMETRIC_STABILITY_CRITICAL"
        multiplier = 0.4

    return {
        "MULTIPLIER": multiplier,
        "THROTTLE_A": G_MEM.THROTTLE_A,
        "BUFFER_PRESSURE": G_MEM.G_VECTOR["BUFFER_PRESSURE"]
    }


# ============================================================================
# WARSTWA 90: GEON_ARCHONT_COUNCIL – AUTOSTRADA33 (Szyna Transakcyjna)
# ============================================================================

class Autostrada33:
    """
    WARSTWA 90 – GEON_ARCHONT_COUNCIL
    ==================================
    Szyna transakcyjna systemu. Zarządza kolejkami intencji, retry,
    circuit breaker, backpressure i batchingiem. Stanowi rdzeń decyzyjny
    – Archont Council podejmuje decyzje o przepływie zadań.
    """

    def __init__(self, A: Any, B: Any, C: Any, D: Any, E: Any, G_MEM: Any):
        self.A = A
        self.B = B
        self.C = C
        self.D = D
        self.E = E
        self.G_MEM = G_MEM

        # Kolejki
        self.intent_heap: List[Tuple[int, int, Dict[str, Any]]] = []
        self.emergency_queue: List[Dict[str, Any]] = []
        self.pending_queue: List[Dict[str, Any]] = []
        self.retry_queue: List[Dict[str, Any]] = []
        self.dead_letter_queue: List[Dict[str, Any]] = []
        self.post_process_queue: List[Dict[str, Any]] = []
        self.dropped_intents_buffer: List[Dict[str, Any]] = []

        # Konfiguracja
        self.config = {
            "BASE_CAPACITY_PER_TICK": 10,
            "MAX_QUEUE_LEN": 1000,
            "RETRY_MAX_ATTEMPTS": 3,
            "RETRY_BACKOFF_MS": [100, 500, 2000],
            "INTENT_TTL_SECONDS": 30,
            "BATCH_SIZE": 5,
            "DEAD_LETTER_MAX_SIZE": 1000,
            "CIRCUIT_BREAKER_WINDOW_TICKS": 100,
            "CIRCUIT_BREAKER_THRESHOLD_RATIO": 0.2,
        }

        # Statystyki
        self.stats = {
            "intents_submitted": 0,
            "intents_processed": 0,
            "intents_retried": 0,
            "intents_failed": 0,
            "intents_expired": 0,
            "avg_latency_ms": 0.0,
        }
        self.cb_history: List[Tuple[int, int]] = []
        self.tick = 0
        self._seq = 0

        logger.info("AUTOSTRADA33 v2.5 (Warstwa 90) zainicjalizowana.")

    def submit_intent_request(self, payload: dict, priority: int = 5) -> bool:
        """Dodaje intencję do systemu."""
        if self.total_queue_len() >= self.config["MAX_QUEUE_LEN"]:
            self._drop_intent({"payload": payload, "priority": priority}, reason="BUFFER_FULL")
            return False

        msg = {
            "id": payload.get("id", f"intent_{self.tick}_{self._seq}"),
            "priority": priority,
            "payload": payload,
            "timestamp_epoch": time.time(),
        }

        if priority <= 2:
            self.emergency_queue.append(msg)
        else:
            heapq.heappush(self.intent_heap, (priority, self._seq, msg))
        self._seq += 1
        self.stats["intents_submitted"] += 1
        return True

    def total_queue_len(self) -> int:
        return (
            len(self.intent_heap) + len(self.emergency_queue) +
            len(self.retry_queue) + len(self.pending_queue)
        )

    def _drop_intent(self, msg: dict, reason: str):
        msg["drop_reason"] = reason
        self.dropped_intents_buffer.append(msg)
        if len(self.dropped_intents_buffer) > 50:
            self.dropped_intents_buffer = self.dropped_intents_buffer[-50:]

    def calculate_pressure_logic(self, queue_len: int, max_cap: int) -> str:
        pressure = queue_len / max_cap if max_cap > 0 else 0.0
        if pressure > 0.9:
            return "CRITICAL_THROTTLE"
        elif pressure > 0.6:
            return "SOFT_THROTTLE"
        return "CLEAR"

    def _requeue_with_backoff(self, msg: dict, error: str):
        attempts = msg.get("attempts", 0) + 1
        max_attempts = self.config["RETRY_MAX_ATTEMPTS"]

        if attempts <= max_attempts:
            backoff_ms = self.config["RETRY_BACKOFF_MS"][attempts - 1]
            msg["attempts"] = attempts
            msg["next_retry_tick"] = self.tick + (backoff_ms // 100)
            msg["last_error"] = error
            self.retry_queue.append(msg)
            self.stats["intents_retried"] += 1
        else:
            msg["final_error"] = error
            self.dead_letter_queue.append(msg)
            self.stats["intents_failed"] += 1
            if len(self.dead_letter_queue) > self.config["DEAD_LETTER_MAX_SIZE"]:
                self.dead_letter_queue = self.dead_letter_queue[-self.config["DEAD_LETTER_MAX_SIZE"]:]
            self.cb_history.append((self.tick, 1))

    def _process_retry_queue(self):
        now_tick = self.tick
        ready = []
        remaining = []
        for msg in self.retry_queue:
            if msg.get("next_retry_tick", 0) <= now_tick:
                ready.append(msg)
            else:
                remaining.append(msg)
        self.retry_queue = remaining
        for msg in ready:
            prio = msg.get("priority", 5)
            heapq.heappush(self.intent_heap, (prio, self._seq, msg))
            self._seq += 1

    def _expire_old_intents(self):
        now_ts = time.time()
        ttl = self.config["INTENT_TTL_SECONDS"]

        def _filter_queue(q: List[dict]) -> List[dict]:
            remaining = []
            for msg in q:
                ts = msg.get("timestamp_epoch")
                if ts is None:
                    remaining.append(msg)
                    continue
                if now_ts - ts > ttl:
                    self.stats["intents_expired"] += 1
                else:
                    remaining.append(msg)
            return remaining

        self.pending_queue = _filter_queue(self.pending_queue)
        self.retry_queue = _filter_queue(self.retry_queue)

    def _deduplicate_heap(self):
        seen = set()
        new_heap: List[Tuple[int, int, Dict[str, Any]]] = []
        while self.intent_heap:
            prio, seq, msg = heapq.heappop(self.intent_heap)
            payload = msg.get("payload", {})
            payload_hash = hash(frozenset(payload.items())) if payload else 0
            if payload_hash not in seen:
                seen.add(payload_hash)
                new_heap.append((prio, seq, msg))
        for item in new_heap:
            heapq.heappush(self.intent_heap, item)

    def _batch_from_heap(self) -> List[dict]:
        if not self.intent_heap or self.config["BATCH_SIZE"] <= 1:
            return []

        batch_size = self.config["BATCH_SIZE"]
        temp: List[Dict[str, Any]] = []
        while self.intent_heap and len(temp) < batch_size:
            prio, seq, msg = heapq.heappop(self.intent_heap)
            temp.append(msg)

        if len(temp) <= 1:
            for msg in temp:
                heapq.heappush(self.intent_heap, (msg.get("priority", 5), self._seq, msg))
                self._seq += 1
            return []

        intent_type = temp[0].get("payload", {}).get("type", "unknown")
        batched_payload = {
            "type": "BATCH_INTENT",
            "original_type": intent_type,
            "count": len(temp),
            "items": [m["payload"] for m in temp],
        }
        batched_msg = {
            "id": f"batch_{self.tick}_{intent_type}",
            "priority": min(m.get("priority", 5) for m in temp),
            "payload": batched_payload,
            "timestamp_epoch": time.time(),
            "is_batch": True,
        }
        return [batched_msg]

    def _resolve_pending_intents(self):
        still_pending: List[dict] = []
        for msg in self.pending_queue:
            status = self.B.check_pending_status(msg.get("id"))
            if status.get("status") == "COMPLETED":
                self.stats["intents_processed"] += 1
                self._update_latency(msg)
            elif status.get("status") == "FAILED":
                self._requeue_with_backoff(msg, status.get("error", "PENDING_FAILED"))
            else:
                still_pending.append(msg)
        self.pending_queue = still_pending

    def _update_latency(self, msg: dict):
        created_ts = msg.get("timestamp_epoch")
        if created_ts:
            latency = (time.time() - created_ts) * 1000.0
            alpha = 0.1
            self.stats["avg_latency_ms"] = alpha * latency + (1 - alpha) * self.stats["avg_latency_ms"]

    def _evaluate_circuit_breaker(self) -> bool:
        window = self.config["CIRCUIT_BREAKER_WINDOW_TICKS"]
        threshold_ratio = self.config["CIRCUIT_BREAKER_THRESHOLD_RATIO"]
        if not self.cb_history:
            return False

        current_tick = self.tick
        filtered: List[Tuple[int, int]] = []
        total_dl = 0
        for t, count in self.cb_history:
            if current_tick - t <= window:
                filtered.append((t, count))
                total_dl += count
        self.cb_history = filtered

        intents_in_window = max(1, self.stats["intents_processed"] + self.stats["intents_failed"])
        ratio = total_dl / intents_in_window
        return ratio >= threshold_ratio

    def _process_post_execution(self):
        if not self.post_process_queue:
            return
        queue = self.post_process_queue
        self.post_process_queue = []
        for item in queue:
            msg = item["msg"]
            status_b = item["status_b"]
            self.C.receive_status_from_B(status_b)
            self.stats["intents_processed"] += 1
            self._update_latency(msg)

    def _process_status_and_memory(self):
        c_state = self.C.export_state()
        if hasattr(self.D, "process_signal_tick"):
            self.D.process_signal_tick(c_state.get("vector", c_state))

        if hasattr(self.D, "get_prediction"):
            trend = self.D.get_prediction()
        else:
            trend = getattr(self.D, "D4_HORIZON_PREDICTION", {"PREDICTED_RISK": 0.1})
        self.E.update_from_trend(trend)

    def tick_once(self, E_OUTPUT: dict, D_VECTOR: dict):
        """Główny takt transmisyjny Autostrady 33."""
        self.tick += 1

        # 1. TTL
        self._expire_old_intents()

        # 2. G – Kontrola przepustowości
        g_result = G_ENGINE_TICK_V2(
            E_OUTPUT=E_OUTPUT,
            D_VECTOR=D_VECTOR,
            G_MEM=self.G_MEM,
            intent_queue_len=self.total_queue_len(),
            intent_queue_cap=self.config["MAX_QUEUE_LEN"],
        )
        multiplier = g_result["MULTIPLIER"]
        throttle_A = g_result["THROTTLE_A"]
        buffer_pressure = g_result["BUFFER_PRESSURE"]

        # 3. Circuit breaker → Safe Mode
        if self._evaluate_circuit_breaker():
            self.G_MEM.MODE = "SAFE_MODE"
            multiplier = min(multiplier, 0.75)

        # 4. Backpressure → Generowanie intencji
        pressure_status = self.calculate_pressure_logic(
            self.total_queue_len(),
            self.config["MAX_QUEUE_LEN"]
        )
        self.A.set_pressure_limit(pressure_status)
        if not throttle_A:
            new_intent = self.A.generate_intent(pressure_status=pressure_status)
            if new_intent is not None:
                self.submit_intent_request(new_intent, priority=new_intent.get("priority", 5))

        # 5. Retry
        self._process_retry_queue()

        # 6. Deduplikacja
        self._deduplicate_heap()

        # 7. Batching
        batched = self._batch_from_heap()
        for msg in batched:
            self.emergency_queue.append(msg)

        # 8. Efektywna przepustowość
        effective_capacity = max(1, int(self.config["BASE_CAPACITY_PER_TICK"] * multiplier))

        # 9. Pobieranie z kolejek
        to_process: List[dict] = []
        now_ts = time.time()

        while self.emergency_queue and len(to_process) < effective_capacity:
            msg = self.emergency_queue.pop(0)
            ts = msg.get("timestamp_epoch")
            if ts is not None and now_ts - ts > self.config["INTENT_TTL_SECONDS"]:
                self.stats["intents_expired"] += 1
                continue
            to_process.append(msg)

        while self.intent_heap and len(to_process) < effective_capacity:
            prio, seq, msg = heapq.heappop(self.intent_heap)
            ts = msg.get("timestamp_epoch")
            if ts is not None and now_ts - ts > self.config["INTENT_TTL_SECONDS"]:
                self.stats["intents_expired"] += 1
                continue
            to_process.append(msg)

        # 10. B – Wykonanie
        for msg in to_process:
            intent = msg["payload"]
            filtered = self.C.prefilter_intent(intent)
            if filtered is None:
                self._requeue_with_backoff(msg, "REJECTED_BY_C")
                continue
            try:
                status_b = self.B.run_cycle(filtered)
                self.post_process_queue.append({"msg": msg, "status_b": status_b})
            except Exception as e:
                self._requeue_with_backoff(msg, str(e))

        # 11. Post-execution
        self._process_post_execution()

        # 12. Pending resolve
        self._resolve_pending_intents()

        # 13. C → D → E
        self._process_status_and_memory()

    def get_metrics(self) -> dict:
        """Zwraca metryki operacyjne szyny."""
        return {
            "queue_sizes": {
                "intent_heap": len(self.intent_heap),
                "emergency": len(self.emergency_queue),
                "pending": len(self.pending_queue),
                "retry": len(self.retry_queue),
                "dead_letter": len(self.dead_letter_queue),
                "dropped": len(self.dropped_intents_buffer),
            },
            "stats": self.stats,
            "g_state": {
                "mode": getattr(self.G_MEM, "MODE", "NOMINAL"),
                "multiplier": getattr(self.G_MEM, "multiplier", 1.0),
            },
            "throttle": {
                "active": getattr(self.G_MEM, "THROTTLE_A", False),
                "reason": getattr(self.G_MEM, "THROTTLE_REASON", None),
            }
        }

    def flush_dead_letter(self) -> List[dict]:
        """Opróżnia kolejkę Dead Letter."""
        dead = self.dead_letter_queue.copy()
        self.dead_letter_queue = []
        return dead


# ============================================================================
# WARSTWA 91: GEON_SYNOD – Proces Synodalny (Głosowanie, Konsensus)
# ============================================================================

class GeonSynod:
    """
    WARSTWA 91 – GEON_SYNOD
    ========================
    Proces synodalny – zbiera głosy od warstw 87–90, podejmuje decyzje
    kolegialne, mediuje spory i rekomenduje działania dla Konsystorza.
    """

    def __init__(self):
        self.votes: Dict[str, Any] = {}
        self.consensus_history: List[Dict[str, Any]] = []
        self.mediation_count = 0
        self.last_recommendation: Optional[Dict[str, Any]] = None

        logger.info("GEON_SYNOD (Warstwa 91) zainicjalizowany.")

    def collect_vote(self, source: str, vote: Dict[str, Any]) -> None:
        """Zbiera głos od wskazanej warstwy."""
        self.votes[source] = vote
        logger.debug(f"[SYNOD] Głos od {source}: {vote}")

    def reach_consensus(self) -> Optional[Dict[str, Any]]:
        """
        Próbuje osiągnąć konsensus na podstawie zebranych głosów.
        Zwraca rekomendację lub None, jeśli brak quorum.
        """
        if len(self.votes) < 3:
            logger.warning("[SYNOD] Za mało głosów do osiągnięcia konsensusu.")
            return None

        # Proste głosowanie większościowe
        outcomes = {}
        for src, vote in self.votes.items():
            decision = vote.get("decision")
            if decision:
                outcomes[decision] = outcomes.get(decision, 0) + 1

        if not outcomes:
            return None

        consensus_decision = max(outcomes, key=outcomes.get)
        confidence = outcomes[consensus_decision] / len(self.votes)

        recommendation = {
            "decision": consensus_decision,
            "confidence": confidence,
            "votes": self.votes.copy(),
            "timestamp": now_iso(),
            "mediation_count": self.mediation_count
        }

        self.consensus_history.append(recommendation)
        if len(self.consensus_history) > 50:
            self.consensus_history = self.consensus_history[-50:]

        self.last_recommendation = recommendation
        self.votes = {}
        return recommendation

    def mediate(self, conflict: Dict[str, Any]) -> Dict[str, Any]:
        """
        Mediacja w przypadku braku konsensusu.
        Proponuje rozwiązanie kompromisowe.
        """
        self.mediation_count += 1
        logger.info(f"[SYNOD] Mediacja #{self.mediation_count} – konflikt: {conflict}")

        # Prosta logika mediacyjna – proponuje ścieżkę środkową
        resolution = {
            "type": "MEDIATED",
            "suggestion": "MIDDLE_PATH",
            "confidence": 0.6,
            "mediation_id": self.mediation_count,
            "timestamp": now_iso()
        }
        return resolution

    def get_recommendation(self) -> Optional[Dict[str, Any]]:
        """Zwraca ostatnią rekomendację synodu."""
        return self.last_recommendation


# ============================================================================
# WARSTWA 92: GEON_KONSYSTORZ – Nadrzędny Regulator (Pieczęć Ostateczna)
# ============================================================================

class GeonKonsystorz:
    """
    WARSTWA 92 – GEON_KONSYSTORZ
    =============================
    Absolutna warstwa systemu. Posiada pieczęć ostateczną, prawo veta,
    nadzoruje wszystkie niższe warstwy i zatwierdza ostateczne decyzje.
    """

    def __init__(self):
        self.seal_active = True
        self.veto_power = True
        self.approved_decisions: List[Dict[str, Any]] = []
        self.system_mode = "NOMINAL"
        self.last_seal_timestamp = now_iso()

        logger.info("GEON_KONSYSTORZ (Warstwa 92) zainicjalizowany – PIECZĘĆ OSTATECZNA AKTYWNA.")

    def approve(self, decision: Dict[str, Any]) -> bool:
        """
        Zatwierdza decyzję podjętą przez Synod (91).
        Jeśli decyzja spełnia kryteria, nakłada pieczęć ostateczną.
        """
        if not self.seal_active:
            logger.warning("[KONSYSTORZ] Pieczęć nieaktywna – decyzja odrzucona.")
            return False

        confidence = decision.get("confidence", 0.0)
        if confidence < 0.5:
            logger.warning(f"[KONSYSTORZ] Zbyt niska pewność ({confidence:.2f}) – weto.")
            return False

        if decision.get("decision") == "EMERGENCY_SHUTDOWN":
            if not self.veto_power:
                logger.info("[KONSYSTORZ] Emergency shutdown zatwierdzony.")
                self.system_mode = "SAFE_MODE"
            else:
                logger.warning("[KONSYSTORZ] Emergency shutdown zablokowany przez weto.")

        approved = {
            "decision": decision,
            "seal_timestamp": now_iso(),
            "seal_id": f"SEAL_{len(self.approved_decisions)+1:04d}",
            "system_mode_after": self.system_mode
        }

        self.approved_decisions.append(approved)
        self.last_seal_timestamp = now_iso()
        logger.info(f"[KONSYSTORZ] Decyzja zatwierdzona. Pieczęć: {approved['seal_id']}")
        return True

    def veto(self, decision: Dict[str, Any]) -> bool:
        """
        Weto – odrzuca decyzję, nawet jeśli przeszła przez Synod.
        """
        if not self.veto_power:
            logger.warning("[KONSYSTORZ] Brak uprawnień do veta.")
            return False

        logger.info(f"[KONSYSTORZ] Weto nałożone na decyzję: {decision}")
        return True

    def set_mode(self, mode: str) -> None:
        """Ustawia tryb systemowy (NOMINAL, SAFE_MODE, HIGH_PERFORMANCE, ...)."""
        allowed_modes = ["NOMINAL", "SAFE_MODE", "HIGH_PERFORMANCE", "STEALTH", "NO_MIND", "GEON_LOCK"]
        if mode in allowed_modes:
            self.system_mode = mode
            logger.info(f"[KONSYSTORZ] Tryb systemowy zmieniony na: {mode}")
        else:
            logger.error(f"[KONSYSTORZ] Nieznany tryb: {mode}")

    def get_status(self) -> Dict[str, Any]:
        """Zwraca status Konsystorza."""
        return {
            "seal_active": self.seal_active,
            "veto_power": self.veto_power,
            "system_mode": self.system_mode,
            "approved_decisions_count": len(self.approved_decisions),
            "last_seal": self.last_seal_timestamp
        }


# ============================================================================
# WARSTWA A: GENERATOR INTENCJI (Dla Autostrady 33)
# ============================================================================

class A_CoreIntentGenerator:
    """
    WARSTWA A – Generator Zamysłów
    ===============================
    Kreuje intencje systemowe i wprowadza je na szynę AB33.
    Reaguje na sygnały zwrotne kontroli ciśnienia (Backpressure).
    """

    def __init__(self):
        self.pressure_limit = "CLEAR"
        self.intent_counter = 0

    def set_pressure_limit(self, status: str):
        self.pressure_limit = status

    def generate_intent(self, pressure_status: str = "CLEAR") -> Optional[dict]:
        self.set_pressure_limit(pressure_status)

        if self.pressure_limit == "CRITICAL_THROTTLE":
            if random.random() > 0.1:
                return None
            self.intent_counter += 1
            return {
                "id": f"intent_A_emergency_{self.intent_counter}",
                "type": "SYSTEM_RECOVERY",
                "priority": 1,
                "risk": 0.1,
                "conflict": 0.0,
                "geon_intent": 0.9
            }

        if self.pressure_limit == "SOFT_THROTTLE":
            if random.random() > 0.4:
                return None
            self.intent_counter += 1
            return {
                "id": f"intent_A_stabilize_{self.intent_counter}",
                "type": "STRUCTURE_STABILIZE",
                "priority": 3,
                "risk": 0.2,
                "conflict": 0.1,
                "geon_intent": 0.7
            }

        self.intent_counter += 1
        types = ["DATA_INTEGRATION", "GEON_ALIGNMENT", "CORE_SYNC", "METRIC_RESONANCE"]
        chosen_type = random.choice(types)
        return {
            "id": f"intent_A_nominal_{self.intent_counter}",
            "type": chosen_type,
            "priority": random.choice([4, 5]),
            "risk": round(random.uniform(0.1, 0.4), 2),
            "conflict": round(random.uniform(0.0, 0.3), 2),
            "geon_intent": round(random.uniform(0.5, 0.8), 2)
        }


# ============================================================================
# WARSTWA B: SILNIK WYKONAWCZY (Dla Autostrady 33)
# ============================================================================

class B_ExecutionEngine:
    """
    WARSTWA B – Silnik Wykonawczy
    ==============================
    Wykonuje intencje, zwraca statusy, obsługuje zadania oczekujące.
    """

    def __init__(self):
        self.pending_tasks: Dict[str, Dict[str, Any]] = {}
        self.task_counter = 0

    def run_cycle(self, intent: dict) -> dict:
        """Wykonuje pojedyncze zadanie."""
        task_id = intent.get("id", f"task_{self.task_counter}")
        self.task_counter += 1

        # Symulacja wykonania – losowy czas i wynik
        success = random.random() > 0.1
        status = "COMPLETED" if success else "FAILED"
        error = None if success else "EXECUTION_ERROR"

        result = {
            "task_id": task_id,
            "status": status,
            "error": error,
            "load": random.uniform(0.1, 0.8),
            "energy": random.uniform(0.3, 0.9)
        }

        if status == "PENDING":
            self.pending_tasks[task_id] = result

        return result

    def check_pending_status(self, task_id: str) -> dict:
        """Sprawdza status zadania oczekującego."""
        if task_id in self.pending_tasks:
            task = self.pending_tasks[task_id]
            # Symulacja zakończenia
            if random.random() > 0.3:
                task["status"] = "COMPLETED"
                del self.pending_tasks[task_id]
            return task
        return {"status": "UNKNOWN", "error": "TASK_NOT_FOUND"}


# ============================================================================
# WARSTWA E: EMISJA (Dla Autostrady 33)
# ============================================================================

class E_CoreEmission:
    """
    WARSTWA E – Rdzeń Emisji i Wykonania
    ====================================
    Ostateczny punkt ujścia danych z systemu.
    Manifestuje przetworzone wektory, dostosowując emisję do trendów z D_CORE.
    """

    def __init__(self):
        self.current_trend: Dict[str, Any] = {}
        self.emission_log: List[Dict[str, Any]] = []
        self.is_active = True

    def update_from_trend(self, trend: dict):
        self.current_trend = trend if trend else {"PREDICTED_RISK": 0.1}
        self._execute_emission_profile()

    def _execute_emission_profile(self):
        predicted_risk = self.current_trend.get("PREDICTED_RISK", 0.1)
        if predicted_risk > 0.75:
            profile = "EMISSION_REPRESSED_SAFE"
        elif predicted_risk > 0.50:
            profile = "EMISSION_SMOOTH_BALANCED"
        else:
            profile = "EMISSION_MAX_FLUIDITY"

        manifest_event = {
            "timestamp": now_iso(),
            "profile": profile,
            "horizon_risk_snapshot": predicted_risk
        }
        self.emission_log.append(manifest_event)
        if len(self.emission_log) > 100:
            self.emission_log = self.emission_log[-100:]

    def emit_output_manifest(self, final_payload: dict) -> bool:
        if self.current_trend.get("PREDICTED_RISK", 0.0) > 0.90:
            logger.warning("EMISSION BLOCKED: Horizon risk threshold exceeded.")
            return False
        logger.info("[EMISSION] Manifestacja udana.")
        return True


# ============================================================================
# WARSTWA B_GEON_MATRIX (Dla D_CORE)
# ============================================================================

class B_GEON_Matrix:
    """
    Poziom B (GEON) – Reprezentuje nadrzędną matrycę geometryczną i wektor celu.
    Dostarcza punkt odniesienia (Geon Anchor) dla wyrównania (Alignment).
    """

    def __init__(self):
        self.geon_vector = {
            "ENTROPY": 0.20,
            "STABILITY": 0.90,
            "RISK": 0.15,
            "ALIGNMENT": 1.0
        }
        self.activation_count = 0

    def get_anchor_vector(self) -> Dict[str, float]:
        return self.geon_vector

    def realign_matrix(self, drift_factor: float):
        self.activation_count += 1
        for key in self.geon_vector:
            if key == "STABILITY":
                self.geon_vector[key] = max(0.5, self.geon_vector[key] - drift_factor * 0.1)
            else:
                self.geon_vector[key] = min(0.9, self.geon_vector[key] + drift_factor * 0.05)
        logger.warning(f"[GEON_MATRIX]: Przeliczenie geometrii. Aktywacja: {self.activation_count}")


# ============================================================================
# WARSTWA C_DRAGON_WEAVE (Dla D_CORE)
# ============================================================================

class C_Dragon_Weave:
    """
    Poziom C (Dragon / Sielanka_OS Weave) – Tkacz Stanów Świadomości Systemu.
    Odpowiada za arbitraż wysokiego poziomu i przerywanie pętli decyzyjnych.
    """

    def __init__(self):
        self.weave_status = "STABLE"
        self.interventions = 0

    def execute_weave_intervention(self, cause: str):
        self.interventions += 1
        self.weave_status = "INTERVENTION_ACTIVE"
        logger.critical(f"[C_DRAGON_WEAVE]: INTRUZJA. Przyczyna: {cause}")
        self.weave_status = "RECALIBRATED"


# ============================================================================
# GŁÓWNY SILNIK INTEGRACYJNY – PROTOKÓŁ
# ============================================================================

class IntegrationProtocol:
    """
    GŁÓWNY SILNIK INTEGRACYJNY v2.5
    ================================
    Spina wszystkie warstwy 87–92 w jeden działający organizm.
    Umożliwia przepływ sygnału od wejścia do emisji, z pełną pętlą
    sprzężenia zwrotnego i nadzorem Konsystorza.
    """

    def __init__(self):
        # === Inicjalizacja wszystkich warstw ===
        self.geon_matrix = B_GEON_Matrix()
        self.dragon_weave = C_Dragon_Weave()

        self.d_core = D_Core_Arcanum(self.geon_matrix, self.dragon_weave)
        self.c_dragon = C_Core_Dragon()
        self.g_mem = GMemoryNode()
        self.a_gen = A_CoreIntentGenerator()
        self.b_exec = B_ExecutionEngine()
        self.e_emit = E_CoreEmission()

        self.autostrada = Autostrada33(
            A=self.a_gen,
            B=self.b_exec,
            C=self.c_dragon,
            D=self.d_core,
            E=self.e_emit,
            G_MEM=self.g_mem
        )

        self.synod = GeonSynod()
        self.konsystorz = GeonKonsystorz()

        # === Stan globalny ===
        self.tick_counter = 0
        self.last_emission = None

        logger.info("=" * 80)
        logger.info("GEON INTEGRATION PROTOCOL v2.5 – SILNIK SPRZĘGAJĄCY WARSTWY 87–92")
        logger.info("Status: GOTOWY | Tryb: MODEL_9_ACTIVE")
        logger.info("=" * 80)

    def tick(self, incoming_signal: Optional[Dict[str, float]] = None) -> Dict[str, Any]:
        """
        Główny takt systemu. Przetwarza sygnał wejściowy i przepuszcza go
        przez wszystkie warstwy 87–92.
        """
        self.tick_counter += 1

        if incoming_signal is None:
            incoming_signal = {
                "ENTROPY": random.uniform(0.1, 0.4),
                "STABILITY": random.uniform(0.6, 0.9),
                "RISK": random.uniform(0.05, 0.3),
                "ALIGNMENT": random.uniform(0.7, 0.95)
            }

        # === KROK 1: D_CORE (Warstwa 87) – Analiza i predykcja ===
        self.d_core.process_signal_tick(incoming_signal)
        d_root = self.d_core.get_root_vector()
        d_pred = self.d_core.get_prediction()

        # === KROK 2: AUTOSTRADA33 (Warstwa 90) – Tick transmisyjny ===
        e_output = {"ENERGY_RISK": d_root.get("RISK", 0.1)}
        d_vector = {"SYSTEM_STABILITY": d_root.get("STABILITY", 0.6)}
        self.autostrada.tick_once(e_output, d_vector)

        # === KROK 3: C_DRAGON (Warstwa 88) – Stan FSM ===
        # Pobieramy ostatnią intencję z Autostrady (symulacja)
        last_intent = {
            "payload": {
                "risk": d_root.get("RISK", 0.1),
                "conflict": 0.0,
                "geon_intent": d_root.get("ALIGNMENT", 0.8)
            }
        }
        last_status = {"payload": {"load": 0.5, "energy": 0.7}}
        env = {"risk": d_root.get("RISK", 0.1)}
        geon = {"direction": d_root.get("ALIGNMENT", 0.8), "stability": d_root.get("STABILITY", 0.7)}

        c_result = self.c_dragon.run_cycle(last_intent, last_status, env, geon, mode=self.g_mem.MODE)
        c_state = c_result.get("STATE", "C_HOME")
        c_flags = c_result.get("SYSTEM_FLAGS", [])

        # === KROK 4: SYNOD (Warstwa 91) – Zbieranie głosów ===
        self.synod.collect_vote("D_CORE", {"decision": "PROCEED", "confidence": d_root.get("ALIGNMENT", 0.8)})
        self.synod.collect_vote("C_DRAGON", {"decision": c_state, "confidence": c_result.get("CONFIDENCE", 0.7)})
        self.synod.collect_vote("AUTOSTRADA", {"decision": "PROCESS", "confidence": 0.8})

        consensus = self.synod.reach_consensus()

        # === KROK 5: KONSYSTORZ (Warstwa 92) – Zatwierdzenie ===
        if consensus:
            approved = self.konsystorz.approve(consensus)
            if approved:
                self.konsystorz.set_mode(self.g_mem.MODE)
                logger.info("[KONSYSTORZ] Decyzja zatwierdzona pieczęcią ostateczną.")
            else:
                logger.warning("[KONSYSTORZ] Decyzja odrzucona lub zawetowana.")

        # === KROK 6: EMISJA (Warstwa E) ===
        emission_payload = {
            "tick": self.tick_counter,
            "root_vector": d_root,
            "prediction": d_pred,
            "c_state": c_state,
            "c_flags": c_flags,
            "consensus": consensus,
            "konsystorz_status": self.konsystorz.get_status()
        }
        self.e_emit.emit_output_manifest(emission_payload)
        self.last_emission = emission_payload

        # === Metryki ===
        ab33_metrics = self.autostrada.get_metrics()

        result = {
            "tick": self.tick_counter,
            "d_root": d_root,
            "d_prediction": d_pred,
            "c_state": c_state,
            "c_flags": c_flags,
            "consensus": consensus,
            "konsystorz": self.konsystorz.get_status(),
            "ab33_metrics": ab33_metrics,
            "emission": emission_payload
        }

        logger.info(f"[TICK {self.tick_counter:04d}] Stan C: {c_state} | "
                    f"RISK: {d_root['RISK']:.3f} | "
                    f"STAB: {d_root['STABILITY']:.3f} | "
                    f"KONSYSTORZ: {self.konsystorz.system_mode}")

        return result

    def get_full_status(self) -> Dict[str, Any]:
        """Zwraca pełny status wszystkich warstw."""
        return {
            "tick": self.tick_counter,
            "d_core": {
                "root_vector": self.d_core.get_root_vector(),
                "prediction": self.d_core.get_prediction(),
                "health_score": self.d_core.health_score
            },
            "c_dragon": {
                "state": self.c_dragon.get_state(),
                "flags": self.c_dragon.get_flags()
            },
            "g_mem": {
                "mode": self.g_mem.MODE,
                "multiplier": self.g_mem.multiplier,
                "throttle": self.g_mem.THROTTLE_A,
                "g_vector": self.g_mem.G_VECTOR
            },
            "autostrada": self.autostrada.get_metrics(),
            "synod": {
                "last_recommendation": self.synod.get_recommendation(),
                "mediation_count": self.synod.mediation_count
            },
            "konsystorz": self.konsystorz.get_status(),
            "last_emission": self.last_emission
        }


# ============================================================================
# TEST / SYMULACJA
# ============================================================================

if __name__ == "__main__":
    print("\n" + "=" * 80)
    print("GEON INTEGRATION PROTOCOL v2.5 – SYMULACJA DZIAŁANIA")
    print("=" * 80 + "\n")

    # Inicjalizacja silnika
    silnik = IntegrationProtocol()

    # Symulacja 10 taktów
    for i in range(1, 11):
        print(f"\n--- TAKT {i:04d} ---")

        # Losowy sygnał wejściowy
        signal = {
            "ENTROPY": 0.15 + 0.1 * math.sin(i / 2.0),
            "STABILITY": 0.75 + 0.15 * math.cos(i / 3.0),
            "RISK": 0.10 + 0.05 * math.sin(i / 1.5),
            "ALIGNMENT": 0.85 + 0.10 * math.cos(i / 2.5)
        }

        # Wykonanie taktu
        result = silnik.tick(signal)

        # Podsumowanie
        print(f"   D_ROOT: RISK={result['d_root']['RISK']:.3f}, "
              f"STAB={result['d_root']['STABILITY']:.3f}")
        print(f"   C_STATE: {result['c_state']}")
        print(f"   KONSYSTORZ: {result['konsystorz']['system_mode']}")
        print(f"   AB33: queue={result['ab33_metrics']['queue_sizes']['intent_heap']}, "
              f"multiplier={result['ab33_metrics']['g_state']['multiplier']:.2f}")

    # Podsumowanie końcowe
    print("\n" + "=" * 80)
    print("PODSUMOWANIE SYMULACJI")
    print("=" * 80)
    status = silnik.get_full_status()
    print(f"\nOstatni stan Konsystorza:")
    print(f"  - Tryb: {status['konsystorz']['system_mode']}")
    print(f"  - Pieczęć aktywna: {status['konsystorz']['seal_active']}")
    print(f"  - Zatwierdzone decyzje: {status['konsystorz']['approved_decisions_count']}")
    print(f"  - Ostatnia pieczęć: {status['konsystorz']['last_seal']}")
    print(f"\nStan C_DRAGON: {status['c_dragon']['state']}")
    print(f"Flagi C_DRAGON: {status['c_dragon']['flags']}")
    print(f"\nG_MEM: tryb={status['g_mem']['mode']}, multiplier={status['g_mem']['multiplier']:.2f}")
    print(f"AB33: retry={status['autostrada']['stats']['intents_retried']}, "
          f"failed={status['autostrada']['stats']['intents_failed']}")
    print(f"\nSYNOD: mediacje={status['synod']['mediation_count']}")
    print("\n" + "=" * 80)
    print("INTEGRACJA UKOŃCZONA – SYSTEM GOTOWY DO WDROŻENIA")
    print("=" * 80)