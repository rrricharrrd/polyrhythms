import logging
import math
import time

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

    def add_rhythm(self, beats: int, tone: Tone = Tone.A):
        self._beats.append(beats)
        self._freqs.append(tone.frequency)
        self._subdivision = math.lcm(*self._beats)

    def set_tempo(self, bpm: int = 60):
        self._beat_interval = 60 / bpm / self._subdivision
        logging.debug(f"Interval {self._beat_interval}")
        t = np.linspace(0, self._duration, int(self._duration * SAMPLE_RATE), endpoint=False)
        self._signals = [self._volume_factor * np.sin(2 * np.pi * freq * t) for freq in self._freqs]

    def play(self):
        while True:
            for i in range(self._subdivision):
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
                time.sleep(self._beat_interval - BEEP_DURATION)
