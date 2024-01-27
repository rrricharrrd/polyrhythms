import logging
import math
import time

import numpy as np
import sounddevice as sd

from polyrhythms.settings import A_FREQUENCY, BEEP_DURATION, E_FREQUENCY, SAMPLE_RATE, VOLUME_FACTOR


class Polyrhythm:
    def __init__(self):
        self._beats = []
        self._freqs = []
        self._subdivision = 1
        self._beat_interval = None
        self._signals = []
        self._duration = BEEP_DURATION
        self._volume_factor = VOLUME_FACTOR

    def add_rhythm(self, beats: int, frequency: int = A_FREQUENCY):
        self._beats.append(beats)
        self._freqs.append(frequency)
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


# Thanks, ChatGPT...
def metronome(beats_per_minute, duration=BEEP_DURATION):
    beat_interval = 60 / beats_per_minute

    beat = 0
    while True:
        frequency = A_FREQUENCY if beat % 2 else E_FREQUENCY

        # Generate a sine wave for the beep sound
        t = np.linspace(0, duration, int(duration * SAMPLE_RATE), endpoint=False)
        signal = VOLUME_FACTOR * np.sin(2 * np.pi * frequency * t)

        # Play the beep sound
        sd.play(signal, samplerate=SAMPLE_RATE)
        sd.wait()

        # Wait for the next beat
        time.sleep(beat_interval - duration)

        beat += 1


if __name__ == "__main__":
    pr = Polyrhythm()
    pr.add_rhythm(3, A_FREQUENCY)
    pr.add_rhythm(4, E_FREQUENCY)
    pr.set_tempo(40)
    for beep in pr.play():
        sd.play(beep, samplerate=SAMPLE_RATE)
        sd.wait()
