from fastapi import (
    APIRouter,
    HTTPException,
    Depends
)

from sqlalchemy.orm import Session

from app.database import get_db

from app.models.schemas import (
    MessageRequest,
    MessageResponse,
    MessageHistoryItem,
    MessageHistoryResponse
)

from app.api.dependencies import (
    orchestrator
)

from app.repositories.session_repository import (
    SessionRepository
)

from app.repositories.message_repository import (
    MessageRepository
)

router = APIRouter()

session_repository = SessionRepository()

message_repository = MessageRepository()


# =====================================================
# POST /message
# =====================================================

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

        raise HTTPException(
            status_code=404,
            detail=str(e)
        )

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


# =====================================================
# GET /messages/{session_id}
# =====================================================

@router.get(
    "/messages/{session_id}",
    response_model=MessageHistoryResponse
)
def get_message_history(
    session_id: str,
    db: Session = Depends(get_db)
):
    """
    Returns the complete conversation
    history for a session.
    """

    session = session_repository.get_session(
        db,
        session_id
    )

    if session is None:

        raise HTTPException(
            status_code=404,
            detail="Session not found."
        )

    messages = (
        message_repository.get_messages_by_session(
            db,
            session_id
        )
    )

    history = [

        MessageHistoryItem(

            role=message.role,

            content=message.content,

            turn_number=message.turn_number

        )

        for message in messages

    ]

    return MessageHistoryResponse(

        messages=history

    )