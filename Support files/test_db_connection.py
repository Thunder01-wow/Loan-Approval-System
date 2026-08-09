# test_db_connection.py
from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os

load_dotenv()
engine = create_engine(os.getenv("DB_URL"))

sample_row = {
    "loan_amnt": 15000, "dti": 18.5, "emp_length": 5, "addr_state": "CA",
    "term": 36, "annual_inc": 65000, "fico_range_low": 680, "fico_range_high": 684,
    "credit_history_months": 120.5, "delinq_2yrs": 0, "inq_last_6mths": 1,
    "open_acc": 8, "pub_rec": 0, "revol_bal": 4500, "revol_util": 35.2,
    "total_acc": 20, "acc_now_delinq": 0, "collections_12_mths_ex_med": 0,
    "pub_rec_bankruptcies": 0, "tax_liens": 0, "acc_open_past_24mths": 2,
    "avg_cur_bal": 8000, "bc_open_to_buy": 3000, "bc_util": 40.0,
    "mo_sin_old_il_acct": 100, "mo_sin_old_rev_tl_op": 150, "mo_sin_rcnt_rev_tl_op": 10,
    "mo_sin_rcnt_tl": 5, "mort_acc": 1, "mths_since_recent_bc": 12,
    "mths_since_recent_inq": 3, "num_accts_ever_120_pd": 0, "num_actv_bc_tl": 3,
    "num_actv_rev_tl": 4, "num_bc_sats": 3, "num_bc_tl": 5, "num_il_tl": 2,
    "num_op_rev_tl": 6, "num_rev_accts": 10, "num_rev_tl_bal_gt_0": 4,
    "num_sats": 8, "num_tl_120dpd_2m": 0, "num_tl_30dpd": 0, "num_tl_90g_dpd_24m": 0,
    "num_tl_op_past_12m": 2, "pct_tl_nvr_dlq": 95.0, "percent_bc_gt_75": 20.0,
    "home_ownership": "RENT", "verification_status": "Verified",
    "purpose": "credit_card", "application_type": "Individual",
    "approval_prediction": True, "approval_probability": 0.82, "predicted_int_rate": 12.4
}

columns = ", ".join(sample_row.keys())
placeholders = ", ".join(f":{k}" for k in sample_row.keys())

with engine.begin() as conn:
    conn.execute(
        text(f"INSERT INTO loan_predictions ({columns}) VALUES ({placeholders})"),
        sample_row
    )
    print("Insert successful.")

    result = conn.execute(text("SELECT id, loan_amnt, dti, approval_prediction, predicted_int_rate FROM loan_predictions"))
    for row in result:
        print(row)