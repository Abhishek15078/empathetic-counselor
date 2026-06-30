from app.database import SessionLocal

from app.models.db_models import (
    Session,
    Message,
    SafetyEvent
)

# ======================================================
# Create Database Session
# ======================================================

db = SessionLocal()

# ======================================================
# Create Conversation Session
# ======================================================

conversation = Session()

db.add(conversation)

db.commit()

db.refresh(conversation)

print("=" * 60)
print("SESSION CREATED")
print("=" * 60)
print("Session ID:", conversation.id)

# ======================================================
# Create User Message
# ======================================================

user_message = Message(
    session_id=conversation.id,
    role="user",
    content="I don't want to live anymore.",
    turn_number=1
)

db.add(user_message)

db.commit()

db.refresh(user_message)

print("\nMESSAGE CREATED")
print("-" * 60)
print("Message ID:", user_message.id)
print("Content:", user_message.content)

# ======================================================
# Create Safety Event
# ======================================================

safety = SafetyEvent(
    session_id=conversation.id,
    message_id=user_message.id,
    stage="semantic_detection",
    response_given=(
        "I'm really sorry you're feeling this way. "
        "You don't have to face this alone. "
        "Please contact a trusted person or "
        "your local emergency services immediately."
    )
)

db.add(safety)

db.commit()

db.refresh(safety)

print("\nSAFETY EVENT CREATED")
print("-" * 60)
print("Safety Event ID:", safety.id)
print("Detection Stage:", safety.stage)

# ======================================================
# Test 1
# Session -> SafetyEvents
# ======================================================

stored_session = (
    db.query(Session)
    .filter(
        Session.id == conversation.id
    )
    .first()
)

print("\n" + "=" * 60)
print("SESSION -> SAFETY EVENTS")
print("=" * 60)

print("Number of Safety Events:")
print(len(stored_session.safety_events))

for event in stored_session.safety_events:

    print()

    print("Stage:")
    print(event.stage)

    print()

    print("Response:")
    print(event.response_given)

# ======================================================
# Test 2
# Message -> SafetyEvent
# ======================================================

stored_message = (
    db.query(Message)
    .filter(
        Message.id == user_message.id
    )
    .first()
)

print("\n" + "=" * 60)
print("MESSAGE -> SAFETY EVENT")
print("=" * 60)

print("Original Message:")
print(stored_message.content)

print()

print("Safety Stage:")
print(stored_message.safety_event.stage)

# ======================================================
# Test 3
# SafetyEvent -> Message
# ======================================================

stored_event = (
    db.query(SafetyEvent)
    .filter(
        SafetyEvent.id == safety.id
    )
    .first()
)

print("\n" + "=" * 60)
print("SAFETY EVENT -> MESSAGE")
print("=" * 60)

print("Stage:")
print(stored_event.stage)

print()

print("Original Message:")
print(stored_event.message.content)

# ======================================================
# Test 4
# SafetyEvent -> Session
# ======================================================

print("\n" + "=" * 60)
print("SAFETY EVENT -> SESSION")
print("=" * 60)

print("Session ID:")
print(stored_event.session.id)

# ======================================================
# Close Database
# ======================================================

db.close()

print("\n" + "=" * 60)
print("ALL SAFETY RELATIONSHIP TESTS PASSED")
print("=" * 60)