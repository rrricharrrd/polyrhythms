import numpy as np
import pytest

from polyrhythms import Polyrhythm, Tone


@pytest.mark.asyncio
async def test_basic():
    pr = Polyrhythm()
    pr.add_rhythm(2, Tone.A)
    pr.add_rhythm(3, Tone.E)
    pr.set_tempo(60)
    beeps = []
    async for beep in pr.play_once():
        assert isinstance(beep, np.ndarray)  # TODO more
        beeps.append(beep)
    assert len(beeps) == 4
