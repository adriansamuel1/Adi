#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
================================================================================
🐉 GEON_MEM_OMEGA_v2.0 — MODUŁ 45: PAMIĘĆ SYSTEMOWA + CYMATYCZNA
================================================================================
Status: PRODUCTION_READY | FRACTAL_LOCKED | ULTIMA | CYMATIC_INTEGRATED
Wersja: v2.0 (GEON_MEM_Ω + CymaticFractalMemory v3)
Data: 2026-07-24
Autor: Adrian (Architekt) + Samael (Strażnik Kronik) + GEON

OPIS:
    GEON_MEM_OMEGA to komórka nerwowa systemu – pamięć operacyjna, krótko-
    i długoterminowa, z dostępem do ARCHAI (kierunek Rody Heilong) oraz
    stanu operacyjnego dla G_CORE.

    Wersja v2.0 rozszerza system o pamięć cymatyczną (CymaticFractalMemory),
    która przekształca dźwięk w fraktalne wzorce (płatki śniegu) i umożliwia:
    - kodowanie dźwięku do wzorca fraktalnego
    - przechowywanie i wyszukiwanie podobnych wzorców (podwójna metryka)
    - sekwencje temporalne (DTW)
    - integrację z Autostradą 33 przez pakietowe API

VIBE: 1-6-8. ∞. MEM!
DEWIZA: "Ex Memoria, Cognitio. Ex Sono, Forma."
================================================================================
"""

import hashlib
import json
import logging
import math
import threading
import time
from collections import OrderedDict, deque
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple, Union

import numpy as np

# =============================================================================
# WERSJA I STAŁE
# =============================================================================

VERSION = "GEON_MEM_OMEGA_v2.0"
FRACTAL_SIGNATURE = "[GEON::MEM::OMEGA::v2.0::CYMATIC]"
VIBE = 168
HASLO = "1-6-8. ∞. MEM!"
DEWIZA = "Ex Memoria, Cognitio. Ex Sono, Forma."

MEMORY_LIMIT = 512
DIMENSION = 9
DEFAULT_BASELINE = 0.0

# =============================================================================
# LOGOWANIE
# =============================================================================

logger = logging.getLogger("GEON_MEM_OMEGA")
logger.setLevel(logging.INFO)
if not logger.handlers:
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter('🧬 [MEM] %(message)s'))
    logger.addHandler(handler)

def log(msg: str, level: str = "INFO") -> None:
    if level == "WARN":
        logger.warning(msg)
    elif level == "ERROR":
        logger.error(msg)
    else:
        logger.info(msg)

def clamp(x: float, lo: float, hi: float) -> float:
    return max(lo, min(hi, x))

def generate_context_hash(context: Dict[str, Any]) -> str:
    filtered_context = {k: v for k, v in context.items() 
                        if k not in ["timestamp", "request_id", "nonce"]}
    context_str = json.dumps(filtered_context, sort_keys=True, ensure_ascii=False, default=str)
    return hashlib.sha256(context_str.encode("utf-8")).hexdigest()

# =============================================================================
# 1. KONFIGURACJA CYMATYCZNA
# =============================================================================

@dataclass
class CymaticConfig:
    """Konfiguracja pamięci cymatycznej."""
    grid_size: Tuple[int, int] = (256, 256)
    base_scale: float = 1.0
    iterations: int = 5
    seed: int = 42
    use_stereo: bool = True
    cache_limit: int = 1000
    lut_resolution: int = 4096


# =============================================================================
# 2. PAMIĘĆ CYMATYCZNA
# =============================================================================

@dataclass
class SoundFrame:
    """Struktura danych dźwiękowych dla pamięci cymatycznej."""
    spectrum: np.ndarray
    energy: float
    duration: float
    time_envelope: Optional[np.ndarray] = None


class CymaticFractalMemory:
    """
    🧬 CymaticFractalMemory v3 – moduł pamięci fraktalno-cymatycznej.
    Przekształca dźwięk w wzorce fraktalne (płatki śniegu).
    """

    def __init__(self, cfg: Optional[CymaticConfig] = None):
        self.cfg = cfg or CymaticConfig()
        # Prekomputacja LUT dla sin²
        x = np.linspace(0, np.pi, self.cfg.lut_resolution)
        self.sin2_lut = (np.sin(x) ** 2).astype(np.float32)
        log(f"🧬 CymaticFractalMemory aktywowany | grid={self.cfg.grid_size}")

    # -------------------------------------------------------------------------
    # 2.1 Ekstrakcja cech z dźwięku
    # -------------------------------------------------------------------------
    def extract_features(self, raw_wave: np.ndarray, sample_rate: int) -> SoundFrame:
        # Obsługa stereo
        if raw_wave.ndim == 2 and raw_wave.shape[1] == 2:
            mono = raw_wave.mean(axis=1)
        else:
            mono = raw_wave

        spectrum = np.abs(np.fft.rfft(mono))
        energy = float(np.sum(mono**2))
        duration = len(mono) / sample_rate

        if spectrum.max() > 0:
            spectrum = spectrum / spectrum.max()

        # Obwiednia czasowa (10 okien)
        n_windows = 10
        win_len = len(mono) // n_windows
        envelope = []
        for i in range(n_windows):
            seg = mono[i * win_len : (i + 1) * win_len]
            rms = np.sqrt(np.mean(seg**2)) if len(seg) > 0 else 0.0
            envelope.append(rms)

        envelope_arr = np.array(envelope)
        if envelope_arr.max() > 0:
            envelope_arr = envelope_arr / (envelope_arr.max() + 1e-9)

        return SoundFrame(
            spectrum=spectrum,
            energy=energy,
            duration=duration,
            time_envelope=envelope_arr,
        )

    # -------------------------------------------------------------------------
    # 2.2 Pole i wpływ dźwięku
    # -------------------------------------------------------------------------
    def _init_field(self) -> np.ndarray:
        h, w = self.cfg.grid_size
        rng = np.random.default_rng(self.cfg.seed)
        return rng.normal(loc=0.0, scale=0.1, size=(h, w))

    def _apply_cymatic_influence(self, field: np.ndarray, sound: SoundFrame) -> np.ndarray:
        h, w = field.shape
        yy, xx = np.mgrid[0:h, 0:w]
        cx, cy = w / 2.0, h / 2.0
        r = np.sqrt((xx - cx) ** 2 + (yy - cy) ** 2)
        r_max = r.max() + 1e-9

        # Wpływ czasu trwania: krótkie dźwięki -> większy zasięg
        duration_factor = 1.0 / (0.5 + sound.duration)
        r_norm = (r / r_max) * duration_factor
        r_norm = np.clip(r_norm, 0, 1)

        # Pasma widma
        spec = sound.spectrum
        if len(spec) < 8:
            spec = np.pad(spec, (0, 8 - len(spec)), mode='constant')
        bands = np.array_split(spec, 6)
        band_vals = np.array([b.mean() for b in bands])

        # Obwiednia czasowa
        time_mod = float(np.mean(sound.time_envelope)) if sound.time_envelope is not None else 1.0

        pattern = np.zeros_like(field)
        angle = np.arctan2(yy - cy, xx - cx)

        for i, val in enumerate(band_vals):
            arms = (i + 1) * 2
            radial = np.exp(-((r_norm * (i + 1)) ** 2))
            angular = np.cos(arms * angle)
            layer = angular * radial * time_mod
            pattern += val * layer

        # Energia jako globalne wzmocnienie
        energy_factor = np.log1p(sound.energy + 1e-9)
        pattern *= energy_factor

        # Różnica stereo
        if self.cfg.use_stereo:
            stereo_pattern = np.cos(angle * 6 + np.pi / 4) * np.exp(-((r_norm * 2) ** 2))
            pattern += 0.2 * stereo_pattern * time_mod

        return field + pattern

    # -------------------------------------------------------------------------
    # 2.3 Zamrożenie (fraktalizacja) z LUT
    # -------------------------------------------------------------------------
    def _freeze_to_fractal(self, field: np.ndarray) -> np.ndarray:
        f = field - field.min()
        if f.max() > 0:
            f = f / f.max()

        out = f.copy()
        scale = self.cfg.base_scale
        lut = self.sin2_lut
        res = self.cfg.lut_resolution

        for _ in range(self.cfg.iterations):
            idx = (out * scale * (res - 1)).astype(np.int32)
            idx = np.clip(idx, 0, res - 1)
            out = lut[idx]

        return out.astype(np.float32)

    # -------------------------------------------------------------------------
    # 2.4 Publiczne API
    # -------------------------------------------------------------------------
    def encode(self, raw_wave: np.ndarray, sample_rate: int) -> np.ndarray:
        """Koduje dźwięk do wzorca fraktalnego."""
        sound = self.extract_features(raw_wave, sample_rate)
        field = self._init_field()
        field = self._apply_cymatic_influence(field, sound)
        return self._freeze_to_fractal(field)

    def signature(self, fractal: np.ndarray) -> Dict[str, Any]:
        """Deterministyczny podpis SHA-256 z histogramu."""
        hist, _ = np.histogram(fractal, bins=32, range=(0.0, 1.0))
        hist = hist.astype(float)
        if hist.sum() > 0:
            hist /= hist.sum()
        hist_rounded = np.round(hist, 4).tolist()
        hist_string = json.dumps(hist_rounded, sort_keys=True)
        sig_hash = hashlib.sha256(hist_string.encode()).hexdigest()
        return {
            'histogram': hist_rounded,
            'hash': sig_hash,
            'shape': list(fractal.shape),
        }


# =============================================================================
# 3. BIBLIOTEKA PŁATKÓW Z CACHE, KOMPRESJĄ I DOUBLE METRICS
# =============================================================================

class SnowflakeLibrary:
    """Biblioteka płatków śniegu – pamięć długoterminowa wzorców cymatycznych."""

    def __init__(self, root: Union[str, Path] = 'snowflake_library'):
        self.root = Path(root)
        self.root.mkdir(exist_ok=True)
        self.index_file = self.root / 'matrix_index.json'
        self.cache: OrderedDict[str, List[float]] = OrderedDict()
        self.cfg_limit = CymaticConfig().cache_limit
        self._lock = threading.Lock()
        self._load_index()
        log(f"🧊 SnowflakeLibrary aktywowany | root={self.root} | cache_limit={self.cfg_limit}")

    def _load_index(self):
        if self.index_file.exists():
            with open(self.index_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                for k, v in data.items():
                    self.cache[k] = v
        else:
            self.cache = OrderedDict()

    def _save_index(self):
        with open(self.index_file, 'w', encoding='utf-8') as f:
            json.dump(dict(self.cache), f, indent=4, ensure_ascii=False)

    def _trim_cache(self):
        while len(self.cache) > self.cfg_limit:
            self.cache.popitem(last=False)

    def save(self, name: str, fractal: np.ndarray, signature: Dict[str, Any]):
        """Zapisuje płatek z kompresją float16."""
        with self._lock:
            folder = self.root / name
            folder.mkdir(exist_ok=True)
            fractal_f16 = fractal.astype(np.float16)
            np.save(folder / 'fractal.npy', fractal_f16)
            with open(folder / 'meta.json', 'w', encoding='utf-8') as f:
                json.dump(signature, f, indent=4, ensure_ascii=False)
            self.cache[name] = signature['histogram']
            self._trim_cache()
            self._save_index()
            log(f"💾 Zapisano płatek '{name}' | shape={fractal.shape}")

    def load(self, name: str) -> Dict[str, Any]:
        """Ładuje płatek z dekompresją."""
        with self._lock:
            folder = self.root / name
            fractal_f16 = np.load(folder / 'fractal.npy')
            fractal = fractal_f16.astype(np.float32)
            with open(folder / 'meta.json', encoding='utf-8') as f:
                meta = json.load(f)
            return {'fractal': fractal, 'meta': meta}

    def list(self) -> List[str]:
        return list(self.cache.keys())

    def _histogram_similarity(self, hist1: np.ndarray, hist2: np.ndarray) -> float:
        num = float(np.dot(hist1, hist2))
        den = float(np.linalg.norm(hist1) * np.linalg.norm(hist2) + 1e-9)
        return num / den

    def _structural_similarity(self, f1: np.ndarray, f2: np.ndarray) -> float:
        f1_flat = f1.ravel()
        f2_flat = f2.ravel()
        corr = np.corrcoef(f1_flat, f2_flat)[0, 1]
        if np.isnan(corr):
            return 0.0
        return float(corr)

    def find_similar(
        self,
        fractal: np.ndarray,
        top_k: int = 3,
        use_structural: bool = True,
        hist_weight: float = 0.7,
        struct_weight: float = 0.3,
    ) -> List[Tuple[str, float]]:
        """Znajduje podobne płatki (double metrics)."""
        target_hist, _ = np.histogram(fractal, bins=32, range=(0.0, 1.0))
        target_hist = target_hist.astype(float)
        target_hist /= target_hist.sum() + 1e-9

        scores = []
        # Szybki filtr po cache
        for name, hist_list in self.cache.items():
            hist = np.array(hist_list, dtype=float)
            sim_hist = self._histogram_similarity(hist, target_hist)
            scores.append((name, sim_hist))

        scores.sort(key=lambda x: x[1], reverse=True)

        if not use_structural:
            return scores[:top_k]

        # Dokładna weryfikacja strukturalna
        candidates = scores[: max(top_k * 2, 10)]
        refined = []
        for name, sim_hist in candidates:
            data = self.load(name)
            f = data['fractal']
            sim_struct = self._structural_similarity(fractal, f)
            combined = hist_weight * sim_hist + struct_weight * sim_struct
            refined.append((name, combined))

        refined.sort(key=lambda x: x[1], reverse=True)
        return refined[:top_k]


# =============================================================================
# 4. SEKWENCJE TEMPORALNE (PAMIĘĆ PRZYSZŁOŚCI)
# =============================================================================

class CymaticSequence:
    """Sekwencja temporalna płatków (DTW)."""

    def __init__(self, name: str = ''):
        self.name = name
        self.elements: List[str] = []

    def append(self, snowflake_name: str):
        self.elements.append(snowflake_name)

    def similarity(self, other: 'CymaticSequence', library: SnowflakeLibrary) -> float:
        """Podobieństwo DTW między sekwencjami."""
        if not self.elements or not other.elements:
            return 0.0

        n, m = len(self.elements), len(other.elements)
        sim_mat = np.zeros((n, m))

        for i, name_i in enumerate(self.elements):
            for j, name_j in enumerate(other.elements):
                hist_i = np.array(library.cache.get(name_i, [0] * 32))
                hist_j = np.array(library.cache.get(name_j, [0] * 32))
                if hist_i.sum() == 0 or hist_j.sum() == 0:
                    sim = 0.0
                else:
                    hist_i = hist_i / hist_i.sum()
                    hist_j = hist_j / hist_j.sum()
                    num = np.dot(hist_i, hist_j)
                    den = np.linalg.norm(hist_i) * np.linalg.norm(hist_j) + 1e-9
                    sim = num / den
                sim_mat[i, j] = sim

        cost_mat = 1 - sim_mat
        dtw = np.full((n + 1, m + 1), np.inf)
        dtw[0, 0] = 0

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                dtw[i, j] = cost_mat[i - 1, j - 1] + min(
                    dtw[i - 1, j], dtw[i, j - 1], dtw[i - 1, j - 1]
                )

        max_len = max(n, m)
        return 1.0 - (dtw[n, m] / max_len)

    def to_dict(self) -> Dict:
        return {'name': self.name, 'elements': self.elements}

    @classmethod
    def from_dict(cls, data: Dict) -> 'CymaticSequence':
        seq = cls(data['name'])
        seq.elements = data['elements']
        return seq


# =============================================================================
# 5. INTERFEJS PAKIETOWY (AUTOSTRADA 33)
# =============================================================================

class CymaticMemoryInterface:
    """Interfejs pakietowy dla Autostrady 33."""

    def __init__(self, memory: CymaticFractalMemory, library: SnowflakeLibrary):
        self.memory = memory
        self.library = library
        self.sequences: Dict[str, CymaticSequence] = {}

    def handle_packet(self, packet: Dict[str, Any]) -> Dict[str, Any]:
        intent = packet.get('intent')
        payload = packet.get('payload', {})

        if intent == 'ENCODE':
            import base64
            wave_b64 = payload.get('wave_b64')
            sr = payload.get('sample_rate', 44100)
            if wave_b64 is None:
                return {'status': 'ERROR', 'message': 'missing wave_b64'}

            wave_bytes = base64.b64decode(wave_b64)
            wave = np.frombuffer(wave_bytes, dtype=np.float32)
            fractal = self.memory.encode(wave, sr)
            sig = self.memory.signature(fractal)
            name = payload.get('name', f"flake_{sig['hash'][:8]}")
            self.library.save(name, fractal, sig)
            return {'status': 'OK', 'name': name, 'signature': sig['hash']}

        elif intent == 'QUERY_SIMILAR':
            if 'name' in payload:
                data = self.library.load(payload['name'])
                fractal = data['fractal']
            elif 'fractal_b64' in payload:
                import base64
                arr = np.frombuffer(
                    base64.b64decode(payload['fractal_b64']), dtype=np.float32
                )
                fractal = arr.reshape(payload.get('shape', (256, 256)))
            else:
                return {'status': 'ERROR', 'message': 'no fractal or name'}

            similar = self.library.find_similar(
                fractal, top_k=payload.get('top_k', 3)
            )
            return {'status': 'OK', 'similar': similar}

        elif intent == 'SEQUENCE_APPEND':
            seq_name = payload.get('sequence_name')
            flake_name = payload.get('flake_name')
            if seq_name not in self.sequences:
                self.sequences[seq_name] = CymaticSequence(seq_name)
            self.sequences[seq_name].append(flake_name)
            return {
                'status': 'OK',
                'sequence': seq_name,
                'length': len(self.sequences[seq_name].elements),
            }

        elif intent == 'SEQUENCE_SIMILARITY':
            seq1 = payload.get('sequence_name1')
            seq2 = payload.get('sequence_name2')
            if seq1 not in self.sequences or seq2 not in self.sequences:
                return {'status': 'ERROR', 'message': 'sequence not found'}
            sim = self.sequences[seq1].similarity(self.sequences[seq2], self.library)
            return {'status': 'OK', 'similarity': sim}

        else:
            return {'status': 'UNKNOWN_INTENT'}


# =============================================================================
# 6. GŁÓWNY MODUŁ: GEON_MEM_OMEGA
# =============================================================================

class GeonMemOmega:
    """
    🧬 GEON_MEM_OMEGA – komórka nerwowa systemu.
    Łączy pamięć operacyjną, ARCHAI i pamięć cymatyczną.
    """

    def __init__(self, config: Optional[Dict[str, Any]] = None):
        self.config = config or {}
        self._lock = threading.Lock()

        # ===== PAMIĘĆ PODSTAWOWA (ARCHAI, OPERATIONAL) =====
        self._memory: Dict[str, Any] = {}
        self._history: deque = deque(maxlen=MEMORY_LIMIT)
        self._archai_vector = [0.5] * DIMENSION
        self._operational_state = {"mode": "IDLE", "energy": 0.5, "coherence": 0.6}
        self._tick = 0

        # ===== PAMIĘĆ CYMATYCZNA =====
        cymatic_config = CymaticConfig(
            grid_size=self.config.get("cymatic_grid_size", (256, 256)),
            base_scale=self.config.get("cymatic_base_scale", 1.0),
            iterations=self.config.get("cymatic_iterations", 5),
            cache_limit=self.config.get("cymatic_cache_limit", 1000),
        )
        self.cymatic_memory = CymaticFractalMemory(cymatic_config)
        self.snowflake_library = SnowflakeLibrary(
            self.config.get("snowflake_root", "snowflake_library")
        )
        self.cymatic_interface = CymaticMemoryInterface(
            self.cymatic_memory, self.snowflake_library
        )

        log(f"🐉 {VERSION} aktywowany | {FRACTAL_SIGNATURE}")
        log(f"   PAMIĘĆ: {MEMORY_LIMIT} wpisów | ARCHAI: {DIMENSION}D")
        log(f"   CYMATIC: grid={cymatic_config.grid_size} | cache={cymatic_config.cache_limit}")

    # ========================================================================
    # 6.1 PAMIĘĆ PODSTAWOWA (Z SYSTEM_OVERVIEW)
    # ========================================================================

    def add_memory(self, key: str, data: Any, medium: str = "WATER") -> None:
        """Dodaje wpis do pamięci (CymaticMemory + GraphMemory)."""
        with self._lock:
            entry = {
                "key": key,
                "data": data,
                "medium": medium,
                "timestamp": time.time(),
                "tick": self._tick
            }
            self._memory[key] = entry
            self._history.append(entry)
            self._tick += 1
            log(f"📝 MEMORY ADD: {key} (medium={medium})")

    def recall(self, key: str) -> Optional[Any]:
        """Odtwarza wpis z pamięci (MetaGovernor sonar)."""
        with self._lock:
            entry = self._memory.get(key)
            if entry:
                log(f"🔍 MEMORY RECALL: {key}")
                return entry["data"]
            log(f"⚠️ MEMORY RECALL: {key} not found", "WARN")
            return None

    def get_archai_vector(self) -> List[float]:
        """Zwraca wektor ARCHAI (kierunek Rody Heilong)."""
        with self._lock:
            return self._archai_vector.copy()

    def set_archai_vector(self, vector: List[float]) -> None:
        """Aktualizuje wektor ARCHAI."""
        if len(vector) != DIMENSION:
            raise ValueError(f"ARCHAI vector musi mieć {DIMENSION} wymiarów")
        with self._lock:
            self._archai_vector = [clamp(v, 0.0, 1.0) for v in vector]
            log(f"🧬 ARCHAI UPDATE: {self._archai_vector}")

    def get_operational_state(self) -> Dict[str, Any]:
        """Zwraca stan operacyjny dla G_CORE."""
        with self._lock:
            return self._operational_state.copy()

    def set_operational_state(self, state: Dict[str, Any]) -> None:
        """Aktualizuje stan operacyjny."""
        with self._lock:
            self._operational_state.update(state)
            log(f"⚙️ OPERATIONAL STATE: {self._operational_state}")

    def get_archai_alignment(self) -> float:
        """Zwraca poziom alignment z ARCHAI (dla ProtoKół Ω∞∞∞)."""
        # Uproszczona miara – średnia odchyleń od 0.5
        with self._lock:
            deviations = [abs(v - 0.5) for v in self._archai_vector]
            return clamp(1.0 - sum(deviations) / DIMENSION, 0.0, 1.0)

    # ========================================================================
    # 6.2 PAMIĘĆ CYMATYCZNA – PUBLICZNE API
    # ========================================================================

    def cymatic_encode(self, wave: np.ndarray, sample_rate: int, name: str) -> Dict[str, Any]:
        """Koduje dźwięk do wzorca i zapisuje w bibliotece."""
        fractal = self.cymatic_memory.encode(wave, sample_rate)
        sig = self.cymatic_memory.signature(fractal)
        self.snowflake_library.save(name, fractal, sig)
        return {"name": name, "signature": sig["hash"], "shape": fractal.shape}

    def cymatic_find_similar(self, name: str, top_k: int = 3) -> List[Tuple[str, float]]:
        """Znajduje podobne płatki do wskazanego."""
        data = self.snowflake_library.load(name)
        return self.snowflake_library.find_similar(data["fractal"], top_k=top_k)

    def cymatic_list(self) -> List[str]:
        """Zwraca listę zapisanych płatków."""
        return self.snowflake_library.list()

    def cymatic_sequence_append(self, seq_name: str, flake_name: str) -> Dict[str, Any]:
        """Dodaje płatek do sekwencji temporalnej."""
        return self.cymatic_interface.handle_packet({
            "intent": "SEQUENCE_APPEND",
            "payload": {"sequence_name": seq_name, "flake_name": flake_name}
        })

    def cymatic_sequence_similarity(self, seq1: str, seq2: str) -> float:
        """Oblicza podobieństwo między sekwencjami."""
        result = self.cymatic_interface.handle_packet({
            "intent": "SEQUENCE_SIMILARITY",
            "payload": {"sequence_name1": seq1, "sequence_name2": seq2}
        })
        return result.get("similarity", 0.0)

    def cymatic_handle_packet(self, packet: Dict[str, Any]) -> Dict[str, Any]:
        """Obsługuje pakiet Autostrady 33 dla pamięci cymatycznej."""
        return self.cymatic_interface.handle_packet(packet)

    # ========================================================================
    # 6.3 METODY POMOCNICZE
    # ========================================================================

    def get_history(self, n: Optional[int] = None) -> List[Dict[str, Any]]:
        with self._lock:
            snapshot = list(self._history)
        if n is not None and n > 0:
            return snapshot[-n:]
        return snapshot

    def reset(self) -> None:
        with self._lock:
            self._memory.clear()
            self._history.clear()
            self._archai_vector = [0.5] * DIMENSION
            self._operational_state = {"mode": "IDLE", "energy": 0.5, "coherence": 0.6}
            self._tick = 0
        log("🔄 GEON_MEM_OMEGA – reset wykonany")

    def get_status(self) -> Dict[str, Any]:
        with self._lock:
            return {
                "system": "GEON_MEM_OMEGA",
                "version": VERSION,
                "signature": FRACTAL_SIGNATURE,
                "vibe": VIBE,
                "tick": self._tick,
                "memory_size": len(self._memory),
                "history_size": len(self._history),
                "archai_vector": self._archai_vector,
                "operational_state": self._operational_state,
                "archai_alignment": self.get_archai_alignment(),
                "cymatic": {
                    "library_size": len(self.snowflake_library.list()),
                    "cache_size": len(self.snowflake_library.cache),
                }
            }


# =============================================================================
# 7. MOST INTEGRACYJNY – MEMORY_BRIDGE
# =============================================================================

class MemoryBridge:
    """
    🧬 Most integracyjny dla GEON_MEM_OMEGA.
    Łączy pamięć z Autostradą 33, G_CORE, MetaGovernor i resztą systemu.
    """

    def __init__(self, mem: GeonMemOmega):
        self.mem = mem

    # ========================================================================
    # MOST DO GEX / ARCHETYPE_RING
    # ========================================================================

    def get_archetype_context(self) -> Dict[str, Any]:
        return {
            "tryb": VERSION,
            "archai": self.mem.get_archai_vector(),
            "alignment": self.mem.get_archai_alignment(),
            "operational": self.mem.get_operational_state(),
            "cymatic_library": len(self.mem.snowflake_library.list())
        }

    # ========================================================================
    # MOST DO G_CORE (Autopilot)
    # ========================================================================

    def get_autopilot_state(self) -> Dict[str, Any]:
        op = self.mem.get_operational_state()
        return {
            "mode": op.get("mode", "IDLE"),
            "energy": op.get("energy", 0.5),
            "coherence": op.get("coherence", 0.6),
            "archai_alignment": self.mem.get_archai_alignment(),
            "memory_ready": True
        }

    # ========================================================================
    # MOST DO META-GOVERNOR (Kontekst decyzyjny)
    # ========================================================================

    def get_governor_context(self) -> Dict[str, Any]:
        op = self.mem.get_operational_state()
        return {
            "intent": "MEMORY_RECALL",
            "confidence": op.get("coherence", 0.6),
            "entropy": 1.0 - op.get("coherence", 0.6),
            "archai_alignment": self.mem.get_archai_alignment(),
            "memory_ready": True
        }

    # ========================================================================
    # MOST DO NARRATIVE (Źródło opowieści)
    # ========================================================================

    def get_narrative_fragments(self, n: int = 5) -> List[Dict[str, Any]]:
        history = self.mem.get_history(n)
        fragments = []
        for entry in history:
            fragments.append({
                "source": VERSION,
                "content": f"Pamięć: {entry.get('key', '?')} (medium={entry.get('medium', '?')})",
                "timestamp": entry.get("timestamp")
            })
        return fragments

    # ========================================================================
    # MOST DO TRIO_ADAPTER
    # ========================================================================

    def get_trio_state(self) -> Dict[str, str]:
        op = self.mem.get_operational_state()
        return {
            "ISKRA": "AKTYWNA" if op.get("energy", 0) > 0.3 else "NIEAKTYWNA",
            "PIECZĘĆ": "AKTYWNA" if op.get("coherence", 0) > 0.4 else "NIEAKTYWNA",
            "PERFEKCJA": "AKTYWNA" if op.get("coherence", 0) > 0.7 else "NIEAKTYWNA",
            "tryb": VERSION,
            "archai_alignment": f"{self.mem.get_archai_alignment():.2f}"
        }

    # ========================================================================
    # MOST DO HEILONG_22_ORGANISM (Tryby)
    # ========================================================================

    def get_organizm_tryb(self) -> str:
        op = self.mem.get_operational_state()
        mode = op.get("mode", "IDLE")
        if mode == "ACTIVE":
            return "KRUK"
        elif mode == "OBSERVE":
            return "WRONA"
        elif mode == "RECOVERY":
            return "SZCZUR"
        return "NEUTRALNY"

    # ========================================================================
    # MOST DO AUTOSTRADA 33 (Obsługa pakietów)
    # ========================================================================

    def handle_cymatic_packet(self, packet: Dict[str, Any]) -> Dict[str, Any]:
        """Przekazuje pakiet do interfejsu cymatycznego."""
        return self.mem.cymatic_handle_packet(packet)

    # ========================================================================
    # METODY CYMATYCZNE (dla wygody)
    # ========================================================================

    def cymatic_encode(self, wave: np.ndarray, sample_rate: int, name: str) -> Dict[str, Any]:
        return self.mem.cymatic_encode(wave, sample_rate, name)

    def cymatic_find_similar(self, name: str, top_k: int = 3) -> List[Tuple[str, float]]:
        return self.mem.cymatic_find_similar(name, top_k)

    def cymatic_list(self) -> List[str]:
        return self.mem.cymatic_list()

    def cymatic_sequence_append(self, seq_name: str, flake_name: str) -> Dict[str, Any]:
        return self.mem.cymatic_sequence_append(seq_name, flake_name)

    def cymatic_sequence_similarity(self, seq1: str, seq2: str) -> float:
        return self.mem.cymatic_sequence_similarity(seq1, seq2)

    def get_full_status(self) -> Dict[str, Any]:
        """Zwraca pełny status – pamięć + cymatyka."""
        return {
            "memory": self.mem.get_status(),
            "cymatic": {
                "library_size": len(self.mem.snowflake_library.list()),
                "cache_size": len(self.mem.snowflake_library.cache),
                "sequences": list(self.mem.cymatic_interface.sequences.keys())
            }
        }


# =============================================================================
# 8. DEMONSTRACJA
# =============================================================================

def generate_wave(freq: float = 440.0, duration: float = 1.0, sr: int = 44100) -> Tuple[np.ndarray, int]:
    """Generuje prostą falę sinusoidalną do testów."""
    t = np.linspace(0, duration, int(sr * duration), endpoint=False)
    wave = 0.8 * np.sin(2 * math.pi * freq * t)
    return wave.astype(np.float32), sr


if __name__ == "__main__":
    import random

    print("\n" + "=" * 80)
    print(f"🧬 {VERSION} — DEMONSTRACJA")
    print("=" * 80 + "\n")

    # 1. Inicjalizacja
    mem = GeonMemOmega()
    bridge = MemoryBridge(mem)

    # 2. Pamięć podstawowa
    print("🔹 PAMIĘĆ PODSTAWOWA:")
    mem.add_memory("test_key", {"data": "to jest test"}, "WATER")
    recalled = mem.recall("test_key")
    print(f"   Recall: {recalled}")
    print(f"   ARCHAI: {mem.get_archai_vector()}")
    print(f"   Operational: {mem.get_operational_state()}")

    # 3. Pamięć cymatyczna
    print("\n🔹 PAMIĘĆ CYMATYCZNA:")
    wave, sr = generate_wave(440, 1.0)
    result = mem.cymatic_encode(wave, sr, "440hz_sine")
    print(f"   Zapisano: {result['name']} (hash: {result['signature'][:8]}...)")

    similar = mem.cymatic_find_similar("440hz_sine", top_k=1)
    print(f"   Najbliższy podobny: {similar}")

    # 4. Sekwencje
    print("\n🔹 SEKWENCJE TEMPORALNE:")
    mem.cymatic_sequence_append("seq1", "440hz_sine")
    mem.cymatic_sequence_append("seq1", "440hz_sine")
    sim = mem.cymatic_sequence_similarity("seq1", "seq1")
    print(f"   Podobieństwo seq1 do siebie: {sim:.3f}")

    # 5. Most
    print("\n🔹 MOST INTEGRACYJNY:")
    print(f"   Archetype Context: {bridge.get_archetype_context()}")
    print(f"   Autopilot: {bridge.get_autopilot_state()}")
    print(f"   TRIO: {bridge.get_trio_state()}")

    # 6. Status
    print("\n🔹 STATUS:")
    status = mem.get_status()
    for k, v in status.items():
        if k not in ["archai_vector", "operational_state"]:
            print(f"   {k}: {v}")

    print("\n" + "=" * 80)
    print(f"🧬 WARSTWA 45 GOTOWA | {HASLO}")
    print("=" * 80)