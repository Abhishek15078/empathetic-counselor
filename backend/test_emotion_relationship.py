from app.database import SessionLocal

from app.models.db_models import (
    Session,
    Message,
    EmotionLog
)

# --------------------------------------------------
# Create Database Session
# --------------------------------------------------

db = SessionLocal()

# --------------------------------------------------
# Create Conversation Session
# --------------------------------------------------

conversation = Session()

db.add(conversation)

db.commit()

db.refresh(conversation)

print("=" * 60)
print("SESSION CREATED")
print("=" * 60)
print("Session ID:", conversation.id)

# --------------------------------------------------
# Create User Message
# --------------------------------------------------

user_message = Message(
    session_id=conversation.id,
    role="user",
    content="I feel very anxious today.",
    turn_number=1
)

db.add(user_message)

db.commit()

db.refresh(user_message)

print("\nMESSAGE CREATED")
print("-" * 60)
print("Message ID:", user_message.id)
print("Content:", user_message.content)

# --------------------------------------------------
# Create Emotion Log
# --------------------------------------------------

emotion = EmotionLog(
    session_id=conversation.id,
    message_id=user_message.id,
    label="fear",
    score=0.94,
    intensity="high",
    trajectory="stable"
)

db.add(emotion)

db.commit()

db.refresh(emotion)

print("\nEMOTION LOG CREATED")
print("-" * 60)
print("Emotion ID:", emotion.id)
print("Emotion:", emotion.label)

# --------------------------------------------------
# Relationship Test 1
# Session -> Messages
# --------------------------------------------------

stored_session = (
    db.query(Session)
    .filter(
        Session.id == conversation.id
    )
    .first()
)

print("\n" + "=" * 60)
print("SESSION -> MESSAGES")
print("=" * 60)

print("Number of Messages:")
print(len(stored_session.messages))

for message in stored_session.messages:

    print(
        f"{message.turn_number}. "
        f"{message.role}: "
        f"{message.content}"
    )

# --------------------------------------------------
# Relationship Test 2
# Session -> Emotion Logs
# --------------------------------------------------

print("\n" + "=" * 60)
print("SESSION -> EMOTION LOGS")
print("=" * 60)

print("Number of Emotion Logs:")
print(len(stored_session.emotion_logs))

for emotion_log in stored_session.emotion_logs:

    print(
        emotion_log.label,
        emotion_log.score,
        emotion_log.intensity,
        emotion_log.trajectory
    )

# --------------------------------------------------
# Relationship Test 3
# Message -> Emotion
# --------------------------------------------------

stored_message = (
    db.query(Message)
    .filter(
        Message.id == user_message.id
    )
    .first()
)

print("\n" + "=" * 60)
print("MESSAGE -> EMOTION")
print("=" * 60)

print("Message:")
print(stored_message.content)

print("\nDetected Emotion:")
print(stored_message.emotion_log.label)
print(stored_message.emotion_log.score)

# --------------------------------------------------
# Relationship Test 4
# Emotion -> Message
# --------------------------------------------------

stored_emotion = (
    db.query(EmotionLog)
    .filter(
        EmotionLog.id == emotion.id
    )
    .first()
)

print("\n" + "=" * 60)
print("EMOTION -> MESSAGE")
print("=" * 60)

print("Emotion:")
print(stored_emotion.label)

print("\nOriginal Message:")
print(stored_emotion.message.content)

# --------------------------------------------------
# Relationship Test 5
# Emotion -> Session
# --------------------------------------------------

print("\n" + "=" * 60)
print("EMOTION -> SESSION")
print("=" * 60)

print("Session ID:")
print(stored_emotion.session.id)

# --------------------------------------------------
# Close Database
# --------------------------------------------------

db.close()

print("\n" + "=" * 60)
print("ALL RELATIONSHIP TESTS PASSED")
print("=" * 60)