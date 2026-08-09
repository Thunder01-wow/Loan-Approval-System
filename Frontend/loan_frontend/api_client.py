"""All HTTP calls to the FastAPI backend live here \u2014 UI code never calls `requests` directly."""

import time
from datetime import datetime

import requests


def base_url_from_predict_url(predict_url: str) -> str:
    return predict_url[: -len("/predict")] if predict_url.endswith("/predict") else predict_url


def check_health(api_url: str) -> dict:
    """Ping the backend's /docs route. Returns a health dict ready to store in session_state."""
    base = base_url_from_predict_url(api_url)
    start = time.time()
    try:
        resp = requests.get(f"{base}/docs", timeout=4)
        latency_ms = round((time.time() - start) * 1000)
        return {
            "status": "up" if resp.status_code == 200 else "down",
            "latency_ms": latency_ms,
            "checked_at": datetime.now().strftime("%H:%M:%S"),
        }
    except requests.exceptions.RequestException:
        return {
            "status": "down",
            "latency_ms": None,
            "checked_at": datetime.now().strftime("%H:%M:%S"),
        }


def submit_application(api_url: str, payload: dict) -> tuple[bool, dict]:
    """
    POST the application to /predict.
    Returns (success, result_or_error_dict). On failure, result_or_error_dict has a
    'message' key with something safe to show the user, and an 'error_type' key.
    """
    try:
        resp = requests.post(api_url, json=payload, timeout=15)
    except requests.exceptions.ConnectionError:
        return False, {
            "error_type": "connection",
            "message": f"Couldn't reach the prediction service at {api_url}. "
                       "Make sure the FastAPI backend is running, or update the endpoint in the sidebar.",
        }
    except requests.exceptions.Timeout:
        return False, {
            "error_type": "timeout",
            "message": "The prediction service took too long to respond. Please try again.",
        }

    if resp.status_code == 200:
        return True, resp.json()

    try:
        detail = resp.json().get("detail", resp.text)
    except ValueError:
        detail = resp.text
    return False, {
        "error_type": "http",
        "message": f"The application couldn't be scored (HTTP {resp.status_code}). {detail}",
    }
