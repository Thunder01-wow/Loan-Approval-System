"""Step 4 \u2014 Review everything, submit to the backend."""

import streamlit as st

import state
from api_client import submit_application
from components import review_card
from labels import (
    APPLICATION_TYPE_LABELS,
    BUREAU_FIELDS,
    HOME_OWNERSHIP_LABELS,
    PURPOSE_LABELS,
    STATE_NAMES,
    VERIFICATION_LABELS,
)


def render(d: dict):
    st.subheader("Review & Submit")

    review_card.render("Loan Details", [
        ("Amount", f"${d['loan_amnt']:,.0f} over {d['term']} months"),
        ("Purpose", PURPOSE_LABELS[d["purpose"]]),
    ])

    review_card.render("Applicant Information", [
        ("Annual Income", f"${d['annual_inc']:,.0f}"),
        ("Employment Length", f"{d['emp_length']} years"),
        ("Home Ownership", HOME_OWNERSHIP_LABELS[d["home_ownership"]]),
        ("Income Verification", VERIFICATION_LABELS[d["verification_status"]]),
        ("Application Type", APPLICATION_TYPE_LABELS[d["application_type"]]),
        ("State", STATE_NAMES.get(d["addr_state"], d["addr_state"])),
    ])

    review_card.render("Credit Profile", [
        ("FICO Score", str(d["fico_score"])),
        ("Debt-to-Income Ratio", f"{d['dti']}%"),
        ("Credit History", f"{d['credit_history_years']} years"),
    ])

    provided_bureau = [
        (label, d.get(key)) for key, label, _ in BUREAU_FIELDS if d.get(key) is not None
    ]
    review_card.render(
        "Bureau Details",
        provided_bureau if provided_bureau else [("None provided", "using dataset averages")],
    )

    if st.session_state.health["status"] == "down":
        st.warning("The prediction backend looks unreachable right now (see sidebar). "
                   "You can still submit \u2014 we'll retry the connection.")

    c1, c2 = st.columns(2)
    with c1:
        if st.button("\u2190 Back"):
            state.go_back()
            st.rerun()
    with c2:
        submit = st.button("Submit Application", type="primary")

    if submit:
        with st.spinner("Scoring application..."):
            success, result = submit_application(st.session_state.api_url, dict(d))

        if success:
            state.record_submission(result)
            state.set_health({
                "status": "up",
                "latency_ms": st.session_state.health.get("latency_ms"),
                "checked_at": st.session_state.health.get("checked_at"),
            })
            state.go_next()
            st.rerun()
        else:
            if result["error_type"] == "connection":
                state.set_health({"status": "down", "latency_ms": None, "checked_at": None})
            st.error(result["message"])
