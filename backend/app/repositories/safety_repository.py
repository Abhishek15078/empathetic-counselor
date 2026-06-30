from sqlalchemy.orm import Session

from app.models.db_models import SafetyEvent


class SafetyRepository:
    """
    Handles database operations
    related to safety events.
    """

    def create_safety_event(
        self,
        db: Session,
        session_id: str,
        message_id: int,
        stage: str,
        response_given: str
    ) -> SafetyEvent:

        safety_event = SafetyEvent(
            session_id=session_id,
            message_id=message_id,
            stage=stage,
            response_given=response_given
        )

        db.add(safety_event)

        db.commit()

        db.refresh(safety_event)

        return safety_event

    def get_safety_events(
        self,
        db: Session,
        session_id: str
    ) -> list[SafetyEvent]:

        return (

            db.query(SafetyEvent)

            .filter(
                SafetyEvent.session_id == session_id
            )

            .order_by(
                SafetyEvent.triggered_at
            )

            .all()

        )