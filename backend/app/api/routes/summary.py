import traceback

from fastapi import (
    APIRouter,
    HTTPException
)

from app.database import SessionLocal

from app.models.schemas import (
    SummaryResponse
)

from app.api.dependencies import (
    orchestrator
)

router = APIRouter(
    tags=["Summary"]
)


@router.get(
    "/session/{session_id}/summary",
    response_model=SummaryResponse
)
async def get_summary(
    session_id: str
):
    """
    Returns a conversation summary using the
    database repositories.
    """

    db = SessionLocal()

    try:

        # -----------------------------
        # Load Session
        # -----------------------------

        session = (
            orchestrator.session_repo.get_session(
                db,
                session_id
            )
        )

        if session is None:

            raise HTTPException(
                status_code=404,
                detail="Session not found."
            )

        # -----------------------------
        # Load Messages
        # -----------------------------

        messages = (
            orchestrator.message_repo.get_messages(
                db,
                session_id
            )
        )

        # -----------------------------
        # Load Emotion History
        # -----------------------------

        emotion_logs = (
            orchestrator.emotion_repo.get_emotion_logs(
                db,
                session_id
            )
        )

        # -----------------------------
        # Emotion Arc
        # -----------------------------

        emotion_arc = [

            log.label

            for log in emotion_logs

        ]

        # -----------------------------
        # Emotional Trajectory
        # -----------------------------

        trajectory = (
            orchestrator.trajectory_tracker.analyze(
                emotion_logs
            )
        )

        # -----------------------------
        # Placeholder Key Moments
        # -----------------------------

        key_moments = []

        if len(messages) >= 1:

            key_moments.append(
                "Conversation started."
            )

        if len(messages) >= 4:

            key_moments.append(
                "Conversation became more detailed."
            )

        if len(messages) >= 8:

            key_moments.append(
                "Extended conversation detected."
            )

        # -----------------------------
        # Response
        # -----------------------------

        return SummaryResponse(

            session_id=session.id,

            turn_count=len(messages),

            emotion_arc=emotion_arc,

            trajectory=trajectory.value,

            key_moments=key_moments

        )

    except HTTPException:

        raise

    except Exception as e:

        traceback.print_exc()

        raise HTTPException(

            status_code=500,

            detail=str(e)

        )

    finally:

        db.close()