"""Raw model field values mapped to proper display labels, and dropdown option lists."""

PURPOSE_LABELS = {
    "debt_consolidation": "Debt Consolidation",
    "small_business": "Small Business",
    "home_improvement": "Home Improvement",
    "major_purchase": "Major Purchase",
    "credit_card": "Credit Card Refinancing",
    "other": "Other",
    "house": "Buying a House",
    "vacation": "Vacation",
    "car": "Car",
    "medical": "Medical Expenses",
    "moving": "Moving / Relocation",
    "renewable_energy": "Renewable Energy",
    "wedding": "Wedding",
}

HOME_OWNERSHIP_LABELS = {
    "MORTGAGE": "Mortgage",
    "RENT": "Rent",
    "OWN": "Own (outright)",
    "ANY": "Other / Not Listed",
}

VERIFICATION_LABELS = {
    "Not Verified": "Not Verified",
    "Source Verified": "Source Verified",
    "Verified": "Verified",
}

APPLICATION_TYPE_LABELS = {
    "Individual": "Individual",
    "Joint App": "Joint Application",
}

STATE_NAMES = {
    "AL": "Alabama", "AK": "Alaska", "AZ": "Arizona", "AR": "Arkansas",
    "CA": "California", "CO": "Colorado", "CT": "Connecticut", "DE": "Delaware",
    "DC": "District of Columbia", "FL": "Florida", "GA": "Georgia", "HI": "Hawaii",
    "IL": "Illinois", "IN": "Indiana", "KS": "Kansas", "KY": "Kentucky",
    "LA": "Louisiana", "ME": "Maine", "MD": "Maryland", "MA": "Massachusetts",
    "MI": "Michigan", "MN": "Minnesota", "MS": "Mississippi", "MO": "Missouri",
    "MT": "Montana", "NE": "Nebraska", "NV": "Nevada", "NH": "New Hampshire",
    "NJ": "New Jersey", "NM": "New Mexico", "NY": "New York", "NC": "North Carolina",
    "ND": "North Dakota", "OH": "Ohio", "OK": "Oklahoma", "OR": "Oregon",
    "PA": "Pennsylvania", "RI": "Rhode Island", "SC": "South Carolina",
    "SD": "South Dakota", "TN": "Tennessee", "TX": "Texas", "UT": "Utah",
    "VT": "Vermont", "VA": "Virginia", "WA": "Washington", "WV": "West Virginia",
    "WI": "Wisconsin", "WY": "Wyoming",
}

# Only the codes the model was trained on (from the backend's Pydantic Literal)
STATE_CODES = [
    "PA", "SD", "IL", "NJ", "GA", "MN", "SC", "RI", "TX", "NC", "CA", "VA", "AZ", "NY",
    "IN", "MD", "KS", "NM", "AL", "WA", "MO", "OH", "LA", "FL", "CO", "MI", "TN", "DC",
    "MA", "WI", "HI", "VT", "DE", "NH", "NE", "CT", "OR", "AR", "MT", "NV", "WV", "WY",
    "OK", "KY", "MS", "ME", "UT", "ND", "AK",
]

# Optional bureau fields: (field_key, display_label, help_text)
BUREAU_FIELDS = [
    ("open_acc", "Open Credit Accounts", "Number of currently open credit lines."),
    ("total_acc", "Total Credit Accounts", "Total number of credit lines ever opened."),
    ("revol_bal", "Revolving Balance ($)", "Total balance carried on revolving credit (e.g. credit cards)."),
    ("revol_util", "Revolving Utilization (%)", "Amount of revolving credit currently in use, as a percentage of total revolving credit."),
    ("delinq_2yrs", "Delinquencies (Last 2 Years)", "Number of 30+ day past-due incidents in the last 2 years."),
    ("inq_last_6mths", "Credit Inquiries (Last 6 Months)", "Number of hard credit inquiries in the last 6 months."),
    ("mort_acc", "Mortgage Accounts", "Number of mortgage accounts."),
    ("bc_open_to_buy", "Available Bankcard Credit ($)", "Total remaining credit available across bankcards."),
    ("bc_util", "Bankcard Utilization (%)", "Percentage of available bankcard credit currently in use."),
    ("mo_sin_old_rev_tl_op", "Age of Oldest Revolving Account (months)", "Months since the oldest revolving credit account was opened."),
    ("num_tl_op_past_12m", "New Accounts Opened (Last 12 Months)", "Number of credit accounts opened in the past 12 months."),
    ("mths_since_recent_inq", "Months Since Last Inquiry", "Number of months since the most recent credit inquiry."),
    ("acc_now_delinq", "Accounts Currently Delinquent", "Number of accounts currently past due."),
]
