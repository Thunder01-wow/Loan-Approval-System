from pydantic import BaseModel, Field
from typing import Optional, Annotated, Literal

class LoanApplicationInput(BaseModel):
    loan_amnt: Annotated[float, Field(..., gt=0, le=40000, description="Loan amount requested by the applicant")]
    term: Annotated[Literal[36, 60], Field(..., description="Loan term in months")]
    purpose: Annotated[Literal[
        "debt_consolidation", "small_business", "home_improvement", "major_purchase",
        "credit_card", "other", "house", "vacation", "car", "medical",
        "moving", "renewable_energy", "wedding"
    ], Field(..., description="Purpose of the loan")]
    annual_inc: Annotated[float, Field(..., gt=0, description="Annual income of the applicant")]
    emp_length: Annotated[float, Field(..., ge=0, le=10, description="Employment length in years")]
    home_ownership: Annotated[Literal["MORTGAGE", "RENT", "OWN", "ANY"], Field(..., description="Home ownership status")]
    verification_status: Annotated[Literal["Not Verified", "Source Verified", "Verified"], Field(..., description="Income verification status")]
    application_type: Annotated[Literal["Individual", "Joint App"], Field(..., description="Type of loan application")]
    addr_state: Annotated[Literal[
        "PA", "SD", "IL", "NJ", "GA", "MN", "SC", "RI", "TX", "NC", "CA", "VA", "AZ", "NY",
        "IN", "MD", "KS", "NM", "AL", "WA", "MO", "OH", "LA", "FL", "CO", "MI", "TN", "DC",
        "MA", "WI", "HI", "VT", "DE", "NH", "NE", "CT", "OR", "AR", "MT", "NV", "WV", "WY",
        "OK", "KY", "MS", "ME", "UT", "ND", "AK"
    ], Field(..., description="Two-letter US state code")]
    dti: Annotated[float, Field(..., ge=0, le=100, description="Debt-to-income ratio")]
    fico_score: Annotated[int, Field(..., ge=300, le=850, description="FICO credit score")]
    credit_history_years: Annotated[float, Field(..., ge=0, description="Number of years of credit history")]

    open_acc: Optional[Annotated[float, Field(ge=0)]] = None
    total_acc: Optional[Annotated[float, Field(ge=0)]] = None
    revol_bal: Optional[Annotated[float, Field(ge=0)]] = None
    revol_util: Optional[Annotated[float, Field(ge=0)]] = None
    delinq_2yrs: Optional[Annotated[float, Field(ge=0)]] = None
    inq_last_6mths: Optional[Annotated[float, Field(ge=0)]] = None
    mort_acc: Optional[Annotated[float, Field(ge=0)]] = None
    bc_open_to_buy: Optional[Annotated[float, Field(ge=0)]] = None
    bc_util: Optional[Annotated[float, Field(ge=0)]] = None
    mo_sin_old_rev_tl_op: Optional[Annotated[float, Field(ge=0)]] = None
    num_tl_op_past_12m: Optional[Annotated[float, Field(ge=0)]] = None
    mths_since_recent_inq: Optional[Annotated[float, Field(ge=0)]] = None
    acc_now_delinq: Optional[Annotated[float, Field(ge=0)]] = None

class PredictionResponse(BaseModel):
    approved: bool = Field(..., description="Whether the loan is predicted to be approved")
    approval_probability: float = Field(..., description="Probability of loan approval")
    predicted_int_rate: Optional[float] = Field(None, description="Predicted interest rate for the loan")