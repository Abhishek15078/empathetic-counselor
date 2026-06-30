from app.database import SessionLocal

from app.repositories.session_repository import (
    SessionRepository
)

db = SessionLocal()

repo = SessionRepository()

# -----------------------
# Create Session
# -----------------------

session = repo.create_session(db)

print("Created")

print(session.id)

# -----------------------
# Exists
# -----------------------

print("\nExists")

print(

    repo.session_exists(
        db,
        session.id
    )

)

# -----------------------
# Update
# -----------------------

repo.update_status(

    db,

    session.id,

    "closed"

)

updated = repo.get_session(

    db,

    session.id

)

print("\nStatus")

print(updated.status)

# -----------------------
# Delete
# -----------------------

repo.delete_session(

    db,

    session.id

)

print("\nDeleted")

print(

    repo.session_exists(

        db,

        session.id

    )

)

db.close()