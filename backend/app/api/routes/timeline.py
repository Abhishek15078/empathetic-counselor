from fastapi import APIRouter, HTTPException

from app.database import SessionLocal

from app.repositories.emotion_repository import EmotionRepository
from app.repositories.session_repository import SessionRepository

from app.models.schemas import (
    TimelinePoint,
    TimelineResponse
)

router = APIRouter(tags=["Timeline"])

emotion_repo = EmotionRepository()
session_repo = SessionRepository()


@router.get(
    "/session/{session_id}/timeline",
    response_model=TimelineResponse
)
async def get_timeline(session_id: str):

    db = SessionLocal()

    try:

        session = session_repo.get_session(
            db,
            session_id
        )

        if session is None:

            raise HTTPException(
                status_code=404,
                detail="Session not found."
            )

        rows = emotion_repo.get_timeline(
            db,
            session.id
        )

        timeline = [

            TimelinePoint(

                turn=turn,

                emotion=label,

                score=score

            )

            for turn, label, score in rows

        ]

        return TimelineResponse(
            timeline=timeline
        )

    finally:

        db.close()