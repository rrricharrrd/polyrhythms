import sounddevice as sd  # type: ignore [import-untyped]

from polyrhythms import Polyrhythm
from polyrhythms.settings import SAMPLE_RATE


class Player:
    def __init__(self, polyrhythm: Polyrhythm):
        self._polyrhythm = polyrhythm
        self._playing = False

    async def start(self):
        self._playing = True
        async for beep in self._polyrhythm.play():
            sd.play(beep, samplerate=SAMPLE_RATE)
            sd.wait()
            if not self._playing:
                break

    def stop(self):
        self._playing = False
