"""A single reusable card renderer, used for every section of the review screen."""

import streamlit as st


def render(title: str, rows: list[tuple[str, str]]):
    """rows: list of (label, value) pairs. If empty, nothing is rendered for that pair."""
    row_html = "".join(
        f"<div class='review-row'><span>{label}</span><span>{value}</span></div>"
        for label, value in rows
    )
    st.markdown(f"<div class='review-card'><h5>{title}</h5>{row_html}</div>", unsafe_allow_html=True)
