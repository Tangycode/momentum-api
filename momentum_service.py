from typing import Dict, Any, List

# ----------------------------------------
# Business Logic Layer
# ----------------------------------------

def calculate_momentum(payload: Dict[str, Any]) -> Dict[str, Any]:
    """
    Computes momentum score based on runs and wickets
    over a rolling set of ball events.

    Designed for reuse across:
    - Live match dashboards
    - AI prediction modules
    - Backend analytics pipelines
    """

    balls: List[Dict[str, Any]] = payload["balls"]

    total_runs = 0
    wickets = 0

    for b in balls:
        total_runs += b["runs_off_bat"] + b.get("extras", 0)
        if b.get("wicket", False):
            wickets += 1

    # Simple explainable momentum model
    momentum_score = total_runs - (wickets * 5)

    if momentum_score > 20:
        trend = "HIGH"
    elif momentum_score > 10:
        trend = "MEDIUM"
    else:
        trend = "LOW"

    return {
        "match_id": payload["match_id"],
        "innings": payload["innings"],
        "momentum_score": momentum_score,
        "trend": trend,
        "total_runs": total_runs,
        "wickets": wickets
    }
