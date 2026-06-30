from app.database import SessionLocal

from app.repositories.session_repository import SessionRepository
from app.repositories.message_repository import MessageRepository
from app.repositories.emotion_repository import EmotionRepository

db = SessionLocal()

session_repo = SessionRepository()
message_repo = MessageRepository()
emotion_repo = EmotionRepository()

# -------------------------
# Create Session
# -------------------------

session = session_repo.create_session(db)

# -------------------------
# Create Messages
# -------------------------

m1 = message_repo.create_message(
    db,
    session.id,
    "user",
    "Hello",
    1
)

m2 = message_repo.create_message(
    db,
    session.id,
    "user",
    "I feel anxious",
    2
)

m3 = message_repo.create_message(
    db,
    session.id,
    "user",
    "I'm feeling better",
    3
)

# -------------------------
# Create Emotion Logs
# -------------------------

emotion_repo.create_emotion_log(
    db,
    session.id,
    m1.id,
    "joy",
    0.91,
    "low",
    "stable"
)

emotion_repo.create_emotion_log(
    db,
    session.id,
    m2.id,
    "fear",
    0.96,
    "high",
    "declining"
)

emotion_repo.create_emotion_log(
    db,
    session.id,
    m3.id,
    "calm",
    0.88,
    "medium",
    "improving"
)

# -------------------------
# Emotion Arc
# -------------------------

print("\nEmotion Arc")

print(
    emotion_repo.get_emotion_arc(
        db,
        session.id
    )
)

# -------------------------
# Latest Emotion
# -------------------------

latest = emotion_repo.get_latest_emotion(
    db,
    session.id
)

print("\nLatest Emotion")

print(latest.label)

# -------------------------
# Count
# -------------------------

print("\nCount")

print(
    emotion_repo.count_emotions(
        db,
        session.id
    )
)

db.close()