from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.orm import (
    declarative_base,
    sessionmaker
)

# ======================================================
# SQLite Database Path
# ======================================================

BASE_DIR = Path(__file__).resolve().parent.parent

DATABASE_URL = (
    f"sqlite:///{BASE_DIR / 'counselor.db'}"
)

# ======================================================
# SQLAlchemy Engine
# ======================================================

engine = create_engine(
    DATABASE_URL,
    connect_args={
        "check_same_thread": False
    }
)

# ======================================================
# Session Factory
# ======================================================

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# ======================================================
# Base Class
# ======================================================

Base = declarative_base()

# ======================================================
# Initialize Database
# ======================================================

def init_database():
    """
    Creates all database tables.
    """

    from app.models import db_models

    Base.metadata.create_all(bind=engine)

# ======================================================
# Database Dependency
# ======================================================

def get_db():
    """
    Creates a database session for one request.

    FastAPI automatically closes the session
    after the request finishes.
    """

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()