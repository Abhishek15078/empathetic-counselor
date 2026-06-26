from fastapi import (
    APIRouter,
    HTTPException
)

from app.models.schemas import (
    MessageRequest,
    MessageResponse
)

from app.api.dependencies import (
    orchestrator
)

router = APIRouter()


@router.post(
    "/message",
    response_model=MessageResponse
)
async def send_message(
    request: MessageRequest
):
    """
    Runs the complete AI pipeline.

    Steps:
    1. Validate request
    2. Load conversation session
    3. Safety screening
    4. Emotion detection
    5. RAG retrieval
    6. LLM generation
    7. Return structured response
    """

    try:

        result = orchestrator.process_message(
            session_id=request.session_id,
            user_message=request.message
        )

        emotion = None

        if result.emotion_result is not None:
            emotion = (
                result.emotion_result.label.value
            )

        trajectory = None

        if result.trajectory is not None:
            trajectory = (
                result.trajectory.value
            )

        return MessageResponse(
            response_text=result.response_text,
            emotion=emotion,
            trajectory=trajectory,
            safety_triggered=result.safety_triggered,
            processing_time_ms=result.processing_time_ms
        )

    except ValueError as e:

        # Invalid session id
        raise HTTPException(
            status_code=404,
            detail=str(e)
        )

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )