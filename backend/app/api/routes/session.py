from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

from sqlalchemy.orm import Session

from app.database import get_db

from app.models.schemas import (
    SessionResponse
)

from app.repositories.session_repository import (
    SessionRepository
)

router = APIRouter(
    tags=["Session"]
)

session_repository = SessionRepository()


@router.post(
    "/session",
    response_model=SessionResponse
)
async def create_session(
    db: Session = Depends(get_db)
):
    """
    Create a new conversation session
    and store it in SQLite.

    Returns
    -------
    SessionResponse
        Contains the generated session UUID.
    """

    try:

        session = session_repository.create_session(
            db
        )

        return SessionResponse(
            session_id=session.id
        )

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )