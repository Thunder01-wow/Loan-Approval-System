# Loan Approval & Valuation System

An end-to-end 2-stage machine learning application that predicts whether a loan application is likely to be approved and, if approved, estimates the interest rate it would carry.

The project combines machine learning, FastAPI, PostgreSQL, and Streamlit into a complete application with model serving, prediction logging, and an interactive multi-step frontend.

> ⚠️ **Portfolio project:** Predictions are estimates for demonstration purposes and are not real lending decisions.

---

## Live Demo

* **Frontend:** `<add your Streamlit Community Cloud link here>`
* **Backend API:** `<add your deployed FastAPI link here>`
* **API Docs:** `<add your deployed FastAPI /docs link here>`

---

## Project Overview

Loan decisioning typically involves two important questions:

1. Should the applicant be approved?
2. If approved, what interest rate should be offered?

This project addresses these questions using a 2-stage machine learning pipeline.

### Stage 1 — Loan Approval

A classification model predicts whether a loan application is likely to be approved.

The model is trained using both LendingClub accepted and rejected loan applications from 2007–2018 Q4, allowing it to learn from genuine rejected applications rather than creating a synthetic negative class.

### Stage 2 — Interest Rate Prediction

If Stage 1 predicts approval, an XGBoost regression model estimates the expected interest rate.

The Stage 2 model is trained using accepted loans and deliberately excludes LendingClub's `grade` and `sub_grade` fields to reduce target leakage.

---

## Features

* 2-stage ML pipeline for loan approval and valuation
* Approval probability prediction
* Interest rate estimation for approved applications
* FastAPI REST API for real-time predictions
* PostgreSQL database for prediction logging
* Interactive Streamlit multi-step application wizard
* Review screen before submitting an application
* Backend health monitoring
* Optional bureau fields handled as `null` rather than `0`
* Separate feature sets for classification and regression
* Model serialization and API-based model serving
* Modular frontend and backend architecture

---

## Model Performance

### Stage 1 — Approval Classifier

| Metric    |     Score |
| --------- | --------: |
| ROC-AUC   | **0.913** |
| Precision |  **0.70** |
| Recall    |  **0.40** |

The current decision threshold prioritizes precision over recall. The relatively low recall is a known limitation and an area for future threshold optimization.

### Stage 2 — Interest Rate Regressor

| Metric |     Score |
| ------ | --------: |
| MAE    |  **1.78** |
| RMSE   |  **2.34** |
| R²     | **0.676** |

---

## Tech Stack

| Layer            | Technologies                        |
| ---------------- | ------------------------------------ |
| Machine Learning | Scikit-learn, XGBoost               |
| Data Processing  | Pandas, NumPy                       |
| Backend          | FastAPI, Uvicorn                    |
| Database         | PostgreSQL                          |
| Frontend         | Streamlit                           |
| Model Storage    | Joblib, XGBoost Native Model Format |
| Deployment       | Streamlit Community Cloud / Render  |
| Version Control  | Git & GitHub                        |

---

## Project Structure

```text
loan-approval-system/
│
├── backend/
│   ├── main.py                  # FastAPI application
│   ├── schemas.py               # API request/response schemas
│   ├── database.py              # PostgreSQL connection and models
│   ├── models_loader.py         # ML model loading
│   ├── config.py                # Environment configuration
│   ├── models/
│   │   ├── stage1/              # Approval model artifacts
│   │   └── stage2/              # Interest-rate model artifacts
│   └── requirements.txt
│
├── loan_frontend/
│   ├── app.py                   # Streamlit entry point
│   ├── api_client.py            # Backend API communication
│   ├── config.py                # Frontend configuration
│   ├── labels.py                # Display labels
│   ├── state.py                 # Session state management
│   ├── styles.py                # Custom styling
│   │
│   ├── components/
│   │   ├── sidebar.py
│   │   ├── progress.py
│   │   └── review_card.py
│   │
│   ├── steps/
│   │   ├── loan_details.py
│   │   ├── applicant_info.py
│   │   ├── credit_profile.py
│   │   ├── bureau_details.py
│   │   ├── review_submit.py
│   │   └── results.py
│   │
│   └── .streamlit/
│       └── config.toml
│
├── README.md
└── requirements.txt
```

---

## Workflow

```text
                    Applicant Details
                           │
                           ▼
                  ┌─────────────────┐
                  │     Stage 1     │
                  │ Approval Model  │
                  └─────────────────┘
                     │           │
                  Reject       Approve
                     │           │
                     ▼           ▼
              ┌───────────┐  ┌─────────────────┐
              │  Rejected │  │     Stage 2     │
              └───────────┘  │ Interest Rate   │
                             │    Regressor    │
                             └─────────────────┘
                                      │
                                      ▼
                             Predicted Interest
                                  Rate (%)
```

### Application Flow

```text
Loan Details
     ↓
Applicant Information
     ↓
Credit Profile
     ↓
Bureau Details
     ↓
Review Application
     ↓
Stage 1 — Approval Prediction
     ↓
If Approved
     ↓
Stage 2 — Interest Rate Prediction
     ↓
Final Result
```

---

## API

### `POST /predict`

Predicts loan approval and, when approved, estimates the expected interest rate.

### Example Request

```json
{
  "loan_amnt": 8000,
  "term": 36,
  "purpose": "debt_consolidation",
  "annual_inc": 95000,
  "emp_length": 10,
  "home_ownership": "MORTGAGE",
  "verification_status": "Verified",
  "application_type": "Individual",
  "addr_state": "CA",
  "dti": 12.5,
  "fico_score": 780,
  "credit_history_years": 15
}
```

Bureau-level fields such as `open_acc`, `revol_util`, and `delinq_2yrs` are optional. When an optional field is not provided, it is handled using the training data statistics rather than replacing the value with `0`.

### Example Response

```json
{
  "approved": true,
  "approval_probability": 0.87,
  "predicted_int_rate": 7.42
}
```

---

## Prediction Logging

The FastAPI backend integrates with PostgreSQL to log prediction requests and results.

The logging layer can store information such as:

* Applicant information
* Prediction result
* Approval probability
* Predicted interest rate
* Prediction timestamp

This provides a foundation for future model monitoring and analytics.

---

## Running Locally

### Clone the Repository

```bash
git clone https://github.com/<your-username>/<repository-name>.git
cd <repository-name>
```

### Backend

Install dependencies:

```bash
cd backend
pip install -r requirements.txt
```

Configure the PostgreSQL connection string using environment variables or a `.env` file.

Start the FastAPI server:

```bash
uvicorn main:app --reload
```

The API will be available at:

```text
http://localhost:8000
```

API documentation:

```text
http://localhost:8000/docs
```

### Frontend

Open another terminal:

```bash
cd loan_frontend
pip install -r requirements.txt
streamlit run app.py
```

The Streamlit application will be available at:

```text
http://localhost:8501
```

The frontend allows the backend URL to be configured through the application's connection settings or the `LOAN_API_URL` environment variable.

---

## ⚠️ Known Limitations

* Stage 1 recall is currently **0.40**, meaning some positive cases are missed.
* The Stage 1 decision threshold can be further optimized based on the desired precision/recall trade-off.
* No SHAP-based explainability layer is currently implemented.
* The API does not currently include authentication.
* The model is trained on historical LendingClub data and should not be treated as a real-world lending decision system.
* Model and data drift monitoring has not yet been implemented.

---

## Future Improvements

* SHAP-based explainable AI (XAI)
* Display per-prediction explanations in the frontend
* Optimize the Stage 1 decision threshold
* Automated tests for FastAPI endpoints
* Automated tests for frontend API calls
* Docker support
* CI/CD using GitHub Actions
* Model versioning
* Model/data drift monitoring
* API authentication
* Batch prediction endpoint
* Production deployment with managed PostgreSQL

---

## Lessons Learned

This project provided hands-on experience with the complete end-to-end machine learning deployment workflow.

Beyond model training, the project involved:

* Working with large real-world datasets
* Building classification and regression pipelines
* Preventing target leakage
* Feature engineering and preprocessing
* Evaluating models using multiple metrics
* Building REST APIs with FastAPI
* Integrating PostgreSQL for prediction logging
* Building a modular Streamlit frontend
* Connecting frontend and backend services
* Handling model serialization and dependency compatibility
* Structuring a machine learning application for deployment

---

## License

MIT

---

## Author

**Devarth Darge**

* GitHub: https://github.com/Thunder01-wow
* LinkedIn: http://www.linkedin.com/in/devarth-darge-69874a316

---

⭐ If you found this project helpful, consider giving it a star!
