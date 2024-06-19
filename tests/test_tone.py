from polyrhythms import A_FREQUENCY, Tone


def test_a() -> None:
    assert Tone.A.frequency == A_FREQUENCY


def test_octave() -> None:
    for tone in Tone:
        assert A_FREQUENCY <= tone.frequency < 2 * A_FREQUENCY
