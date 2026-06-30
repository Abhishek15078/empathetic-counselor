from app.database import SessionLocal
from app.models.db_models import (
    Session,
    Message
)

# -----------------------------------------
# Create a database session
# -----------------------------------------

db = SessionLocal()

try:

    # -----------------------------------------
    # Create a new conversation session
    # -----------------------------------------

    conversation = Session()

    db.add(conversation)

    db.commit()

    db.refresh(conversation)

    print("Session ID:")
    print(conversation.id)

    # -----------------------------------------
    # Add messages to the relationship
    # -----------------------------------------

    conversation.messages.append(
        Message(
            role="user",
            content="Hello",
            turn_number=1
        )
    )

    conversation.messages.append(
        Message(
            role="assistant",
            content="Hi! How can I help you?",
            turn_number=2
        )
    )

    conversation.messages.append(
        Message(
            role="user",
            content="I feel anxious.",
            turn_number=3
        )
    )

    db.commit()

    # -----------------------------------------
    # Verify all messages in database
    # -----------------------------------------

    print("\nAll Messages in Database:\n")

    all_messages = db.query(Message).all()

    print(f"Count = {len(all_messages)}\n")

    for message in all_messages:

        print(
            f"ID: {message.id} | "
            f"Session: {message.session_id} | "
            f"{message.role}: {message.content}"
        )

    # -----------------------------------------
    # Load THIS session again from database
    # -----------------------------------------

    stored = (
        db.query(Session)
        .filter(
            Session.id == conversation.id
        )
        .first()
    )

    # -----------------------------------------
    # Display relationship
    # -----------------------------------------

    print("\nMessages stored for this session:\n")

    for message in stored.messages:

        print(
            f"{message.turn_number}. "
            f"{message.role}: "
            f"{message.content}"
        )

finally:

    db.close()