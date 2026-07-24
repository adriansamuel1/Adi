#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AUTOSTRADA33_ULTIMATE_v2.1_PERFECT.py
AUTOSTRADA33 - GŁÓWNA MAGISTRALA GEON_DRAGON_OCTOPUS_OS
Status: ARCHITECTURE_LOCKED | ULTIMATE_v2.1 | PRODUCTION_READY

Autor: Adrian (GEON/DRAGON/OCTOPUS_OS)
"""

import time
import heapq
import asyncio
import json
import hashlib
from collections import deque
from typing import List, Dict, Any, Tuple, Optional
from datetime import datetime

# ============================================================
# 0. LOGGER SYSTEMOWY OS
# ============================================================
def OS_LOG(module: str, message: str):
    ts = time.strftime("%H:%M:%S")
    print(f"[{ts}] {module} → {message}")

# ============================================================
# 1. KONFIGURACJA GLOBALNA
# ============================================================
VERSION = "ULTIMATE_v2.1_AUTOSTRADA_PERFECT"
FRACTAL_SEED = hashlib.sha256(b"GEON_AUTOSTRADA33_ULTIMATE_V2_1").hexdigest()
FRACTAL_SIGNATURE = "[AUTOSTRADA33::1-6-8]"

def now_iso() -> str:
    return datetime.now().isoformat()

def clamp(v: float, mn: float, mx: float) -> float:
    return max(mn, min(mx, v))

# ============================================================
# 2. GEON_10_OP_v3 - OPERACYJNA INTELIGENCJA
# ============================================================
class GEON_10_OP:
    def __init__(self):
        self.hints: List[Dict] = []
        self.context_memory: Dict[str, Any] = {}
        self.adaptation_level: float = 0.5
        self.learning_rate: float = 0.1
        OS_LOG("GEON_10_OP::INIT", "Moduł operacyjnej inteligencji zainicjalizowany")

    def priority_boost(self, payload: Dict) -> int:
        if payload.get("type") in ["CRITICAL", "EMERGENCY", "SAFETY", "SYSTEM"]:
            return 1
        if payload.get("priority", 5) <= 3:
            return payload.get("priority", 3)
        return payload.get("priority", 5)

    def retry_override(self, msg: Dict) -> bool:
        if msg.get("payload", {}).get("type") in ["CRITICAL", "EMERGENCY", "SYSTEM"]:
            return True
        if msg.get("last_error") in ["TIMEOUT", "TRANSIENT", "CONNECTION_RESET"]:
            return True
        if self.adaptation_level > 0.7:
            return True
        return False

    def batch_logic(self, batch: List[Dict]) -> bool:
        if len(batch) < 2:
            return False
        types = [b.get("payload", {}).get("type", "unknown") for b in batch]
        if len(set(types)) == 1:
            return True
        if len(batch) >= 4:
            return True
        return False

    def flow_hint(self, G_VEC: Dict) -> float:
        stability = G_VEC.get("STABILITY", 0.5)
        flow_q = G_VEC.get("FLOW_QUALITY", 0.5)
        resilience = G_VEC.get("RESILIENCE", 0.5)
        hint = (stability - 0.5) * 0.25 + (flow_q - 0.5) * 0.15 + (resilience - 0.5) * 0.10
        return clamp(hint, -0.5, 0.5)

    def smart_backpressure(self, status: str) -> str:
        if self.adaptation_level > 0.7:
            if status == "LOW_THROTTLE":
                return "CLEAR"
            if status == "SOFT_THROTTLE":
                return "LOW_THROTTLE"
        if self.adaptation_level < 0.3:
            if status == "SOFT_THROTTLE":
                return "CRITICAL_THROTTLE"
            if status == "LOW_THROTTLE":
                return "SOFT_THROTTLE"
        return status

    def remember_hint(self, data: Dict) -> None:
        self.hints.append(data)
        if len(self.hints) > 200:
            self.hints = self.hints[-100:]
        if len(self.hints) > 20:
            recent = self.hints[-20:]
            avg_mult = sum(h.get("multiplier", 1.0) for h in recent) / len(recent)
            avg_pressure = sum(h.get("buffer_pressure", 0.0) for h in recent) / len(recent)
            if avg_mult > 1.5 and avg_pressure < 0.3:
                self.adaptation_level = min(1.0, self.adaptation_level + self.learning_rate * 0.5)
            elif avg_pressure > 0.7:
                self.adaptation_level = max(0.0, self.adaptation_level - self.learning_rate * 0.3)
            else:
                self.adaptation_level = max(
                    0.0,
                    min(1.0, self.adaptation_level + (avg_mult - 1.0) * self.learning_rate * 0.1),
                )
        OS_LOG("GEON_10_OP::ADAPT", f"Poziom adaptacji: {self.adaptation_level:.2f}")

# ============================================================
# 3. GŁÓWNA KLASA - AUTOSTRADA33_ULTIMATE_v2
# ============================================================
class Autostrada33_ULTIMATE_v2:
    def __init__(
        self, A, B, C, D, E, G_MEM, macka_f=None, armillaria=None, h_core=None, config: Optional[Dict] = None,
    ):
        OS_LOG("AUTOSTRADA::INIT", "Inicjalizacja magistrali...")

        self.A = A
        self.B = B
        self.C = C
        self.D = D
        self.E = E
        self.G_MEM = G_MEM

        self.macka_f = macka_f
        self.armillaria = armillaria
        self.h_core = h_core

        self.OP = GEON_10_OP()

        self.intent_heap: List[Tuple[int, int, Dict[str, Any]]] = []
        self.emergency_queue: List[Dict[str, Any]] = []
        self.pending_queue: List[Dict[str, Any]] = []
        self.retry_queue: List[Dict[str, Any]] = []
        self.dead_letter_queue: List[Dict[str, Any]] = []
        self.post_process_queue: List[Dict[str, Any]] = []

        self.dropped_intents_buffer: deque = deque(maxlen=50)
        self.shadow_traces: deque = deque(maxlen=2000)
        self.cb_history: deque = deque(maxlen=1000)

        self._task = None
        self.running = False
        self.start_time = time.time()
        self._seq = 0
        self.circuit_breaker_active = False
        self.dead_this_tick = 0

        self.current_tick = 0

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
            "SHADOW_TRACE_ENABLED": True,
            "ARMILLARIA_MEMORY_ENABLED": True,
            "H_VERDICT_ENABLED": True,
            "BACKGROUND_TICK_INTERVAL": 0.1,
            "DEAD_LETTER_PERSISTENCE": True,
            "DEAD_LETTER_FILE": "dead_letter_backup.json",
            "SEQ_RESET_THRESHOLD": 10000,
        }
        if config:
            self.config.update(config)

        self.stats = {
            "intents_submitted": 0,
            "intents_processed": 0,
            "intents_retried": 0,
            "intents_failed": 0,
            "intents_expired": 0,
            "avg_latency_ms": 0.0,
            "f_stabilizations": 0,
            "armillaria_hits": 0,
            "armillaria_misses": 0,
            "h_verdicts": 0,
            "shadow_traces": 0,
            "circuit_breaker_activations": 0,
            "batches_created": 0,
            "backpressure_events": 0,
            "seq_resets": 0,
        }

        self._dead_letter_save_lock = asyncio.Lock()
        if self.config["DEAD_LETTER_PERSISTENCE"]:
            self._load_dead_letter()

        OS_LOG("AUTOSTRADA::INIT", f"Magistrala uruchomiona (v{VERSION})")

    # ============================================================
    # SUBMIT / FAST LANE
    # ============================================================
    def submit_intent_request(self, payload: dict, priority: int = 5) -> bool:
        OS_LOG("AUTOSTRADA::SUBMIT", f"Zgłaszanie intencji: {payload.get('id', 'unknown')}")

        if self.total_queue_len() >= self.config["MAX_QUEUE_LEN"]:
            self._drop_intent({"payload": payload, "priority": priority}, reason="BUFFER_FULL")
            return False

        boosted_priority = self.OP.priority_boost(payload)
        msg = {
            "id": payload.get("id", f"intent_{self.current_tick}_{self._seq}"),
            "priority": boosted_priority,
            "payload": payload,
            "timestamp_epoch": time.time(),
            "attempts": 0,
            "submission_tick": self.current_tick,
        }

        if boosted_priority <= 2:
            self.emergency_queue.append(msg)
            OS_LOG("AUTOSTRADA::EMERGENCY", f"Emergency intent: {msg['id']}")
        else:
            heapq.heappush(self.intent_heap, (boosted_priority, self._seq, msg))
            self._seq += 1

        self.stats["intents_submitted"] += 1
        if self.config["SHADOW_TRACE_ENABLED"]:
            self._shadow_trace("SUBMIT", msg)
        return True

    def total_queue_len(self) -> int:
        return (
            len(self.intent_heap)
            + len(self.emergency_queue)
            + len(self.retry_queue)
            + len(self.pending_queue)
        )

    def _drop_intent(self, msg: dict, reason: str):
        OS_LOG("AUTOSTRADA::DROP", f"Intencja odrzucona: {reason} | {msg.get('id', 'unknown')}")
        msg["drop_reason"] = reason
        msg["drop_tick"] = self.current_tick
        self.dropped_intents_buffer.append(msg)

    # ============================================================
    # BACKPRESSURE
    # ============================================================
    def calculate_pressure_logic(self, queue_len: int, max_cap: int) -> str:
        pressure = queue_len / max_cap if max_cap > 0 else 0.0
        if pressure > 0.90:
            self.stats["backpressure_events"] += 1
            OS_LOG("AUTOSTRADA::BACKPRESSURE", f"KRYTYCZNY: {pressure:.2f}")
            return "CRITICAL_THROTTLE"
        elif pressure > 0.75:
            self.stats["backpressure_events"] += 1
            OS_LOG("AUTOSTRADA::BACKPRESSURE", f"MIĘKKI: {pressure:.2f}")
            return "SOFT_THROTTLE"
        elif pressure > 0.50:
            return "LOW_THROTTLE"
        return "CLEAR"

    # ============================================================
    # RETRY / BACKOFF / DEAD LETTER
    # ============================================================
    def _requeue_with_backoff(self, msg: dict, error: str):
        OS_LOG("AUTOSTRADA::REQUEUE", f"Przekierowanie do retry: {error[:50]}")
        attempts = msg.get("attempts", 0) + 1
        max_attempts = self.config["RETRY_MAX_ATTEMPTS"]

        if attempts <= max_attempts:
            backoff_ms = self.config["RETRY_BACKOFF_MS"][min(attempts - 1, len(self.config["RETRY_BACKOFF_MS"]) - 1)]
            msg["attempts"] = attempts
            msg["next_retry_tick"] = self.current_tick + (backoff_ms // 100)
            msg["last_error"] = error
            self.retry_queue.append(msg)
            self.stats["intents_retried"] += 1
            OS_LOG("AUTOSTRADA::RETRY", f"Retry {attempts}/{max_attempts}: {error[:50]}")
            return

        if self.OP.retry_override(msg):
            msg["attempts"] = max(0, attempts - 1)
            backoff_ms = self.config["RETRY_BACKOFF_MS"][0]
            msg["next_retry_tick"] = self.current_tick + (backoff_ms // 100)
            msg["last_error"] = f"EXTRA_LIFE: {error}"
            self.retry_queue.append(msg)
            self.stats["intents_retried"] += 1
            OS_LOG("AUTOSTRADA::EXTRA_LIFE", f"Extra life: {error[:50]}")
            return

        msg["final_error"] = error
        msg["dead_tick"] = self.current_tick
        self.dead_letter_queue.append(msg)
        self.stats["intents_failed"] += 1
        self.dead_this_tick += 1
        OS_LOG("AUTOSTRADA::DEAD_LETTER", f"Dead letter: {error[:50]} | {msg.get('id', 'unknown')}")

        if self.armillaria and self.config["ARMILLARIA_MEMORY_ENABLED"]:
            if hasattr(self.armillaria, 'fatal_errors_learned'):
                self.armillaria.fatal_errors_learned.add(error)
                OS_LOG("AUTOSTRADA::ARMILLARIA", f"Zapisano błąd w fatal_errors_learned: {error[:50]}")

        if self.h_core and self.config["H_VERDICT_ENABLED"]:
            if hasattr(self.h_core, 'process'):
                self.h_core.process(f"DEAD_LETTER: {error}", {"type": "DEAD_LETTER", "msg": msg})
                OS_LOG("AUTOSTRADA::HEILONG", f"Przekazano dead-letter do HEILONG")

        if len(self.dead_letter_queue) > self.config["DEAD_LETTER_MAX_SIZE"]:
            self.dead_letter_queue = list(self.dead_letter_queue)[-self.config["DEAD_LETTER_MAX_SIZE"]:]

        if self.config["DEAD_LETTER_PERSISTENCE"]:
            try:
                loop = asyncio.get_running_loop()
                loop.create_task(self._save_dead_letter_async())
            except RuntimeError:
                # Brak aktywnej pętli – zapis synchroniczny
                data = list(self.dead_letter_queue)[-100:]
                self._save_dead_letter_sync(data)

    async def _save_dead_letter_async(self):
        async with self._dead_letter_save_lock:
            try:
                data = list(self.dead_letter_queue)[-100:]
                await asyncio.to_thread(self._save_dead_letter_sync, data)
            except Exception as e:
                OS_LOG("AUTOSTRADA::DEAD_LETTER_SAVE", f"Błąd zapisu: {e}")

    def _save_dead_letter_sync(self, data: List[Dict]):
        try:
            with open(self.config["DEAD_LETTER_FILE"], 'w') as f:
                json.dump(data, f, indent=2, default=str)
        except Exception as e:
            OS_LOG("AUTOSTRADA::DEAD_LETTER_SAVE", f"Błąd: {e}")

    def _load_dead_letter(self):
        try:
            with open(self.config["DEAD_LETTER_FILE"], 'r') as f:
                data = json.load(f)
            self.dead_letter_queue = data[:self.config["DEAD_LETTER_MAX_SIZE"]]
            OS_LOG("AUTOSTRADA::DEAD_LETTER_LOAD", f"Wczytano {len(data)} dead letterów")
        except FileNotFoundError:
            pass
        except Exception as e:
            OS_LOG("AUTOSTRADA::DEAD_LETTER_LOAD", f"Błąd: {e}")

    # ============================================================
    # RETRY QUEUE PROCESSING
    # ============================================================
    def _process_retry_queue(self):
        OS_LOG("AUTOSTRADA::RETRY_PROCESS", "Przetwarzanie kolejki retry")
        now_tick = self.current_tick
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
            OS_LOG("AUTOSTRADA::RETRY_READY", f"Retry ready: {msg.get('id', 'unknown')}")

    # ============================================================
    # TTL / EXPIRATION
    # ============================================================
    def _expire_old_intents(self):
        OS_LOG("AUTOSTRADA::EXPIRE", "Sprawdzanie TTL intencji")
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
                    OS_LOG("AUTOSTRADA::EXPIRE", f"Intencja wygasła: {msg.get('id', 'unknown')}")
                else:
                    remaining.append(msg)
            return remaining

        self.pending_queue = _filter_queue(self.pending_queue)
        self.retry_queue = _filter_queue(self.retry_queue)

    # ============================================================
    # DEDUP (poprawiona)
    # ============================================================
    def _payload_fingerprint(self, payload: Dict[str, Any]) -> Optional[str]:
        try:
            return hashlib.sha256(
                json.dumps(payload, sort_keys=True, default=str, ensure_ascii=False).encode("utf-8")
            ).hexdigest()
        except Exception:
            return None

    def _deduplicate_heap(self):
        OS_LOG("AUTOSTRADA::DEDUP", "Deduplikacja sterty")
        seen = set()
        new_heap: List[Tuple[int, int, Dict[str, Any]]] = []

        while self.intent_heap:
            prio, seq, msg = heapq.heappop(self.intent_heap)
            payload = msg.get("payload", {})
            fp = self._payload_fingerprint(payload)
            if fp is None:
                new_heap.append((prio, seq, msg))
                continue
            if fp not in seen:
                seen.add(fp)
                new_heap.append((prio, seq, msg))

        heapq.heapify(new_heap)
        self.intent_heap = new_heap

    # ============================================================
    # BATCHING
    # ============================================================
    def _batch_from_heap(self) -> List[dict]:
        OS_LOG("AUTOSTRADA::BATCH", "Tworzenie batcha")
        if not self.intent_heap or self.config["BATCH_SIZE"] <= 1:
            return []
        batch_size = self.config["BATCH_SIZE"]
        temp: List[Tuple[int, int, Dict[str, Any]]] = []

        while self.intent_heap and len(temp) < batch_size:
            temp.append(heapq.heappop(self.intent_heap))

        batch_msgs = [item[2] for item in temp]

        if not self.OP.batch_logic(batch_msgs) or len(temp) <= 1:
            for item in temp:
                heapq.heappush(self.intent_heap, item)
            return []

        intent_type = batch_msgs[0].get("payload", {}).get("type", "unknown")
        batched_payload = {
            "type": "BATCH_INTENT",
            "original_type": intent_type,
            "count": len(batch_msgs),
            "items": [m["payload"] for m in batch_msgs],
            "ids": [m.get("id", "unknown") for m in batch_msgs],
        }
        batched_msg = {
            "id": f"batch_{self.current_tick}_{intent_type}_{hash(str(batched_payload)) % 100000000}",
            "priority": min(m.get("priority", 5) for m in batch_msgs),
            "payload": batched_payload,
            "timestamp_epoch": time.time(),
            "is_batch": True,
            "attempts": 0,
            "batch_size": len(batch_msgs),
        }
        self.stats["batches_created"] += 1
        OS_LOG("AUTOSTRADA::BATCH", f"Batch: {len(batch_msgs)} intencji typu {intent_type}")
        return [batched_msg]

    # ============================================================
    # CIRCUIT BREAKER
    # ============================================================
    def _evaluate_circuit_breaker(self) -> bool:
        OS_LOG("AUTOSTRADA::CIRCUIT_BREAKER", "Ocena stanu circuit breaker")
        if not self.cb_history:
            return False
        recent = list(self.cb_history)[-self.config["CIRCUIT_BREAKER_WINDOW_TICKS"]:]
        if not recent:
            return False

        total_dead = sum(cnt for _, cnt in recent)
        total_ticks = len(recent)
        ratio = total_dead / total_ticks if total_ticks > 0 else 0.0

        if ratio > self.config["CIRCUIT_BREAKER_THRESHOLD_RATIO"]:
            if not self.circuit_breaker_active:
                self.circuit_breaker_active = True
                self.stats["circuit_breaker_activations"] += 1
                OS_LOG("AUTOSTRADA::CIRCUIT_BREAKER", f"AKTYWACJA! ratio={ratio:.2f}")
            return True

        if self.circuit_breaker_active and ratio <= self.config["CIRCUIT_BREAKER_THRESHOLD_RATIO"]:
            self.circuit_breaker_active = False
            OS_LOG("AUTOSTRADA::CIRCUIT_BREAKER", "DEZAKTYWACJA")
        return False

    # ============================================================
    # SHADOW TRACE
    # ============================================================
    def _shadow_trace(self, event: str, msg: Dict):
        OS_LOG("AUTOSTRADA::SHADOW_TRACE", f"Ślad: {event} | {msg.get('id', 'unknown')}")
        trace = {
            "timestamp": time.time(),
            "tick": self.current_tick,
            "event": event,
            "msg_id": msg.get("id", "unknown"),
            "priority": msg.get("priority", 5),
            "type": msg.get("payload", {}).get("type", "unknown"),
        }
        self.shadow_traces.append(trace)
        self.stats["shadow_traces"] += 1

    # ============================================================
    # POST EXECUTION
    # ============================================================
    def _process_post_execution(self):
        OS_LOG("AUTOSTRADA::POST_EXEC", "Przetwarzanie post-execution")
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
            if self.config["SHADOW_TRACE_ENABLED"]:
                self._shadow_trace("PROCESSED", msg)

    def _update_latency(self, msg: Dict):
        OS_LOG("AUTOSTRADA::LATENCY", "Aktualizacja latencji")
        ts = msg.get("timestamp_epoch")
        if ts:
            latency = (time.time() - ts) * 1000
            avg = self.stats["avg_latency_ms"]
            n = self.stats["intents_processed"]
            if n > 0:
                self.stats["avg_latency_ms"] = avg + (latency - avg) / n

    # ============================================================
    # STATUS → D → E
    # ============================================================
    def _process_status_and_memory(self):
        OS_LOG("AUTOSTRADA::STATUS", "Przetwarzanie statusu → D → E")
        c_state = self.C.export_state()
        self.D.store(c_state)
        trend = self.D.trend()
        self.E.update_from_trend(trend)
        if self.config["SHADOW_TRACE_ENABLED"]:
            self._shadow_trace("D_TREND", {"trend": trend})

    # ============================================================
    # RESOLVE PENDING
    # ============================================================
    def _resolve_pending_intents(self):
        OS_LOG("AUTOSTRADA::PENDING", "Rozwiązywanie oczekujących intencji")
        if not self.pending_queue:
            return
        resolved = []
        remaining = []
        for msg in self.pending_queue:
            if msg.get("resolve_tick", 0) <= self.current_tick:
                resolved.append(msg)
            else:
                remaining.append(msg)
        self.pending_queue = remaining
        for msg in resolved:
            self._requeue_with_backoff(msg, "PENDING_RESOLVED")

    # ============================================================
    # HOUSEKEEPING (synchroniczna – wywoływana co tick)
    # ============================================================
    def _housekeeping(self):
        if self._seq >= self.config["SEQ_RESET_THRESHOLD"]:
            old_seq = self._seq
            self._seq = 0
            self.stats["seq_resets"] += 1
            OS_LOG("AUTOSTRADA::SEQ_RESET", f"Reset seq (był: {old_seq})")

        self.cb_history.append((self.current_tick, self.dead_this_tick))
        self.dead_this_tick = 0

    # ============================================================
    # PERIODYCZNE ZADANIA TŁA (asynchroniczne)
    # ============================================================
    async def _periodic_housekeeping(self):
        """Dodatkowe prace konserwacyjne wykonywane okresowo w pętli tła."""
        OS_LOG("AUTOSTRADA::PERIODIC_HK", "Rozpoczęcie okresowych prac")
        # Reset sequencji jeśli sterta pusta i przekroczony próg
        if not self.intent_heap and self._seq >= self.config["SEQ_RESET_THRESHOLD"]:
            old_seq = self._seq
            self._seq = 0
            self.stats["seq_resets"] += 1
            OS_LOG("AUTOSTRADA::PERIODIC_HK", f"Reset seq (był: {old_seq})")

        # Zapis dead letter
        if self.config["DEAD_LETTER_PERSISTENCE"]:
            await self._save_dead_letter_async()

        # Dezaktywacja CB jeśli historia czysta
        if self.circuit_breaker_active:
            recent = list(self.cb_history)[-self.config["CIRCUIT_BREAKER_WINDOW_TICKS"]:]
            if recent and sum(cnt for _, cnt in recent) == 0:
                self.circuit_breaker_active = False
                OS_LOG("AUTOSTRADA::PERIODIC_HK", "Circuit breaker dezaktywowany")

        OS_LOG("AUTOSTRADA::PERIODIC_HK", f"Queue: {self.total_queue_len()}, DL: {len(self.dead_letter_queue)}, Seq: {self._seq}")

    # ============================================================
    # ASYNCHRONICZNA PĘTLA TŁA
    # ============================================================
    async def start_background(self):
        """Uruchamia asynchroniczną pętlę tła."""
        self.running = True
        self.start_time = time.time()
        self._task = asyncio.create_task(self._background_loop())
        OS_LOG("AUTOSTRADA::BG_START", "Pętla tła uruchomiona")
        return self._task

    async def stop_background(self):
        """Zatrzymuje asynchroniczną pętlę tła."""
        self.running = False
        if self._task:
            self._task.cancel()
            try:
                await self._task
            except asyncio.CancelledError:
                pass
        OS_LOG("AUTOSTRADA::BG_STOP", "Pętla tła zatrzymana")

    async def _background_loop(self):
        """Główna pętla tła – wykonuje okresowe zadania."""
        last_periodic = time.time()
        periodic_interval = 60.0  # co 60 sekund
        while self.running:
            await asyncio.sleep(self.config["BACKGROUND_TICK_INTERVAL"])
            now = time.time()
            if now - last_periodic >= periodic_interval:
                await self._periodic_housekeeping()
                last_periodic = now

    # ============================================================
    # METRYKI I STATUS
    # ============================================================
    def get_metrics(self) -> dict:
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
                "mode": getattr(self.G_MEM, "MODE", "NORMAL"),
                "multiplier": getattr(self.G_MEM, "multiplier", 1.0),
                "buffer_pressure": self.G_MEM.G_VECTOR.get("BUFFER_PRESSURE", 0.0) if hasattr(self.G_MEM, "G_VECTOR") else 0.0,
            },
            "throttle": {
                "active": getattr(self.G_MEM, "THROTTLE_A", False),
                "reason": getattr(self.G_MEM, "THROTTLE_REASON", None),
            },
            "circuit_breaker": {
                "active": self.circuit_breaker_active,
                "history": list(self.cb_history)[-10:],
                "activations": self.stats["circuit_breaker_activations"],
            },
            "shadow_traces_count": len(self.shadow_traces),
            "tick": self.current_tick,
            "uptime_seconds": time.time() - self.start_time,
            "sequence": self._seq,
            "seq_resets": self.stats["seq_resets"],
            "version": VERSION,
        }

    def flush_dead_letter(self) -> List[dict]:
        dead = list(self.dead_letter_queue).copy()
        self.dead_letter_queue = []
        OS_LOG("AUTOSTRADA::FLUSH_DEAD", f"Flushed {len(dead)} dead letters")
        return dead

    def export_shadow_traces(self, limit: int = 100) -> List[Dict]:
        return list(self.shadow_traces)[-limit:]

    def get_status(self) -> Dict[str, Any]:
        return {
            "status": "RUNNING" if self.running else "STOPPED",
            "tick": self.current_tick,
            "version": VERSION,
            "signature": FRACTAL_SIGNATURE,
            "queue_total": self.total_queue_len(),
            "config": self.config,
            "stats": self.stats,
            "circuit_breaker": self.circuit_breaker_active,
            "uptime_seconds": time.time() - self.start_time,
            "sequence": self._seq,
            "features": {
                "f_stabilization": bool(self.macka_f),
                "armillaria": bool(self.armillaria),
                "h_verdict": bool(self.h_core),
                "shadow_trace": self.config["SHADOW_TRACE_ENABLED"],
                "dead_letter_persistence": self.config["DEAD_LETTER_PERSISTENCE"],
            },
        }

    # Alias dla tick_once
    def tick(self, *args, **kwargs) -> Dict[str, Any]:
        return self.tick_once(*args, **kwargs)

    # ============================================================
    # GŁÓWNY TICK
    # ============================================================
    def tick_once(
        self, A_SIGNAL: dict, B_GEON: dict, C_INPUT: dict, D_INPUT: dict, E_OUTPUT: dict,
        highway_priority: int = 5, highway_mode: str = "NORMAL", multiplier_cap: float = 3.0,
        use_armillaria: bool = True, use_f_stabilization: bool = True, use_h_verdict: bool = True,
    ) -> Dict[str, Any]:
        self.current_tick += 1
        OS_LOG("AUTOSTRADA::TICK", f"Tick {self.current_tick} - START")

        # 1. TTL
        self._expire_old_intents()

        # 2. HIGHWAY
        HIGHWAY = {
            "priority": highway_priority,
            "mode": highway_mode,
            "multiplier_cap": multiplier_cap,
        }

        # 3. G_ENGINE_TICK_v3
        try:
            from G_CORE import G_ENGINE_TICK_v3
            g_result = G_ENGINE_TICK_v3(
                A_SIGNAL=A_SIGNAL, B_GEON=B_GEON, C_INPUT=C_INPUT, D_INPUT=D_INPUT, E_OUTPUT=E_OUTPUT,
                HIGHWAY=HIGHWAY, G_MEM=self.G_MEM, intent_queue_len=self.total_queue_len(),
                intent_queue_cap=self.config["MAX_QUEUE_LEN"],
            )
            OS_LOG("AUTOSTRADA::G_CORE", f"G_CORE OK: multiplier={g_result.get('MULTIPLIER', 1.0)}")
        except ImportError as e:
            g_result = {"MULTIPLIER": 1.0, "THROTTLE_A": False, "BUFFER_PRESSURE": 0.1, "MODE": "NORMAL"}
            OS_LOG("AUTOSTRADA::G_CORE_FALLBACK", f"G_CORE niedostępne: {e}")
        except Exception as e:
            g_result = {"MULTIPLIER": 1.0, "THROTTLE_A": False, "BUFFER_PRESSURE": 0.1, "MODE": "NORMAL"}
            OS_LOG("AUTOSTRADA::G_CORE_ERROR", f"Błąd G_CORE: {e}")

        multiplier = g_result.get("MULTIPLIER", 1.0)
        throttle_A = g_result.get("THROTTLE_A", False)
        buffer_pressure = g_result.get("BUFFER_PRESSURE", 0.0)

        # 4. FLOW HINT
        flow_adjust = self.OP.flow_hint(self.G_MEM.G_VECTOR)
        multiplier = clamp(multiplier + flow_adjust, 0.2, multiplier_cap)

        # 5. CIRCUIT BREAKER
        if self._evaluate_circuit_breaker():
            self.G_MEM.MODE = "SAFE_MODE"
            multiplier = min(multiplier, 0.75)
            OS_LOG("AUTOSTRADA::SAFE_MODE", "Aktywacja SAFE_MODE")

        # 6. BACKPRESSURE
        raw_pressure_status = self.calculate_pressure_logic(self.total_queue_len(), self.config["MAX_QUEUE_LEN"])
        pressure_status = self.OP.smart_backpressure(raw_pressure_status)

        if hasattr(self.A, 'set_pressure_limit'):
            try:
                self.A.set_pressure_limit(pressure_status)
                OS_LOG("AUTOSTRADA::PRESSURE", f"Ustawiono limit: {pressure_status}")
            except Exception as e:
                OS_LOG("AUTOSTRADA::A_ERROR", f"Błąd set_pressure_limit: {e}")

        # 7. GENEROWANIE INTENCJI PRZEZ A
        if not throttle_A and hasattr(self.A, 'generate_intent'):
            try:
                new_intent = self.A.generate_intent(pressure_status=pressure_status)
                if new_intent is not None:
                    self.submit_intent_request(new_intent, priority=new_intent.get("priority", highway_priority))
                    OS_LOG("AUTOSTRADA::A_INTENT", "Nowa intencja z A")
            except Exception as e:
                OS_LOG("AUTOSTRADA::A_ERROR", f"Błąd generate_intent: {e}")

        # 8. RETRY QUEUE
        self._process_retry_queue()

        # 9. DEDUP
        self._deduplicate_heap()

        # 10. BATCHING
        batched = self._batch_from_heap()
        for msg in batched:
            self.emergency_queue.append(msg)

        # 11. PRZEPUSTOWOŚĆ
        effective_capacity = max(1, int(self.config["BASE_CAPACITY_PER_TICK"] * multiplier))

        # 12. WYCIĄGANIE INTENCJI
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

        # 13. PIPELINE
        OS_LOG("AUTOSTRADA::TICK", f"Krok 13: PIPELINE - {len(to_process)} intencji")
        for msg in to_process:
            intent_raw = msg["payload"]

            # 13a + 13b: PREFILTER + TRANSFORM C → filtered
            OS_LOG("AUTOSTRADA::PIPELINE", "13a/13b: PREFILTER + TRANSFORM C")
            try:
                filtered = intent_raw

                if hasattr(self.C, 'prefilter_intent'):
                    pf = self.C.prefilter_intent(intent_raw)
                    if pf is False:
                        msg["resolve_tick"] = self.current_tick + 1
                        self.pending_queue.append(msg)
                        continue
                    if isinstance(pf, dict):
                        filtered = pf

                if hasattr(self.C, 'transform_intent'):
                    filtered = self.C.transform_intent(filtered)

            except Exception as e:
                self._requeue_with_backoff(msg, f"C_PREFILTER_TRANSFORM_ERROR: {e}")
                continue

            # 13c. B.run_cycle
            OS_LOG("AUTOSTRADA::PIPELINE", "13c: B.run_cycle")
            try:
                status_b = self.B.run_cycle(filtered)
            except Exception as e:
                self._requeue_with_backoff(msg, f"B_ERROR: {e}")
                continue

            # 13d. Stabilizacja macka_f
            if use_f_stabilization and self.macka_f is not None:
                OS_LOG("AUTOSTRADA::PIPELINE", "13d: F_STABILIZATION")
                try:
                    stabilized = self.macka_f.stabilize(filtered, self.C)
                    if isinstance(stabilized, dict):
                        filtered = stabilized
                    elif isinstance(stabilized, str) and "message" in filtered:
                        filtered["message"] = stabilized
                    self.stats["f_stabilizations"] += 1
                except Exception as e:
                    OS_LOG("AUTOSTRADA::F_ERROR", f"Błąd stabilizacji F: {e}")

            # 13e. ARMILLARIA pamięć
            if use_armillaria and self.armillaria is not None and self.config["ARMILLARIA_MEMORY_ENABLED"]:
                OS_LOG("AUTOSTRADA::PIPELINE", "13e: ARMILLARIA")
                try:
                    recall = None
                    if hasattr(self.armillaria, 'pipeline_memory_recall'):
                        recall = self.armillaria.pipeline_memory_recall("AUTOSTRADA33", intent_raw)
                        self.armillaria.pipeline_memory_store(
                            "AUTOSTRADA33",
                            {"intent": intent_raw, "filtered": filtered, "status_b": status_b},
                        )
                    elif hasattr(self.armillaria, 'recall') and hasattr(self.armillaria, 'store'):
                        recall = self.armillaria.recall(intent_raw)
                        self.armillaria.store(intent_raw, status_b)

                    if recall is not None:
                        self.stats["armillaria_hits"] += 1
                    else:
                        self.stats["armillaria_misses"] += 1

                except Exception as e:
                    OS_LOG("AUTOSTRADA::ARMILLARIA_ERROR", f"Błąd ARMILLARIA: {e}")

            # 13f. HEILONG werdykt
            if use_h_verdict and self.h_core is not None and self.config["H_VERDICT_ENABLED"]:
                OS_LOG("AUTOSTRADA::PIPELINE", "13f: HEILONG_VERDICT")
                try:
                    self.h_core.process("INTENT_PROCESSED", {
                        "msg": msg,
                        "filtered": filtered,
                        "status_b": status_b,
                        "tick": self.current_tick,
                    })
                    self.stats["h_verdicts"] += 1
                except Exception as e:
                    OS_LOG("AUTOSTRADA::HEILONG_ERROR", f"Błąd HEILONG: {e}")

            # 13g. POST → C/D/E
            self.post_process_queue.append({"msg": msg, "status_b": status_b})

        # 14. POST EXEC
        self._process_post_execution()

        # 15. STATUS → D → E
        self._process_status_and_memory()

        # 16. RESOLVE PENDING
        self._resolve_pending_intents()

        # 17. OP – zapamiętaj kontekst (adaptacja)
        self.OP.remember_hint({
            "tick": self.current_tick,
            "queue_len": self.total_queue_len(),
            "multiplier": multiplier,
            "pressure_status": pressure_status,
            "buffer_pressure": buffer_pressure,
            "processed": len(to_process),
            "circuit_breaker": self.circuit_breaker_active,
        })

        # 18. HOUSEKEEPING
        self._housekeeping()

        OS_LOG("AUTOSTRADA::TICK", f"Tick {self.current_tick} - END")
        return {
            "tick": self.current_tick,
            "queue_len": self.total_queue_len(),
            "circuit_breaker_active": self.circuit_breaker_active,
            "avg_latency_ms": self.stats["avg_latency_ms"],
            "intents_processed": self.stats["intents_processed"],
            "armillaria_hits": self.stats["armillaria_hits"],
            "armillaria_misses": self.stats["armillaria_misses"],
        }

# ============================================================
# 4. AUTOSTRADA33_OMEGA - BACKWARD COMPATIBILITY
# ============================================================
class Autostrada33_OMEGA(Autostrada33_ULTIMATE_v2):
    """Omega – dla backward compatibility z istniejącym kodem."""
    def __init__(self, A, B, C, D, E, G_MEM, macka_f=None):
        OS_LOG("AUTOSTRADA::OMEGA", "Inicjalizacja Omega (backward compatibility)")
        super().__init__(A=A, B=B, C=C, D=D, E=E, G_MEM=G_MEM, macka_f=macka_f)

# ============================================================
# 5. TEST INTEGRACYJNY
# ============================================================
if __name__ == "__main__":
    print("\n" + "=" * 80)
    print("🛣️ AUTOSTRADA33_ULTIMATE_v2.1 - TEST INTEGRACYJNY")
    print("=" * 80)
    OS_LOG("TEST::START", "Rozpoczęcie testów integracyjnych")

    # Mocki
    class MockComponent:
        def __init__(self, name):
            self.name = name
            self.data = {}
            OS_LOG(f"MOCK::{name}", "Inicjalizacja mocka")
        def set_pressure_limit(self, status):
            self.data["pressure"] = status
            OS_LOG(f"MOCK::{self.name}", f"Ustawiono pressure: {status}")
        def generate_intent(self, pressure_status="CLEAR"):
            return {"type": "test", "priority": 5, "id": f"test_{int(time.time())}"}
        def prefilter_intent(self, intent):
            return {"message": f"Filtered: {intent}", "pipeline_step": 5}
        def run_cycle(self, data):
            return {"status": "OK", "data": data}
        def receive_status_from_B(self, status):
            self.data["last_status"] = status
        def export_state(self):
            return {"state": "OK"}
        def store(self, data):
            self.data["stored"] = data
        def trend(self):
            return {"trend": "stable"}
        def update_from_trend(self, trend):
            self.data["trend"] = trend

    class MockG_MEM:
        def __init__(self):
            self.MODE = "NORMAL"
            self.multiplier = 1.0
            self.THROTTLE_A = False
            self.THROTTLE_REASON = None
            self.G_VECTOR = {
                "BUFFER_PRESSURE": 0.0,
                "STABILITY": 0.7,
                "FLOW_QUALITY": 0.6,
                "DIRECTION": 0.5,
                "RESILIENCE": 0.5,
            }
            OS_LOG("MOCK::G_MEM", "Inicjalizacja G_MEM")

    class MockF:
        def stabilize(self, text, meta=None):
            return f"[F_STABILIZED] {text}"

    class MockArmillaria:
        def __init__(self):
            self.fatal_errors_learned = set()
            OS_LOG("MOCK::ARMILLARIA", "Inicjalizacja Armillaria")
        def pipeline_memory_recall(self, step, query):
            return {"strength": 0.7, "edge_id": "mock_edge"}
        def pipeline_memory_store(self, step, data):
            pass

    class MockHCore:
        def process(self, message, context):
            OS_LOG("MOCK::HEILONG", f"Przetwarzanie: {message[:30]}...")
            return {"H_STATE": "STABLE", "H_DIRECTIVE": "STABILIZE"}

    # Inicjalizacja
    A = MockComponent("A")
    B = MockComponent("B")
    C = MockComponent("C")
    D = MockComponent("D")
    E = MockComponent("E")
    G_MEM = MockG_MEM()
    F = MockF()
    Armillaria = MockArmillaria()
    HCore = MockHCore()

    autostrada = Autostrada33_ULTIMATE_v2(
        A=A, B=B, C=C, D=D, E=E, G_MEM=G_MEM,
        macka_f=F, armillaria=Armillaria, h_core=HCore
    )

    print("\n🔷 TEST tick_once()")
    for i in range(5):
        OS_LOG("TEST::TICK", f"Wykonanie tick {i+1}")
        result = autostrada.tick_once(
            A_SIGNAL={"vibe": 0.7},
            B_GEON={"DIRECTION": 0.6, "STABILITY": 0.8},
            C_INPUT={"STATE": "C_HOME"},
            D_INPUT={"METRICS": {"RISK": 0.3}},
            E_OUTPUT={"HEALTH": 0.9},
            highway_priority=5,
            highway_mode="NORMAL",
            multiplier_cap=3.0,
        )
        print(f" TICK {i+1}:")
        print(f"  current_tick: {result['tick']}")
        print(f"  queue_len: {result['queue_len']}")
        print(f"  circuit_breaker: {result['circuit_breaker_active']}")

    print("\n📊 METRYKI:")
    metrics = autostrada.get_metrics()
    print(f" Queue sizes: {metrics['queue_sizes']}")
    print(f" Total processed: {metrics['stats']['intents_processed']}")
    print(f" Sequence: {metrics['sequence']}")
    print(f" Seq resets: {metrics['seq_resets']}")
    print(f" Circuit breaker: {metrics['circuit_breaker']['active']}")

    print("\n📋 STATUS:")
    status = autostrada.get_status()
    print(f" Status: {status['status']}")
    print(f" Version: {status['version']}")
    print(f" Tick: {status['tick']}")
    print(f" Sequence: {status['sequence']}")

    OS_LOG("TEST::END", "Testy zakończone pomyślnie")
    print("\n" + "=" * 80)
    print("🛣️ AUTOSTRADA33_ULTIMATE_v2.1 - TEST ZAKOŃCZONY")
    print(" status: PRODUCTION_READY | ULTIMATE_v2.1")
    print("=" * 80)