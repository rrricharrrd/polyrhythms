import asyncio
import logging
import math
from typing import AsyncGenerator

import numpy as np

from polyrhythms import Tone
from polyrhythms.settings import BEEP_DURATION, SAMPLE_RATE, VOLUME_FACTOR


class Polyrhythm:
    def __init__(self):
        self._beats = []
        self._freqs = []
        self._subdivision = 1
        self._beat_interval = None
        self._signals = []
        self._duration = BEEP_DURATION
        self._volume_factor = VOLUME_FACTOR
        self._stopped = True

    def add_rhythm(self, beats: int, tone: Tone = Tone.A) -> None:
        self._beats.append(beats)
        self._freqs.append(tone.frequency)
        self._subdivision = math.lcm(*self._beats)

    def set_tempo(self, bpm: int = 60) -> None:
        self._beat_interval = 60 / bpm / self._subdivision  # Calculate minimal time between beeps
        logging.debug(f"Interval {self._beat_interval}")
        self._duration = min(BEEP_DURATION, 0.98 * self._beat_interval)  # Ensure that beeps fit
        t = np.linspace(0, self._duration, int(self._duration * SAMPLE_RATE), endpoint=False)
        self._signals = [self._volume_factor * np.sin(2 * np.pi * freq * t) for freq in self._freqs]

    async def play_once(self) -> AsyncGenerator[np.ndarray, None]:
        for i in range(self._subdivision):  # One complete iteration over the entire for-loop is one beat
            signals = []
            log_str = ""
            for ix, b in enumerate(self._beats):
                if i % b == 0:
                    log_str += str(b)
                    signals.append(self._signals[ix])
            logging.debug(log_str)
            if signals:
                signal = sum(signals)
                yield signal
            await asyncio.sleep(self._beat_interval - self._duration)

    async def play(self) -> AsyncGenerator[np.ndarray, None]:
        self._stopped = False
        while not self._stopped:
            async for signal in self.play_once():
                yield signal

    def stop(self) -> None:
        self._stopped = True
