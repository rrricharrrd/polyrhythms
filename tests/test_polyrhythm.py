import numpy as np

from polyrhythms import Polyrhythm, Tone


def test_basic():
    pr = Polyrhythm()
    pr.add_rhythm(2, Tone.A)
    pr.add_rhythm(3, Tone.E)
    pr.set_tempo(60)
    beep = next(pr.play())
    assert isinstance(beep, np.ndarray)  # TODO more
