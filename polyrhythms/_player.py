import logging

import sounddevice as sd

from polyrhythms import Polyrhythm
from polyrhythms.settings import SAMPLE_RATE


class Player:
    def __init__(self, polyrhythm: Polyrhythm):
        self._polyrhythm = polyrhythm
        self._is_playing = False

    def is_playing(self) -> bool:
        return self._is_playing

    async def start(self) -> None:
        self._is_playing = True
        async for beep in self._polyrhythm.play():
            sd.play(beep, samplerate=SAMPLE_RATE)
            sd.wait()
            if not self._is_playing:
                break

    def stop(self) -> None:
        logging.info("Stopping player")
        self._is_playing = False
