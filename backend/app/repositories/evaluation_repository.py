from sqlalchemy.orm import Session

from app.models.db_models import EvaluationMetric


class EvaluationRepository:
    """
    Handles database operations
    related to evaluation metrics.
    """

    def create_metric(
        self,
        db: Session,
        session_id: str,
        turn_number: int,
        empathy_score: float,
        helpfulness_score: float,
        safety_score: float
    ) -> EvaluationMetric:

        metric = EvaluationMetric(
            session_id=session_id,
            turn_number=turn_number,
            empathy_score=empathy_score,
            helpfulness_score=helpfulness_score,
            safety_score=safety_score
        )

        db.add(metric)

        db.commit()

        db.refresh(metric)

        return metric

    def get_metrics(
        self,
        db: Session,
        session_id: str
    ) -> list[EvaluationMetric]:

        return (

            db.query(EvaluationMetric)

            .filter(
                EvaluationMetric.session_id == session_id
            )

            .order_by(
                EvaluationMetric.turn_number
            )

            .all()

        )