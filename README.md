# momentum-api
Overview

The Momentum API calculates match momentum using recent ball-by-ball data. It provides a real-time, explainable momentum score and trend (HIGH / MEDIUM / LOW) for use in Khel AI MVP dashboards and analytical widgets. The API is fully integration-ready, stateless, and works directly with live payload data instead of any hardcoded logic.

Features
Calculates real-time momentum score
Returns match trend (HIGH / MEDIUM / LOW)
Uses runs and wickets as core signals
Fully payload-driven (no static data)
Stateless and scalable design
Clean separation of service and route logic
Endpoint

POST /momentum

Request
{
  "match_id": "match_001",
  "innings": 1,
  "balls": [
    {
      "ball": 10.1,
      "runs_off_bat": 4,
      "extras": 0,
      "wicket": false
    }
  ]
}
Response
{
  "status": "success",
  "data": {
    "match_id": "match_001",
    "innings": 1,
    "momentum_score": 18,
    "trend": "MEDIUM",
    "total_runs": 18,
    "wickets": 1
  }
}
Run Locally
pip install -r requirements.txt
uvicorn main:app --reload
Deployment

https://momentum-api-student3.onrender.com

Key Improvement

Converted from static/demo logic → fully dynamic, payload-driven, explainable momentum model with stateless architecture suitable for Khel AI MVP integration.
