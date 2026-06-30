from datetime import UTC, datetime
import uuid

from sqlalchemy import (
    Column,
    String,
    DateTime,
    Integer,
    Text,
    Float,
    ForeignKey
)

from sqlalchemy.orm import (
    relationship
)

from app.database import Base


# ==========================================================
# Session Table
# ==========================================================

class Session(Base):
    """
    Database table representing
    one conversation session.
    """

    __tablename__ = "sessions"

    id = Column(
        String,
        primary_key=True,
        default=lambda: str(uuid.uuid4())
    )

    created_at = Column(
        DateTime,
        default=lambda: datetime.now(UTC)
    )

    status = Column(
        String,
        default="active"
    )

    # ---------------------------
    # Relationships
    # ---------------------------

    messages = relationship(
        "Message",
        back_populates="session",
        cascade="all, delete-orphan"
    )

    emotion_logs = relationship(
        "EmotionLog",
        back_populates="session",
        cascade="all, delete-orphan"
    )

    safety_events = relationship(
        "SafetyEvent",
        back_populates="session",
        cascade="all, delete-orphan"
    )

    eval_metrics = relationship(
        "EvalMetric",
        back_populates="session",
        cascade="all, delete-orphan"
    )


# ==========================================================
# Message Table
# ==========================================================

class Message(Base):
    """
    Database table representing
    one message in a conversation.
    """

    __tablename__ = "messages"

    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    session_id = Column(
        String,
        ForeignKey("sessions.id"),
        nullable=False
    )

    role = Column(
        String,
        nullable=False
    )

    content = Column(
        Text,
        nullable=False
    )

    turn_number = Column(
        Integer,
        nullable=False
    )

    created_at = Column(
        DateTime,
        default=lambda: datetime.now(UTC)
    )

    # ---------------------------
    # Relationships
    # ---------------------------

    session = relationship(
        "Session",
        back_populates="messages"
    )

    emotion_log = relationship(
        "EmotionLog",
        back_populates="message",
        uselist=False
    )

    safety_event = relationship(
        "SafetyEvent",
        back_populates="message",
        uselist=False
    )


# ==========================================================
# Emotion Log Table
# ==========================================================

class EmotionLog(Base):
    """
    Stores detected emotion.
    """

    __tablename__ = "emotion_logs"

    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    session_id = Column(
        String,
        ForeignKey("sessions.id"),
        nullable=False
    )

    message_id = Column(
        Integer,
        ForeignKey("messages.id"),
        nullable=False,
        unique=True
    )

    label = Column(
        String,
        nullable=False
    )

    score = Column(
        Float,
        nullable=False
    )

    intensity = Column(
        String,
        nullable=False
    )

    trajectory = Column(
        String,
        nullable=False
    )

    created_at = Column(
        DateTime,
        default=lambda: datetime.now(UTC)
    )

    # ---------------------------
    # Relationships
    # ---------------------------

    session = relationship(
        "Session",
        back_populates="emotion_logs"
    )

    message = relationship(
        "Message",
        back_populates="emotion_log"
    )


# ==========================================================
# Safety Event Table
# ==========================================================

class SafetyEvent(Base):
    """
    Stores safety triggers.
    """

    __tablename__ = "safety_events"

    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    session_id = Column(
        String,
        ForeignKey("sessions.id"),
        nullable=False
    )

    message_id = Column(
        Integer,
        ForeignKey("messages.id"),
        nullable=False,
        unique=True
    )

    triggered_at = Column(
        DateTime,
        default=lambda: datetime.now(UTC)
    )

    stage = Column(
        String,
        nullable=False
    )

    response_given = Column(
        Text,
        nullable=False
    )

    # ---------------------------
    # Relationships
    # ---------------------------

    session = relationship(
        "Session",
        back_populates="safety_events"
    )

    message = relationship(
        "Message",
        back_populates="safety_event"
    )


# ==========================================================
# Evaluation Metrics Table
# ==========================================================

class EvalMetric(Base):
    """
    Stores evaluation scores.
    """

    __tablename__ = "eval_metrics"

    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    session_id = Column(
        String,
        ForeignKey("sessions.id"),
        nullable=False
    )

    turn_number = Column(
        Integer,
        nullable=False
    )

    empathy_score = Column(
        Float,
        nullable=False
    )

    helpfulness_score = Column(
        Float,
        nullable=False
    )

    safety_score = Column(
        Float,
        nullable=False
    )

    created_at = Column(
        DateTime,
        default=lambda: datetime.now(UTC)
    )

    # ---------------------------
    # Relationship
    # ---------------------------

    session = relationship(
        "Session",
        back_populates="eval_metrics"
    )