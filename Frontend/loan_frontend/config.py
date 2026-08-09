"""App-wide configuration constants."""

import os

DEFAULT_API_URL = os.environ.get("LOAN_API_URL", "http://localhost:8000/predict")

STEPS = [
    "Loan Details",
    "Applicant Info",
    "Credit Profile",
    "Bureau Details",
    "Review & Submit",
]

