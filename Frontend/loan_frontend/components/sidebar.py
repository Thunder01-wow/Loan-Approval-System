"""Sidebar: connection settings, live health check, session info, model metrics."""

import streamlit as st

import state
from api_client import check_health
from config import STEPS

_STATUS_DOT = {"up": "health-up", "down": "health-down", "unknown": "health-unknown"}
_STATUS_TEXT = {"up": "Backend reachable", "down": "Backend unreachable", "unknown": "Not checked yet"}


def render():
    with st.sidebar:
        st.markdown("### Loan Approval & Valuation")
        st.caption("2-stage ML pipeline \u2014 approval classifier + interest rate regressor")

        st.divider()
        _render_connection_section()

        st.divider()
        _render_session_section()

        st.divider()
        st.caption("Portfolio demo \u2014 predictions are estimates, not real lending decisions.")


def _render_connection_section():
    st.markdown("**API Connection**")

    with st.expander("Connection settings", expanded=False):
        new_url = st.text_input("Prediction endpoint", value=st.session_state.api_url)
        state.set_api_url(new_url)

    health = st.session_state.health
    dot_class = _STATUS_DOT[health["status"]]
    st.markdown(
        f"<span class='health-dot {dot_class}'></span>{_STATUS_TEXT[health['status']]}",
        unsafe_allow_html=True,
    )
    if health["latency_ms"] is not None:
        st.caption(f"Response time: {health['latency_ms']} ms \u00b7 checked {health['checked_at']}")
    elif health["checked_at"] is not None:
        st.caption(f"Checked {health['checked_at']}")

    if st.button("Check connection", use_container_width=True):
        with st.spinner("Pinging backend..."):
            state.set_health(check_health(st.session_state.api_url))
        st.rerun()


def _render_session_section():
    st.markdown("**Session**")
    current = STEPS[min(st.session_state.step, len(STEPS) - 1)]
    st.caption(f"Step {st.session_state.step + 1} of {len(STEPS)}: {current}")
    st.caption(f"Predictions made this session: {st.session_state.submissions_this_session}")
    if st.button("Reset application", use_container_width=True):
        state.reset_form()
        st.rerun()


