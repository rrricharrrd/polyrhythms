from enum import IntEnum

A_FREQUENCY = 440


class Tone(IntEnum):
    A = 0
    Bb = 1
    B = 2
    C = 3
    Db = 4
    D = 5
    Eb = 6
    E = 7
    F = 8
    Gb = 9
    G = 10
    Ab = 11

    @property
    def frequency(self) -> int:
        return int(A_FREQUENCY * 2 ** (self.value / 12))
