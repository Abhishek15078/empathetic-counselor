from app.database import SessionLocal

from app.repositories.session_repository import (
    SessionRepository
)

from app.repositories.message_repository import (
    MessageRepository
)

db = SessionLocal()

session_repo = SessionRepository()

message_repo = MessageRepository()

# -----------------------------
# Create Session
# -----------------------------

session = session_repo.create_session(db)

print("Session")

print(session.id)

# -----------------------------
# Insert Messages
# -----------------------------

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
    "Hi!",
    2
)

message_repo.create_message(
    db,
    session.id,
    "user",
    "I feel anxious.",
    3
)

# -----------------------------
# Get All Messages
# -----------------------------

print("\nConversation")

messages = message_repo.get_messages(
    db,
    session.id
)

for message in messages:

    print(
        message.turn_number,
        message.role,
        message.content
    )

# -----------------------------
# Last Turn
# -----------------------------

print("\nLast Turn")

print(

    message_repo.get_last_turn_number(
        db,
        session.id
    )

)

# -----------------------------
# Latest Message
# -----------------------------

latest = message_repo.get_latest_message(
    db,
    session.id
)

print("\nLatest Message")

print(
    latest.turn_number,
    latest.content
)

# -----------------------------
# Delete Latest
# -----------------------------

message_repo.delete_message(
    db,
    latest.id
)

print("\nAfter Delete")

messages = message_repo.get_messages(
    db,
    session.id
)

for message in messages:

    print(
        message.turn_number,
        message.role
    )

db.close()