import pickle
import joblib
import json
from xgboost import XGBClassifier , XGBRegressor
from app.config import settings

def _load_json(path):
    with open(path) as f:
        return json.load(f)

def _load_pickle(path):
    with open(path, "rb") as f:
        return pickle.load(f)

# Stage 1 — preprocessor + model loaded separately
stage1_preprocessor = joblib.load(settings.stage1_preprocessor_path)
stage1_model = XGBClassifier()
stage1_model.load_model(settings.stage1_model_json_path)

# Stage 2 — now also split
stage2_preprocessor = joblib.load(settings.stage2_preprocessor_path)
stage2_model = XGBRegressor()
stage2_model.load_model(settings.stage2_model_json_path)

stage2_defaults = _load_json(settings.stage2_defaults_path)