from sqlalchemy.orm import Session

from app.models.db_models import Message


class MessageRepository:
    """
    Handles database operations
    related to messages.
    """

    # -----------------------------
    # Create Message
    # -----------------------------

    def create_message(
        self,
        db: Session,
        session_id: str,
        role: str,
        content: str,
        turn_number: int
    ) -> Message:

        message = Message(
            session_id=session_id,
            role=role,
            content=content,
            turn_number=turn_number
        )

        db.add(message)

        db.commit()

        db.refresh(message)

        return message

    # --------------------------------------------------
    # Get Messages By Session (NEW - Lesson 11.5)
    # --------------------------------------------------

    def get_messages_by_session(
        self,
        db: Session,
        session_id: str
    ) -> list[Message]:
        """
        Returns every message belonging
        to a conversation session,
        ordered by turn number.
        """

        return (

            db.query(Message)

            .filter(
                Message.session_id == session_id
            )

            .order_by(
                Message.turn_number.asc()
            )

            .all()

        )

    # -----------------------------
    # Get All Messages
    # -----------------------------

    def get_messages(
        self,
        db: Session,
        session_id: str
    ) -> list[Message]:
        """
        Backward-compatible wrapper.
        """

        return self.get_messages_by_session(
            db,
            session_id
        )

    # -----------------------------
    # Get Last Turn Number
    # -----------------------------

    def get_last_turn_number(
        self,
        db: Session,
        session_id: str
    ) -> int:

        last_message = (

            db.query(Message)

            .filter(
                Message.session_id == session_id
            )

            .order_by(
                Message.turn_number.desc()
            )

            .first()

        )

        if last_message is None:

            return 0

        return last_message.turn_number

    # -----------------------------
    # Get Latest Message
    # -----------------------------

    def get_latest_message(
        self,
        db: Session,
        session_id: str
    ) -> Message | None:

        return (

            db.query(Message)

            .filter(
                Message.session_id == session_id
            )

            .order_by(
                Message.turn_number.desc()
            )

            .first()

        )

    # -----------------------------
    # Delete Message
    # -----------------------------

    def delete_message(
        self,
        db: Session,
        message_id: int
    ) -> bool:

        message = (

            db.query(Message)

            .filter(
                Message.id == message_id
            )

            .first()

        )

        if message is None:

            return False

        db.delete(message)

        db.commit()

        return True