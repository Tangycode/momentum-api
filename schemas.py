from pydantic import BaseModel, Field
from typing import List, Optional, Dict

class BallEvent(BaseModel):
    over: int = Field(..., ge=0)
    ball_in_over: int = Field(..., ge=1, le=6)
    over_ball: str
    runs: int = Field(..., ge=0)
    extras: int = Field(..., ge=0)
    wicket: int = Field(..., ge=0, le=1)

class MomentumRequest(BaseModel):
    innings_id: str
    recent_over_count: int
    ball_events: List[BallEvent]

    # Khel AI extensions
    match: Optional[Dict] = None
    teams: Optional[Dict] = None
    players: Optional[Dict] = None
