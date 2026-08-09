"""Step 3 \u2014 Optional bureau details. Blank fields are sent as null so the backend
falls back to its own training-set defaults."""

import streamlit as st

import state
from labels import BUREAU_FIELDS


def render(d: dict):
    st.subheader("Bureau Details")
    st.caption("Optional. Leave any field blank if you don't have it \u2014 the model will use "
               "dataset averages instead.")
    with st.form("bureau_details_form"):
        for key, label, help_text in BUREAU_FIELDS:
            d[key] = st.number_input(
                label, min_value=0.0, value=d.get(key, None),
                help=help_text, step=1.0, format="%.1f",
            )
        st.write("")
        c1, c2 = st.columns(2)
        back = c1.form_submit_button("\u2190 Back")
        nxt = c2.form_submit_button("Next \u2192", type="primary")

    if back:
        state.go_back()
        st.rerun()
    if nxt:
        state.go_next()
        st.rerun()
