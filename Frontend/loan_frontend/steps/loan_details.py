"""Step 0 \u2014 Loan Details."""

import streamlit as st

import state
from labels import PURPOSE_LABELS


def render(d: dict):
    st.subheader("Loan Details")
    with st.form("loan_details_form"):
        d["loan_amnt"] = st.number_input(
            "Loan Amount Requested ($)", min_value=1.0, max_value=40000.0,
            value=d.get("loan_amnt", 10000.0), step=500.0,
            help="Maximum of $40,000.",
        )
        d["term"] = st.selectbox(
            "Loan Term", options=[36, 60],
            index=[36, 60].index(d.get("term", 36)),
            format_func=lambda x: f"{x} months ({x // 12} years)",
        )
        d["purpose"] = st.selectbox(
            "Purpose of Loan", options=list(PURPOSE_LABELS.keys()),
            index=list(PURPOSE_LABELS.keys()).index(d.get("purpose", "debt_consolidation")),
            format_func=lambda k: PURPOSE_LABELS[k],
        )
        st.write("")
        if st.form_submit_button("Next \u2192", type="primary"):
            state.go_next()
            st.rerun()
