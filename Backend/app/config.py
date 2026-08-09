
from pydantic_settings import BaseSettings
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent  # backend/

class Settings(BaseSettings):
    db_url: str

    stage1_preprocessor_path: str = str(BASE_DIR / "models" / "stage1_preprocessor.joblib")
    stage1_model_json_path: str = str(BASE_DIR / "models" / "stage1_model.json")

    stage2_metadata_path: str = str(BASE_DIR / "models" / "stage2_int_rate_regressor_metadata.json")
    stage2_preprocessor_path: str = str(BASE_DIR / "models" / "stage2_preprocessor.joblib")
    stage2_model_json_path: str = str(BASE_DIR / "models" / "stage2_model.json")
    stage2_defaults_path: str = str(BASE_DIR / "models" / "stage2_feature_defaults.json")

    class Config:
        env_file = ".env"

settings = Settings()