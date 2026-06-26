from fastapi import (
    APIRouter,
    HTTPException
)

from app.models.schemas import (
    SummaryResponse
)

from app.api.dependencies import (
    orchestrator
)

from app.services.memory import (
    TrajectoryTracker
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
    Returns an overview of the conversation.

    Includes:
    - Total turns
    - Emotion timeline
    - Overall emotional trajectory
    - Key moments (placeholder for now)
    """

    try:

        session = (
            orchestrator
            .memory_manager
            .get_session(session_id)
        )

        trajectory = (
            TrajectoryTracker.analyze(
                session.get_emotion_log()
            )
        )

        emotions = [

            emotion.label.value

            for emotion in
            session.get_emotion_log()

        ]

        return SummaryResponse(
            session_id=session.session_id,
            turn_count=len(
                session.messages
            ),
            emotion_arc=emotions,
            trajectory=trajectory.value,
            key_moments=[]
        )

    except ValueError:

        raise HTTPException(
            status_code=404,
            detail="Session not found."
        )

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )