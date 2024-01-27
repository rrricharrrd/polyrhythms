import argparse
import asyncio
import sys

from polyrhythms import Player, Polyrhythm, Tone


def parse_args(args):
    parser = argparse.ArgumentParser()
    parser.add_argument("--tempo", "-t", type=int, default=60, help="Tempo (beats per minute)")
    parser.add_argument("--rhythms", "-r", nargs="+", help="Subdivisions of beat")
    # TODO add notes
    return parser.parse_args()


def main(argv=None):
    argv = argv or sys.argv[1:]
    args = parse_args(argv)

    pr = Polyrhythm()
    tones = [Tone.A, Tone.E]  # TODO make configurable
    for ix, rhythm in enumerate(args.rhythms):
        rhythm = int(rhythm)
        tone = tones[ix % 2]
        pr.add_rhythm(rhythm, tone)
    pr.set_tempo(args.tempo)

    player = Player(pr)
    asyncio.run(player.start())


if __name__ == "__main__":
    main()
