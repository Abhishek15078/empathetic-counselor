from app.database import SessionLocal

from app.repositories.session_repository import (
    SessionRepository
)

from app.repositories.message_repository import (
    MessageRepository
)

from app.services.context import (
    ContextBuilder
)


# ----------------------------------
# Dummy Emotion Result
# ----------------------------------

class DummyEmotion:

    class Label:
        value = "anxiety"

    class Intensity:
        value = "high"

    label = Label()
    intensity = Intensity()


# ----------------------------------
# Database
# ----------------------------------

db = SessionLocal()

session_repo = SessionRepository()

message_repo = MessageRepository()

builder = ContextBuilder()


# ----------------------------------
# Create Session
# ----------------------------------

session = session_repo.create_session(db)

print("Session Created")

print(session.id)


# ----------------------------------
# Insert Messages
# ----------------------------------

message_repo.create_message(
    db,
    session.id,
    "user",
    "Hello",
    1
)

message_repo.create_message(
    db,
    session.id,
    "assistant",
    "Hi! How are you feeling today?",
    2
)

message_repo.create_message(
    db,
    session.id,
    "user",
    "I feel anxious about my exams.",
    3
)


# ----------------------------------
# Refresh ORM Object
# ----------------------------------

db.refresh(session)


# ----------------------------------
# Dummy RAG Chunks
# ----------------------------------

rag_chunks = [

    (
        "Take slow deep breaths and focus on the present moment.",
        {
            "category": "breathing"
        }
    ),

    (
        "Write down your worries and challenge negative thoughts.",
        {
            "category": "journaling"
        }
    )

]


# ----------------------------------
# Build Context
# ----------------------------------

messages = builder.build(

    session=session,

    emotion_result=DummyEmotion(),

    rag_chunks=rag_chunks

)


# ----------------------------------
# Print Prompt
# ----------------------------------

print("\n========== PROMPT ==========\n")

for message in messages:

    print(f"Role: {message['role']}")

    print(message["content"])

    print("-" * 60)


db.close()