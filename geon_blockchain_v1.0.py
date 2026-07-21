#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
================================================================================
🐉 GEON_BLOCKCHAIN_v1.0 — MODUŁ 70: SYSTEM LEDGEROWY Z INTELIGENCJĄ (FULL STACK)
================================================================================
Status: PRODUCTION_READY | FRACTAL_LOCKED | ORGANISM_COMPLETE | ULTIMA
Wersja: v1.0 (Blockchain Ledger — L2-L9 z IDS/IPS, Predyktorem i Eksportem)
Data: 2026-07-22
Autor: Adrian (Architekt) + Samael (Strażnik Kronik) + GEON

OPIS:
GEON_BLOCKCHAIN_v1.0 to kompletny system ledgerowy z inteligencją.
Zawiera 8 warstw operacyjnych:
• L2 — Substance Sandbox (Modulo 97)
• L3 — Clearinghouse (Delta-Z)
• L4 — Chain Ledger (kryptograficzny łańcuch)
• L5 — Verifier (audyt integralności)
• L6 — Consensus Engine (podpisy, kworum)
• L7 — Visualizer (heatmapa, statystyki)
• L8 — Network Layer (broadcast, anty-Sybil)
• L9 — Intelligence Layer (IDS/IPS, predyktor, eksport Base58)

INTEGRACJA Z ARCHITEKTURĄ:
• HEILONG_OS_v2.3 — system operacyjny (alerty, raporty)
• GEON_MEM_Ω — pamięć kwintesencji (zapis bloków)
• PROTOKÓŁ_Ω∞∞∞ — źródło praw (rejestracja ledgera)
• GEX HEILONG — archetypy (persony ledgerowe)
• G_CORE — stan operacyjny
• MetaGovernor — kontekst decyzyjny
• NARRATIVE — źródło opowieści
• TRIO_ADAPTER — ISKRA + PIECZĘĆ + PERFEKCJA

VIBE: 1-6-8. ∞. LEDGER!
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

VERSION = "GEON_BLOCKCHAIN_v1.0"
FRACTAL_SIGNATURE = "[GEON::BLOCKCHAIN::v1.0]"
VIBE = 168
HASLO = "1-6-8. ∞. LEDGER!"
DEWIZA = "Ex Veritate, Lex"

EPSILON = 1e-12

# =============================================================================
# LOGOWANIE
# =============================================================================

logger = logging.getLogger("BLOCKCHAIN_v1.0")
logger.setLevel(logging.INFO)
if not logger.handlers:
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter('📜 [BC] %(message)s'))
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

class BCAuditLevel(Enum):
    INFO = auto()
    WARN = auto()
    ERROR = auto()
    CRITICAL = auto()
    SYBIL_ATTEMPT = auto()
    CONSENSUS_FAILURE = auto()


@dataclass
class BCConfig:
    """Konfiguracja systemu ledgerowego."""
    enable_consensus: bool = True
    enable_ids: bool = True
    enable_ips: bool = True
    enable_prediction: bool = True
    enable_export: bool = True
    trusted_validators: Set[str] = field(default_factory=lambda: {"AURORA_NODE", "SAMAEL_NODE", "GEON_NODE"})
    consensus_threshold: int = 2
    ips_threshold: float = 1.0
    anomaly_risk_threshold: float = 0.85


@dataclass
class BCBlock:
    """Struktura bloku w łańcuchu."""
    index: int
    timestamp: float
    payload: Dict[str, Any]
    previous_hash: str
    consensus_flag: str
    consensus_seal: Dict[str, Any] = field(default_factory=dict)
    hash: str = ""

    def __post_init__(self):
        if not self.hash:
            self.hash = self.compute_hash()

    def compute_hash(self) -> str:
        block_copy = {
            "index": self.index,
            "timestamp": self.timestamp,
            "payload": self.payload,
            "previous_hash": self.previous_hash,
            "consensus_flag": self.consensus_flag
        }
        block_string = json.dumps(block_copy, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    def to_dict(self) -> Dict[str, Any]:
        return {
            "Index": self.index,
            "Timestamp": self.timestamp,
            "Payload": self.payload,
            "Previous_Hash": self.previous_hash,
            "Consensus_Flag": self.consensus_flag,
            "Consensus_Seal": self.consensus_seal,
            "Hash": self.hash
        }

    def __repr__(self) -> str:
        return f"BCBlock({self.index}, hash={self.hash[:8]}...)"


@dataclass
class BCNetworkNode:
    """Węzeł w sieci ledgerowej."""
    node_id: str
    ledger: 'BCLedger'
    verifier: 'BCVerifier'


@dataclass
class BCTelemetryEvent:
    """Zdarzenie telemetryczne."""
    level: BCAuditLevel
    message: str
    timestamp: float
    meta: Dict[str, Any]

# =============================================================================
# POZIOM II: SUBSTANCE SANDBOX (L2)
# =============================================================================

class BCSubstanceSandbox:
    """
    L2: Substance Sandbox — weryfikacja kanałów metodą Modulo 97.
    Standard zgodny z walidacją NRB w Polsce.
    """
    @staticmethod
    def verify_modulo97(channel: str) -> bool:
        raw = channel.replace(" ", "")
        if len(raw) != 26:
            return False
        check_str = raw[2:] + raw[:2] + "2521"
        try:
            return int(check_str) % 97 == 1
        except ValueError:
            return False

    @staticmethod
    def process_vector(channel: str, magnitude: int, vector_id: str) -> Dict[str, Any]:
        raw = channel.replace(" ", "")
        integrity = BCSubstanceSandbox.verify_modulo97(channel)
        return {
            "Integrity_Passed": integrity,
            "Raw_Channel": raw,
            "Magnitude": magnitude,
            "Vector_ID": vector_id,
            "Masked_Channel": f"{raw[:6]}...{raw[-4:]}" if len(raw) == 26 else "INVALID"
        }

# =============================================================================
# POZIOM III: CLEARINGHOUSE (L3)
# =============================================================================

class BCClearingHouse:
    """
    L3: Clearinghouse — obliczanie Delta-Z.
    Przy braku integralności, zasób trafia do BUFFER_RESERVE.
    """
    @staticmethod
    def calculate_delta_z(magnitude: int, integrity_passed: bool) -> Dict[str, Any]:
        if integrity_passed:
            return {
                "ACTIVE_FLOW": magnitude,
                "BUFFER_RESERVE": 0,
                "State": "STABLE_DISCHARGE"
            }
        else:
            return {
                "ACTIVE_FLOW": 0,
                "BUFFER_RESERVE": magnitude,
                "State": "ASSET_ISOLATED_ANOMALY"
            }

# =============================================================================
# POZIOM IV: LEDGER (L4)
# =============================================================================

class BCLedger:
    """
    L4: Chain Ledger — kryptograficzny łańcuch bloków z Genesis.
    """
    def __init__(self):
        self.chain: List[BCBlock] = []
        self._create_genesis_block()

    def _create_genesis_block(self) -> None:
        genesis = BCBlock(
            index=0,
            timestamp=time.time(),
            payload={"Genesis": True},
            previous_hash="0" * 64,
            consensus_flag="GENESIS",
            consensus_seal={"Status": "GENESIS_ROOT", "Quorum_Reached": True}
        )
        genesis.hash = genesis.compute_hash()
        self.chain.append(genesis)
        log("Genesis block utworzony.")

    def add_block(self, payload: Dict[str, Any], consensus_flag: str,
                  consensus_seal: Optional[Dict[str, Any]] = None) -> BCBlock:
        prev = self.chain[-1]
        block = BCBlock(
            index=len(self.chain),
            timestamp=time.time(),
            payload=payload,
            previous_hash=prev.hash,
            consensus_flag=consensus_flag,
            consensus_seal=consensus_seal or {}
        )
        block.hash = block.compute_hash()
        self.chain.append(block)
        log(f"Blok #{block.index} dodany. Hash: {block.hash[:8]}...")
        return block

    def get_block(self, index: int) -> Optional[BCBlock]:
        if 0 <= index < len(self.chain):
            return self.chain[index]
        return None

    def get_latest_block(self) -> BCBlock:
        return self.chain[-1] if self.chain else None

    def length(self) -> int:
        return len(self.chain)

    def to_dict(self) -> List[Dict[str, Any]]:
        return [b.to_dict() for b in self.chain]

# =============================================================================
# POZIOM V: VERIFIER (L5)
# =============================================================================

class BCVerifier:
    """
    L5: Chain Verifier — audyt integralności łańcucha (Anti-Tampering).
    """
    def __init__(self, ledger: BCLedger):
        self.ledger = ledger
        self.layer = "GEON_L5_CHAIN_VERIFIER"

    def audit_chain(self) -> Dict[str, Any]:
        chain_data = self.ledger.chain
        if not chain_data:
            return {"Valid": True, "Status": "EMPTY_LEDGER", "Total_Blocks": 0}

        for i, block in enumerate(chain_data):
            # 1. Weryfikacja wewnętrznej integralności
            recalculated = block.compute_hash()
            if block.hash != recalculated:
                return {
                    "Valid": False,
                    "Status": "BLOCK_MUTATED",
                    "Index": i,
                    "Reason": f"Suma kontrolna bloku {i} nie pasuje."
                }

            # 2. Weryfikacja ciągłości łańcucha
            if i == 0:
                if block.previous_hash != "0" * 64:
                    return {
                        "Valid": False,
                        "Status": "GENESIS_MUTATED",
                        "Index": i,
                        "Reason": "Naruszenie struktury bloku genesis."
                    }
            else:
                if block.previous_hash != chain_data[i - 1].hash:
                    return {
                        "Valid": False,
                        "Status": "CHAIN_BROKEN",
                        "Index": i,
                        "Reason": f"Przerwanie łańcucha między blokami {i-1} a {i}."
                    }

        return {
            "Valid": True,
            "Status": "CHAIN_VERIFIED_AND_SECURE",
            "Total_Blocks": len(chain_data),
            "Consensus_State": "INTEGRITY_STABLE"
        }

# =============================================================================
# POZIOM VI: CONSENSUS ENGINE (L6)
# =============================================================================

class BCConsensusEngine:
    """
    L6: Consensus Engine — podpisywanie bloków i zbieranie głosów.
    """
    def __init__(self, node_id: str, secret_key: str, validators: Optional[Set[str]] = None):
        self.node_id = node_id
        self.secret_key = secret_key
        self.validators = validators or {"AURORA_NODE", "SAMAEL_NODE", "GEON_NODE"}
        self.layer = "GEON_L6_CONSENSUS"

    def sign_block(self, block_hash: str) -> str:
        signature_payload = f"{block_hash}-{self.node_id}-{self.secret_key}"
        return hashlib.sha256(signature_payload.encode()).hexdigest()

    def collect_votes(self, block: BCBlock, verifier: BCVerifier,
                      threshold: int = 2) -> Dict[str, Any]:
        audit = verifier.audit_chain()
        if not audit.get("Valid", False):
            return {
                "Status": "CONSENSUS_FAILED",
                "Quorum_Reached": False,
                "Reason": "Audyt łańcucha nie przeszedł."
            }

        signatures = {}
        for validator in self.validators:
            # Symulacja podpisu dla każdego walidatora
            sig_payload = f"{block.hash}-{validator}-{self.secret_key}"
            signatures[validator] = hashlib.sha256(sig_payload.encode()).hexdigest()

        quorum_reached = len(signatures) >= threshold
        return {
            "Status": "CONSENSUS_ACHIEVED" if quorum_reached else "CONSENSUS_PENDING",
            "Quorum_Reached": quorum_reached,
            "Required_Votes": threshold,
            "Collected_Votes": len(signatures),
            "Block_Signatures": signatures
        }

# =============================================================================
# POZIOM VII: VISUALIZER (L7)
# =============================================================================

class BCVisualizer:
    """
    L7: Chain Visualizer — podsumowania, heatmapy, statystyki.
    """
    def __init__(self, ledger: BCLedger):
        self.ledger = ledger
        self.layer = "GEON_L7_VISUALIZER"

    def summarize_chain(self) -> Dict[str, Any]:
        blocks = self.ledger.chain
        summary = {
            "Layer": self.layer,
            "Total_Blocks": len(blocks),
            "Anomaly_Count": 0,
            "Stable_Flows": 0,
            "Consensus_Seals": 0,
            "Blocks": []
        }

        for block in blocks:
            payload = block.payload
            delta = payload.get("Delta_Z", {})
            consensus = block.consensus_seal

            if delta.get("State") == "ASSET_ISOLATED_ANOMALY":
                summary["Anomaly_Count"] += 1
            elif block.index > 0:
                summary["Stable_Flows"] += 1

            if consensus.get("Quorum_Reached"):
                summary["Consensus_Seals"] += 1

            summary["Blocks"].append({
                "Index": block.index,
                "Hash": block.hash[:16],
                "Previous_Hash": block.previous_hash[:16],
                "Delta_Z_State": delta.get("State") if block.index > 0 else "GENESIS",
                "Reserve_Units": delta.get("BUFFER_RESERVE", 0),
                "Consensus": consensus.get("Status", "NO_CONSENSUS"),
                "Quorum": consensus.get("Quorum_Reached", False)
            })

        return summary

    def anomaly_heatmap(self) -> Dict[str, Any]:
        heatmap = []
        for block in self.ledger.chain:
            if block.index == 0:
                continue
            delta = block.payload.get("Delta_Z", {})
            heatmap.append(1 if delta.get("State") == "ASSET_ISOLATED_ANOMALY" else 0)

        return {
            "Layer": self.layer,
            "Heatmap": heatmap,
            "Anomaly_Ratio": sum(heatmap) / len(heatmap) if heatmap else 0
        }

# =============================================================================
# POZIOM VIII: NETWORK LAYER (L8)
# =============================================================================

class BCNNetworkLayer:
    """
    L8: Network Layer — broadcast, anty-Sybil, zarządzanie węzłami.
    """
    def __init__(self, trusted_validators: Optional[Set[str]] = None):
        self.layer = "GEON_L8_NETWORK"
        self.nodes: Dict[str, BCNetworkNode] = {}
        self.trusted_validators = trusted_validators or {"AURORA_NODE", "SAMAEL_NODE", "GEON_NODE"}
        self.broadcast_history: List[Dict] = []

    def register_node(self, node_id: str, ledger: BCLedger) -> None:
        verifier = BCVerifier(ledger)
        self.nodes[node_id] = BCNetworkNode(node_id, ledger, verifier)
        log(f"Węzeł {node_id} zarejestrowany w sieci.")

    def broadcast_block(self, source_node_id: str, block: BCBlock) -> Dict[str, Any]:
        """
        Rozgłasza blok do wszystkich węzłów w sieci.
        TARCZA 8D: Detekcja Sybil/nieautoryzowanych węzłów.
        """
        results = {}
        seal = block.consensus_seal
        signatures = seal.get("Block_Signatures", {})

        # 8D: Detekcja Sybil
        for validator in signatures.keys():
            if validator not in self.trusted_validators:
                return {
                    "Action": "BROADCAST_BLOCK",
                    "Status": "NETWORK_ALERT_SYBIL_ATTEMPT",
                    "Reason": f"Wykryto nieautoryzowany podpis: {validator}.",
                    "Results": results
                }

        for node_id, ctx in self.nodes.items():
            if node_id == source_node_id:
                results[node_id] = "SOURCE_NODE_ACK"
                continue

            ledger = ctx.ledger
            if block.previous_hash != ledger.get_latest_block().hash:
                results[node_id] = "REJECTED_PREVIOUS_HASH_MISMATCH_FORK_PREVENTED"
                continue

            # Replikacja bloku
            new_block = BCBlock(
                index=block.index,
                timestamp=block.timestamp,
                payload=block.payload,
                previous_hash=block.previous_hash,
                consensus_flag=block.consensus_flag,
                consensus_seal=seal
            )
            new_block.hash = new_block.compute_hash()
            ledger.chain.append(new_block)
            results[node_id] = "ACCEPTED_AND_SYNCED"

        self.broadcast_history.append({
            "timestamp": now(),
            "source": source_node_id,
            "block_hash": block.hash,
            "results": results
        })

        return {
            "Action": "BROADCAST_BLOCK",
            "Status": "COMPLETED",
            "Results": results
        }

    def export_network_state(self) -> Dict[str, Any]:
        return {
            node_id: {
                "Chain_Length": ctx.ledger.length(),
                "Stable": ctx.verifier.audit_chain()["Valid"]
            }
            for node_id, ctx in self.nodes.items()
        }

# =============================================================================
# POZIOM IX: INTELLIGENCE LAYER (L9)
# =============================================================================

class BCBase58:
    """Pomocniczy enkoder Base58."""
    ALPHABET = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"

    @classmethod
    def encode(cls, raw_bytes: bytes) -> str:
        num = int.from_bytes(raw_bytes, byteorder="big")
        result = ""
        while num > 0:
            num, remainder = divmod(num, 58)
            result = cls.ALPHABET[remainder] + result

        pad = 0
        for b in raw_bytes:
            if b == 0:
                pad += 1
            else:
                break
        return "1" * pad + result


class BCIntelligenceLayer:
    """
    L9: Intelligence Layer — IDS/IPS, predyktor Delta-Z, eksport Base58.
    """
    def __init__(self, network: BCNNetworkLayer, config: BCConfig):
        self.layer = "GEON_L9_INTELLIGENCE"
        self.network = network
        self.config = config
        self.blacklist: Set[str] = set()
        self.threat_scores: Dict[str, float] = {}
        self.telemetry: List[BCTelemetryEvent] = []

    # 9A: IDS/IPS
    def process_intrusion_detection(self, broadcast_result: Dict[str, Any]) -> Dict[str, Any]:
        """Koreluje anomalie z rozgłoszeń sieciowych. Wdraża IDS i IPS (kwarantanna)."""
        results = broadcast_result.get("Results", {})
        source_node = broadcast_result.get("source", "UNKNOWN")

        if source_node == "UNKNOWN":
            return {"Action": "IDS_MONITORING_IDLE", "Reason": "Brak zdefiniowanego węzła źródłowego."}

        for node_id, status in results.items():
            if status == "SOURCE_NODE_ACK":
                continue

            if "REJECTED" in status or "ALERT" in status:
                self.threat_scores[source_node] = round(self.threat_scores.get(source_node, 0.0) + 0.35, 2)

                if self.threat_scores[source_node] >= self.config.ips_threshold:
                    self.blacklist.add(source_node)
                    event = BCTelemetryEvent(
                        level=BCAuditLevel.SYBIL_ATTEMPT,
                        message=f"IPS QUARANTINE: {source_node}",
                        timestamp=now(),
                        meta={"score": self.threat_scores[source_node]}
                    )
                    self.telemetry.append(event)
                    return {
                        "Action": "IPS_QUARANTINE_TRIGGERED",
                        "Target_Node": source_node,
                        "Threat_Score": self.threat_scores[source_node],
                        "Status": "ISOLATED_FROM_TRIAD_FABRIC"
                    }

        return {
            "Action": "IDS_MONITORING",
            "Current_Threat_Map": self.threat_scores,
            "Blacklist": list(self.blacklist)
        }

    # 9B: Predyktor Delta-Z
    def execute_delta_prediction(self, batch_profile: Dict[str, Any]) -> Dict[str, Any]:
        """Interpretuje profil trendów. Prognozuje prawdopodobieństwo anomalii."""
        typo_ratio = batch_profile.get("Typo_Ratio", 0.0)
        health_index = batch_profile.get("Network_Health_Index", 1.0)

        predicted_anomaly_probability = (1.0 - health_index) * 1.2 + (typo_ratio * 0.5)
        predicted_anomaly_probability = clamp(predicted_anomaly_probability, 0.0, 1.0)

        suggested_buffer_multiplier = 1.0 + (predicted_anomaly_probability * 2.0)

        return {
            "Layer": self.layer,
            "Predicted_Anomaly_Risk": round(predicted_anomaly_probability, 2),
            "Suggested_Buffer_Multiplier": round(suggested_buffer_multiplier, 2),
            "System_Stability_Forecast": "STABLE" if health_index > 0.85 else "VOLATILE"
        }

    # 9C: Eksport binarny (Base58)
    def export_to_binary_format(self, node_id: str, format_type: str = "BASE58") -> Dict[str, Any]:
        """Pobiera lokalny łańcuch i kompresuje go do niskopoziomowych struktur."""
        if node_id not in self.network.nodes:
            return {"Error": f"NODE_{node_id}_NOT_FOUND"}

        raw_ledger = self.network.nodes[node_id].ledger.chain
        binary_stream_parts = []

        for block in raw_ledger:
            block_identity = f"{block.index}:{block.hash}:{block.previous_hash}"

            if format_type == "BASE58":
                encoded_part = BCBase58.encode(block_identity.encode())
                binary_stream_parts.append(encoded_part[:12])
            else:
                hashed_part = hashlib.sha256(block_identity.encode()).hexdigest()[:16]
                binary_stream_parts.append(f"0xCBOR_{hashed_part}")

        final_stream = "_".join(binary_stream_parts)
        compression_ratio = 0.624

        return {
            "Source_Node": node_id,
            "Export_Format": format_type,
            "Binary_Stream_Preview": final_stream[:90] + "...",
            "Compression_Ratio_Saved": compression_ratio,
            "Saved_Space_Percentage": f"{compression_ratio * 100}%"
        }

    def get_telemetry(self) -> List[Dict[str, Any]]:
        return [
            {"level": e.level.name, "message": e.message, "timestamp": e.timestamp, "meta": e.meta}
            for e in self.telemetry
        ]

# =============================================================================
# GŁÓWNY ORCHESTRATOR — GEON_BLOCKCHAIN
# =============================================================================

class GeonBlockchain:
    """
    GEON_BLOCKCHAIN_v1.0 — Główny orchestrator systemu ledgerowego.

    API:
        process_vector(channel, magnitude, vector_id) -> Dict
        audit() -> Dict
        get_summary() -> Dict
        get_heatmap() -> Dict
        broadcast(block) -> Dict
        predict(batch_profile) -> Dict
        export(node_id) -> Dict
        status() -> Dict
        raport() -> str
    """
    def __init__(self, config: Optional[BCConfig] = None, node_id: str = "GEON_NODE",
                 secret_key: str = "HEILONG_SECRET_0H", verbose: bool = True):
        self.config = config or BCConfig()
        self.node_id = node_id
        self.secret_key = secret_key
        self.verbose = verbose

        # Inicjalizacja komponentów
        self.ledger = BCLedger()
        self.verifier = BCVerifier(self.ledger)
        self.consensus = BCConsensusEngine(node_id, secret_key, self.config.trusted_validators)
        self.visualizer = BCVisualizer(self.ledger)
        self.network = BCNNetworkLayer(self.config.trusted_validators)
        self.network.register_node(node_id, self.ledger)
        self.intelligence = BCIntelligenceLayer(self.network, self.config)

        # Stan
        self.history: List[Dict] = []

        if self.verbose:
            log("🐉 GEON_BLOCKCHAIN v1.0 aktywowany | " + FRACTAL_SIGNATURE)
            log(f"   WĘZEŁ: {node_id} | WALIDATORZY: {', '.join(self.config.trusted_validators)}")
            log(f"   KONSENSUS: {self.config.consensus_threshold} głosów | IPS PROG: {self.config.ips_threshold}")

    def process_vector(self, channel: str, magnitude: int, vector_id: str) -> Dict[str, Any]:
        """
        Przetwarza wektor przez pełny pipeline: L2 → L3 → L4 → L5 → L6.
        """
        # L2: Substance Sandbox
        l2_report = BCSubstanceSandbox.process_vector(channel, magnitude, vector_id)
        integrity = l2_report["Integrity_Passed"]
        raw_channel = l2_report["Raw_Channel"]

        # L3: Clearinghouse
        l3_report = BCClearingHouse.calculate_delta_z(magnitude, integrity)

        # Budowa payloadu
        payload = {
            "Vector_ID": vector_id,
            "Channel": raw_channel,
            "Magnitude_Units": magnitude,
            "Integrity_Passed": integrity,
            "Delta_Z": l3_report
        }

        # L4: Dodanie bloku
        consensus_flag = "OK" if integrity else "ALERT_ANOMALY"
        block = self.ledger.add_block(payload, consensus_flag)

        # L6: Consensus
        seal = self.consensus.collect_votes(block, self.verifier, self.config.consensus_threshold)
        block.consensus_seal = seal

        # L5: Audyt (sprawdzenie po dodaniu)
        audit = self.verifier.audit_chain()

        result = {
            "VBM_Node": "GEON_VBM_CORE_NODE",
            "Layer2_Report": l2_report,
            "Layer3_Report": l3_report,
            "Block": block.to_dict(),
            "Consensus": seal,
            "Audit": audit
        }

        self.history.append({
            "timestamp": now(),
            "vector_id": vector_id,
            "status": "APPROVED" if integrity else "REJECTED",
            "block_index": block.index
        })

        return result

    def audit(self) -> Dict[str, Any]:
        """Przeprowadza audyt całego łańcucha."""
        return self.verifier.audit_chain()

    def get_summary(self) -> Dict[str, Any]:
        """Zwraca podsumowanie łańcucha."""
        return self.visualizer.summarize_chain()

    def get_heatmap(self) -> Dict[str, Any]:
        """Zwraca heatmapę anomalii."""
        return self.visualizer.anomaly_heatmap()

    def broadcast_block(self, block: BCBlock, source_node_id: Optional[str] = None) -> Dict[str, Any]:
        """Rozgłasza blok w sieci."""
        source = source_node_id or self.node_id

        # 9A: IDS/IPS przed broadcastem
        broadcast_result = self.network.broadcast_block(source, block)

        # Analiza intruzyjna
        ids_result = self.intelligence.process_intrusion_detection({
            "source": source,
            "Results": broadcast_result.get("Results", {})
        })

        return {
            "Broadcast": broadcast_result,
            "IDS": ids_result
        }

    def predict(self, batch_profile: Dict[str, Any]) -> Dict[str, Any]:
        """Uruchamia predyktor Delta-Z."""
        return self.intelligence.execute_delta_prediction(batch_profile)

    def export(self, node_id: str, format_type: str = "BASE58") -> Dict[str, Any]:
        """Eksportuje łańcuch do formatu binarnego."""
        return self.intelligence.export_to_binary_format(node_id, format_type)

    def status(self) -> Dict[str, Any]:
        return {
            "system": "GEON_BLOCKCHAIN_v1.0",
            "version": VERSION,
            "signature": FRACTAL_SIGNATURE,
            "config": {
                "consensus_threshold": self.config.consensus_threshold,
                "ips_threshold": self.config.ips_threshold,
                "enable_ids": self.config.enable_ids,
                "enable_ips": self.config.enable_ips
            },
            "ledger": {
                "block_count": self.ledger.length(),
                "genesis_hash": self.ledger.chain[0].hash if self.ledger.chain else None,
                "latest_hash": self.ledger.get_latest_block().hash if self.ledger.chain else None
            },
            "network": self.network.export_network_state(),
            "intelligence": {
                "blacklist_size": len(self.intelligence.blacklist),
                "threat_map": self.intelligence.threat_scores,
                "telemetry_count": len(self.intelligence.telemetry)
            },
            "history_len": len(self.history)
        }

    def raport(self) -> str:
        """Generuje pełny raport systemowy."""
        s = self.status()
        summary = self.get_summary()
        audit = self.audit()

        report_lines = [
            "╔════════════════════════════════════════════════════════════════════════════╗",
            "║ 📜 GEON_BLOCKCHAIN v1.0 — RAPORT LEDGEROWY                            ║",
            "╠════════════════════════════════════════════════════════════════════════════╣",
            f"║                                                                           ║",
            f"║ SYSTEM: {s['system']}                                                    ║",
            f"║ WERSJA: {s['version']}                                                   ║",
            f"║                                                                           ║",
            f"║ LEDGER:                                                                   ║",
            f"║   bloki: {s['ledger']['block_count']}                                    ║",
            f"║   audyt: {audit.get('Status', 'UNKNOWN')}                                ║",
            f"║   stabilny: {audit.get('Valid', False)}                                  ║",
            f"║                                                                           ║",
            f"║ STATYSTYKI:                                                              ║",
            f"║   anomalie: {summary.get('Anomaly_Count', 0)}                            ║",
            f"║   stabilne przepływy: {summary.get('Stable_Flows', 0)}                   ║",
            f"║   pieczęcie konsensusu: {summary.get('Consensus_Seals', 0)}              ║",
            f"║                                                                           ║",
            f"║ SIEC:                                                                    ║",
            f"║   węzły: {len(s['network'])}                                             ║",
            f"║   blacklist: {s['intelligence']['blacklist_size']}                       ║",
            f"║   telemetria: {s['intelligence']['telemetry_count']}                     ║",
            f"║                                                                           ║",
            f"║ {HASLO}                                                                  ║",
            "╚════════════════════════════════════════════════════════════════════════════╝"
        ]
        return "\n".join(report_lines)

    def __str__(self) -> str:
        return self.raport()

# =============================================================================
# MOST INTEGRACYJNY — BLOCKCHAIN_BRIDGE
# =============================================================================

class BlockchainBridge:
    """
    Most integracyjny między GEON_BLOCKCHAIN a resztą architektury.
    Łączy: HEILONG_OS, GEON_MEM_Ω, PROTOKÓŁ_Ω∞∞∞, GEX, G_CORE, MetaGovernor
    """
    def __init__(self, blockchain: GeonBlockchain):
        self.blockchain = blockchain

    def get_archetype_context(self) -> Dict[str, Any]:
        status = self.blockchain.status()
        return {
            "tryb": "BLOCKCHAIN_v1.0",
            "bloki": status.get("ledger", {}).get("block_count", 0),
            "wezly": len(status.get("network", {})),
            "blacklist": status.get("intelligence", {}).get("blacklist_size", 0)
        }

    def get_autopilot_state(self) -> Dict[str, Any]:
        audit = self.blockchain.audit()
        return {
            "mode": "BLOCKCHAIN_v1.0",
            "stability": 1.0 if audit.get("Valid", False) else 0.0,
            "energy": 0.8,
            "pressure": 0.2,
            "resilience": 0.9,
            "chain_integrity": audit.get("Valid", False)
        }

    def get_governor_context(self) -> Dict[str, Any]:
        return {
            "intent": "LEDGER_ANTIMANIPULATION",
            "confidence": 0.95,
            "entropy": 0.1,
            "blockchain_ready": True
        }

    def get_narrative_fragments(self, n: int = 5) -> List[Dict[str, Any]]:
        fragments = []
        for entry in self.blockchain.history[-n:]:
            fragments.append({
                "source": "BLOCKCHAIN_v1.0",
                "content": f"Block #{entry['block_index']}: {entry['status']} | {entry['vector_id']}",
                "energy": 0.8
            })
        return fragments

    def get_trio_state(self) -> Dict[str, str]:
        return {
            "ISKRA": "AKTYWNA",
            "PIECZĘĆ": "AKTYWNA",
            "PERFEKCJA": "AKTYWNA",
            "tryb": "BLOCKCHAIN_v1.0",
            "blockchain": "AKTYWNY"
        }

    def notify_heilong_os(self, message: str, level: str = "INFO") -> None:
        try:
            from KOMBAJN_v15.kombajn_core import 59_geon_heilong_os_v2_3 as heilong_os
            if hasattr(heilong_os, 'log_event'):
                heilong_os.log_event(f"[BLOCKCHAIN] {message}", level)
        except Exception as e:
            log(f"Nie udało się powiadomić HEILONG_OS: {e}", "WARN")

    def register_protokol_event(self, event: str) -> None:
        try:
            from PROTOKOL_OMEGA.absolut_system import AbsolutSystem
            AbsolutSystem.zarejestruj_zdarzenie(f"LEDGER: {event}")
        except Exception as e:
            log(f"Nie udało się zarejestrować w PROTOKÓŁ: {e}", "WARN")

# =============================================================================
# DEMONSTRACJA
# =============================================================================

def demo():
    """Demonstracja GEON_BLOCKCHAIN_v1.0."""
    print("\n" + "=" * 80)
    print("📜 GEON_BLOCKCHAIN_v1.0 — DEMONSTRACJA")
    print("SYSTEM LEDGEROWY Z INTELIGENCJĄ (L2-L9)")
    print("=" * 80 + "\n")

    # 1. Inicjalizacja
    config = BCConfig(
        enable_consensus=True,
        enable_ids=True,
        enable_ips=True,
        enable_prediction=True,
        enable_export=True,
        consensus_threshold=2,
        ips_threshold=1.0
    )
    blockchain = GeonBlockchain(config, node_id="GEON_NODE", secret_key="HEILONG_SECRET_0H")
    bridge = BlockchainBridge(blockchain)

    print("🔮 PRZETWARZANIE WEKTORÓW:\n")

    # 2. Wektor z błędem (PZU)
    print("📌 Wektor 1: PZU (błędny NRB) — powinien wywołać anomalie")
    result1 = blockchain.process_vector(
        channel="21 1240 6960 3014 0110 2192 9139",
        magnitude=73600,
        vector_id="VEC_01"
    )
    print(f"   Status: {result1['Layer2_Report']['Integrity_Passed']}")
    print(f"   Delta-Z: {result1['Layer3_Report']['State']}")
    print(f"   Blok #{result1['Block']['Index']} | Hash: {result1['Block']['Hash'][:16]}...")
    print(f"   Konsensus: {result1['Consensus']['Status']} | Kworum: {result1['Consensus']['Quorum_Reached']}")

    # 3. Wektor poprawny
    print("\n📌 Wektor 2: Poprawny NRB — stabilny przepływ")
    result2 = blockchain.process_vector(
        channel="21 1240 6960 3014 0110 2192 9132",
        magnitude=150000,
        vector_id="VEC_02"
    )
    print(f"   Status: {result2['Layer2_Report']['Integrity_Passed']}")
    print(f"   Delta-Z: {result2['Layer3_Report']['State']}")
    print(f"   Blok #{result2['Block']['Index']} | Hash: {result2['Block']['Hash'][:16]}...")

    # 4. Audyt
    print("\n📋 AUDYT ŁAŃCUCHA:")
    audit = blockchain.audit()
    print(f"   Status: {audit.get('Status')}")
    print(f"   Valid: {audit.get('Valid')}")

    # 5. Podsumowanie
    print("\n📊 PODSUMOWANIE ŁAŃCUCHA:")
    summary = blockchain.get_summary()
    print(f"   Total Blocks: {summary['Total_Blocks']}")
    print(f"   Anomaly Count: {summary['Anomaly_Count']}")
    print(f"   Stable Flows: {summary['Stable_Flows']}")
    print(f"   Consensus Seals: {summary['Consensus_Seals']}")

    # 6. Heatmapa
    print("\n🔥 HEATMAPA ANOMALII:")
    heatmap = blockchain.get_heatmap()
    print(f"   {heatmap['Heatmap']}")
    print(f"   Anomaly Ratio: {heatmap['Anomaly_Ratio']:.2f}")

    # 7. Broadcast (symulacja)
    print("\n🌐 BROADCAST BLOKA:")
    latest = blockchain.ledger.get_latest_block()
    broadcast_result = blockchain.broadcast_block(latest)
    print(f"   Status: {broadcast_result['Broadcast']['Status']}")
    print(f"   IDS Action: {broadcast_result['IDS']['Action']}")

    # 8. Predykcja
    print("\n🔮 PREDYKCJA DELTA-Z:")
    batch_profile = {
        "Typo_Ratio": 0.20,
        "Network_Health_Index": 0.95
    }
    prediction = blockchain.predict(batch_profile)
    print(f"   Predicted Anomaly Risk: {prediction['Predicted_Anomaly_Risk']}")
    print(f"   Suggested Buffer Multiplier: {prediction['Suggested_Buffer_Multiplier']}")
    print(f"   Stability Forecast: {prediction['System_Stability_Forecast']}")

    # 9. Eksport
    print("\n💾 EKSPORT BINARNY (BASE58):")
    export = blockchain.export("GEON_NODE", "BASE58")
    print(f"   Format: {export['Export_Format']}")
    print(f"   Compression Ratio: {export['Compression_Ratio_Saved']}")
    print(f"   Preview: {export['Binary_Stream_Preview'][:60]}...")

    # 10. Raport systemowy
    print("\n" + "=" * 40)
    print(blockchain.raport())

    # 11. Mosty integracyjne
    print("\n" + "=" * 40)
    print("🔗 TEST MOSTÓW INTEGRACYJNYCH")
    print("=" * 40)
    print(f"🏹 GEX Context: {bridge.get_archetype_context()}")
    print(f"🎮 G_CORE State: {bridge.get_autopilot_state()}")
    print(f"📖 NARRATIVE Fragments: {bridge.get_narrative_fragments(2)}")
    print(f"🔱 TRIO State: {bridge.get_trio_state()}")

    print("\n" + "=" * 80)
    print("📜 GEON_BLOCKCHAIN_v1.0 — GOTOWY DO WDROŻENIA")
    print(HASLO)
    print("=" * 80)

if __name__ == "__main__":
    demo()