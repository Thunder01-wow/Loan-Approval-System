# stage1_prep.py
"""""
import pandas as pd
import numpy as np

STAGE1_FEATURES = ["Amount Requested", "Debt-To-Income Ratio", "Employment Length", "State"]

def load_and_prep_stage1(accepted_path, rejected_path):
    Loads raw accepted/rejected data, applies stage-1-safe cleaning ONLY.
    Deliberately does NOT impute — nulls are preserved for the caller to handle
    post-split, to avoid the per-file-median leakage bug discovered on 2026-07-31.

    accepted = pd.read_csv(accepted_path, low_memory=False,
                            usecols=["loan_amnt", "dti", "emp_length", "addr_state"])
    rejected = pd.read_csv(rejected_path, low_memory=False,
                            usecols=["Amount Requested", "Debt-To-Income Ratio",
                                      "Employment Length", "State"])

    # emp_length conversion — identical logic both sides
    accepted["emp_length"] = (
        accepted["emp_length"]
        .replace({"< 1 year": 0, "10+ years": 10, "n/a": np.nan})
        .str.extract(r"(\d+)")
        .astype(float)
    )
    rejected["Employment Length"] = (
        rejected["Employment Length"]
        .replace({"< 1 year": 0, "10+ years": 10, "n/a": np.nan})
        .str.extract(r"(\d+)")
        .astype(float)
    )

    # DTI: rejected's is a % string, accepted's is already numeric
    rejected["Debt-To-Income Ratio"] = pd.to_numeric(
        rejected["Debt-To-Income Ratio"].str.rstrip("%"), errors="coerce"
    )

    # Rename accepted to shared naming scheme
    accepted = accepted.rename(columns={
        "loan_amnt": "Amount Requested",
        "dti": "Debt-To-Income Ratio",
        "emp_length": "Employment Length",
        "addr_state": "State"
    })

    accepted["target"] = 1
    rejected["target"] = 0

    stage1_df = pd.concat([accepted, rejected], ignore_index=True)

    # Cap DTI outliers — legitimate fix, keep this one
    stage1_df["Debt-To-Income Ratio"] = stage1_df["Debt-To-Income Ratio"].clip(lower=0, upper=100)

    return stage1_df
"""


""""
from stage1_prep import load_and_prep_stage1, STAGE1_FEATURES

stage1_df = load_and_prep_stage1("data/raw/accepted_2007_to_2018Q4.csv",
                                "data/raw/rejected_2007_to_2018Q4.csv")






"""

"""""
@app.post("/predict", response_model=PredictionResponse)
def predict(application: LoanApplicationInput):
    user_input = application.dict()

    stage1_input = build_stage1_input(user_input)
    stage1_transformed = stage1_preprocessor.transform(stage1_input)
    approval_pred = bool(stage1_model.predict(stage1_transformed)[0])
    approval_prob = float(stage1_model.predict_proba(stage1_transformed)[0][1])

    if approval_pred:
        full_row = build_full_feature_row(user_input)
        input_df = pd.DataFrame([full_row])
        stage2_transformed = stage2_preprocessor.transform(input_df)
        predicted_rate = round(float(stage2_model.predict(stage2_transformed)[0]), 2)

    record = {
        **user_input,
        "approval_prediction": approval_pred,
        "approval_probability": round(approval_prob, 4),
        "predicted_int_rate": predicted_rate
    }
    insert_prediction(record)

    return PredictionResponse(
        approved=approval_pred,
        approval_probability=round(approval_prob, 4),
        predicted_int_rate=predicted_rate
    )
"""