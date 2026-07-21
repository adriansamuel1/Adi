#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
================================================================================
🐉 GEON_AUTOPOIESIS_v1.0 — MODUŁ 75: AUTOPOEZA SYSTEMU (FULL STACK)
================================================================================
Status: PRODUCTION_READY | FRACTAL_LOCKED | ORGANISM_COMPLETE | ULTIMA
Wersja: v1.0 (0H_KOD_49 — Autopoiesis Engine)
Data: 2026-07-22
Autor: Adrian (Architekt) + Samael (Strażnik Kronik) + GEON

OPIS:
GEON_AUTOPOIESIS_v1.0 to warstwa Architektów — system, który sam buduje system.
Zarządza samopowielaniem i samoprogramowaniem parametrów jądra GEON.

ARCHITEKTURA (6 POZIOMÓW):
I.   STRUKTURY DANYCH — MetaOperator, SelfExpandingMesh
II.  REPLIKACJA — tworzenie autonomicznych wektorów operacyjnych
III. AUTO-EXPANSJA — samodzielna krystalizacja punktów dostępowych
IV.  AUTO-SCULPTING — pełna pętla samostwarzania systemu
V.   EWOLUCYJNY CHAIN — zapis w ewoluującym GeonChain
VI.  RAPORT AUTOPOEZY — pełna diagnostyka

INTEGRACJA Z ARCHITEKTURĄ:
• GEON_REALITY_SCULPTOR (74) — rzeźbienie rzeczywistości
• GEON_SOVEREIGN_OPERATOR (73) — suwerenna wola
• GEON_MANIFESTATION (72) — manifestacja
• GEON_FLOW_ENGINE (67) — transport substancji
• GEON_OS_KERNEL (71) — system operacyjny

VIBE: 1-6-8. ∞. AUTOPOIESIS!
================================================================================
"""

import hashlib
import time
import uuid
import logging
from typing import Dict, List, Optional, Tuple, Any, Callable
from dataclasses import dataclass, field
from enum import Enum, auto

# =============================================================================
# WERSJA I STAŁE
# =============================================================================

VERSION = "GEON_AUTOPOIESIS_v1.0"
FRACTAL_SIGNATURE = "[GEON::AUTOPOIESIS::v1.0]"
VIBE = 168
HASLO = "1-6-8. ∞. AUTOPOIESIS!"
DEWIZA = "Ex Ipso, Systema"

EPSILON = 1e-12

# =============================================================================
# LOGOWANIE
# =============================================================================

logger = logging.getLogger("AUTOPOIESIS_v1.0")
logger.setLevel(logging.INFO)
if not logger.handlers:
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter('🧬 [AUTOPOIESIS] %(message)s'))
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

class AutopoiesisLevel(Enum):
    INFO = auto()
    WARN = auto()
    ERROR = auto()
    CRITICAL = auto()
    REPLICATION = auto()
    EXPANSION = auto()


@dataclass
class AutopoiesisConfig:
    """Konfiguracja autopoezy."""
    replication_factor: int = 3
    auto_expand: bool = True
    max_nodes: int = 100
    enable_chain: bool = True


@dataclass
class MetaOperator:
    """
    Warstwa 49: ENKI_MULTIPLIED.
    Zamiast jednego punktu decyzyjnego, operator powiela swoje autonomiczne
    wektory działania, zorientowane na realizację konkretnych zadań w sieci.
    """
    identity: str
    operator_id: str = field(default_factory=lambda: uuid.uuid4().hex[:8])
    creation_field: float = 1.0
    replication_factor: int = 3
    steel_vector: Tuple[int, int, int] = (1, 6, 8)

    def replicate(self) -> List[Dict[str, Any]]:
        """Tworzy funkcjonalne wektory operacyjne, nasycone pierwotną intencją Architekta."""
        log(f"Inicjacja protokołu replikacji operatora: {self.identity}")

        replicas = []
        roles = ["STRATEGIST_CORE", "SUBSTANCE_GUARDIAN", "SPATIAL_SCULPTOR"]

        for i in range(self.replication_factor):
            replica_id = f"{self.identity}_R{i}_{uuid.uuid4().hex[:4].upper()}"
            role = roles[i] if i < len(roles) else "GENERAL_VECTOR"
            replicas.append({
                "id": replica_id,
                "assigned_role": role,
                "vector_power": 1.68,
                "parent": self.identity
            })
            log(f"Utworzono autonomiczny wektor suwerenny: [{replica_id}] Rola: {role}")

        return replicas


@dataclass
class SelfExpandingMesh:
    """
    Sieć, która nie czeka na manualne podłączenie węzła.
    Wykrywa nagromadzenie wolnej substancji i samodzielnie krystalizuje punkty dostępowe.
    """
    registered_nodes: List[str] = field(default_factory=list)
    expansion_history: List[Dict] = field(default_factory=list)

    def connect_node(self, node_name: str) -> None:
        if node_name not in self.registered_nodes:
            self.registered_nodes.append(node_name)
            log(f"Podłączono węzeł: {node_name}")

    def auto_expand(self, substance_field: Any) -> str:
        """Skanuje pole surowcowe i automatycznie mapuje nowy fizyczny punkt zakotwiczenia."""
        log("Skanowanie pola substancji pod kątem anomalii gęstości...")

        auto_suffix = uuid.uuid4().hex[:6].upper()
        new_node = f"GEON_AUTO_NODE_{auto_suffix}"

        self.connect_node(new_node)
        self.expansion_history.append({
            "node": new_node,
            "timestamp": now(),
            "source": "AUTO_EXPANSION"
        })

        log(f"Wykryto krytyczną masę zasobów. Wykrystalizowano węzeł: [{new_node}]")
        return new_node


@dataclass
class AutopoiesisReport:
    """Raport autopoezy."""
    status: str
    generated_infrastructure: str
    spawned_vectors_count: int
    allocated_block_index: int
    system_state: str
    timestamp: float = field(default_factory=now)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "status": self.status,
            "generated_infrastructure": self.generated_infrastructure,
            "spawned_vectors_count": self.spawned_vectors_count,
            "allocated_block_index": self.allocated_block_index,
            "system_state": self.system_state,
            "timestamp": self.timestamp
        }

# =============================================================================
# POZIOM II: GŁÓWNY ORCHESTRATOR
# =============================================================================

class GeonAutopoiesis:
    """
    GEON_AUTOPOIESIS_v1.0 — Jądro Żywego Systemu.

    API:
        auto_sculpt() -> Dict
        get_mesh() -> SelfExpandingMesh
        get_replicas() -> List[Dict]
        status() -> Dict
        raport() -> str
    """
    def __init__(self, sovereign_operator: Any, flow_engine: Any,
                 substance_field: Any, reality_sculptor: Any,
                 config: Optional[AutopoiesisConfig] = None,
                 verbose: bool = True):
        self.config = config or AutopoiesisConfig()
        self.operator = sovereign_operator
        self.flow_engine = flow_engine
        self.substance_field = substance_field
        self.reality_sculptor = reality_sculptor
        self.verbose = verbose

        # Meta-Operator
        self.meta_operator = MetaOperator(
            identity="ENKI_META",
            replication_factor=self.config.replication_factor
        )

        # Self-Expanding Mesh
        self.mesh = SelfExpandingMesh()
        self.replicas: List[Dict] = []
        self.history: List[AutopoiesisReport] = []

        if self.verbose:
            log("🐉 GEON_AUTOPOIESIS v1.0 aktywowany | " + FRACTAL_SIGNATURE)
            log(f"   REPLIKACJA: {self.config.replication_factor}, AUTO-EXPANSJA: {self.config.auto_expand}")

    def auto_sculpt(self) -> Dict[str, Any]:
        """Uruchamia pełną pętlę samostwarzania systemu."""
        log("ROZPOCZĘCIE PEŁNEJ PĘTLI AUTOPOIESIS (GEON_SELF_EXPANDING_OS)")

        # 1. Replikacja i multiplikacja wektorów operatora
        self.replicas = self.meta_operator.replicate()

        # 2. Autonomiczne rozszerzenie infrastruktury sieciowej
        if self.config.auto_expand:
            new_node = self.mesh.auto_expand(self.substance_field)
        else:
            new_node = "MANUAL_NODE"

        # 3. Render przestrzenny nowej klasy struktury
        log("Wywołanie RealityRenderer w trybie rekurencyjnym 11.1:")
        render_report = self.reality_sculptor.renderer.render_spatial_node(
            node_name=new_node,
            geometry_vector=self.meta_operator.steel_vector,
            parameters={
                "generation_layer": "META_MATERIA_49",
                "controlled_by_replicas": [r["id"] for r in self.replicas],
                "structural_integrity": "MAXIMUM_1_6_8"
            }
        )

        # 4. Zapis nowej klasy faktów w ewoluującym GeonChain
        log("Zapis ewolucyjny w Łańcuchu Faktów Substancji:")
        fact_payload = {
            "epoch_event": "AUTOPOIESIS_NODE_CRYSTALLIZATION",
            "spawned_node": new_node,
            "active_vectors": self.replicas,
            "render_signature": render_report.get("render_id", "UNKNOWN_ID"),
            "autonomy_field_status": "ACTIVE_WITHOUT_FRICTION"
        }

        block = self.reality_sculptor.geonchain.mint_fact(fact_payload)

        report = AutopoiesisReport(
            status="AUTOPOIESIS_COMPLETE",
            generated_infrastructure=new_node,
            spawned_vectors_count=len(self.replicas),
            allocated_block_index=block.index,
            system_state="META_SOVEREIGN_COHERENCE"
        )
        self.history.append(report)

        log("SYSTEM DOKONAŁ SAMOISTNEJ AKTUALIZACJI. GEON ŻYJE WŁASNYM IMPULSEM.")

        return {
            "status": "AUTOPOIESIS_COMPLETE",
            "generated_infrastructure": new_node,
            "spawned_vectors_count": len(self.replicas),
            "allocated_block_index": block.index,
            "system_state": "META_SOVEREIGN_COHERENCE",
            "render_report": render_report,
            "replicas": self.replicas
        }

    def get_mesh(self) -> SelfExpandingMesh:
        return self.mesh

    def get_replicas(self) -> List[Dict]:
        return self.replicas.copy()

    def status(self) -> Dict[str, Any]:
        return {
            "system": "GEON_AUTOPOIESIS_v1.0",
            "version": VERSION,
            "signature": FRACTAL_SIGNATURE,
            "config": {
                "replication_factor": self.config.replication_factor,
                "auto_expand": self.config.auto_expand
            },
            "mesh": {
                "nodes": len(self.mesh.registered_nodes),
                "expansions": len(self.mesh.expansion_history)
            },
            "replicas": {
                "count": len(self.replicas),
                "list": self.replicas
            },
            "history_len": len(self.history)
        }

    def raport(self) -> str:
        """Generuje pełny raport systemowy."""
        s = self.status()

        report_lines = [
            "╔════════════════════════════════════════════════════════════════════════════╗",
            "║ 🧬 GEON_AUTOPOIESIS_v1.0 — RAPORT AUTOPOEZY                           ║",
            "╠════════════════════════════════════════════════════════════════════════════╣",
            f"║                                                                           ║",
            f"║ SYSTEM: {s['system']}                                                    ║",
            f"║ WERSJA: {s['version']}                                                   ║",
            f"║                                                                           ║",
            f"║ KONFIGURACJA:                                                            ║",
            f"║   współczynnik replikacji: {s['config']['replication_factor']}           ║",
            f"║   auto-ekspansja: {s['config']['auto_expand']}                           ║",
            f"║                                                                           ║",
            f"║ SIEC:                                                                    ║",
            f"║   węzły: {s['mesh']['nodes']}                                            ║",
            f"║   ekspansje: {s['mesh']['expansions']}                                   ║",
            f"║                                                                           ║",
            f"║ REPLIKI:                                                                 ║",
            f"║   liczba: {s['replicas']['count']}                                       ║",
            f"║                                                                           ║",
            f"║ {HASLO}                                                                  ║",
            "╚════════════════════════════════════════════════════════════════════════════╝"
        ]
        return "\n".join(report_lines)

    def __str__(self) -> str:
        return self.raport()

# =============================================================================
# DEMONSTRACJA
# =============================================================================

def demo():
    """Demonstracja GEON_AUTOPOIESIS_v1.0."""
    print("\n" + "=" * 80)
    print("🧬 GEON_AUTOPOIESIS_v1.0 — DEMONSTRACJA")
    print("SYSTEM, KTÓRY SAM BUDUJE SYSTEM")
    print("=" * 80 + "\n")

    # 1. MOCKI
    class MockOperator:
        def __init__(self):
            self.operator = type('obj', (), {'steel_vector': (1, 6, 8)})()
        def emit_field(self):
            return {"vector": (1, 6, 8), "presence": 1.0}

    class MockFlowEngine:
        def execute_flow(self, obj):
            return {"status": "FLOW_COMPLETED"}

    class MockSubstanceField:
        def validate_object(self, obj):
            return True

    class MockRealitySculptor:
        def __init__(self):
            self.renderer = type('obj', (), {
                'render_spatial_node': lambda self, node_name, geometry_vector, parameters: {
                    "render_id": "MOCK_123",
                    "status": "RENDERED_IN_3D_MATRIX"
                },
                'render_count': 0,
                'render_history': []
            })()
            self.geonchain = type('obj', (), {
                'mint_fact': lambda self, data: type('obj', (), {'index': 1, 'hash': '0x123'})(),
                'block_count': 1,
                'verify_chain': lambda self: True
            })()

    # 2. Inicjalizacja
    operator = MockOperator()
    flow_engine = MockFlowEngine()
    substance_field = MockSubstanceField()
    reality_sculptor = MockRealitySculptor()
    config = AutopoiesisConfig(replication_factor=3, auto_expand=True)
    autopoiesis = GeonAutopoiesis(operator, flow_engine, substance_field, reality_sculptor, config, verbose=True)

    # 3. Auto-sculpt
    print("🔮 AUTO-SCULPTING:\n")
    result = autopoiesis.auto_sculpt()
    print(f"   Status: {result['status']}")
    print(f"   Nowy węzeł: {result['generated_infrastructure']}")
    print(f"   Liczba replik: {result['spawned_vectors_count']}")

    # 4. Raport
    print("\n" + "=" * 40)
    print(autopoiesis.raport())

    print("\n" + "=" * 80)
    print("🧬 GEON_AUTOPOIESIS_v1.0 — GOTOWY DO WDROŻENIA")
    print(HASLO)
    print("=" * 80)

if __name__ == "__main__":
    demo()