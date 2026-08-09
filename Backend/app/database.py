from sqlalchemy import create_engine, text
from app.config import settings

engine = create_engine(settings.db_url)

def insert_prediction(record: dict):
    columns = ", ".join(record.keys())
    placeholders = ", ".join(f":{k}" for k in record.keys())
    with engine.begin() as conn:
        conn.execute(
            text(f"INSERT INTO loan_predictions ({columns}) VALUES ({placeholders})"),
            record
        )