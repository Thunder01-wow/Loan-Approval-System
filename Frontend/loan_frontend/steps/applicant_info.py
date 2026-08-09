"""Step 1 \u2014 Applicant Information."""

import streamlit as st

import state
from labels import (
    APPLICATION_TYPE_LABELS,
    HOME_OWNERSHIP_LABELS,
    STATE_CODES,
    STATE_NAMES,
    VERIFICATION_LABELS,
)


def render(d: dict):
    st.subheader("Applicant Information")
    with st.form("applicant_info_form"):
        d["annual_inc"] = st.number_input(
            "Annual Income ($)", min_value=1.0,
            value=d.get("annual_inc", 60000.0), step=1000.0,
        )
        d["emp_length"] = st.slider(
            "Employment Length (years)", min_value=0.0, max_value=10.0,
            value=d.get("emp_length", 5.0), step=0.5,
            help="10 represents 10 or more years.",
        )
        d["home_ownership"] = st.selectbox(
            "Home Ownership Status", options=list(HOME_OWNERSHIP_LABELS.keys()),
            index=list(HOME_OWNERSHIP_LABELS.keys()).index(d.get("home_ownership", "RENT")),
            format_func=lambda k: HOME_OWNERSHIP_LABELS[k],
        )
        d["verification_status"] = st.selectbox(
            "Income Verification Status", options=list(VERIFICATION_LABELS.keys()),
            index=list(VERIFICATION_LABELS.keys()).index(d.get("verification_status", "Not Verified")),
        )
        d["application_type"] = st.selectbox(
            "Application Type", options=list(APPLICATION_TYPE_LABELS.keys()),
            index=list(APPLICATION_TYPE_LABELS.keys()).index(d.get("application_type", "Individual")),
            format_func=lambda k: APPLICATION_TYPE_LABELS[k],
        )
        d["addr_state"] = st.selectbox(
            "State", options=STATE_CODES,
            index=STATE_CODES.index(d.get("addr_state", "CA")),
            format_func=lambda code: f"{STATE_NAMES.get(code, code)} ({code})",
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
