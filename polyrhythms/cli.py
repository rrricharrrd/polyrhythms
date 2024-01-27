import argparse
import sys

import sounddevice as sd

from polyrhythms import Polyrhythm
from polyrhythms.settings import A_FREQUENCY, E_FREQUENCY, SAMPLE_RATE


def parse_args(args):
    parser = argparse.ArgumentParser()
    parser.add_argument("--tempo", "-t", type=int, default=60, help="Tempo (beats per minute)")
    parser.add_argument("--rhythms", "-r", nargs="+", help="Subdivions of beat")
    # TODO add notes
    return parser.parse_args()


def main(argv=None):
    argv = argv or sys.argv[1:]
    args = parse_args(argv)

    pr = Polyrhythm()
    notes = [A_FREQUENCY, E_FREQUENCY]  # TODO make configurable
    for ix, rhythm in enumerate(args.rhythms):
        rhythm = int(rhythm)
        note = notes[ix % 2]
        pr.add_rhythm(rhythm, note)
    pr.set_tempo(args.tempo)

    for beep in pr.play():
        sd.play(beep, samplerate=SAMPLE_RATE)
        sd.wait()


if __name__ == "__main__":
    main()
