Purpose

Analyze recent overs to determine innings momentum using explainable rules.

Endpoint

POST /momentum

Input Schema
innings_id
recent_over_count
ball_events[]
Output Schema
recent_overs
runs_pattern
wickets_pattern
run_delta
wicket_pressure
momentum_label
explanation
Sample Response
{
  "innings_id": "I001",
  "recent_overs": [1,2,3],
  "runs_pattern": [6,12,8],
  "wickets_pattern": [0,0,1],
  "run_delta": 2,
  "wicket_pressure": 1,
  "momentum_label": "steady",
  "explanation": "Balanced performance without major swings"
}
Validation Errors
Missing innings_id → 400
Invalid recent_over_count → 400
Empty ball_events → 400
Duplicate/invalid sequence → 400
Integration Notes
Can consume Over Summary API output
Uses strict chronological grouping
Explainable rule-based classification
Frontend-ready JSON
