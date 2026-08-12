from sqlalchemy import create_engine, text
from app.config import settings

engine = create_engine(settings.db_url)

CREATE_TABLE_SQL = """
CREATE TABLE IF NOT EXISTS loan_predictions (
    id SERIAL PRIMARY KEY,
    loan_amnt FLOAT, term INTEGER, emp_length FLOAT, annual_inc FLOAT, dti FLOAT,
    fico_range_low INTEGER, fico_range_high INTEGER, credit_history_months FLOAT,
    delinq_2yrs FLOAT, inq_last_6mths FLOAT, open_acc FLOAT, pub_rec FLOAT,
    revol_bal FLOAT, revol_util FLOAT, total_acc FLOAT, acc_now_delinq FLOAT,
    collections_12_mths_ex_med FLOAT, pub_rec_bankruptcies FLOAT, tax_liens FLOAT,
    acc_open_past_24mths FLOAT, avg_cur_bal FLOAT, bc_open_to_buy FLOAT, bc_util FLOAT,
    mo_sin_old_il_acct FLOAT, mo_sin_old_rev_tl_op FLOAT, mo_sin_rcnt_rev_tl_op FLOAT,
    mo_sin_rcnt_tl FLOAT, mort_acc FLOAT, mths_since_recent_bc FLOAT,
    mths_since_recent_inq FLOAT, num_accts_ever_120_pd FLOAT, num_actv_bc_tl FLOAT,
    num_actv_rev_tl FLOAT, num_bc_sats FLOAT, num_bc_tl FLOAT, num_il_tl FLOAT,
    num_op_rev_tl FLOAT, num_rev_accts FLOAT, num_rev_tl_bal_gt_0 FLOAT, num_sats FLOAT,
    num_tl_120dpd_2m FLOAT, num_tl_30dpd FLOAT, num_tl_90g_dpd_24m FLOAT,
    num_tl_op_past_12m FLOAT, pct_tl_nvr_dlq FLOAT, percent_bc_gt_75 FLOAT,
    home_ownership TEXT, verification_status TEXT, purpose TEXT, addr_state TEXT,
    application_type TEXT, approval_prediction BOOLEAN, approval_probability FLOAT,
    predicted_int_rate FLOAT, created_at TIMESTAMP DEFAULT NOW()
);
"""


def init_db():
    with engine.begin() as conn:
        conn.execute(text(CREATE_TABLE_SQL))

def insert_prediction(record: dict):
    columns = ", ".join(record.keys())
    placeholders = ", ".join(f":{k}" for k in record.keys())
    with engine.begin() as conn:
        conn.execute(
            text(f"INSERT INTO loan_predictions ({columns}) VALUES ({placeholders})"),
            record
        )
