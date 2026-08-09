"""Step 5 \u2014 Prediction results."""

import streamlit as st

import state


def render():
    result = st.session_state.result or {}
    approved = result.get("approved")
    probability = result.get("approval_probability", 0.0)
    predicted_rate = result.get("predicted_int_rate")

    if approved:
        st.success("### Loan Approved \u2705")
    else:
        st.error("### Loan Not Approved")

    c1, c2 = st.columns(2)
    c1.metric("Approval Probability", f"{probability * 100:.1f}%")
    c2.metric("Predicted Interest Rate", f"{predicted_rate:.2f}%" if predicted_rate is not None else "N/A")

    if not approved:
        st.info(
            "This estimate is based on the details provided \u2014 a lower debt-to-income ratio, "
            "a longer credit history, or a higher FICO score generally improve approval odds. "
            "This is not a final lending decision."
        )

    st.divider()
    if st.button("Start a New Application", type="primary"):
        state.reset_form()
        st.rerun()
