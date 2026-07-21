#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
================================================================================
🐉 GEON_ORGANISM_ABC_33 — FINALNA WERSJA v3.1 ULTIMA
================================================================================
Status: PRODUCTION_READY | ARCHITECTURE_LOCKED | FRACTAL_PERFECTED | ULTIMA
Wersja: v3.1 FINAL (Pełna integracja z GEON_SYSTEM)
Data: 2026-07-21
Architekt: Adrian Samuel Bogusławski (GEON/HEILONG/DRAGON)

ARCHITEKTURA:
  - Triada 33 Płatków / 3 Bramy: Alfa (11), Beta (22), Gamma (33)
  - Filtrowanie i sanityzacja kwantowej luki szumu (7 → 8)
  - Przestrzeń Cyklu Węzłowego: [0, 1, 2, 3, 4, 5, 6, 8, 9]
  - Trzy Rdzenie Rezonansowe: A (Lotos/Wektor), B (Wir/Exec), C (Meta-Shield)
  - Magistrala Autostrada 33 (Event Bus / Interfejs Modułów Zewnętrznych)
  - Mikro-algorytm: 4→1→2→5→6→6→5→8→1
  - EventBus: System zdarzeń Pub/Sub
  - Thresholds: Progi adaptacyjne (noise, load, energy)
  - Decoy Logs: Tryb stealth_flow
  - Correction_A: Feedback do A
  - Vortex Resonance Sync: Synchronizacja wiru

VIBE: 1-6-8-3-3. ∞. KLAWO JAK CHOLERA
================================================================================
"""

import sys
import math
import logging
import copy
from typing import Dict, Any, List, Optional, Tuple, Callable
from datetime import datetime
from enum import Enum
from dataclasses import dataclass, field

# =============================================================================
# 0. KONFIGURACJA SYSTEMU LOGOWANIA
# =============================================================================

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] [%(levelname)s] [GEON_33] :: %(message)s",
    datefmt="%H:%M:%S"
)
logger = logging.getLogger("GEON_ORGANISM_33")

def LOG_INFO(msg: str) -> None:
    logger.info(msg)

def LOG_WARN(msg: str) -> None:
    logger.warning(msg)

def LOG_ERR(msg: str) -> None:
    logger.error(msg)

def LOG_DEBUG(msg: str) -> None:
    logger.debug(msg)


# =============================================================================
# 1. STAŁE ARCHITEKTONICZNE I ALFABET CYKLICZNY
# =============================================================================

VERSION = "GEON_ORGANISM_ABC_33_v3.1_FINAL"
FRACTAL_SIGNATURE = "[GEON::ORGANISM::33::ULTIMA]"

VALID_DIGITS_33: List[int] = [0, 1, 2, 3, 4, 5, 6, 8, 9]
TRIAD_CYCLE_33: List[int] = [0, 1, 2, 3, 4, 5, 6, 8, 9, 0]
MICRO_ALGORITHM_33: List[int] = [4, 1, 2, 5, 6, 6, 5, 8, 1]

STEP_NAMES_33: Dict[int, str] = {
    0: "WĘZEŁ ZERO / ŹRÓDŁO (Zero Point)",
    1: "INICJACJA / WEKTOR INTENCJI (Initiation)",
    2: "PERCEPCJA / ANALIZA PROCESU (Perception)",
    3: "SYNCHRONIZACJA TRIADY / REZONANS 33 (Triad Sync)",
    4: "KOREKTA / BALANS STRUKTURY (Correction)",
    5: "TRANSFORMACJA / SUBSTANCJA (Transformation)",
    6: "STABILIZACJA / WIR SILNIKA (Vortex)",
    8: "RELACJA / SYNCHRONICZNOŚĆ (Relation)",
    9: "DOMKNIĘCIE / PEŁNIA FRAKTALNA (Completion)"
}


class GateStatus(Enum):
    OPEN = "open"
    CLOSED = "closed"
    BLOCKED = "blocked"


class Mode(Enum):
    NORMAL = "normal"
    SAFE = "safe_mode"
    STEALTH = "stealth_flow"
    HIGH_PERFORMANCE = "high_performance"


class AlertLevel(Enum):
    INFO = "info"
    WARNING = "warning"
    CRITICAL = "critical"


# =============================================================================
# 2. FILTRY CZYSZCZĄCE I SANITYZACJA WARSTWY 33
# =============================================================================

def sanitize_value_33(val: float) -> float:
    """
    Sanityzacja sygnału w Autostradzie 33.
    Przepuszcza cyfrę 3 (Rezonans Triady), zamienia cyfrę 7 (Luka Szumu) na 8.
    """
    val_str = f"{float(val):.8f}"
    if '7' in val_str:
        val_str = val_str.replace('7', '8')
    return float(val_str)


def sanitize_string_33(text: str) -> str:
    """Sanityzacja stringa — zamienia 7 na 8."""
    return text.replace('7', '8')


def compute_geon_hash(data: str) -> int:
    """Oblicza sumę kontrolną wartości wektorowej w rezonansie 33."""
    acc = 0
    for char in data:
        acc = (acc * 33 + ord(char)) % 999999
    return acc


# =============================================================================
# 3. EVENT BUS (SYSTEM KOMUNIKACJI)
# =============================================================================

class EventBus33:
    """System zdarzeń dla komunikacji wewnętrznej."""
    
    def __init__(self, max_history: int = 100):
        self._subscribers: Dict[str, List[Callable[[Dict[str, Any]], None]]] = {}
        self._history: List[Dict[str, Any]] = []
        self._max_history = max_history
        LOG_INFO("📡 EventBus33 aktywowany")
    
    def subscribe(self, event_type: str, callback: Callable[[Dict[str, Any]], None]) -> None:
        """Subskrybuje zdarzenie."""
        if event_type not in self._subscribers:
            self._subscribers[event_type] = []
        self._subscribers[event_type].append(callback)
    
    def unsubscribe(self, event_type: str, callback: Callable[[Dict[str, Any]], None]) -> None:
        """Anuluje subskrypcję."""
        if event_type in self._subscribers:
            self._subscribers[event_type] = [cb for cb in self._subscribers[event_type] if cb != callback]
    
    def publish(self, event_type: str, payload: Dict[str, Any]) -> None:
        """Emituje zdarzenie."""
        event = {
            "timestamp": datetime.now().isoformat(),
            "type": event_type,
            "payload": payload
        }
        self._history.append(event)
        if len(self._history) > self._max_history:
            self._history = self._history[-self._max_history:]
        
        if event_type in self._subscribers:
            for callback in self._subscribers[event_type]:
                try:
                    callback(payload)
                except Exception as e:
                    LOG_ERR(f"Błąd handlera dla {event_type}: {e}")
    
    def get_history(self, limit: int = 20) -> List[Dict[str, Any]]:
        return self._history[-limit:]
    
    def clear(self) -> None:
        self._history = []


# =============================================================================
# 4. WEKTOR SYGNAŁOWY I OBIEKT INTENCJI
# =============================================================================

@dataclass
class GeonSignal:
    """Jednostka informacji (Wektor) przechodząca przez Rdzenie A-B-C."""
    intent_id: str
    payload: Dict[str, Any]
    raw_value: float = 1.0
    priority: int = 5
    sanitized_value: float = field(init=False)
    current_step: int = field(init=False, default=0)
    timestamp: str = field(init=False, default_factory=lambda: datetime.now().isoformat())
    history: List[str] = field(init=False, default_factory=list)
    vortex_detected: bool = field(init=False, default=False)
    
    def __post_init__(self):
        self.sanitized_value = sanitize_value_33(self.raw_value)
        self.priority = max(0, min(10, self.priority))
        # Sanityzacja payload
        for k, v in self.payload.items():
            if isinstance(v, (int, float)):
                self.payload[k] = sanitize_value_33(v)
            elif isinstance(v, str):
                self.payload[k] = sanitize_string_33(v)
    
    def log_step(self, step_id: int, message: str) -> None:
        self.current_step = step_id
        entry = f"Step [{step_id} - {STEP_NAMES_33.get(step_id, 'UNKNOWN')}]: {message}"
        self.history.append(entry)
        LOG_DEBUG(f"[{self.intent_id}] -> {entry}")
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.intent_id,
            "priority": self.priority,
            "payload": self.payload,
            "raw_value": self.raw_value,
            "sanitized_value": self.sanitized_value,
            "current_step": self.current_step,
            "step_name": STEP_NAMES_33.get(self.current_step, "UNKNOWN"),
            "timestamp": self.timestamp,
            "history": self.history[-10:]
        }


# =============================================================================
# 5. RDZENIE REZONANSU A-B-C
# =============================================================================

class CoreA_LandingPad:
    """Rdzeń A (Alfa): LandingPad, Ingestia Intencji i Wstępny Wektor."""
    
    def __init__(self, event_bus: Optional[EventBus33] = None):
        self.event_bus = event_bus or EventBus33()
        self.processed_count = 0
        LOG_INFO("🌀 Rdzeń A (Alfa) — LandingPad aktywowany")
    
    def process(self, signal: GeonSignal) -> bool:
        self.processed_count += 1
        signal.log_step(1, f"Inicjalizacja wektora intencji w Rdzeniu A (ID: {signal.intent_id})")
        
        # Sprawdzenie czystości wartości
        if signal.sanitized_value != signal.raw_value:
            signal.log_step(2, f"Wykryto szum '7'. Korekta: {signal.raw_value:.6f} → {signal.sanitized_value:.6f}")
        else:
            signal.log_step(2, "Sygnał wejściowy czysty.")
        
        # Emit przez EventBus
        self.event_bus.publish("CORE_A_PROCESS", {"signal_id": signal.intent_id, "status": "processed"})
        
        return True
    
    def get_stats(self) -> Dict[str, Any]:
        return {"processed": self.processed_count}


class CoreB_VortexEngine:
    """Rdzeń B (Beta): Wir Silnika Exec, Przetwarzanie i Wykonanie Obliczeń."""
    
    def __init__(self, event_bus: Optional[EventBus33] = None):
        self.event_bus = event_bus or EventBus33()
        self.processed_count = 0
        self.thresholds = {
            "noise_threshold": 0.06,
            "load_threshold": 10,
            "micro_threshold": 8,
            "energy_reserve": 30
        }
        self.memory: List[Dict[str, Any]] = []
        self.vortex_active = False
        LOG_INFO("🌀 Rdzeń B (Beta) — Vortex Engine aktywowany")
    
    def process(self, signal: GeonSignal) -> bool:
        self.processed_count += 1
        signal.log_step(3, "Wejście w Rezonans Triady (Węzeł 33). Synchronizacja parametrów.")
        signal.log_step(4, "Korekta i bilansowanie ładunku procesowego.")
        
        # Sprawdzenie progów
        if self.thresholds["energy_reserve"] < 30:
            signal.log_step(3, "⚠️ Niska energia — aktywacja trybu vortex_stabilization")
            self.vortex_active = True
            signal.vortex_detected = True
        
        # Wykonanie przekształcenia matematycznego
        calc_factor = math.sin(signal.sanitized_value * math.pi / 33.0)
        signal.payload["_geon_exec_factor"] = round(calc_factor, 6)
        
        signal.log_step(5, f"Transformacja substancji: factor={calc_factor:.6f}")
        signal.log_step(6, "Stabilizacja wiru silnika (Vortex Lock)")
        
        # Mikro-algorytm jeśli warunki spełnione
        if self.thresholds["load_threshold"] >= self.thresholds["micro_threshold"]:
            self._run_micro_algorithm(signal)
        
        # Emit przez EventBus
        self.event_bus.publish("CORE_B_PROCESS", {
            "signal_id": signal.intent_id, 
            "status": "processed",
            "factor": calc_factor
        })
        
        return True
    
    def _run_micro_algorithm(self, signal: GeonSignal) -> None:
        """Mikro-algorytm 4→1→2→5→6→6→5→8→1."""
        signal.log_step(4, "🔄 Uruchomienie mikro-algorytmu")
        for step in MICRO_ALGORITHM_33:
            signal.log_step(step, f"Mikro-krok: {STEP_NAMES_33.get(step, 'UNKNOWN')}")
            if step == 6:
                # Podwójne 6 → vortex
                signal.vortex_detected = True
                signal.log_step(6, "🌀 Vortex detected (6→6)")
    
    def adapt_thresholds(self) -> None:
        """Adaptacja progów na podstawie pamięci."""
        if len(self.memory) < 5:
            return
        recent = self.memory[-5:]
        error_ratio = sum(1 for m in recent if "error" in str(m.get("result", ""))) / 5
        
        if error_ratio > 0.2:
            self.thresholds["noise_threshold"] = max(0.03, self.thresholds["noise_threshold"] - 0.01)
            self.thresholds["load_threshold"] = max(3, self.thresholds["load_threshold"] - 1)
        else:
            self.thresholds["noise_threshold"] = min(0.06, self.thresholds["noise_threshold"] + 0.005)
            self.thresholds["load_threshold"] = min(10, self.thresholds["load_threshold"] + 1)
        
        LOG_DEBUG(f"Progi zadaptowane: {self.thresholds}")
    
    def get_thresholds(self) -> Dict[str, Any]:
        return self.thresholds.copy()
    
    def get_stats(self) -> Dict[str, Any]:
        return {
            "processed": self.processed_count,
            "thresholds": self.thresholds,
            "vortex_active": self.vortex_active,
            "memory_depth": len(self.memory)
        }


class CoreC_MetaShield:
    """Rdzeń C (Gamma): Meta-Shield, Synchro-Dominanta, Walidacja i Domknięcie."""
    
    def __init__(self, event_bus: Optional[EventBus33] = None):
        self.event_bus = event_bus or EventBus33()
        self.processed_count = 0
        self.corrections_sent = 0
        self.decoy_logs: List[Dict[str, Any]] = []
        self.gates = {
            "GATE_11_ALFA": GateStatus.OPEN,
            "GATE_22_BETA": GateStatus.OPEN,
            "GATE_33_GAMMA": GateStatus.OPEN
        }
        LOG_INFO("🌀 Rdzeń C (Gamma) — Meta-Shield aktywowany")
    
    def process(self, signal: GeonSignal) -> bool:
        self.processed_count += 1
        signal.log_step(8, "Sprawdzenie synchroniczności relacyjnej w Rdzeniu C.")
        
        # Ostateczna weryfikacja czystości danych
        has_invalid_7 = any(
            '7' in str(v) for v in signal.payload.values() 
            if isinstance(v, (int, float, str))
        )
        
        if has_invalid_7:
            signal.log_step(8, "❌ Wykryto naruszenie fali 7 w Rdzeniu C!")
            self.event_bus.publish("SIGNAL_REJECTED", {"signal_id": signal.intent_id})
            return False
        
        signal.log_step(9, "✅ Domknięcie fraktalne (Pełnia). Sygnał zweryfikowany.")
        
        # Emit przez EventBus
        self.event_bus.publish("CORE_C_PROCESS", {
            "signal_id": signal.intent_id,
            "status": "verified",
            "hash": compute_geon_hash(signal.intent_id + str(signal.timestamp))
        })
        
        return True
    
    def send_correction_to_A(self, reason: str) -> Dict[str, Any]:
        """Wysyła korektę do A."""
        self.corrections_sent += 1
        correction = {
            "action": "throttle" if reason in ["load", "energy"] else "pause",
            "reason": reason,
            "new_priority_base": 3 if reason == "load" else 2,
            "priority_override": None,
            "timestamp": datetime.now().isoformat()
        }
        self.event_bus.publish("CORRECTION_TO_A", correction)
        LOG_INFO(f"📤 CORRECTION_A → A: {reason}")
        return correction
    
    def generate_decoy_log(self, message: str) -> None:
        """Generuje decoy log dla trybu stealth_flow."""
        entry = {
            "timestamp": datetime.now().isoformat(),
            "message": message,
            "type": "DECOY"
        }
        self.decoy_logs.append(entry)
        LOG_DEBUG(f"🕵️ Decoy log: {message[:50]}...")
    
    def set_gate(self, gate: str, status: GateStatus) -> None:
        """Ustawia status bramy."""
        if gate in self.gates:
            self.gates[gate] = status
            LOG_INFO(f"Brama {gate} → {status.value}")
    
    def get_gate_status(self) -> Dict[str, str]:
        return {k: v.value for k, v in self.gates.items()}
    
    def get_stats(self) -> Dict[str, Any]:
        return {
            "processed": self.processed_count,
            "corrections_sent": self.corrections_sent,
            "decoy_logs_count": len(self.decoy_logs),
            "gates": self.get_gate_status()
        }


# =============================================================================
# 6. MAGISTRALA AUTOSTRADA 33 (EVENT BUS & MODULE ROUTER)
# =============================================================================

class Autostrada33:
    """
    Autostrada 33 — Wysokowydajna Magistrala Systemowa.
    Łączy Organizm A-B-C z zewnętrznymi modułami użytkownika.
    """
    
    def __init__(self):
        self.petals = 33
        self.event_bus = EventBus33()
        
        # Rdzenie
        self.core_a = CoreA_LandingPad(self.event_bus)
        self.core_b = CoreB_VortexEngine(self.event_bus)
        self.core_c = CoreC_MetaShield(self.event_bus)
        
        # Rejestr modułów
        self.registered_modules: Dict[str, Any] = {}
        
        # Statystyki
        self.stats = {
            "signals_processed": 0,
            "signals_rejected": 0,
            "modules_connected": 0
        }
        
        LOG_INFO("🛣️ Autostrada 33 gotowa. Węzły 11, 22, 33 aktywne.")
        LOG_INFO(f"   Sygnatura: {FRACTAL_SIGNATURE}")
        LOG_INFO(f"   Wersja: {VERSION}")
    
    # =========================================================================
    # REJESTRACJA MODUŁÓW
    # =========================================================================
    
    def register_module(self, name: str, module_instance: Any) -> None:
        """Podłącza zewnętrzny moduł do Autostrady 33."""
        self.registered_modules[name] = module_instance
        self.stats["modules_connected"] += 1
        LOG_INFO(f"🔗 Podpięto zewnętrzny moduł: [{name}]")
        self.event_bus.publish("MODULE_REGISTERED", {"name": name})
    
    def unregister_module(self, name: str) -> None:
        """Odłącza moduł."""
        if name in self.registered_modules:
            del self.registered_modules[name]
            self.stats["modules_connected"] -= 1
            LOG_INFO(f"🔗 Odłączono moduł: [{name}]")
    
    def get_modules(self) -> List[str]:
        """Zwraca listę zarejestrowanych modułów."""
        return list(self.registered_modules.keys())
    
    # =========================================================================
    # PIPELINE WYKONAWCZY
    # =========================================================================
    
    def execute_pipeline(
        self, 
        intent_id: str, 
        payload: Dict[str, Any], 
        raw_value: float = 1.0,
        priority: int = 5
    ) -> Tuple[bool, GeonSignal]:
        """
        Pełny cykl przejazdu sygnału przez Rdzenie A-B-C na Autostradzie 33.
        """
        LOG_INFO(f"🚀 Pipeline start: {intent_id}")
        
        signal = GeonSignal(intent_id, payload, raw_value, priority)
        signal.log_step(0, "Wejście w Węzeł Zero / Autostrada 33.")
        
        # Przejście przez Rdzeń A
        if not self.core_a.process(signal):
            self.stats["signals_rejected"] += 1
            LOG_WARN(f"❌ Signal rejected at Core A: {intent_id}")
            return False, signal
        
        # Przejście przez Rdzeń B
        if not self.core_b.process(signal):
            self.stats["signals_rejected"] += 1
            LOG_WARN(f"❌ Signal rejected at Core B: {intent_id}")
            return False, signal
        
        # Przejście przez Rdzeń C
        if not self.core_c.process(signal):
            self.stats["signals_rejected"] += 1
            LOG_WARN(f"❌ Signal rejected at Core C: {intent_id}")
            return False, signal
        
        self.stats["signals_processed"] += 1
        LOG_INFO(f"✅ Signal processed: {intent_id}")
        
        # Emit przez EventBus
        self.event_bus.publish("PIPELINE_COMPLETE", {
            "signal_id": intent_id,
            "steps": len(signal.history)
        })
        
        return True, signal
    
    # =========================================================================
    # ROUTING DO MODUŁÓW
    # =========================================================================
    
    def route_to_module(self, target_module: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """
        Transmituje dane bezpośrednio do wybranego modułu przez Bramę 33.
        """
        LOG_INFO(f"🔄 Routing do modułu: [{target_module}]")
        
        if target_module not in self.registered_modules:
            LOG_ERR(f"Moduł [{target_module}] nie jest zarejestrowany!")
            return {"status": "ERROR", "message": f"Module {target_module} not found"}
        
        # Sanityzacja na Autostradzie 33
        clean_payload = {}
        for k, v in payload.items():
            if isinstance(v, (int, float)):
                clean_payload[k] = sanitize_value_33(v)
            elif isinstance(v, str):
                clean_payload[k] = sanitize_string_33(v)
            elif isinstance(v, dict):
                clean_payload[k] = self._sanitize_dict(v)
            else:
                clean_payload[k] = v
        
        mod = self.registered_modules[target_module]
        
        # Wywołanie dedykowanego interfejsu
        if hasattr(mod, "receive_geon_signal"):
            result = mod.receive_geon_signal(clean_payload)
        elif callable(mod):
            result = mod(clean_payload)
        else:
            result = {"status": "SUCCESS", "data": clean_payload}
        
        # Emit przez EventBus
        self.event_bus.publish("ROUTE_COMPLETE", {
            "module": target_module,
            "result": result
        })
        
        return result
    
    def _sanitize_dict(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Sanityzacja słownika rekurencyjnie."""
        result = {}
        for k, v in data.items():
            if isinstance(v, (int, float)):
                result[k] = sanitize_value_33(v)
            elif isinstance(v, str):
                result[k] = sanitize_string_33(v)
            elif isinstance(v, dict):
                result[k] = self._sanitize_dict(v)
            else:
                result[k] = v
        return result
    
    # =========================================================================
    # METODY STATUSU
    # =========================================================================
    
    def get_status(self) -> Dict[str, Any]:
        """Zwraca pełny status systemu."""
        return {
            "version": VERSION,
            "signature": FRACTAL_SIGNATURE,
            "timestamp": datetime.now().isoformat(),
            "petals": self.petals,
            "stats": self.stats,
            "modules": self.get_modules(),
            "gates": self.core_c.get_gate_status(),
            "core_a": self.core_a.get_stats(),
            "core_b": self.core_b.get_stats(),
            "core_c": self.core_c.get_stats(),
            "thresholds": self.core_b.get_thresholds(),
            "event_history": len(self.event_bus.get_history())
        }
    
    def get_event_history(self, limit: int = 20) -> List[Dict[str, Any]]:
        return self.event_bus.get_history(limit)
    
    def reset(self) -> None:
        """Resetuje system."""
        self.stats = {"signals_processed": 0, "signals_rejected": 0, "modules_connected": 0}
        self.event_bus.clear()
        LOG_INFO("🔄 Autostrada 33 zresetowana")


# =============================================================================
# 7. PRZYKŁADOWE MODUŁY ZEWNĘTRZNE
# =============================================================================

class HeliosSystemModule:
    """Dedykowany moduł sterujący dla systemu HELIOS."""
    
    def __init__(self, name: str = "HELIOS_CTRL"):
        self.name = name
        self.last_received: Optional[Dict] = None
        LOG_INFO(f"☀️ Moduł HELIOS [{name}] aktywowany")
    
    def receive_geon_signal(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        self.last_received = payload
        temp = payload.get("temperature", 20.0)
        power_limit = payload.get("power_limit", 100.0)
        
        return {
            "system": "HELIOS_SYSTEM",
            "module": self.name,
            "status": "OPERATIONAL",
            "adjusted_output": round(temp * 1.08, 3),
            "power_safe_mode": power_limit <= 90.0,
            "timestamp": datetime.now().isoformat()
        }
    
    def get_last(self) -> Optional[Dict]:
        return self.last_received


class GeonOSModule:
    """Moduł integracji z GEON_OS."""
    
    def __init__(self):
        self.messages: List[Dict] = []
        LOG_INFO("🐉 Moduł GEON_OS aktywowany")
    
    def receive_geon_signal(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        self.messages.append({
            "timestamp": datetime.now().isoformat(),
            "payload": payload
        })
        return {
            "status": "ACK",
            "message": "Signal received by GEON_OS",
            "queue_size": len(self.messages)
        }


# =============================================================================
# 8. DEMONSTRACJA SYSTEMOWA
# =============================================================================

def demo():
    print("\n" + "=" * 80)
    print("🐉 GEON_ORGANISM_ABC_33 — FINALNA WERSJA v3.1 ULTIMA")
    print(f"   {VERSION}")
    print("=" * 80)
    print(f"Status: PRODUCTION_READY | ARCHITECTURE_LOCKED | FRACTAL_PERFECTED")
    print(f"Sygnatura: {FRACTAL_SIGNATURE}")
    print("=" * 80 + "\n")
    
    # Inicjalizacja Autostrady 33
    highway = Autostrada33()
    
    # Subskrypcje demo
    def on_pipeline_complete(payload):
        print(f"   📡 [EVENT] PIPELINE_COMPLETE: {payload.get('signal_id')}")
    
    def on_correction(payload):
        print(f"   📡 [EVENT] CORRECTION_TO_A: {payload.get('reason')}")
    
    highway.event_bus.subscribe("PIPELINE_COMPLETE", on_pipeline_complete)
    highway.event_bus.subscribe("CORRECTION_TO_A", on_correction)
    
    # =====================================================================
    # TEST 1: Rejestracja modułów
    # =====================================================================
    
    print("🔹 TEST 1: Rejestracja modułów")
    helios = HeliosSystemModule("HELIOS_MAIN")
    geon_os = GeonOSModule()
    
    highway.register_module("HELIOS_MAIN", helios)
    highway.register_module("GEON_OS", geon_os)
    print(f"   Moduły: {highway.get_modules()}")
    print("-" * 60 + "\n")
    
    # =====================================================================
    # TEST 2: Pipeline przez A-B-C
    # =====================================================================
    
    print("🔹 TEST 2: Pipeline przez Rdzenie A-B-C")
    payload = {
        "mode": "AUTONOMOUS",
        "power_limit": 97.5,
        "target_frequency": 33.0,
        "temperature": 27.5
    }
    
    success, signal = highway.execute_pipeline(
        intent_id="INTENT_HELIOS_001",
        payload=payload,
        raw_value=17.33,
        priority=7
    )
    
    print(f"   Status: {'✅ SUKCES' if success else '❌ PORAŻKA'}")
    print(f"   ID: {signal.intent_id}")
    print(f"   Raw: {signal.raw_value:.6f} → Sanitized: {signal.sanitized_value:.6f}")
    print(f"   Priority: {signal.priority}")
    print(f"   Exec factor: {signal.payload.get('_geon_exec_factor', 'N/A')}")
    print(f"   Vortex: {signal.vortex_detected}")
    print(f"   Steps: {len(signal.history)}")
    print("-" * 60 + "\n")
    
    # =====================================================================
    # TEST 3: Routing do modułu HELIOS
    # =====================================================================
    
    print("🔹 TEST 3: Routing do modułu HELIOS")
    response = highway.route_to_module("HELIOS_MAIN", {
        "temperature": 27.5,
        "power_limit": 85.0,
        "mode": "ECO"
    })
    
    print(f"   Status: {response.get('status')}")
    print(f"   Adjusted output: {response.get('adjusted_output', 'N/A')}")
    print(f"   Power safe mode: {response.get('power_safe_mode', 'N/A')}")
    print("-" * 60 + "\n")
    
    # =====================================================================
    # TEST 4: Routing do GEON_OS
    # =====================================================================
    
    print("🔹 TEST 4: Routing do modułu GEON_OS")
    response2 = highway.route_to_module("GEON_OS", {
        "command": "SYNC",
        "layer": 33,
        "data": {"status": "ACTIVE"}
    })
    
    print(f"   Status: {response2.get('status')}")
    print(f"   Message: {response2.get('message')}")
    print(f"   Queue size: {response2.get('queue_size')}")
    print("-" * 60 + "\n")
    
    # =====================================================================
    # TEST 5: Korekta do A
    # =====================================================================
    
    print("🔹 TEST 5: Korekta do A (CORRECTION_A)")
    correction = highway.core_c.send_correction_to_A("load")
    print(f"   Action: {correction.get('action')}")
    print(f"   Reason: {correction.get('reason')}")
    print(f"   New priority base: {correction.get('new_priority_base')}")
    print("-" * 60 + "\n")
    
    # =====================================================================
    # TEST 6: Decoy Log
    # =====================================================================
    
    print("🔹 TEST 6: Decoy Log (stealth_flow)")
    highway.core_c.generate_decoy_log("System status: NORMAL. No anomalies detected.")
    highway.core_c.generate_decoy_log("Helios: Power consumption within limits.")
    print(f"   Decoy logs: {len(highway.core_c.decoy_logs)}")
    for log in highway.core_c.decoy_logs:
        print(f"     🕵️ {log['message']}")
    print("-" * 60 + "\n")
    
    # =====================================================================
    # TEST 7: Event History
    # =====================================================================
    
    print("🔹 TEST 7: Event History")
    events = highway.get_event_history(5)
    print(f"   Events: {len(events)}")
    for event in events:
        print(f"     📡 {event['type']}: {str(event['payload'])[:50]}...")
    print("-" * 60 + "\n")
    
    # =====================================================================
    # STATUS SYSTEMU
    # =====================================================================
    
    print("=" * 80)
    print("📊 STATUS SYSTEMU")
    print("=" * 80)
    
    status = highway.get_status()
    print(f"Wersja: {status['version']}")
    print(f"Sygnatura: {status['signature']}")
    print(f"Płatki: {status['petals']}")
    print(f"\n--- STATYSTYKI ---")
    for key, value in status['stats'].items():
        print(f"  {key}: {value}")
    
    print(f"\n--- MODUŁY ---")
    for mod in status['modules']:
        print(f"  • {mod}")
    
    print(f"\n--- BRAMY ---")
    for gate, status_val in status['gates'].items():
        print(f"  {gate}: {status_val}")
    
    print(f"\n--- RDZEŃ A ---")
    for key, value in status['core_a'].items():
        print(f"  {key}: {value}")
    
    print(f"\n--- RDZEŃ B ---")
    for key, value in status['core_b'].items():
        if key == "thresholds":
            print(f"  {key}:")
            for tk, tv in value.items():
                print(f"    {tk}: {tv}")
        else:
            print(f"  {key}: {value}")
    
    print(f"\n--- RDZEŃ C ---")
    for key, value in status['core_c'].items():
        if key == "gates":
            print(f"  {key}:")
            for gk, gv in value.items():
                print(f"    {gk}: {gv}")
        else:
            print(f"  {key}: {value}")
    
    print("\n" + "=" * 80)
    print("🐉 SYSTEM ZSYNCHRONIZOWANY | KLAWO JAK CHOLERA | 1-6-8-3-3. ∞")
    print("=" * 80 + "\n")


# =============================================================================
# 9. URUCHOMIENIE
# =============================================================================

if __name__ == "__main__":
    demo()