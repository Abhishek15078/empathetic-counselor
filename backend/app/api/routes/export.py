from io import BytesIO

from fastapi import (
    APIRouter,
    HTTPException
)

from fastapi.responses import StreamingResponse

from app.database import SessionLocal

from app.repositories.session_repository import (
    SessionRepository
)

from app.repositories.message_repository import (
    MessageRepository
)

router = APIRouter(
    tags=["Export"]
)

session_repo = SessionRepository()

message_repo = MessageRepository()


@router.get(
    "/session/{session_id}/export"
)
async def export_conversation(
    session_id: str
):
    """
    Downloads the conversation as a text file.
    """

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

        messages = (
            message_repo.get_messages_by_session(
                db,
                session_id
            )
        )

        lines = []

        lines.append(
            "Empathetic Counselor Conversation"
        )

        lines.append("=" * 40)

        lines.append("")

        for message in messages:

            role = (
                "User"
                if message.role == "user"
                else "Assistant"
            )

            lines.append(
                f"{role}:"
            )

            lines.append(
                message.content
            )

            lines.append("")

            lines.append("-" * 40)

            lines.append("")

        conversation = "\n".join(lines)

        file_stream = BytesIO(
            conversation.encode("utf-8")
        )

        return StreamingResponse(

            file_stream,

            media_type="text/plain",

            headers={

                "Content-Disposition":

                f'attachment; filename="conversation_{session_id}.txt"'

            }

        )

    finally:

        db.close()