from pydantic import BaseModel, ConfigDict


# --------------------------------------------------
# Session
# --------------------------------------------------

class SessionResponse(BaseModel):
    """
    Response returned after creating a new session.
    """

    session_id: str


# --------------------------------------------------
# Message
# --------------------------------------------------

class MessageRequest(BaseModel):
    """
    Request body for sending a message.
    """

    session_id: str
    message: str


class MessageResponse(BaseModel):
    """
    Response returned after the AI processes a message.
    """

    response_text: str

    emotion: str | None = None

    trajectory: str | None = None

    safety_triggered: bool

    processing_time_ms: int


# --------------------------------------------------
# Message History (NEW)
# --------------------------------------------------

class MessageHistoryItem(BaseModel):
    """
    Represents a single stored message.
    """

    role: str

    content: str

    turn_number: int

    model_config = ConfigDict(
        from_attributes=True
    )


class MessageHistoryResponse(BaseModel):
    """
    Response returned by
    GET /api/messages/{session_id}
    """

    messages: list[MessageHistoryItem]


# --------------------------------------------------
# Summary
# --------------------------------------------------

class SummaryResponse(BaseModel):
    """
    Response returned for conversation summary.
    """

    session_id: str

    turn_count: int

    emotion_arc: list[str]

    trajectory: str

    key_moments: list[str]


# --------------------------------------------------
# Health
# --------------------------------------------------

class HealthResponse(BaseModel):
    """
    Health check endpoint response.
    """

    status: str