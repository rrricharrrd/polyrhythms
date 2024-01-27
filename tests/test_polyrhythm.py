import numpy as np

from polyrhythms import Polyrhythm, Tone


async def test_basic():
    pr = Polyrhythm()
    pr.add_rhythm(2, Tone.A)
    pr.add_rhythm(3, Tone.E)
    pr.set_tempo(60)
    async for beep in pr.play():
        import pdb

        pdb.set_trace()
        assert isinstance(beep, np.ndarray)  # TODO more
        break
