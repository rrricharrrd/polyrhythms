# +
import logging
import math
import time

import numpy as np
import sounddevice as sd

from .settings import (
    A_FREQUENCY,
    BEEP_DURATION,
    E_FREQUENCY,
    SAMPLE_RATE,
    VOLUME_FACTOR,
)


class Polyrhythm:
    def __init__(self):
        self._beats = []
        self._freqs = []
        self._subdivision = 1

    def add_rhythm(self, beats: int, frequency: int = A_FREQUENCY):
        self._beats.append(beats)
        self._freqs.append(frequency)
        self._subdivision = math.lcm(*self._beats)

    def play(self, beats_per_minute: int = 20):
        beat_interval = 60 / beats_per_minute / self._subdivision
        logging.debug(f"Interval {beat_interval}")
        while True:
            for i in range(self._subdivision):
                beeps = ""
                for b in self._beats:
                    if i % b == 0:
                        beeps += str(b)
                print(beeps)
            time.sleep(beat_interval - BEEP_DURATION)


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


# # Adjust the beats_per_minute value based on your desired tempo
# metronome(beats_per_minute=120)


if __name__ == "__main__":
    pr = Polyrhythm()
    pr.add_rhythm(2)
    pr.add_rhythm(3)

    pr.play()
