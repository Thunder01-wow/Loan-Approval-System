"""Custom CSS on top of the native theme in .streamlit/config.toml."""

import streamlit as st

CUSTOM_CSS = """
<style>
#MainMenu, footer {visibility: hidden;}

.block-container {padding-top: 2.5rem; max-width: 760px;}

h1 {font-weight: 700; letter-spacing: -0.02em;}
h3 {font-weight: 600; margin-top: 0.25rem;}

.step-track {display: flex; justify-content: space-between; margin-bottom: 0.4rem;}
.step-item {font-size: 0.8rem; color: #9CA3AF; text-align: center; flex: 1;}
.step-item.done {color: #2563EB;}
.step-item.current {color: #111827; font-weight: 600;}
.step-dot {display: inline-block; width: 8px; height: 8px; border-radius: 50%;
           margin-right: 4px; background: #D1D5DB;}
.step-dot.done {background: #2563EB;}
.step-dot.current {background: #111827;}

div[data-testid="stForm"] {
    border: 1px solid #E5E7EB;
    border-radius: 12px;
    padding: 1.5rem 1.5rem 0.75rem 1.5rem;
    background-color: #FAFAFA;
}

.review-card {
    border: 1px solid #E5E7EB;
    border-radius: 10px;
    padding: 1rem 1.25rem;
    margin-bottom: 0.75rem;
    background-color: #FAFAFA;
}
.review-card h5 {margin: 0 0 0.5rem 0; color: #2563EB; font-size: 0.85rem;
                  text-transform: uppercase; letter-spacing: 0.04em;}
.review-row {display: flex; justify-content: space-between; font-size: 0.92rem;
             padding: 0.15rem 0; color: #374151;}
.review-row span:first-child {color: #6B7280;}

.stButton>button {width: 100%; border-radius: 8px; font-weight: 500;}

.health-dot {display: inline-block; width: 9px; height: 9px; border-radius: 50%; margin-right: 6px;}
.health-up {background: #16A34A;}
.health-down {background: #DC2626;}
.health-unknown {background: #9CA3AF;}
</style>
"""


def inject():
    st.markdown(CUSTOM_CSS, unsafe_allow_html=True)
