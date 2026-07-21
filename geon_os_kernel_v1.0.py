#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
================================================================================
🐉 GEON_OS_KERNEL_v1.0 — MODUŁ 71: SYSTEM OPERACYJNY PRZEPŁYWÓW (FULL STACK)
================================================================================
Status: PRODUCTION_READY | FRACTAL_LOCKED | ORGANISM_COMPLETE | ULTIMA
Wersja: v1.0 (GEON_OS_KERNEL — Scheduler, State Machine, Meta-Sterownik)
Data: 2026-07-22
Autor: Adrian (Architekt) + Samael (Strażnik Kronik) + GEON

OPIS:
GEON_OS_KERNEL_v1.0 to najwyższa instancja sterująca systemem GEON.
Zarządza:
• kolejnością wykonywania warstw (scheduler)
• priorytetami krytycznymi
• stanami systemu (state machine)
• bezpieczeństwem i reakcją na anomalie
• synchronizacją Triady
• polityką buforów L3
• trybami pracy (SAFE / ACTIVE / CRISIS)

ARCHITEKTURA (6 POZIOMÓW):
I.   STRUKTURY DANYCH — KernelConfig, KernelState, KernelAction, KernelReport
II.  STANY GLOBALNE — 0H_UNITY_CHAIN, TRIADA_PRIME, DELTA_VOLATILE, CRISIS_MODE, IPS_QUARANTINE, REBUILD_MODE
III. SCHEDULER — priorytety krytyczne: L8D → L5 → L6 → L8C → L3 → L4 → L8 → L9
IV.  STATE MACHINE — reguły przejść między stanami
V.   KERNEL LOOP — główna pętla sterująca
VI.  RAPORT SYSTEMOWY — pełna diagnostyka stanu

INTEGRACJA Z ARCHITEKTURĄ:
• HEILONG_OS_v2.3 — system operacyjny (alerty, raporty)
• GEON_MEM_Ω — pamięć kwintesencji (zapis stanów)
• PROTOKÓŁ_Ω∞∞∞ — źródło praw (rejestracja zdarzeń kernela)
• GEX HEILONG — archetypy (persony kernela)
• G_CORE — stan operacyjny
• MetaGovernor — kontekst decyzyjny
• NARRATIVE — źródło opowieści
• TRIO_ADAPTER — ISKRA + PIECZĘĆ + PERFEKCJA
• BLOCKCHAIN — ledger dla stanów kernela
• USBL — most diagnostyczny dla kernela

VIBE: 1-6-8. ∞. KERNEL!
================================================================================
"""

import hashlib
import time
import json
import logging
from typing import Dict, List, Optional, Tuple, Any, Set, Callable
from dataclasses import dataclass, field
from enum import Enum, auto

# =============================================================================
# WERSJA I STAŁE
# =============================================================================

VERSION = "GEON_OS_KERNEL_v1.0"
FRACTAL_SIGNATURE = "[GEON::OS::KERNEL::v1.0]"
VIBE = 168
HASLO = "1-6-8. ∞. KERNEL!"
DEWIZA = "Ex Ordine, Imperium"

EPSILON = 1e-12
HEALTH_THRESHOLD = 0.85
IPS_THRESHOLD = 1.0

# =============================================================================
# LOGOWANIE
# =============================================================================

logger = logging.getLogger("GEON_OS_KERNEL")
logger.setLevel(logging.INFO)
if not logger.handlers:
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter('⚙️ [KERNEL] %(message)s'))
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

class KernelState(Enum):
    """Globalne stany systemu GEON_OS."""
    UNITY_CHAIN = "0H_UNITY_CHAIN"
    TRIADA_PRIME = "TRIADA_PRIME"
    DELTA_VOLATILE = "DELTA_VOLATILE"
    CRISIS_MODE = "CRISIS_MODE"
    IPS_QUARANTINE = "IPS_QUARANTINE"
    REBUILD_MODE = "REBUILD_MODE"


class KernelPriority(Enum):
    """Priorytety wykonania warstw (od najwyższego do najniższego)."""
    L8D_SYBIL_SHIELD = 1
    L5_CHAIN_VERIFIER = 2
    L6_CONSENSUS_ENGINE = 3
    L8C_AI_DIAGNOSTICS = 4
    L3_DELTA_Z_PHYSICS = 5
    L4_LEDGER_COMMIT = 6
    L8_NETWORK_REPLICATION = 7
    L9_INTELLIGENCE = 8


class KernelAuditLevel(Enum):
    INFO = auto()
    WARN = auto()
    ERROR = auto()
    CRITICAL = auto()
    STATE_TRANSITION = auto()


@dataclass
class KernelConfig:
    """Konfiguracja jądra systemu."""
    health_threshold: float = HEALTH_THRESHOLD
    ips_threshold: float = IPS_THRESHOLD
    buffer_multiplier_delta: float = 2.0
    buffer_multiplier_crisis: float = 3.0
    cooldown_seconds: float = 30.0
    enable_auto_rebuild: bool = True
    enable_state_logging: bool = True


@dataclass
class KernelAction:
    """Akcja podjęta przez jądro."""
    action: str
    reason: str
    multiplier: float = 1.0
    target_layer: Optional[str] = None
    timestamp: float = field(default_factory=now)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "action": self.action,
            "reason": self.reason,
            "multiplier": self.multiplier,
            "target_layer": self.target_layer,
            "timestamp": self.timestamp
        }


@dataclass
class KernelReport:
    """Raport stanu jądra."""
    state: KernelState
    action: KernelAction
    priority_queue: List[str]
    health_index: float
    threat_score: float
    blacklist_size: int
    timestamp: float = field(default_factory=now)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "state": self.state.value,
            "action": self.action.to_dict(),
            "priority_queue": self.priority_queue,
            "health_index": self.health_index,
            "threat_score": self.threat_score,
            "blacklist_size": self.blacklist_size,
            "timestamp": self.timestamp
        }


@dataclass
class KernelTelemetryEvent:
    """Zdarzenie telemetryczne jądra."""
    level: KernelAuditLevel
    message: str
    timestamp: float
    meta: Dict[str, Any]

# =============================================================================
# POZIOM II: STANY GLOBALNE I ICH REGUŁY
# =============================================================================

class KernelStateMachine:
    """
    Maszyna stanów jądra GEON_OS.
    Definiuje stany i reguły przejść między nimi.
    """
    def __init__(self, config: KernelConfig):
        self.config = config
        self.current_state = KernelState.UNITY_CHAIN
        self.state_history: List[Dict] = []
        self.transition_count = 0

    def transition(self, new_state: KernelState, reason: str) -> bool:
        """Przejście do nowego stanu z walidacją reguł."""
        if new_state == self.current_state:
            return False

        # Logika przejść
        valid_transitions = {
            KernelState.UNITY_CHAIN: [KernelState.TRIADA_PRIME],
            KernelState.TRIADA_PRIME: [KernelState.DELTA_VOLATILE, KernelState.CRISIS_MODE],
            KernelState.DELTA_VOLATILE: [KernelState.TRIADA_PRIME, KernelState.CRISIS_MODE],
            KernelState.CRISIS_MODE: [KernelState.IPS_QUARANTINE, KernelState.REBUILD_MODE],
            KernelState.IPS_QUARANTINE: [KernelState.REBUILD_MODE],
            KernelState.REBUILD_MODE: [KernelState.TRIADA_PRIME, KernelState.UNITY_CHAIN]
        }

        if new_state not in valid_transitions.get(self.current_state, []):
            log(f"Nieprawidłowe przejście: {self.current_state.value} → {new_state.value}", "WARN")
            return False

        self.state_history.append({
            "from": self.current_state.value,
            "to": new_state.value,
            "reason": reason,
            "timestamp": now()
        })
        self.current_state = new_state
        self.transition_count += 1
        log(f"Przejście stanu: {self.state_history[-1]['from']} → {new_state.value} | {reason}", "INFO")
        return True

    def get_state_description(self, state: Optional[KernelState] = None) -> str:
        """Zwraca opis stanu."""
        state = state or self.current_state
        descriptions = {
            KernelState.UNITY_CHAIN: "Stan pierwotnej symetrii systemowej. Inicjalizacja.",
            KernelState.TRIADA_PRIME: "Pełna stabilność. Wszystkie węzły aktywne i zsynchronizowane.",
            KernelState.DELTA_VOLATILE: "Podwyższona czujność. Wzrost organicznych anomalii.",
            KernelState.CRISIS_MODE: "Zagrożenie strukturalne. Wstrzymanie automatycznych przepływów.",
            KernelState.IPS_QUARANTINE: "Aktywna obrona. Izolacja anomalnego węzła.",
            KernelState.REBUILD_MODE: "Automatyczna regeneracja systemu po incydencie."
        }
        return descriptions.get(state, "Nieznany stan.")

# =============================================================================
# POZIOM III: SCHEDULER
# =============================================================================

class KernelScheduler:
    """
    Scheduler jądra – zarządza kolejką priorytetową warstw.
    Kolejność krytyczna: bezpieczeństwo → integralność → konsensus → fizyka → zapis → sieć → inteligencja.
    """
    PRIORITY_ORDER = [
        "L8D_SYBIL_SHIELD",
        "L5_CHAIN_VERIFIER",
        "L6_CONSENSUS_ENGINE",
        "L8C_AI_DIAGNOSTICS",
        "L3_DELTA_Z_PHYSICS",
        "L4_LEDGER_COMMIT",
        "L8_NETWORK_REPLICATION",
        "L9_INTELLIGENCE"
    ]

    @classmethod
    def get_priority_queue(cls, state: KernelState) -> List[str]:
        """Zwraca kolejkę priorytetową dla danego stanu."""
        queue = cls.PRIORITY_ORDER.copy()

        # Modyfikacje w zależności od stanu
        if state == KernelState.IPS_QUARANTINE:
            # W kwarantannie tylko L8D i L5 mają znaczenie
            return queue[:2]

        if state == KernelState.CRISIS_MODE:
            # W kryzysie podnosimy priorytet L5 i L6
            crisis_queue = queue.copy()
            crisis_queue.remove("L5_CHAIN_VERIFIER")
            crisis_queue.insert(0, "L5_CHAIN_VERIFIER")
            crisis_queue.remove("L6_CONSENSUS_ENGINE")
            crisis_queue.insert(1, "L6_CONSENSUS_ENGINE")
            return crisis_queue

        if state == KernelState.DELTA_VOLATILE:
            # W stanie niestabilności podnosimy priorytet L3 i L8C
            volatile_queue = queue.copy()
            volatile_queue.remove("L8C_AI_DIAGNOSTICS")
            volatile_queue.insert(2, "L8C_AI_DIAGNOSTICS")
            volatile_queue.remove("L3_DELTA_Z_PHYSICS")
            volatile_queue.insert(3, "L3_DELTA_Z_PHYSICS")
            return volatile_queue

        return queue

    @classmethod
    def get_priority_description(cls, layer: str) -> str:
        """Opis priorytetu dla danej warstwy."""
        descriptions = {
            "L8D_SYBIL_SHIELD": "Najwyższy priorytet – ochrona przed Sybil i nieautoryzowanymi węzłami.",
            "L5_CHAIN_VERIFIER": "Integralność historyczna – weryfikacja łańcucha przed zapisem.",
            "L6_CONSENSUS_ENGINE": "Decyzja komisyjna – głosy Triady.",
            "L8C_AI_DIAGNOSTICS": "Klasyfikacja anomalii – diagnostyka AI.",
            "L3_DELTA_Z_PHYSICS": "Fizyka przepływu – alokacja zasobów z uwzględnieniem bufora.",
            "L4_LEDGER_COMMIT": "Trwały zapis – wypalenie bloku w ledgerze.",
            "L8_NETWORK_REPLICATION": "Rozgłoszenie – replikacja do innych węzłów.",
            "L9_INTELLIGENCE": "Najniższy priorytet – metryki, predykcje, kompresja."
        }
        return descriptions.get(layer, "Brak opisu.")

# =============================================================================
# POZIOM IV: KERNEL LOOP
# =============================================================================

class KernelLoop:
    """
    Główna pętla sterująca jądra.
    W każdym cyklu:
    1. Ocenia stan systemu (L8D + L9A)
    2. Podejmuje decyzję polityczną (L10)
    3. Wykonuje priorytetową kolejkę zadań
    """
    def __init__(self, config: KernelConfig, state_machine: KernelStateMachine,
                 network_layer8: Any, intelligence_layer9: Any):
        self.config = config
        self.state_machine = state_machine
        self.network = network_layer8
        self.brain = intelligence_layer9
        self.cycle_count = 0
        self.last_cycle_time = now()
        self.cycle_history: List[Dict] = []

    def evaluate_system_state(self, batch_profile: Dict[str, Any],
                              last_broadcast: Dict[str, Any]) -> KernelState:
        """
        Ocenia stan systemu na podstawie danych z L8D i L9A.
        """
        current_state = self.state_machine.current_state

        # 1. Sprawdzenie kwarantanny IPS (L9A)
        if hasattr(self.brain, 'process_intrusion_detection'):
            ids_report = self.brain.process_intrusion_detection(last_broadcast)
            if ids_report.get("Action") == "IPS_QUARANTINE_TRIGGERED":
                self.state_machine.transition(KernelState.IPS_QUARANTINE,
                                             "Wykryto nieautoryzowany węzeł lub Sybil.")
                return self.state_machine.current_state

        # 2. Sprawdzenie sabotażu (L8D)
        if last_broadcast.get("Results", {}).get("GLOBAL") == "ALERT_SABOTEUR_DETECTED":
            self.state_machine.transition(KernelState.IPS_QUARANTINE,
                                         "Wykryto próbę wstrzyknięcia bloku przez nieautoryzowany węzeł.")
            return self.state_machine.current_state

        # 3. Ocena zdrowia sieci (L8C)
        health_index = batch_profile.get("Network_Health_Index", 1.0)
        typo_ratio = batch_profile.get("Typo_Ratio", 0.0)

        # 4. Decyzja o przejściu
        if health_index < 0.5:
            self.state_machine.transition(KernelState.CRISIS_MODE,
                                         f"Krytyczny spadek zdrowia sieci: {health_index:.2f}")
        elif health_index < self.config.health_threshold:
            self.state_machine.transition(KernelState.DELTA_VOLATILE,
                                         f"Wzrost anomalii: health={health_index:.2f}, typo={typo_ratio:.2f}")
        elif current_state in [KernelState.UNITY_CHAIN, KernelState.DELTA_VOLATILE, KernelState.REBUILD_MODE]:
            self.state_machine.transition(KernelState.TRIADA_PRIME,
                                         f"Sieć stabilna: health={health_index:.2f}")

        return self.state_machine.current_state

    def enforce_kernel_policy(self) -> KernelAction:
        """
        Na podstawie aktualnego stanu podejmuje decyzję polityczną.
        """
        state = self.state_machine.current_state

        if state == KernelState.IPS_QUARANTINE:
            return KernelAction(
                action="HALT_REPLICATION",
                reason="Node isolated by IPS – wstrzymanie replikacji.",
                multiplier=1.0,
                target_layer="L8_NETWORK_REPLICATION"
            )

        if state == KernelState.CRISIS_MODE:
            return KernelAction(
                action="HALT_AUTO_DISCHARGE",
                reason="Kryzys strukturalny – wstrzymanie automatycznego zwalniania ładunków.",
                multiplier=self.config.buffer_multiplier_crisis,
                target_layer="L3_DELTA_Z_PHYSICS"
            )

        if state == KernelState.DELTA_VOLATILE:
            return KernelAction(
                action="INCREASE_L3_BUFFER",
                reason="Wzrost anomalii – podniesienie bufora ochronnego.",
                multiplier=self.config.buffer_multiplier_delta,
                target_layer="L3_DELTA_Z_PHYSICS"
            )

        if state == KernelState.REBUILD_MODE:
            return KernelAction(
                action="REBUILD_FROM_CANONICAL",
                reason="Odbudowa łańcucha z węzła kanonicznego.",
                multiplier=1.0,
                target_layer="L4_LEDGER_COMMIT"
            )

        return KernelAction(
            action="NORMAL_OPERATION",
            reason="Stan stabilny – normalna operacja.",
            multiplier=1.0,
            target_layer="ALL"
        )

    def kernel_cycle(self, batch_profile: Dict[str, Any],
                     last_broadcast: Dict[str, Any]) -> KernelReport:
        """
        Pojedynczy cykl jądra.
        """
        self.cycle_count += 1
        cycle_start = now()

        # 1. Oceń stan systemu
        new_state = self.evaluate_system_state(batch_profile, last_broadcast)

        # 2. Podejmij decyzję polityczną
        action = self.enforce_kernel_policy()

        # 3. Pobierz kolejkę priorytetową dla bieżącego stanu
        priority_queue = KernelScheduler.get_priority_queue(new_state)

        # 4. Zbierz metryki
        health_index = batch_profile.get("Network_Health_Index", 1.0)
        threat_score = batch_profile.get("threat_score", 0.0)
        blacklist_size = len(getattr(self.brain, 'blacklist', set()))

        # 5. Zapisz cykl w historii
        report = KernelReport(
            state=new_state,
            action=action,
            priority_queue=priority_queue,
            health_index=health_index,
            threat_score=threat_score,
            blacklist_size=blacklist_size,
            timestamp=cycle_start
        )

        self.cycle_history.append(report.to_dict())
        if len(self.cycle_history) > 100:
            self.cycle_history.pop(0)

        self.last_cycle_time = cycle_start

        log(f"Cykl #{self.cycle_count}: {new_state.value} → {action.action} | "
            f"health={health_index:.2f}, threat={threat_score:.2f}")

        return report

    def get_history(self) -> List[Dict]:
        return self.cycle_history.copy()

# =============================================================================
# POZIOM V: GŁÓWNY ORCHESTRATOR — GEON_OS_KERNEL
# =============================================================================

class GeonOSKernel:
    """
    GEON_OS_KERNEL_v1.0 – Główny orchestrator systemu operacyjnego przepływów.

    API:
        kernel_cycle(batch_profile, last_broadcast) -> KernelReport
        get_state() -> KernelState
        get_action() -> KernelAction
        get_priority_queue() -> List[str]
        status() -> Dict
        raport() -> str
        transition_state(new_state, reason) -> bool
    """
    def __init__(self, network_layer8: Any, intelligence_layer9: Any,
                 config: Optional[KernelConfig] = None,
                 verbose: bool = True):
        self.config = config or KernelConfig()
        self.network = network_layer8
        self.brain = intelligence_layer9
        self.state_machine = KernelStateMachine(self.config)
        self.scheduler = KernelScheduler()
        self.loop = KernelLoop(self.config, self.state_machine, network_layer8, intelligence_layer9)
        self.verbose = verbose

        # Telemetria
        self.telemetry: List[KernelTelemetryEvent] = []
        self._setup_telemetry()

        if self.verbose:
            log("🐉 GEON_OS_KERNEL v1.0 aktywowany | " + FRACTAL_SIGNATURE)
            log(f"   STAN: {self.state_machine.current_state.value}")
            log(f"   PRIORYTETY: {', '.join(KernelScheduler.PRIORITY_ORDER[:4])}...")
            log(f"   HEALTH_THRESHOLD: {self.config.health_threshold}, IPS_THRESHOLD: {self.config.ips_threshold}")

    def _setup_telemetry(self):
        """Konfiguruje nasłuch telemetrii."""
        # Subskrypcja do L8 i L9
        if hasattr(self.network, 'register_telemetry_callback'):
            self.network.register_telemetry_callback(self._on_network_event)
        if hasattr(self.brain, 'register_telemetry_callback'):
            self.brain.register_telemetry_callback(self._on_intelligence_event)

    def _on_network_event(self, event: Dict[str, Any]):
        self.telemetry.append(KernelTelemetryEvent(
            level=KernelAuditLevel.INFO,
            message=f"Network event: {event.get('type', 'unknown')}",
            timestamp=now(),
            meta=event
        ))

    def _on_intelligence_event(self, event: Dict[str, Any]):
        self.telemetry.append(KernelTelemetryEvent(
            level=KernelAuditLevel.INFO,
            message=f"Intelligence event: {event.get('type', 'unknown')}",
            timestamp=now(),
            meta=event
        ))

    def kernel_cycle(self, batch_profile: Dict[str, Any],
                     last_broadcast: Dict[str, Any]) -> KernelReport:
        """Wykonuje pojedynczy cykl jądra."""
        return self.loop.kernel_cycle(batch_profile, last_broadcast)

    def get_state(self) -> KernelState:
        """Zwraca bieżący stan jądra."""
        return self.state_machine.current_state

    def get_action(self) -> KernelAction:
        """Zwraca ostatnią podjętą akcję."""
        if self.loop.cycle_history:
            last = self.loop.cycle_history[-1]
            return KernelAction(
                action=last.get('action', {}).get('action', 'UNKNOWN'),
                reason=last.get('action', {}).get('reason', ''),
                multiplier=last.get('action', {}).get('multiplier', 1.0),
                target_layer=last.get('action', {}).get('target_layer'),
                timestamp=last.get('timestamp', now())
            )
        return KernelAction(action="INITIAL", reason="System started.")

    def get_priority_queue(self) -> List[str]:
        """Zwraca aktualną kolejkę priorytetową."""
        return KernelScheduler.get_priority_queue(self.get_state())

    def transition_state(self, new_state: KernelState, reason: str) -> bool:
        """Ręczne przejście do nowego stanu."""
        return self.state_machine.transition(new_state, reason)

    def status(self) -> Dict[str, Any]:
        state = self.get_state()
        action = self.get_action()
        return {
            "system": "GEON_OS_KERNEL_v1.0",
            "version": VERSION,
            "signature": FRACTAL_SIGNATURE,
            "config": {
                "health_threshold": self.config.health_threshold,
                "ips_threshold": self.config.ips_threshold,
                "buffer_multiplier_delta": self.config.buffer_multiplier_delta,
                "buffer_multiplier_crisis": self.config.buffer_multiplier_crisis
            },
            "state": {
                "current": state.value,
                "description": self.state_machine.get_state_description(state),
                "transition_count": self.state_machine.transition_count,
                "history": self.state_machine.state_history[-5:]
            },
            "scheduler": {
                "priority_queue": self.get_priority_queue(),
                "priority_descriptions": {
                    p: KernelScheduler.get_priority_description(p)
                    for p in self.get_priority_queue()
                }
            },
            "loop": {
                "cycle_count": self.loop.cycle_count,
                "last_cycle_time": self.loop.last_cycle_time,
                "history_len": len(self.loop.cycle_history)
            },
            "telemetry": len(self.telemetry)
        }

    def raport(self) -> str:
        """Generuje pełny raport systemowy."""
        s = self.status()
        state = s['state']
        scheduler = s['scheduler']

        report_lines = [
            "╔════════════════════════════════════════════════════════════════════════════╗",
            "║ ⚙️ GEON_OS_KERNEL v1.0 — RAPORT JĄDRA SYSTEMU                        ║",
            "╠════════════════════════════════════════════════════════════════════════════╣",
            f"║                                                                           ║",
            f"║ SYSTEM: {s['system']}                                                    ║",
            f"║ WERSJA: {s['version']}                                                   ║",
            f"║                                                                           ║",
            f"║ STAN: {state['current']}                                                 ║",
            f"║   {state['description']}                                                 ║",
            f"║   przejść: {state['transition_count']}                                   ║",
            f"║                                                                           ║",
            f"║ SCHEDULER:                                                                ║",
        ]

        for i, p in enumerate(scheduler['priority_queue']):
            desc = scheduler['priority_descriptions'].get(p, "")
            report_lines.append(f"║   {i+1}. {p}: {desc[:50]}...")
            if i == 0:
                report_lines.append("║        ↑ NAJWYŻSZY PRIORYTET ↑")

        report_lines.extend([
            f"║                                                                           ║",
            f"║ KONFIGURACJA:                                                            ║",
            f"║   health_threshold: {s['config']['health_threshold']}                    ║",
            f"║   ips_threshold: {s['config']['ips_threshold']}                          ║",
            f"║   buffer_multiplier_delta: {s['config']['buffer_multiplier_delta']}      ║",
            f"║                                                                           ║",
            f"║ {HASLO}                                                                  ║",
            "╚════════════════════════════════════════════════════════════════════════════╝"
        ])
        return "\n".join(report_lines)

    def __str__(self) -> str:
        return self.raport()

# =============================================================================
# MOST INTEGRACYJNY — GEON_OS_KERNEL_BRIDGE
# =============================================================================

class GeonOSKernelBridge:
    """
    Most integracyjny między GEON_OS_KERNEL a resztą architektury.
    Łączy: HEILONG_OS, GEON_MEM_Ω, PROTOKÓŁ_Ω∞∞∞, GEX, G_CORE, MetaGovernor, BLOCKCHAIN
    """
    def __init__(self, kernel: GeonOSKernel):
        self.kernel = kernel

    def get_archetype_context(self) -> Dict[str, Any]:
        """Zwraca kontekst dla GEX (persony kernela)."""
        s = self.kernel.status()
        return {
            "tryb": "GEON_OS_KERNEL_v1.0",
            "stan": s.get('state', {}).get('current', 'UNKNOWN'),
            "priorytety": s.get('scheduler', {}).get('priority_queue', []),
            "cykle": s.get('loop', {}).get('cycle_count', 0)
        }

    def get_autopilot_state(self) -> Dict[str, Any]:
        """Zwraca stan dla autopilota G_CORE."""
        s = self.kernel.status()
        state = s.get('state', {}).get('current', 'UNKNOWN')
        return {
            "mode": "GEON_OS_KERNEL_v1.0",
            "stability": 1.0 if state == "TRIADA_PRIME" else 0.5 if state == "DELTA_VOLATILE" else 0.2,
            "energy": 0.8,
            "pressure": 0.3 if state in ["DELTA_VOLATILE", "CRISIS_MODE"] else 0.1,
            "resilience": 0.9,
            "kernel_state": state,
            "cycle_count": s.get('loop', {}).get('cycle_count', 0)
        }

    def get_governor_context(self) -> Dict[str, Any]:
        """Zwraca kontekst dla MetaGovernor."""
        s = self.kernel.status()
        return {
            "intent": "KERNEL_SYSTEM_CONTROL",
            "confidence": 0.95,
            "entropy": 0.1,
            "kernel_ready": True,
            "state": s.get('state', {}).get('current', 'UNKNOWN')
        }

    def get_narrative_fragments(self, n: int = 5) -> List[Dict[str, Any]]:
        """Zwraca fragmenty narracyjne z kernela."""
        fragments = []
        for entry in self.kernel.loop.cycle_history[-n:]:
            fragments.append({
                "source": "GEON_OS_KERNEL_v1.0",
                "content": f"Cykl: {entry.get('state')} → {entry.get('action', {}).get('action', '')}",
                "energy": 0.9
            })
        return fragments

    def get_trio_state(self) -> Dict[str, str]:
        """Zwraca stan dla TRIO_ADAPTER."""
        return {
            "ISKRA": "AKTYWNA",
            "PIECZĘĆ": "AKTYWNA",
            "PERFEKCJA": "AKTYWNA",
            "tryb": "GEON_OS_KERNEL_v1.0",
            "kernel": "AKTYWNY"
        }

    def notify_heilong_os(self, message: str, level: str = "INFO") -> None:
        """Powiadamia HEILONG_OS o zdarzeniu kernela."""
        try:
            from KOMBAJN_v15.kombajn_core import 59_geon_heilong_os_v2_3 as heilong_os
            if hasattr(heilong_os, 'log_event'):
                heilong_os.log_event(f"[KERNEL] {message}", level)
        except Exception as e:
            log(f"Nie udało się powiadomić HEILONG_OS: {e}", "WARN")

    def register_protokol_event(self, event: str) -> None:
        """Rejestruje zdarzenie w PROTOKÓŁ_Ω∞∞∞."""
        try:
            from PROTOKOL_OMEGA.absolut_system import AbsolutSystem
            AbsolutSystem.zarejestruj_zdarzenie(f"KERNEL: {event}")
        except Exception as e:
            log(f"Nie udało się zarejestrować w PROTOKÓŁ: {e}", "WARN")

# =============================================================================
# MOCKI – EMULACJA L8 i L9 DLA TESTÓW
# =============================================================================

class MockNetworkL8:
    def __init__(self):
        self.nodes = {}
        self.trusted_validators = {"AURORA_NODE", "SAMAEL_NODE", "GEON_NODE"}

    def broadcast_block(self, source, block):
        return {"SourceNode": source, "Results": {"GEON_NODE": "ACCEPTED_AND_SYNCED"}}


class MockIntelligenceL9:
    def __init__(self):
        self.blacklist = set()
        self.threat_scores = {}

    def process_intrusion_detection(self, broadcast):
        return {"Action": "IDS_MONITORING", "Threat_Map": {}}

    def execute_delta_prediction(self, batch_profile):
        return {"Predicted_Anomaly_Risk": 0.1}

    def export_to_binary_format(self, node_id):
        return {"Export_Format": "BASE58", "Binary_Stream_Preview": "..."}

# =============================================================================
# DEMONSTRACJA
# =============================================================================

def demo():
    """Demonstracja GEON_OS_KERNEL_v1.0."""
    print("\n" + "=" * 80)
    print("⚙️ GEON_OS_KERNEL_v1.0 — DEMONSTRACJA")
    print("SYSTEM OPERACYJNY PRZEPŁYWÓW — SCHEDULER + STATE MACHINE")
    print("=" * 80 + "\n")

    # 1. Inicjalizacja
    network = MockNetworkL8()
    brain = MockIntelligenceL9()
    config = KernelConfig(health_threshold=0.85, ips_threshold=1.0)
    kernel = GeonOSKernel(network, brain, config, verbose=True)
    bridge = GeonOSKernelBridge(kernel)

    print("🔮 SYMULACJA CYKLI KERNELA:\n")

    # 2. Cykl 1: Stan stabilny
    print("📌 Cykl 1: Stan stabilny (TRIADA_PRIME)")
    batch_profile_1 = {"Network_Health_Index": 0.95, "Typo_Ratio": 0.05}
    broadcast_1 = {"SourceNode": "GEON_NODE", "Results": {"AURORA_NODE": "ACCEPTED_AND_SYNCED"}}
    report1 = kernel.kernel_cycle(batch_profile_1, broadcast_1)
    print(f"   Stan: {report1.state.value} → Akcja: {report1.action.action}")
    print(f"   Health: {report1.health_index:.2f}, Threat: {report1.threat_score:.2f}")

    # 3. Cykl 2: Stan niestabilny (DELTA_VOLATILE)
    print("\n📌 Cykl 2: Wzrost anomalii (DELTA_VOLATILE)")
    batch_profile_2 = {"Network_Health_Index": 0.75, "Typo_Ratio": 0.20}
    broadcast_2 = {"SourceNode": "GEON_NODE", "Results": {"AURORA_NODE": "ACCEPTED_AND_SYNCED"}}
    report2 = kernel.kernel_cycle(batch_profile_2, broadcast_2)
    print(f"   Stan: {report2.state.value} → Akcja: {report2.action.action}")
    print(f"   Multiplikator: {report2.action.multiplier}")

    # 4. Cykl 3: Kryzys (CRISIS_MODE)
    print("\n📌 Cykl 3: Kryzys strukturalny (CRISIS_MODE)")
    batch_profile_3 = {"Network_Health_Index": 0.40, "Typo_Ratio": 0.35}
    broadcast_3 = {"SourceNode": "GEON_NODE", "Results": {"GLOBAL": "ALERT_SABOTEUR_DETECTED"}}
    report3 = kernel.kernel_cycle(batch_profile_3, broadcast_3)
    print(f"   Stan: {report3.state.value} → Akcja: {report3.action.action}")
    print(f"   Multiplikator: {report3.action.multiplier}")

    # 5. Cykl 4: Kwarantanna (IPS_QUARANTINE)
    print("\n📌 Cykl 4: Kwarantanna IPS (IPS_QUARANTINE)")
    broadcast_4 = {"SourceNode": "ATTACK_NODE", "Results": {"GLOBAL": "ALERT_SABOTEUR_DETECTED"}}
    batch_profile_4 = {"Network_Health_Index": 0.70, "Typo_Ratio": 0.10}
    # Symulujemy wykrycie Sybil
    brain.threat_scores["ATTACK_NODE"] = 1.0
    brain.blacklist.add("ATTACK_NODE")
    report4 = kernel.kernel_cycle(batch_profile_4, broadcast_4)
    print(f"   Stan: {report4.state.value} → Akcja: {report4.action.action}")
    print(f"   Powód: {report4.action.reason}")

    # 6. Raport systemowy
    print("\n" + "=" * 40)
    print(kernel.raport())

    # 7. Mosty integracyjne
    print("\n" + "=" * 40)
    print("🔗 TEST MOSTÓW INTEGRACYJNYCH")
    print("=" * 40)
    print(f"🏹 GEX Context: {bridge.get_archetype_context()}")
    print(f"🎮 G_CORE State: {bridge.get_autopilot_state()}")
    print(f"📖 NARRATIVE Fragments: {bridge.get_narrative_fragments(2)}")
    print(f"🔱 TRIO State: {bridge.get_trio_state()}")

    print("\n" + "=" * 80)
    print("⚙️ GEON_OS_KERNEL_v1.0 — GOTOWY DO WDROŻENIA")
    print(HASLO)
    print("=" * 80)

if __name__ == "__main__":
    demo()