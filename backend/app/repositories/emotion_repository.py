from sqlalchemy.orm import Session

from app.models.db_models import EmotionLog, Message


class EmotionRepository:
    """
    Handles database operations
    related to emotion logs.
    """

    # ----------------------------------
    # Create Emotion Log
    # ----------------------------------

    def create_emotion_log(
        self,
        db: Session,
        session_id: str,
        message_id: int,
        label: str,
        score: float,
        intensity: str,
        trajectory: str
    ) -> EmotionLog:

        emotion = EmotionLog(
            session_id=session_id,
            message_id=message_id,
            label=label,
            score=score,
            intensity=intensity,
            trajectory=trajectory
        )

        db.add(emotion)
        db.commit()
        db.refresh(emotion)

        return emotion

    # ----------------------------------
    # Get All Emotion Logs
    # ----------------------------------

    def get_emotion_logs(
        self,
        db: Session,
        session_id: str
    ) -> list[EmotionLog]:

        return (
            db.query(EmotionLog)
            .filter(
                EmotionLog.session_id == session_id
            )
            .order_by(
                EmotionLog.created_at
            )
            .all()
        )

    # ----------------------------------
    # Latest Emotion
    # ----------------------------------

    def get_latest_emotion(
        self,
        db: Session,
        session_id: str
    ):

        return (
            db.query(EmotionLog)
            .filter(
                EmotionLog.session_id == session_id
            )
            .order_by(
                EmotionLog.created_at.desc()
            )
            .first()
        )

    # ----------------------------------
    # Emotion Arc
    # ----------------------------------

    def get_emotion_arc(
        self,
        db: Session,
        session_id: str
    ):

        logs = self.get_emotion_logs(
            db,
            session_id
        )

        return [
            log.label
            for log in logs
        ]

    # ----------------------------------
    # Count
    # ----------------------------------

    def count_emotions(
        self,
        db: Session,
        session_id: str
    ):

        return (
            db.query(EmotionLog)
            .filter(
                EmotionLog.session_id == session_id
            )
            .count()
        )

    # ----------------------------------
    # Delete
    # ----------------------------------

    def delete_emotion_log(
        self,
        db: Session,
        emotion_id: int
    ):

        emotion = (
            db.query(EmotionLog)
            .filter(
                EmotionLog.id == emotion_id
            )
            .first()
        )

        if emotion is None:
            return False

        db.delete(emotion)
        db.commit()

        return True

    # ----------------------------------
    # Timeline
    # ----------------------------------

    def get_timeline(
        self,
        db: Session,
        session_id: str
    ):

        return (

            db.query(

                Message.turn_number,

                EmotionLog.label,

                EmotionLog.score

            )

            .join(

                Message,

                EmotionLog.message_id == Message.id

            )

            .filter(

                EmotionLog.session_id == session_id

            )

            .order_by(

                Message.turn_number

            )

            .all()

        )