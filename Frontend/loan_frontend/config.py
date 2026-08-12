"""App-wide configuration constants."""

import os

DEFAULT_API_URL = os.environ.get("LOAN_API_URL", "https://loan-approval-system-y2pg.onrender.com/predict")

STEPS = [
    "Loan Details",
    "Applicant Info",
    "Credit Profile",
    "Bureau Details",
    "Review & Submit",
]

