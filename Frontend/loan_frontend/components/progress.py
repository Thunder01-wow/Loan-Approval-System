"""Step tracker shown above the active form."""

import streamlit as st

from config import STEPS


def render():
    items = []
    for i, label in enumerate(STEPS):
        cls = "done" if i < st.session_state.step else "current" if i == st.session_state.step else ""
        items.append(f"<div class='step-item {cls}'><span class='step-dot {cls}'></span>{label}</div>")
    st.markdown(f"<div class='step-track'>{''.join(items)}</div>", unsafe_allow_html=True)
    clamped_step = min(st.session_state.step, len(STEPS) - 1)
    st.progress(clamped_step / (len(STEPS) - 1))
