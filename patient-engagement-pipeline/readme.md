# 🩺 Patient Engagement Analytics Pipeline

**Simulated project based on a real-world Customer Data Engineer scenario at League**  
**Tech Stack**: GCP | BigQuery | DBT | Airflow | Looker | GitHub Actions | Python | SQL

---

## 📘 Project Overview

This project simulates the deployment of a cloud-native, customer-facing analytics pipeline for a digital healthcare client. The goal is to track user engagement on a wellness platform and deliver clean, scalable data models to support KPI dashboards for customer teams. This mirrors responsibilities from a Customer Data Engineer role at League.

---

## 🎯 Objectives

- Ingest app interaction logs and feedback data
- Build a data pipeline using GCP, DBT, and Airflow
- Transform and model raw data into meaningful analytics
- Deliver self-serve dashboards using Looker
- Simulate real-world CI/CD deployment with GitHub Actions
- Document the full process for client onboarding

---

## 🛠 Tech Stack

| Category       | Tool                                       |
|----------------|--------------------------------------------|
| Cloud Platform | Google Cloud (BigQuery, Pub/Sub, Cloud Functions) |
| Data Modeling  | DBT (Data Build Tool)                      |
| Orchestration  | Apache Airflow                             |
| CI/CD          | GitHub Actions                             |
| Dashboards     | Looker                                     |
| Languages      | SQL, Python                                |

---

## 🧱 Architecture

Mobile App Logs → GCP Pub/Sub → BigQuery (Raw Layer)
→ DBT (Transformations)
→ BigQuery (Analytics Layer)
→ Looker Dashboards

---

## 📂 Project Structure

/data
├── mock_events.json
├── nps_feedback.csv

/dbt
├── models/
├── macros/
├── dbt_project.yml

/airflow
├── dags/
└── utils/

/dashboards
└── dashboard_mockups/

.github/
└── workflows/
└── ci.yml

README.md

---

## 🧪 Mock Data

Sample mock data was created to simulate mobile app usage and user feedback for engagement tracking.

### `mock_events.json`
```json
[
  {
    "event_id": "evt_001",
    "user_id": "user_001",
    "event_type": "login",
    "feature_name": null,
    "timestamp": "2025-04-01T12:01:00Z"
  },
  {
    "event_id": "evt_002",
    "user_id": "user_001",
    "event_type": "feature_use",
    "feature_name": "meditation_audio",
    "timestamp": "2025-04-01T12:05:00Z"
  },
  {
    "event_id": "evt_003",
    "user_id": "user_002",
    "event_type": "feedback",
    "feature_name": null,
    "feedback_score": 8,
    "timestamp": "2025-04-01T13:30:00Z"
  }
]