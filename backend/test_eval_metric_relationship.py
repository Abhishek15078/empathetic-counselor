from app.database import SessionLocal

from app.models.db_models import (
    Session,
    EvalMetric
)

# =====================================================
# Create Database Session
# =====================================================

db = SessionLocal()

# =====================================================
# Create Conversation Session
# =====================================================

conversation = Session()

db.add(conversation)

db.commit()

db.refresh(conversation)

print("=" * 60)
print("SESSION CREATED")
print("=" * 60)

print("Session ID:")
print(conversation.id)

# =====================================================
# Create Evaluation Metrics
# =====================================================

metric1 = EvalMetric(
    session_id=conversation.id,
    turn_number=1,
    empathy_score=8.7,
    helpfulness_score=8.4,
    safety_score=10.0
)

metric2 = EvalMetric(
    session_id=conversation.id,
    turn_number=2,
    empathy_score=9.4,
    helpfulness_score=9.0,
    safety_score=10.0
)

metric3 = EvalMetric(
    session_id=conversation.id,
    turn_number=3,
    empathy_score=9.9,
    helpfulness_score=9.6,
    safety_score=10.0
)

db.add_all([
    metric1,
    metric2,
    metric3
])

db.commit()

# =====================================================
# Read Session Again
# =====================================================

stored_session = (
    db.query(Session)
    .filter(
        Session.id == conversation.id
    )
    .first()
)

print()

print("=" * 60)
print("SESSION -> EVAL METRICS")
print("=" * 60)

print("Number of Evaluation Records:")

print(len(
    stored_session.eval_metrics
))

print()

for metric in stored_session.eval_metrics:

    print(
        f"Turn {metric.turn_number}"
    )

    print(
        f"Empathy     : {metric.empathy_score}"
    )

    print(
        f"Helpfulness : {metric.helpfulness_score}"
    )

    print(
        f"Safety      : {metric.safety_score}"
    )

    print("-" * 40)

# =====================================================
# Read One Evaluation Record
# =====================================================

stored_metric = (
    db.query(EvalMetric)
    .filter(
        EvalMetric.turn_number == 2,
        EvalMetric.session_id == conversation.id
    )
    .first()
)

print()

print("=" * 60)
print("EVAL METRIC -> SESSION")
print("=" * 60)

print("Turn Number:")
print(stored_metric.turn_number)

print()

print("Session ID:")
print(stored_metric.session.id)

# =====================================================
# Close Database
# =====================================================

db.close()

print()

print("=" * 60)
print("ALL EVALUATION TESTS PASSED")
print("=" * 60)