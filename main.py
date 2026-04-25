from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from schemas import MomentumRequest
from services import validate_ball_events, build_momentum

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Momentum API is running"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/momentum")
def momentum(request: MomentumRequest):

    if not request.innings_id:
        raise HTTPException(status_code=400, detail="Missing innings_id")

    if request.recent_over_count <= 0:
        raise HTTPException(status_code=400, detail="recent_over_count must be > 0")

    if not request.ball_events:
        raise HTTPException(status_code=400, detail="ball_events cannot be empty")

    try:
        validate_ball_events(request.ball_events)
        result = build_momentum(request.ball_events, request.recent_over_count)

        return {
            "innings_id": request.innings_id,
            **result
        }

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception:
        raise HTTPException(status_code=500, detail="Internal server error")
