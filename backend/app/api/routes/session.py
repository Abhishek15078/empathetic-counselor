from fastapi import (
    APIRouter,
    HTTPException
)

from app.models.schemas import (
    SessionResponse
)

from app.api.dependencies import (
    orchestrator
)

router = APIRouter(
    tags=["Session"]
)


@router.post(
    "/session",
    response_model=SessionResponse
)
async def create_session():
    """
    Create a new conversation session.

    Returns
    -------
    SessionResponse
        Contains the generated session UUID.
    """

    try:

        session = (
            orchestrator
            .memory_manager
            .create_session()
        )

        return SessionResponse(
            session_id=session.session_id
        )

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )