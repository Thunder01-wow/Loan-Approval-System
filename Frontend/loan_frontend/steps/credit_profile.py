"""Step 2 \u2014 Credit Profile."""

import streamlit as st

import state


def render(d: dict):
    st.subheader("Credit Profile")
    with st.form("credit_profile_form"):
        d["fico_score"] = st.slider(
            "FICO Credit Score", min_value=300, max_value=850,
            value=int(d.get("fico_score", 700)),
        )
        d["dti"] = st.number_input(
            "Debt-to-Income Ratio (%)", min_value=0.0, max_value=100.0,
            value=d.get("dti", 20.0), step=0.5,
            help="Total monthly debt payments divided by gross monthly income.",
        )
        d["credit_history_years"] = st.number_input(
            "Length of Credit History (years)", min_value=0.0,
            value=d.get("credit_history_years", 8.0), step=0.5,
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
