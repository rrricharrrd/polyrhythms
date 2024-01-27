import asyncio
import logging

import streamlit as st

from polyrhythms import Player, Polyrhythm, Tone

st.title("Polyrhythm Practice")


pr = Polyrhythm()
player = Player(pr)


def tempo_change():
    player.stop()


def start_player():
    logging.debug("Starting")
    asyncio.run(player.start())


def stop_player():
    logging.debug("Stopping")
    player.stop()


tempo = st.sidebar.slider("Tempo", min_value=10, max_value=180, value=60, step=1, on_change=tempo_change)
rhythm1 = st.sidebar.number_input("Rhythm 1", min_value=1, max_value=10, value=None, step=1)
rhythm2 = st.sidebar.number_input("Rhythm 2", min_value=1, max_value=10, value=None, step=1)

if rhythm1 is not None:
    pr.add_rhythm(int(rhythm1), Tone.A)
if rhythm2 is not None:
    pr.add_rhythm(int(rhythm2), Tone.E)
pr.set_tempo(tempo)


if not (rhythm1 is None and rhythm2 is None):
    start = st.button("Start", on_click=start_player)
    stop = st.button("Stop", on_click=stop_player)
