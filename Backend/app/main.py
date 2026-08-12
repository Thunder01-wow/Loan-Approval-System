from contextlib import asynccontextmanager

import pandas as pd
from fastapi import FastAPI, HTTPException
from app.schemas import LoanApplicationInput, PredictionResponse
from fastapi.responses import JSONResponse
from app.model_loader import stage1_model, stage2_model, stage2_defaults ,stage1_preprocessor , stage2_preprocessor
from app.database import insert_prediction, init_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield


app = FastAPI(title="Loan Approval & Rate Prediction API", lifespan=lifespan)


def build_stage1_input(user_input: dict) -> pd.DataFrame:
    # Stage 1 was trained on renamed columns + missing-indicator flags.
    # Since these are required fields in the schema, the user always
    # supplies them — so the _missing flags are always False here.
    stage1_row = {
        "Amount Requested": user_input["loan_amnt"],
        "Debt-To-Income Ratio": user_input["dti"],
        "Employment Length": user_input["emp_length"],
        "Amount Requested_missing": False,
        "Debt-To-Income Ratio_missing": False,
        "Employment Length_missing": False,
        "State": user_input["addr_state"],
    }
    return pd.DataFrame([stage1_row])


def build_full_feature_row(user_input: dict) -> dict:
    row = dict(stage2_defaults)
    for key, value in user_input.items():
        if value is not None:
            row[key] = value
    row["fico_range_low"] = user_input["fico_score"] - 2
    row["fico_range_high"] = user_input["fico_score"] + 2
    row["credit_history_months"] = user_input["credit_history_years"] * 12
    return row


@app.get("/health")
def health_check():
    return {"status": "healthy"}


@app.get("/defaults")
def get_defaults():
    return stage2_defaults


@app.get("/home")
def home():
    return {"message": "Welcome to the Loan Approval & Rate Prediction API"}


@app.post("/predict", response_model=PredictionResponse)
def predict(application: LoanApplicationInput):
    user_input = application.dict()
    # Stage 1: Predict approval
    stage1_input = build_stage1_input(user_input)
    stage1_transformed = stage1_preprocessor.transform(stage1_input)
    approval_pred = bool(stage1_model.predict(stage1_transformed)[0])
    approval_prob = float(stage1_model.predict_proba(stage1_transformed)[0][1])

    predicted_rate = None
    try:
        # always build full_row — needed for the DB record either way,
        # whether or not Stage 2 actually runs
        full_row = build_full_feature_row(user_input)
        if approval_pred:
            input_df = pd.DataFrame([full_row])
            stage2_transformed = stage2_preprocessor.transform(input_df)
            predicted_rate = round(
                float(stage2_model.predict(stage2_transformed)[0]), 2
            )
        # drop request-only fields that aren't real DB columns
        db_row = {
            k: v for k, v in full_row.items()
            if k not in ("fico_score", "credit_history_years")
        }
        record = {
            **db_row,
            "approval_prediction": approval_pred,
            "approval_probability": round(approval_prob, 4),
            "predicted_int_rate": predicted_rate,
        }
        insert_prediction(record)
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error during prediction or database insertion: {e}"
        )
    return PredictionResponse(
        approved=approval_pred,
        approval_probability=round(approval_prob, 4),
        predicted_int_rate=predicted_rate,
    )
