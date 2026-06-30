from app.database import (
    SessionLocal,
    init_database
)

from app.models.db_models import (
    Session
)


def main():
    """
    Test inserting a Session into the SQLite database.
    """

    # Ensure tables exist
    init_database()

    # Open a database session
    db = SessionLocal()

    try:
        # Create a new Session object
        conversation = Session()

        # Stage the object for insertion
        db.add(conversation)

        # Commit the transaction
        db.commit()

        # Refresh object with latest database values
        db.refresh(conversation)

        print("=" * 50)
        print("Conversation saved successfully!")
        print("=" * 50)
        print(f"Session ID : {conversation.id}")
        print(f"Created At : {conversation.created_at}")
        print(f"Status     : {conversation.status}")
        print("=" * 50)

    except Exception as e:

        db.rollback()

        print("Database Error:")
        print(e)

    finally:

        db.close()


if __name__ == "__main__":
    main()