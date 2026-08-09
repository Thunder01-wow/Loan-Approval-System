"""Session state initialization and the small set of mutations allowed on it."""

import streamlit as st

from config import DEFAULT_API_URL


def init():
    if "step" not in st.session_state:
        st.session_state.step = 0
    if "data" not in st.session_state:
        st.session_state.data = {}
    if "result" not in st.session_state:
        st.session_state.result = None
    if "api_url" not in st.session_state:
        st.session_state.api_url = DEFAULT_API_URL
    if "health" not in st.session_state:
        st.session_state.health = {"status": "unknown", "latency_ms": None, "checked_at": None}
    if "submissions_this_session" not in st.session_state:
        st.session_state.submissions_this_session = 0


def go_next():
    st.session_state.step += 1


def go_back():
    st.session_state.step -= 1


def reset_form():
    st.session_state.step = 0
    st.session_state.data = {}
    st.session_state.result = None


def set_api_url(new_url: str):
    if new_url != st.session_state.api_url:
        st.session_state.api_url = new_url
        st.session_state.health = {"status": "unknown", "latency_ms": None, "checked_at": None}


def set_health(health: dict):
    st.session_state.health = health


def record_submission(result: dict):
    st.session_state.result = result
    st.session_state.submissions_this_session += 1
