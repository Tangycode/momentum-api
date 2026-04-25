from typing import List, Dict
from collections import defaultdict

def validate_ball_events(ball_events: List[Dict]):
    seen = set()

    for ball in ball_events:
        key = (ball["over"], ball["ball_in_over"])

        if key in seen:
            raise ValueError(f"Duplicate ball detected: {key}")
        seen.add(key)

        expected = f"{ball['over']}.{ball['ball_in_over']}"
        if ball["over_ball"] != expected:
            raise ValueError(f"Invalid over_ball format: expected {expected}")

        if ball["runs"] < 0 or ball["extras"] < 0:
            raise ValueError("Runs/extras cannot be negative")

    sorted_events = sorted(ball_events, key=lambda x: (x["over"], x["ball_in_over"]))
    if ball_events != sorted_events:
        raise ValueError("Ball events must be in chronological order")


def group_overs(ball_events: List[Dict]):
    overs = defaultdict(lambda: {"runs": 0, "wickets": 0})

    for ball in ball_events:
        over = ball["over"]
        overs[over]["runs"] += ball["runs"] + ball["extras"]
        overs[over]["wickets"] += ball["wicket"]

    return dict(sorted(overs.items()))


def classify_momentum(runs_pattern, wickets_pattern):
    total_runs = sum(runs_pattern[-2:])
    total_wickets = sum(wickets_pattern[-2:])

    # Attacking
    if total_runs >= 18 and total_wickets <= 1:
        return "attacking", "High scoring in recent overs with minimal wickets"

    # Collapse
    if total_wickets >= 2:
        return "collapse", "Multiple wickets lost in recent overs"

    # Recovery
    if len(runs_pattern) >= 2 and runs_pattern[-1] > runs_pattern[-2] and sum(wickets_pattern) > 0:
        return "recovery", "Run rate improving after losing wickets"

    # Steady
    return "steady", "Balanced performance without major swings"


def build_momentum(ball_events: List[Dict], recent_over_count: int):
    overs = group_overs(ball_events)

    if len(overs) == 0:
        raise ValueError("No overs available")

    over_numbers = list(overs.keys())
    recent_over_numbers = over_numbers[-recent_over_count:]

    runs_pattern = [overs[o]["runs"] for o in recent_over_numbers]
    wickets_pattern = [overs[o]["wickets"] for o in recent_over_numbers]

    run_delta = runs_pattern[-1] - runs_pattern[0] if len(runs_pattern) > 1 else 0
    wicket_pressure = sum(wickets_pattern)

    momentum_label, explanation = classify_momentum(runs_pattern, wickets_pattern)

    return {
        "recent_overs": recent_over_numbers,
        "runs_pattern": runs_pattern,
        "wickets_pattern": wickets_pattern,
        "run_delta": run_delta,
        "wicket_pressure": wicket_pressure,
        "momentum_label": momentum_label,
        "explanation": explanation
    }
