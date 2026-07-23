#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🐉 GRON_ANTYSKRĘT_v2 – moduł stabilizacji wektora i anty‑skrajności
Dla CRISTAL_PALACE_OS / GEON.
Detekcja manipulacji, rozjazdów, presji totalnej.
Rezonans 1‑6‑8: suwerenność, harmonia A+S, ciągłość nacisku.
"""

from collections import deque
from dataclasses import dataclass
import hashlib
import time
from typing import Any, Dict, Literal, Optional, TypedDict

Status = Literal["OK", "ALARM"]


@dataclass
class WejscieAntySkret:
  """Dane wejściowe dla sensora. Wszystkie w skali 0.0–1.0"""

  narracja: float = 0.0  # siła narzucania narracji / redefinicji pojęć
  presja: float = 0.0  # poziom presji (żądania, ataki, spam)
  zmiany: float = 0.0  # częstotliwość zmian kierunku / intencji
  konflikty: float = 0.0  # poziom sprzeczności w systemie
  zasady: float = 0.0  # 0 = zasady stabilne, 1 = totalna niestabilność


@dataclass
class KonfiguracjaAntySkret:
  base_threshold: float = 0.6
  suwerennosc_weight: float = 1.0
  harmonia_weight: float = 1.0
  ciaglosc_weight: float = 1.0
  hysteresis_ticks: int = 3  # liczba ticków do zmiany statusu
  syzyf_window: int = 10  # okno dla detekcji powtarzalnych manipulacji
  syzyf_threshold: int = 5  # ile razy ten sam hash w oknie = anomalia


class AntySkretResult(TypedDict):
  status: Status
  rekomendacja: str
  akcja_systemowa: Dict[str, Any]
  telemetry: Dict[str, Any]


class FolwarkSensor:
  """Wczesna faza: konflikt przy niestabilnych zasadach"""

  def evaluate(self, we: WejscieAntySkret) -> float:
    raw = we.konflikty * we.zasady
    return min(1.0, raw * 1.2)


class KataloniaSensor:
  """Rozjazd od wektora PRIME: zmiany + konflikty"""

  def evaluate(self, we: WejscieAntySkret) -> float:
    raw = (we.zmiany + we.konflikty) / 2.0
    return min(1.0, raw**1.5)


class Orwell1984Sensor:
  """Późna faza: presja + narracja"""

  def evaluate(self, we: WejscieAntySkret) -> float:
    combined = (we.narracja + we.presja) / 2.0
    if combined <= 0.5:
      return combined * 0.8
    else:
      return min(1.0, 0.4 + (combined - 0.5) * 1.6)


class SyzyfSensor:
  """Wykrywa powtarzalne, cykliczne manipulacje."""

  def __init__(self, window: int = 10, threshold: int = 5):
    self.window = window
    self.threshold = threshold
    self.history = deque(maxlen=window)

  def _hash_intencji(self, pakiet: Dict[str, Any]) -> str:
    key = f"{pakiet.get('intent','')}{pakiet.get('target','')}{pakiet.get('payload','')}"
    return hashlib.md5(key.encode()).hexdigest()

  def evaluate(self, pakiet: Dict[str, Any]) -> float:
    if not pakiet:
      return 0.0
    h = self._hash_intencji(pakiet)
    self.history.append(h)
    counts: Dict[str, int] = {}
    for x in self.history:
      counts[x] = counts.get(x, 0) + 1
    max_repeat = max(counts.values()) if counts else 0
    if max_repeat >= self.threshold:
      return min(1.0, (max_repeat - self.threshold + 1) / self.threshold)
    return 0.0


class DynamicznyProg168:

  def __init__(self, cfg: KonfiguracjaAntySkret):
    self.cfg = cfg

  def oblicz_prog(
      self,
      we: WejscieAntySkret,
      uderza_w_suwerennosc: bool,
      harmonia_triady: float,
      ciaglosc_nacisku: float,
  ) -> float:
    prog = self.cfg.base_threshold
    # 1 – suwerenność
    if uderza_w_suwerennosc:
      prog *= 0.3
    # 6 – harmonia
    harmonia_factor = 1.0 - harmonia_triady
    prog *= 1.0 - 0.4 * harmonia_factor * self.cfg.harmonia_weight
    # 8 – ciągłość nacisku
    prog *= 1.0 - 0.5 * ciaglosc_nacisku * self.cfg.ciaglosc_weight
    return max(0.05, min(0.95, prog))


class GronAntySkret:

  def __init__(self, cfg: Optional[KonfiguracjaAntySkret] = None):
    self.cfg = cfg or KonfiguracjaAntySkret()
    self.folwark = FolwarkSensor()
    self.katalonia = KataloniaSensor()
    self.orwell = Orwell1984Sensor()
    self.syzyf = SyzyfSensor(
        window=self.cfg.syzyf_window, threshold=self.cfg.syzyf_threshold
    )
    self.prog168 = DynamicznyProg168(self.cfg)

    self.last_status: Status = "OK"
    self.alarm_holdoff: int = 0
    self.ok_holdoff: int = 0
    self.tick_counter: int = 0

  def _fusion_anomalii(self, f: float, k: float, o: float, s: float) -> float:
    raw = 0.25 * f + 0.25 * k + 0.35 * o + 0.15 * s
    return min(1.0, raw)

  def _akcje_systemowe(
      self, scores: Dict[str, float], anomaly: float, status: Status
  ) -> Dict[str, Any]:
    actions: Dict[str, Any] = {}
    if status != "ALARM":
      return actions

    actions["PRIME_MIRROR"] = "ACTIVATE_MAX_DEPTH"
    actions["TENSION"] = "RESET_TO_ZERO"
    actions["FLOW"] = "RE_ALIGN_TO_PRIME_CONTINUOUS"

    if scores["folwark"] > 0.7:
      actions["FOLWARK_ACTION"] = "REDUCE_EXTERNAL_AGENTS"
    if scores["katalonia"] > 0.7:
      actions["KATALONIA_ACTION"] = "FORCE_REALIGN"
    if scores["orwell"] > 0.8:
      actions["ORWELL_ACTION"] = "ACTIVATE_SILENT_SOVEREIGN"
    if scores["syzyf"] > 0.6:
      actions["SYZYF_ACTION"] = "CLEAR_REPEATING_PATTERNS"
    if anomaly > 0.85:
      actions["EMERGENCY"] = "SHUTDOWN_EXTERNAL_COMMS"
    return actions

  def evaluate(
      self,
      wejscie: WejscieAntySkret,
      uderza_w_suwerennosc: bool = False,
      harmonia_triady: float = 1.0,
      ciaglosc_nacisku: float = 0.0,
      pakiet: Optional[Dict[str, Any]] = None,
  ) -> AntySkretResult:
    t_start = time.time()
    self.tick_counter += 1

    folwark_score = self.folwark.evaluate(wejscie)
    katalonia_score = self.katalonia.evaluate(wejscie)
    orwell_score = self.orwell.evaluate(wejscie)
    syzyf_score = self.syzyf.evaluate(pakiet or {}) if pakiet else 0.0

    scores = {
        "folwark": folwark_score,
        "katalonia": katalonia_score,
        "orwell": orwell_score,
        "syzyf": syzyf_score,
    }

    anomaly = self._fusion_anomalii(
        folwark_score, katalonia_score, orwell_score, syzyf_score
    )
    prog = self.prog168.oblicz_prog(
        wejscie, uderza_w_suwerennosc, harmonia_triady, ciaglosc_nacisku
    )

    raw_status: Status = "ALARM" if anomaly >= prog else "OK"
    status: Status = raw_status

    if (
        raw_status == "ALARM"
        and self.last_status == "OK"
        and self.alarm_holdoff > 0
    ):
      status = "OK"
      self.alarm_holdoff -= 1
    elif (
        raw_status == "OK"
        and self.last_status == "ALARM"
        and self.ok_holdoff > 0
    ):
      status = "ALARM"
      self.ok_holdoff -= 1
    else:
      if raw_status == "ALARM":
        self.ok_holdoff = self.cfg.hysteresis_ticks
        self.alarm_holdoff = 0
      else:
        self.alarm_holdoff = self.cfg.hysteresis_ticks
        self.ok_holdoff = 0
      self.last_status = status

    actions = self._akcje_systemowe(scores, anomaly, status)

    telemetry: Dict[str, Any] = {
        "raw_scores": scores,
        "anomaly": anomaly,
        "threshold": prog,
        "dynamic_factors": {
            "uderza_w_suwerennosc": uderza_w_suwerennosc,
            "harmonia_triady": harmonia_triady,
            "ciaglosc_nacisku": ciaglosc_nacisku,
        },
        "hysteresis": {
            "last_status": self.last_status,
            "alarm_holdoff": self.alarm_holdoff,
            "ok_holdoff": self.ok_holdoff,
        },
        "timestamp": t_start,
        "tick": self.tick_counter,
        "execution_time_ms": int((time.time() - t_start) * 1000),
    }

    return AntySkretResult(
        status=status,
        rekomendacja=(
            "STABILIZACJA_168" if status == "ALARM" else "OBSERWACJA"
        ),
        akcja_systemowa=actions,
        telemetry=telemetry,
    )


if __name__ == "__main__":
  cfg = KonfiguracjaAntySkret(base_threshold=0.6)
  gron = GronAntySkret(cfg)

  we = WejscieAntySkret(
      narracja=0.9, presja=0.8, zmiany=0.7, konflikty=0.6, zasady=0.9
  )

  result = gron.evaluate(
      we,
      uderza_w_suwerennosc=True,
      harmonia_triady=0.2,
      ciaglosc_nacisku=0.8,
      pakiet={"intent": "PUSH", "target": "CORE", "payload": "SPAM"},
  )

  print("Wynik GRON_ANTYSKRĘT_v2:")
  for k, v in result.items():
    print(f"  {k}: {v}")
