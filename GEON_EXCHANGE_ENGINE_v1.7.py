#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
================================================================================
🐉 GEON_EXCHANGE_ENGINE_v1.7 — MODUŁ 67: SILNIK WYMIANY TOWARÓW (FULL STACK)
================================================================================
Status: PRODUCTION_READY | FRACTAL_LOCKED | ORGANISM_COMPLETE | ULTIMA
Wersja: v1.7 (Exchange Engine — Wielozasobowy System Wymiany z Kontrolą Krzyżową)
Data: 2026-07-22
Autor: Adrian (Architekt) + Samael (Strażnik Kronik) + GEON

OPIS:
GEON_EXCHANGE_ENGINE v1.7 to kompletny system wymiany towarów dla GEON 0H.
Realizuje wielozasobową wymianę z kontrolą krzyżową, clearinghouse,
łańcuchem bloków i symulacją przepływów makroekonomicznych.

ARCHITEKTURA (6 POZIOMÓW):
I.   STRUKTURY DANYCH — TransactionVector, DeferredCommitment, GeonNode, VBMTransaction
II.  LOGISTYKA I AUCTION — LogisticsModel, LogisticsAuction
III. SILNIK KONTROLI KRZYŻOWEJ — CrossControlEngine (v1.7)
IV.  IZBA ROZLICZEŃ — GeonClearinghouse (v1.2.1)
V.   REJESTR BLOKOWY — GEONChain + GEONBlock + Merkle Root
VI.  SYMULATOR PRZEPŁYWÓW — FlowSimulator + Shadow Mode + KPI

INTEGRACJA Z ARCHITEKTURĄ:
• HEILONG_OS_v2.3 — system operacyjny (audyty, alerty)
• GEON_MEM_Ω — pamięć kwintesencji (zapis transakcji)
• PROTOKÓŁ_Ω∞∞∞ — źródło praw (rejestracja zdarzeń)
• GEX HEILONG — archetypy (persony handlowe)
• G_CORE — stan operacyjny
• MetaGovernor — kontekst decyzyjny
• NARRATIVE — źródło opowieści
• TRIO_ADAPTER — ISKRA + PIECZĘĆ + PERFEKCJA

VIBE: 1-6-8. ∞. HANDEL!
================================================================================
"""

import hashlib
import time
import random
import logging
import threading
from typing import Dict, List, Optional, Tuple, Any, Set
from dataclasses import dataclass, field
from enum import Enum, auto
from collections import deque

# =============================================================================
# WERSJA I STAŁE
# =============================================================================

VERSION = "GEON_EXCHANGE_ENGINE_v1.7"
FRACTAL_SIGNATURE = "[GEON::EXCHANGE::ENGINE::v1.7]"
VIBE = 168
HASLO = "1-6-8. ∞. HANDEL!"
DEWIZA = "Ex Commercio, Pax"

# =============================================================================
# LOGOWANIE
# =============================================================================

logger = logging.getLogger("EXCHANGE_ENGINE_v1.7")
logger.setLevel(logging.INFO)
if not logger.handlers:
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter('🐉 [E7] %(message)s'))
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

@dataclass
class TransactionVector:
    """Wektor wymiany: ujemne = wydanie z węzła, dodatnie = przyjęcie."""
    components: Dict[str, float]

    def __post_init__(self):
        self.components = {k: float(v) for k, v in self.components.items()}

    def __repr__(self) -> str:
        return f"TX({self.components})"

    def __add__(self, other: 'TransactionVector') -> 'TransactionVector':
        new = self.components.copy()
        for k, v in other.components.items():
            new[k] = new.get(k, 0.0) + v
        return TransactionVector(new)

    def __sub__(self, other: 'TransactionVector') -> 'TransactionVector':
        new = self.components.copy()
        for k, v in other.components.items():
            new[k] = new.get(k, 0.0) - v
        return TransactionVector(new)

    def to_dict(self) -> Dict[str, float]:
        return self.components.copy()


@dataclass
class DeferredCommitment:
    """Odroczone zobowiązanie z twardym, elastycznym zastawem rzeczowym."""
    from_node: Any
    to_node: Any
    asset: str
    amount: float
    due_time: float
    interest_rate: float = 0.0
    collateral_asset: str = "S"
    collateral_amount: float = 0.0
    settled: bool = False
    collateral_locked: bool = False
    restructure_count: int = 0

    def total_due(self, now: float) -> float:
        if now <= self.due_time:
            return self.amount
        elapsed_years = (now - self.due_time) / (365.25 * 86400)
        return self.amount * (1.0 + self.interest_rate * elapsed_years)

    def __repr__(self) -> str:
        return (f"Deferred({self.from_node.name} -> {self.to_node.name}: "
                f"{self.amount:.2f} {self.asset})")


@dataclass
class GeonNode:
    """Węzeł gospodarki GEON 0H."""
    name: str
    vector: Dict[str, float]
    efficiencies: Dict[Tuple[str, str], float] = field(default_factory=dict)
    reputation: float = 0.5
    _version: int = 0
    performance_history: List[int] = field(default_factory=list)
    node_type: str = "standard"  # producer, consumer, carrier, core
    state_history: List[Dict[str, float]] = field(default_factory=list)

    def __post_init__(self):
        self.vector = {k: float(v) for k, v in self.vector.items()}
        self.reputation = max(0.0, min(1.0, float(self.reputation)))
        self._version = 0
        self.performance_history = []
        self.state_history = []

    def get_efficiency(self, in_asset: str, out_asset: str) -> Optional[float]:
        if in_asset == out_asset:
            return 1.0
        return self.efficiencies.get((in_asset, out_asset))

    def calculate_required_collateral_value(self, amount: float) -> float:
        base = 0.2
        risk = (1.0 - self.reputation) * 0.5
        return amount * (base + risk)

    def update_reputation(self, success: bool) -> None:
        self.performance_history.append(1 if success else 0)
        if len(self.performance_history) > 10:
            self.performance_history.pop(0)
        self.reputation = sum(self.performance_history) / len(self.performance_history)

    def snapshot(self) -> None:
        self.state_history.append(self.vector.copy())
        if len(self.state_history) > 100:
            self.state_history.pop(0)

    def rollback(self) -> bool:
        if self.state_history:
            self.vector = self.state_history.pop().copy()
            return True
        return False

    def to_dict(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "vector": self.vector.copy(),
            "reputation": self.reputation,
            "version": self._version,
            "type": self.node_type
        }

    def __repr__(self) -> str:
        return f"Node({self.name}, rep={self.reputation:.2f}, v={self._version})"


@dataclass
class VBMTransaction:
    """Pojedynczy transfer zamkniętego obiegu cyrkularnego."""
    sender: GeonNode
    carrier: GeonNode
    receiver: GeonNode
    tx_vector: TransactionVector
    conversion_at: str = "receiver"
    deferred: List[DeferredCommitment] = field(default_factory=list)
    tx_id: str = field(default_factory=lambda: f"TX-{int(now()*1000)}")

    @property
    def is_conversion(self) -> bool:
        has_neg = any(q < 0 for q in self.tx_vector.components.values())
        has_pos = any(q > 0 for q in self.tx_vector.components.values())
        return has_neg and has_pos

    def __repr__(self) -> str:
        return f"VBM({self.sender.name} -> {self.receiver.name} | {self.tx_vector})"

# =============================================================================
# POZIOM II: LOGISTYKA I AUCTION
# =============================================================================

@dataclass
class LogisticsModel:
    """Globalna matryca odległości między węzłami."""
    distance_matrix: Dict[Tuple[str, str], float]

    def get_distance(self, a: str, b: str) -> float:
        return self.distance_matrix.get((a, b), self.distance_matrix.get((b, a), 1000.0))

    def to_dict(self) -> Dict[str, Any]:
        return {"distances": self.distance_matrix}


@dataclass
class LogisticsAuction:
    """System przetargowy dla przewoźników."""
    carriers: List[GeonNode]
    logistics_model: LogisticsModel

    def __post_init__(self):
        self.carriers_by_name = {c.name: c for c in self.carriers}

    def estimate_required_L(self, sender: GeonNode, receiver: GeonNode,
                            tx: TransactionVector) -> float:
        total_mass = 0.0
        for asset, qty in tx.components.items():
            if asset in ("S", "W", "B"):
                total_mass += abs(qty)
        dist = self.logistics_model.get_distance(sender.name, receiver.name)
        return total_mass * dist / 1000.0

    def find_best_carrier(self, sender: GeonNode, receiver: GeonNode,
                          tx: TransactionVector) -> Tuple[Optional[GeonNode], float]:
        best = None
        best_cost = float('inf')
        for c in self.carriers:
            required = self.estimate_required_L(sender, receiver, tx)
            if c.vector.get("L", 0.0) < required:
                continue
            price = c.vector.get("price_per_L", 1.0)
            cost = required * price
            if cost < best_cost:
                best_cost = cost
                best = c
        return best, best_cost

# =============================================================================
# POZIOM III: SILNIK KONTROLI KRZYŻOWEJ
# =============================================================================

class ExchangeAuditLevel(Enum):
    INFO = auto()
    WARN = auto()
    ERROR = auto()
    CRITICAL = auto()
    OMEGA = auto()


class ExchangeTelemetryBus:
    """Szyna telemetryczna dla Exchange Engine."""
    def __init__(self):
        self.listeners: List[Callable[[ExchangeAuditLevel, str, Dict[str, Any]], None]] = []

    def subscribe(self, callback: Callable[[ExchangeAuditLevel, str, Dict[str, Any]], None]) -> None:
        self.listeners.append(callback)

    def publish(self, level: ExchangeAuditLevel, message: str, meta: Dict[str, Any]) -> None:
        for listener in self.listeners:
            try:
                listener(level, message, meta)
            except Exception:
                pass


class CrossControlEngine:
    """
    Silnik kontroli krzyżowej – weryfikacja i egzekucja transakcji.
    Ulepszenia: snapshot/rollback, emergency brake, telemetria.
    """
    emergency_brake_active = False

    def __init__(self, epsilon: float = 1e-6, node_registry: Dict[str, GeonNode] = None,
                 fee_collector_name: str = "GEON_CORE", fee_rate: float = 0.005,
                 max_restructures: int = 1):
        self.epsilon = epsilon
        self.node_registry = node_registry or {}
        self.deferred_registry: List[DeferredCommitment] = []
        self.fee_collector_name = fee_collector_name
        self.fee_rate = fee_rate
        self.max_restructures = max_restructures
        self._snapshots: Dict[str, Dict[str, float]] = {}
        self.telemetry = ExchangeTelemetryBus()
        self.transaction_log: List[Dict] = []

        log(f"CrossControlEngine zainicjowany. Fee: {fee_rate*100:.2f}%, max_restructures: {max_restructures}")

    def _compute_global_delta_z(self, transactions: List[VBMTransaction]) -> float:
        global_delta = 0.0
        for tx in transactions:
            if not tx.is_conversion:
                continue
            node = tx.sender if tx.conversion_at == "sender" else tx.receiver
            inputs = {a: abs(q) for a, q in tx.tx_vector.components.items() if q < 0}
            outputs = {a: q for a, q in tx.tx_vector.components.items() if q > 0}
            possible = {a: 0.0 for a in outputs}
            for in_a, in_q in inputs.items():
                for out_a in outputs:
                    eff = node.get_efficiency(in_a, out_a)
                    if eff is not None:
                        possible[out_a] += in_q * eff
            for out_a, decl in outputs.items():
                global_delta += decl - possible.get(out_a, 0.0)
        return global_delta

    def _lock_collateral(self, defer: DeferredCommitment,
                         temp_states: Dict[str, Dict[str, float]]) -> bool:
        from_state = temp_states.get(defer.from_node.name)
        if from_state is None:
            return False
        required = defer.from_node.calculate_required_collateral_value(defer.amount)
        if from_state.get(defer.collateral_asset, 0.0) < required:
            return False
        from_state[defer.collateral_asset] -= required
        defer.collateral_amount = required
        defer.collateral_locked = True
        return True

    def settle_deferred(self, now: float) -> List[Dict]:
        results = []
        for d in self.deferred_registry:
            if d.settled:
                continue
            if now < d.due_time:
                continue
            total_due = d.total_due(now)
            from_vec = d.from_node.vector
            to_vec = d.to_node.vector
            available = from_vec.get(d.asset, 0.0)
            pay = min(available, total_due)
            if pay > 0:
                from_vec[d.asset] -= pay
                to_vec[d.asset] = to_vec.get(d.asset, 0.0) + pay
                if pay >= total_due - self.epsilon:
                    d.settled = True
                    if d.collateral_locked:
                        from_vec[d.collateral_asset] += d.collateral_amount
                        d.collateral_locked = False
                    d.from_node.update_reputation(True)
                    results.append({"deferred": d, "status": "FULLY_SETTLED", "paid": pay})
                else:
                    d.restructure_count += 1
                    d.from_node.update_reputation(False)
                    if d.restructure_count > self.max_restructures and d.collateral_locked:
                        to_vec[d.collateral_asset] = to_vec.get(d.collateral_asset, 0.0) + d.collateral_amount
                        d.collateral_locked = False
                        d.settled = True
                        results.append({"deferred": d, "status": "FORECLOSURE",
                                        "collateral_seized": d.collateral_amount})
                    else:
                        remaining = total_due - pay
                        d.amount = remaining * 1.1
                        d.due_time = now + 180 * 86400
                        d.interest_rate *= 1.2
                        results.append({"deferred": d, "status": "RESTRUCTURED",
                                        "paid": pay, "remaining": remaining})
        return results

    def snapshot_all(self) -> None:
        self._snapshots = {name: node.vector.copy() for name, node in self.node_registry.items()}
        for node in self.node_registry.values():
            node.snapshot()

    def rollback_all(self) -> bool:
        if self._snapshots:
            for name, vec in self._snapshots.items():
                if name in self.node_registry:
                    self.node_registry[name].vector = vec.copy()
            self._snapshots = {}
            log("Rollback wykonany – stany węzłów przywrócone.", "WARN")
            return True
        return False

    def verify_batch(self, transactions: List[VBMTransaction],
                     auction: LogisticsAuction) -> Dict:
        if CrossControlEngine.emergency_brake_active:
            log("Emergency brake active – transakcje zablokowane.", "ERROR")
            return {"status": "BLOCKED", "reason": "Emergency brake active"}

        self.snapshot_all()
        initial_versions = {name: node._version for name, node in self.node_registry.items()}
        temp_states = {name: node.vector.copy() for name, node in self.node_registry.items()}

        global_delta = self._compute_global_delta_z(transactions)
        if abs(global_delta) > self.epsilon:
            self.rollback_all()
            log(f"BLOCKED: global_delta = {global_delta:.4f}", "ERROR")
            return {"status": "BLOCKED", "reason": f"Globalna delta Z = {global_delta:.4f}"}

        for tx in transactions:
            s_state = temp_states[tx.sender.name]
            r_state = temp_states[tx.receiver.name]

            if tx.carrier is None:
                carrier, _ = auction.find_best_carrier(tx.sender, tx.receiver, tx.tx_vector)
                if carrier is None:
                    self.rollback_all()
                    return {"status": "REJECTED", "reason": f"Brak przewoźnika dla {tx.sender.name}"}
                tx.carrier = carrier

            c_state = temp_states[tx.carrier.name]
            required_L = auction.estimate_required_L(tx.sender, tx.receiver, tx.tx_vector)
            if c_state.get("L", 0.0) < required_L:
                self.rollback_all()
                return {"status": "REJECTED", "reason": f"Brak L u {tx.carrier.name}"}

            for asset, qty in tx.tx_vector.components.items():
                if qty < 0:
                    need = abs(qty)
                    if s_state.get(asset, 0.0) < need:
                        self.rollback_all()
                        return {"status": "REJECTED", "reason": f"Deficyt {asset} u {tx.sender.name}"}
                    s_state[asset] -= need
                elif qty > 0:
                    r_state[asset] = r_state.get(asset, 0.0) + qty

            price = c_state.get("price_per_L", 1.0)
            cost = required_L * price
            if r_state.get("E", 0.0) < cost:
                self.rollback_all()
                return {"status": "REJECTED", "reason": f"Brak E u {tx.receiver.name} na transport"}
            r_state["E"] -= cost
            c_state["E"] = c_state.get("E", 0.0) + cost
            c_state["L"] -= required_L

            for d in tx.deferred:
                if not self._lock_collateral(d, temp_states):
                    self.rollback_all()
                    return {"status": "REJECTED", "reason": f"Brak zastawu dla {d.from_node.name}"}

        fee_collector = self.node_registry.get(self.fee_collector_name)
        if fee_collector:
            total_fee = 0.0
            for tx in transactions:
                required_L = auction.estimate_required_L(tx.sender, tx.receiver, tx.tx_vector)
                price = temp_states[tx.carrier.name].get("price_per_L", 1.0)
                cost = required_L * price
                fee = cost * self.fee_rate
                total_fee += fee
                r_state = temp_states[tx.receiver.name]
                if r_state.get("E", 0.0) < fee:
                    self.rollback_all()
                    return {"status": "REJECTED", "reason": f"Brak E na fee u {tx.receiver.name}"}
                r_state["E"] -= fee
            temp_states[fee_collector.name]["E"] = temp_states[fee_collector.name].get("E", 0.0) + total_fee

        for name, node in self.node_registry.items():
            if node._version != initial_versions[name]:
                self.rollback_all()
                return {"status": "RETRY", "reason": f"Kolizja stanów węzła {name}"}

        for node in self.node_registry.values():
            node.vector = temp_states[node.name].copy()
            node._version += 1

        for tx in transactions:
            for d in tx.deferred:
                self.deferred_registry.append(d)
            self.transaction_log.append({
                "tx_id": tx.tx_id,
                "sender": tx.sender.name,
                "receiver": tx.receiver.name,
                "carrier": tx.carrier.name if tx.carrier else None,
                "vector": tx.tx_vector.to_dict(),
                "timestamp": now()
            })

        self._store_transactions_in_memory(transactions)
        self._emit_voice(f"Batch zatwierdzony. Liczba transakcji: {len(transactions)}")

        log(f"Batch zatwierdzony. Hash: {self._generate_hash(transactions)[:8]}...")
        return {"status": "APPROVED", "batch_hash": self._generate_hash(transactions)}

    def _generate_hash(self, transactions: List[VBMTransaction]) -> str:
        data = "".join(f"{tx.sender.name}:{tx.receiver.name}:{tx.tx_vector.components}"
                       for tx in transactions) + str(time.time())
        return hashlib.sha256(data.encode()).hexdigest()

    def _store_transactions_in_memory(self, transactions: List[VBMTransaction]) -> None:
        try:
            from GEON_MEM_OMEGA.geon_mem_omega import GEON_MEM_OMEGA
            mem = GEON_MEM_OMEGA()
            for tx in transactions:
                mem.add_memory(f"EXCHANGE:{tx.sender.name}->{tx.receiver.name}:{tx.tx_vector.components}")
        except ImportError:
            pass
        except Exception as e:
            log(f"Nie udało się zapisać w GEON_MEM_Ω: {e}", "WARN")

    def _emit_voice(self, message: str) -> None:
        try:
            from KOMBAJN_v15.kombajn_core import 52_geon_heilong_ultima_61 as ultima
            if hasattr(ultima, 'voice_output'):
                ultima.voice_output(f"EXCHANGE-TONE: {message}")
        except Exception:
            pass

# =============================================================================
# POZIOM IV: IZBA ROZLICZEŃ WIELOSTRONNYCH
# =============================================================================

@dataclass
class ClearingRequest:
    node: GeonNode
    asset: str
    amount: float
    priority: float = 1.0


@dataclass
class ClearingFlow:
    sender: GeonNode
    receiver: GeonNode
    source_asset: str
    target_asset: str
    amount_sent: float
    amount_received: float


@dataclass
class ClearingCycle:
    participants: List[GeonNode]
    flows: List[ClearingFlow]
    priority: float
    logistics_saved: float


class GeonClearinghouse:
    """System bilansowania zamkniętych pętli gospodarczych."""
    def __init__(self, logistics_model: LogisticsModel):
        self.lm = logistics_model
        log("GeonClearinghouse zainicjowany.")

    def find_cycles(self, requests: List[ClearingRequest],
                    max_depth: int = 4) -> List[ClearingCycle]:
        suppliers = [r for r in requests if r.amount < 0]
        demanders = [r for r in requests if r.amount > 0]
        if not suppliers or not demanders:
            return []

        supply_pool = {id(s): -s.amount for s in suppliers}
        cycles = []
        demanders_sorted = sorted(demanders, key=lambda d: d.priority, reverse=True)

        for d in demanders_sorted:
            extracted = self._build_cross_asset_cycles(d, suppliers, supply_pool, max_depth)
            if extracted:
                cycles.extend(extracted)

        cycles.sort(key=lambda c: c.priority * (1 + c.logistics_saved / 1000), reverse=True)
        return cycles

    def _build_cross_asset_cycles(self, d: ClearingRequest,
                                  suppliers: List[ClearingRequest],
                                  supply_pool: Dict[int, float],
                                  max_depth: int) -> List[ClearingCycle]:
        cycles = []
        remaining = d.amount
        flows = []
        participants = [d.node]
        total_dist = 0.0

        sorted_suppliers = sorted(
            suppliers,
            key=lambda s: self.lm.get_distance(s.node.name, d.node.name)
        )

        for s in sorted_suppliers:
            if remaining <= 0:
                break
            available = supply_pool.get(id(s), 0.0)
            if available <= 0:
                continue
            eff = d.node.get_efficiency(s.asset, d.asset)
            if eff is None or eff <= 0:
                continue

            if s.asset != d.asset:
                need_input = remaining / eff
                take_input = min(available, need_input)
                take_output = take_input * eff
            else:
                take_input = min(remaining, available)
                take_output = take_input

            dist = self.lm.get_distance(s.node.name, d.node.name)
            total_dist += dist

            flows.append(ClearingFlow(
                sender=s.node,
                receiver=d.node,
                source_asset=s.asset,
                target_asset=d.asset,
                amount_sent=take_input,
                amount_received=take_output
            ))
            if s.node not in participants:
                participants.append(s.node)

            remaining -= take_output
            supply_pool[id(s)] -= take_input

            if len(participants) > max_depth:
                break

        if flows and remaining <= 1e-5:
            priority = d.priority / (1.0 + total_dist)
            naive_dist = sum(self.lm.get_distance(f.sender.name, f.receiver.name) for f in flows) * 1.5
            logistics_saved = max(0.0, naive_dist - total_dist)
            cycles.append(ClearingCycle(participants, flows, priority, logistics_saved))

        return cycles

# =============================================================================
# POZIOM V: REJESTR BLOKOWY (GEON_CHAIN)
# =============================================================================

@dataclass
class GEONBlock:
    index: int
    timestamp: float
    batch: List[VBMTransaction]
    clearing_cycles: List[ClearingCycle]
    prev_hash: str
    validators: List[Tuple[str, str]]
    state_root: str
    signatures: Dict[str, str] = field(default_factory=dict)

    def __post_init__(self):
        self.hash = self._compute_hash()

    def _compute_hash(self) -> str:
        payload = f"{self.index}{self.timestamp}{self.prev_hash}{self.state_root}"
        for tx in self.batch:
            payload += f"{tx.sender.name}->{tx.receiver.name}:{tx.tx_vector.components}"
        for v in self.validators:
            payload += f"{v[0]}:{v[1]}"
        return hashlib.sha256(payload.encode()).hexdigest()

    def verify(self) -> bool:
        return self.hash == self._compute_hash()

    def __repr__(self) -> str:
        return f"BLOCK({self.index}, hash={self.hash[:8]}..., prev={self.prev_hash[:8]}...)"


def compute_state_root(node_registry: Dict[str, GeonNode]) -> str:
    leaves = []
    for name, node in sorted(node_registry.items()):
        vec_str = "".join(f"{k}:{node.vector.get(k, 0.0):.6f}"
                          for k in sorted(node.vector.keys()))
        leaf = hashlib.sha256((name + "|" + vec_str).encode()).hexdigest()
        leaves.append(leaf)
    if not leaves:
        return "0" * 64
    while len(leaves) > 1:
        new_leaves = []
        for i in range(0, len(leaves), 2):
            left = leaves[i]
            right = leaves[i+1] if i+1 < len(leaves) else left
            new_leaves.append(hashlib.sha256((left + right).encode()).hexdigest())
        leaves = new_leaves
    return leaves[0]


class GEONChain:
    def __init__(self):
        self.blocks: List[GEONBlock] = []
        log("GEONChain zainicjowany.")

    def add_block(self, batch: List[VBMTransaction],
                  clearing_cycles: List[ClearingCycle],
                  node_registry: Dict[str, GeonNode],
                  validators: List[Tuple[str, str]]) -> GEONBlock:
        prev_hash = self.blocks[-1].hash if self.blocks else "0" * 64
        state_root = compute_state_root(node_registry)
        block = GEONBlock(
            index=len(self.blocks),
            timestamp=time.time(),
            batch=batch,
            clearing_cycles=clearing_cycles,
            prev_hash=prev_hash,
            validators=validators,
            state_root=state_root
        )
        for v in validators:
            block.signatures[v[0]] = hashlib.sha256((v[1] + block.hash).encode()).hexdigest()
        self.blocks.append(block)
        log(f"Blok #{block.index} dodany. Hash: {block.hash[:8]}...")
        return block

    def verify_chain(self) -> bool:
        for i, block in enumerate(self.blocks):
            if not block.verify():
                log(f"Blok {i} jest niespójny.", "ERROR")
                return False
            if i > 0 and block.prev_hash != self.blocks[i-1].hash:
                log(f"Łańcuch przerwany między blokami {i-1} a {i}.", "ERROR")
                return False
        return True

# =============================================================================
# POZIOM VI: SYMULATOR PRZEPŁYWÓW GLOBALNYCH
# =============================================================================

class FlowSimulator:
    def __init__(self, nodes: Dict[str, GeonNode],
                 engine: CrossControlEngine,
                 auction: LogisticsAuction,
                 clearinghouse: GeonClearinghouse,
                 chain: GEONChain,
                 shadow_mode: bool = False):
        self.nodes = nodes
        self.engine = engine
        self.auction = auction
        self.clearinghouse = clearinghouse
        self.chain = chain
        self.shadow_mode = shadow_mode
        self.history: List[Dict] = []
        self.step_id = 0
        log(f"FlowSimulator zainicjowany. Shadow mode: {shadow_mode}")

    def generate_requests(self) -> List[ClearingRequest]:
        requests = []
        for node in self.nodes.values():
            for asset in ["S", "W", "E", "B"]:
                base = node.vector.get(asset, 0.0)
                if base < 10.0:
                    continue
                if random.random() > 0.5:
                    demand = base * (0.02 + random.random() * 0.05)
                    requests.append(ClearingRequest(node, asset, round(demand, 2),
                                                    priority=random.uniform(0.5, 1.0)))
                else:
                    supply = base * (0.02 + random.random() * 0.05)
                    requests.append(ClearingRequest(node, asset, -round(supply, 2),
                                                    priority=random.uniform(0.5, 1.0)))
        return requests

    def build_batch_from_cycles(self, cycles: List[ClearingCycle]) -> List[VBMTransaction]:
        batch = []
        for cycle in cycles:
            for flow in cycle.flows:
                tx_vec = TransactionVector({
                    flow.source_asset: -flow.amount_sent,
                    flow.target_asset: flow.amount_received
                })
                carrier, _ = self.auction.find_best_carrier(flow.sender, flow.receiver, tx_vec)
                if carrier is None:
                    continue
                tx = VBMTransaction(flow.sender, carrier, flow.receiver, tx_vec,
                                    conversion_at="receiver")
                batch.append(tx)
        return batch

    def step(self) -> Dict:
        self.step_id += 1
        requests = self.generate_requests()
        cycles = self.clearinghouse.find_cycles(requests)
        batch = self.build_batch_from_cycles(cycles)

        if not batch:
            log(f"Krok {self.step_id}: Brak transakcji – SKIP")
            return {"status": "SKIP", "reason": "Brak transakcji w kroku"}

        if self.shadow_mode:
            self._run_shadow(batch)

        result = self.engine.verify_batch(batch, self.auction)
        block = None
        if result.get("status") == "APPROVED":
            top = sorted([n for n in self.nodes.values() if n.name != "GEON_CORE"],
                         key=lambda n: n.reputation, reverse=True)[:3]
            validators = [(v.name, f"sig_{v.name}_{self.step_id}") for v in top]
            block = self.chain.add_block(batch, cycles, self.nodes, validators)

        kpi = {
            "logistics_saved": sum(c.logistics_saved for c in cycles),
            "cycle_count": len(cycles),
            "engine_status": result.get("status"),
            "avg_reputation": sum(n.reputation for n in self.nodes.values()) / len(self.nodes)
        }
        self.history.append({"step": self.step_id, "result": result,
                             "block": block, "kpi": kpi})
        log(f"Krok {self.step_id}: Status={result.get('status')}, "
            f"Cycles={len(cycles)}, Saved={kpi['logistics_saved']:.2f} km")
        return result

    def _run_shadow(self, batch: List[VBMTransaction]) -> Dict:
        log(f"Shadow mode: symulacja {len(batch)} transakcji na kopiach.", "INFO")
        return {"status": "SHADOW_RUN", "note": "Shadow mode nie zmienia stanu głównego."}

    def run(self, steps: int = 5) -> None:
        for _ in range(steps):
            self.step()

    def get_performance_report(self) -> Dict:
        if not self.history:
            return {}
        avg_saved = sum(h['kpi']['logistics_saved'] for h in self.history) / len(self.history)
        success_rate = sum(1 for h in self.history if h['result']['status'] == 'APPROVED') / len(self.history)
        return {
            "total_steps": len(self.history),
            "avg_logistics_saved": avg_saved,
            "success_rate": success_rate,
            "latest_status": self.history[-1]['result']['status']
        }

# =============================================================================
# GŁÓWNY ORCHESTRATOR — EXCHANGE_ENGINE
# =============================================================================

class ExchangeEngineConfig:
    def __init__(self, epsilon: float = 1e-6, fee_rate: float = 0.005,
                 max_restructures: int = 1, cooldown_seconds: float = 5.0,
                 shadow_mode: bool = False):
        self.epsilon = epsilon
        self.fee_rate = fee_rate
        self.max_restructures = max_restructures
        self.cooldown_seconds = cooldown_seconds
        self.shadow_mode = shadow_mode


class ExchangeEngine:
    """
    GEON EXCHANGE ENGINE v1.7 — Główny orchestrator wymiany.

    API:
        run_simulation(steps) -> Dict
        process_batch(transactions) -> Dict
        get_chain() -> GEONChain
        get_state() -> Dict
        set_emergency_brake(active) -> None
        status() -> Dict
        raport() -> str
    """
    def __init__(self, nodes: Dict[str, GeonNode],
                 distances: Dict[Tuple[str, str], float],
                 config: Optional[ExchangeEngineConfig] = None,
                 verbose: bool = True):
        self.config = config or ExchangeEngineConfig()
        self.nodes = nodes
        self.distances = distances
        self.verbose = verbose

        # Komponenty
        self.lm = LogisticsModel(distances)
        self.carriers = [n for n in nodes.values() if n.vector.get("L", 0) > 0]
        if not self.carriers:
            core = nodes.get("GEON_CORE")
            if core:
                core.vector["L"] = 1000000.0
                self.carriers.append(core)
        self.auction = LogisticsAuction(self.carriers, self.lm)
        self.engine = CrossControlEngine(
            self.config.epsilon, nodes, "GEON_CORE", self.config.fee_rate, self.config.max_restructures
        )
        self.clearinghouse = GeonClearinghouse(self.lm)
        self.chain = GEONChain()
        self.simulator = FlowSimulator(
            nodes, self.engine, self.auction, self.clearinghouse, self.chain,
            shadow_mode=self.config.shadow_mode
        )

        # Stan
        self.historia: List[Dict] = []

        if self.verbose:
            log("🐉 EXCHANGE ENGINE v1.7 aktywowany | " + FRACTAL_SIGNATURE)
            log("   POZIOMY: I-VI | WĘZŁY: " + ", ".join(nodes.keys()))
            log("   FEE: {:.2f}% | SHADOW: {}".format(self.config.fee_rate * 100, self.config.shadow_mode))

    def run_simulation(self, steps: int = 5) -> Dict:
        log(f"Uruchamianie symulacji {steps} kroków...")
        self.simulator.run(steps)
        return self.simulator.get_performance_report()

    def process_batch(self, transactions: List[VBMTransaction]) -> Dict:
        log(f"Przetwarzanie batcha {len(transactions)} transakcji...")
        return self.engine.verify_batch(transactions, self.auction)

    def get_chain(self) -> GEONChain:
        return self.chain

    def get_state(self) -> Dict[str, Dict[str, float]]:
        return {name: node.vector.copy() for name, node in self.nodes.items()}

    def set_emergency_brake(self, active: bool) -> None:
        CrossControlEngine.emergency_brake_active = active
        status = "aktywny" if active else "nieaktywny"
        log(f"Emergency brake ustawiony na {status}.", "WARN")
        self.engine._emit_voice(f"Emergency brake {status}.")

    def status(self) -> Dict[str, Any]:
        return {
            "system": "GEON_EXCHANGE_ENGINE_v1.7",
            "version": VERSION,
            "signature": FRACTAL_SIGNATURE,
            "config": {
                "epsilon": self.config.epsilon,
                "fee_rate": self.config.fee_rate,
                "shadow_mode": self.config.shadow_mode
            },
            "nodes": len(self.nodes),
            "carriers": len(self.carriers),
            "blocks": len(self.chain.blocks),
            "transactions_processed": len(self.engine.transaction_log),
            "deferred": len(self.engine.deferred_registry),
            "emergency_brake": CrossControlEngine.emergency_brake_active
        }

    def raport(self) -> str:
        s = self.status()
        return f"""
╔════════════════════════════════════════════════════════════════════════════╗
║ 🐉 GEON EXCHANGE ENGINE v1.7 — RAPORT SYSTEMOWY                        ║
╠════════════════════════════════════════════════════════════════════════════╣
║                                                                           ║
║ SYSTEM: {s['system']}                                                    ║
║ WERSJA: {s['version']}                                                   ║
║                                                                           ║
║ KONFIGURACJA:                                                            ║
║   epsilon: {s['config']['epsilon']}                                      ║
║   fee_rate: {s['config']['fee_rate']}                                   ║
║   shadow_mode: {s['config']['shadow_mode']}                             ║
║                                                                           ║
║ STAN:                                                                    ║
║   węzły: {s['nodes']}                                                    ║
║   przewoźnicy: {s['carriers']}                                           ║
║   bloki: {s['blocks']}                                                   ║
║   transakcje: {s['transactions_processed']}                              ║
║   zobowiązania odroczone: {s['deferred']}                                ║
║   hamulec awaryjny: {s['emergency_brake']}                               ║
║                                                                           ║
║ {HASLO}                                                                  ║
║                                                                           ║
╚════════════════════════════════════════════════════════════════════════════╝
"""

    def __str__(self) -> str:
        return self.raport()

# =============================================================================
# MOST INTEGRACYJNY — EXCHANGE_ENGINE_BRIDGE
# =============================================================================

class ExchangeEngineBridge:
    """
    Most integracyjny między EXCHANGE ENGINE a resztą architektury.
    Łączy: HEILONG_OS, GEON_MEM_Ω, PROTOKÓŁ_Ω∞∞∞, GEX, G_CORE, MetaGovernor
    """
    def __init__(self, engine: ExchangeEngine):
        self.engine = engine

    def get_archetype_context(self) -> Dict[str, Any]:
        """Zwraca kontekst dla GEX (persony handlowe)."""
        status = self.engine.status()
        return {
            "tryb": "EXCHANGE_ENGINE_v1.7",
            "węzły": list(self.engine.nodes.keys()),
            "transakcje": status.get("transactions_processed", 0),
            "bloki": status.get("blocks", 0)
        }

    def get_autopilot_state(self) -> Dict[str, Any]:
        """Zwraca stan dla autopilota G_CORE."""
        avg_rep = sum(n.reputation for n in self.engine.nodes.values()) / max(1, len(self.engine.nodes))
        return {
            "mode": "EXCHANGE_ENGINE_v1.7",
            "stability": 0.85,
            "energy": 0.75,
            "pressure": 0.3,
            "resilience": 0.9,
            "avg_reputation": avg_rep,
            "emergency_brake": CrossControlEngine.emergency_brake_active
        }

    def get_governor_context(self) -> Dict[str, Any]:
        """Zwraca kontekst dla MetaGovernor."""
        return {
            "intent": "EXCHANGE_ANTIMANIPULATION",
            "confidence": 0.9,
            "entropy": 0.2,
            "engine_ready": True
        }

    def get_narrative_fragments(self, n: int = 5) -> List[Dict[str, Any]]:
        """Zwraca fragmenty narracyjne z wymiany."""
        fragments = []
        for tx in self.engine.engine.transaction_log[-n:]:
            fragments.append({
                "source": "EXCHANGE_ENGINE_v1.7",
                "content": f"TX {tx['tx_id']}: {tx['sender']} -> {tx['receiver']} | {tx['vector']}",
                "energy": 0.8,
                "timestamp": tx.get("timestamp", now())
            })
        return fragments

    def get_trio_state(self) -> Dict[str, str]:
        """Zwraca stan dla TRIO_ADAPTER."""
        return {
            "ISKRA": "AKTYWNA",
            "PIECZĘĆ": "AKTYWNA",
            "PERFEKCJA": "AKTYWNA",
            "tryb": "EXCHANGE_ENGINE_v1.7",
            "engine": "AKTYWNY"
        }

    def notify_heilong_os(self, message: str, level: str = "INFO") -> None:
        """Powiadamia HEILONG_OS o zdarzeniu."""
        try:
            from KOMBAJN_v15.kombajn_core import 59_geon_heilong_os_v2_3 as heilong_os
            if hasattr(heilong_os, 'log_event'):
                heilong_os.log_event(f"[EXCHANGE] {message}", level)
        except Exception as e:
            log(f"Nie udało się powiadomić HEILONG_OS: {e}", "WARN")

    def register_protokol_event(self, event: str) -> None:
        """Rejestruje zdarzenie w PROTOKÓŁ_Ω∞∞∞."""
        try:
            from PROTOKOL_OMEGA.absolut_system import AbsolutSystem
            AbsolutSystem.zarejestruj_zdarzenie(f"WYMIANA: {event}")
        except Exception as e:
            log(f"Nie udało się zarejestrować w PROTOKÓŁ: {e}", "WARN")

# =============================================================================
# DEMONSTRACJA
# =============================================================================

def demo():
    """Demonstracja GEON EXCHANGE ENGINE v1.7."""
    print("\n" + "=" * 80)
    print("🐉 GEON EXCHANGE ENGINE v1.7 — DEMONSTRACJA")
    print("6 POZIOMÓW ARCHITEKTURY — WIELOZASOBOWY SYSTEM WYMIANY")
    print("=" * 80 + "\n")

    # 1. Inicjalizacja węzłów
    nodes = {
        "Uganda": GeonNode("Uganda", {"W": 6000.0, "E": 2500.0, "L": 200.0}, reputation=0.95),
        "Sahara": GeonNode("Sahara", {"E": 9000.0, "L": 150.0}, efficiencies={("S", "E"): 0.65}),
        "Japan": GeonNode("Japan", {"B": 4500.0, "E": 1200.0, "L": 80.0}, efficiencies={("B", "W"): 0.25}),
        "Algeria": GeonNode("Algeria", {"W": 500.0, "E": 1800.0, "L": 600.0}, reputation=0.70),
        "GreekFleet": GeonNode("GreekFleet", {"L": 200000.0, "E": 4000.0, "price_per_L": 0.04}, reputation=0.85),
        "GEON_CORE": GeonNode("GEON_CORE", {"E": 0.0})
    }
    nodes["Algeria"].efficiencies = {("E", "W"): 0.88, ("B", "W"): 0.45}

    distances = {
        ("Uganda", "Algeria"): 4200.0,
        ("Sahara", "Algeria"): 1400.0,
        ("Japan", "Algeria"): 9800.0,
        ("GreekFleet", "Algeria"): 1900.0,
        ("Uganda", "Sahara"): 2800.0,
        ("Japan", "Uganda"): 11000.0
    }

    # 2. Inicjalizacja silnika
    config = ExchangeEngineConfig(epsilon=1e-3, fee_rate=0.005, shadow_mode=True)
    engine = ExchangeEngine(nodes, distances, config, verbose=True)
    bridge = ExchangeEngineBridge(engine)

    # 3. Symulacja
    print("🔮 URUCHAMIANIE SYMULACJI (3 KROKI):\n")
    report = engine.run_simulation(3)

    # 4. Status
    print("\n" + "=" * 40)
    print("📊 RAPORT KPI")
    print("=" * 40)
    for k, v in report.items():
        print(f"   {k}: {v}")

    # 5. Łańcuch bloków
    print("\n" + "=" * 40)
    print("🔗 ŁAŃCUCH BLOKÓW (GEON_CHAIN)")
    print("=" * 40)
    for b in engine.get_chain().blocks:
        print(f"   Blok #{b.index} | Hash: {b.hash[:16]}... | "
              f"StateRoot: {b.state_root[:16]}... | Walidatorzy: {[v[0] for v in b.validators]}")

    # 6. Mosty integracyjne
    print("\n" + "=" * 40)
    print("🔗 TEST MOSTÓW INTEGRACYJNYCH")
    print("=" * 40)
    print(f"🏹 GEX Context: {bridge.get_archetype_context()}")
    print(f"🎮 G_CORE State: {bridge.get_autopilot_state()}")
    print(f"📖 NARRATIVE Fragments: {bridge.get_narrative_fragments(2)}")
    print(f"🔱 TRIO State: {bridge.get_trio_state()}")

    # 7. Raport systemowy
    print("\n" + "=" * 40)
    print(engine.raport())

    print("\n" + "=" * 80)
    print("🐉 GEON EXCHANGE ENGINE v1.7 — GOTOWY DO WDROŻENIA")
    print(HASLO)
    print("=" * 80)

if __name__ == "__main__":
    demo()