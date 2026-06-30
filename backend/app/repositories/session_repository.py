from sqlalchemy.orm import Session

from app.models.db_models import Session as SessionModel


class SessionRepository:
    """
    Handles all database operations
    related to conversation sessions.
    """

    # -----------------------------
    # Create Session
    # -----------------------------

    def create_session(
        self,
        db: Session
    ) -> SessionModel:

        session = SessionModel()

        db.add(session)

        db.commit()

        db.refresh(session)

        return session

    # -----------------------------
    # Get Session
    # -----------------------------

    def get_session(
        self,
        db: Session,
        session_id: str
    ) -> SessionModel | None:

        return (

            db.query(SessionModel)

            .filter(
                SessionModel.id == session_id
            )

            .first()

        )

    # -----------------------------
    # Check Session Exists
    # -----------------------------

    def session_exists(
        self,
        db: Session,
        session_id: str
    ) -> bool:

        session = self.get_session(
            db,
            session_id
        )

        return session is not None

    # -----------------------------
    # Update Session Status
    # -----------------------------

    def update_status(
        self,
        db: Session,
        session_id: str,
        status: str
    ) -> SessionModel | None:

        session = self.get_session(
            db,
            session_id
        )

        if session is None:

            return None

        session.status = status

        db.commit()

        db.refresh(session)

        return session

    # -----------------------------
    # Delete Session
    # -----------------------------

    def delete_session(
        self,
        db: Session,
        session_id: str
    ) -> bool:

        session = self.get_session(
            db,
            session_id
        )

        if session is None:

            return False

        db.delete(session)

        db.commit()

        return True