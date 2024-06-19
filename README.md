# Polyrhythms

The term "polyrhythm" denotes a musical pattern whereby two (or more) rhythms are played simultaneously,
but which do not directly overlap with each other.
For example, for a given beat, you can have two rhythms playing at the same time,
one of which subdivides each beat into two, and the other into three (this is often called a *hemiola*).
See [wikipedia](https://en.wikipedia.org/wiki/Polyrhythm) article for more information.

When learning the piano (or any other instrument which can produce multiple musical lines at once), polyrhythms can be tricky.
At a slow enough tempo, it is possible to count according to a subdivision of the beat that encompasses both rhythms:
for example, to play a 3:2 polyrhythm, you can count up to 6 quickly in your head and play on the relevant subdivisions
(e.g. 1 and 4 for the "2" rhythm: 1, 3, and 5 for the "3" rhythm).
However, for more complicated polyrhythms at higher tempos,
such an approach is unfeasible and you simply have to learn to "feel it".
This library provides tools to help develop that feel.

## Installation
Install using `pip` from root of repository:

```bash
pip install .
```

## Development
It is recommended to use the provided pre-commit hook configuration. Run:

```bash
pip install pre-commit
pre-commit install
pre-commit run --all-files
```

## CLI
Installing the package also installs a command-line script. For example, to play a 3:2 polyrhythm at 60 bpm:

```bash
play-polyrhythm -t 60 -r 2 3
```

See `play-polyrhythm --help` for full options.

### API
See `Player`, `Polyrhythm`, `Tone` classes. TODO more info...