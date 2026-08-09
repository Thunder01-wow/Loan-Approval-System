"""
Loan Approval & Valuation \u2014 Streamlit frontend entry point.
Run with: streamlit run app.py
"""

import streamlit as st

import state
import styles
from components import progress, sidebar
from steps import applicant_info, bureau_details, credit_profile, loan_details, results, review_submit

st.set_page_config(page_title="Loan Approval & Valuation", page_icon="\U0001F4B5", layout="centered")
styles.inject()
state.init()
sidebar.render()

st.title("Loan Approval & Valuation")
st.caption("Fill in the applicant's details below. Fields marked optional can be left blank \u2014 "
           "we'll fall back to dataset averages for the prediction.")
d = st.session_state.data
step = st.session_state.step

if step < 5:
    progress.render()
    st.write("")

if step == 0:
    loan_details.render(d)
elif step == 1:
    applicant_info.render(d)
elif step == 2:
    credit_profile.render(d)
elif step == 3:
    bureau_details.render(d)
elif step == 4:
    review_submit.render(d)
elif step == 5:
    results.render()
