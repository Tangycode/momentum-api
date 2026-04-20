from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

from momentum_service import calculate_momentum

app = FastAPI()

# -----------------------------
# Input Schema
# -----------------------------

class BallEvent(BaseModel):
    ball: float
    runs_off_bat: int
    extras: int = 0
    wicket: bool = False

class MomentumInput(BaseModel):
    match_id: str
    innings: int
    balls: List[BallEvent]

# -----------------------------
# API Route
# -----------------------------

@app.post("/momentum")
def momentum(input_data: MomentumInput):
    """
    Returns match momentum based on recent ball events.
    Fully integration-ready and stateless.
    """
    try:
        result = calculate_momentum(input_data.dict())
        return {
            "status": "success",
            "data": result
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
