from datetime import datetime

from app.services.context import (
    ContextBuilder
)

from app.services.memory import (
    ConversationSession
)

from app.models.emotion import (
    EmotionResult,
    EmotionLabel,
    IntensityLevel
)


def test_context_builder():

    session = ConversationSession()

    session.add_message(
        role="user",
        content="I feel anxious about exams."
    )

    session.add_message(
        role="assistant",
        content="Can you tell me more about it?"
    )

    emotion_result = EmotionResult(
        label=EmotionLabel.FEAR,
        score=0.91,
        intensity=IntensityLevel.HIGH,
        is_concerning=True,
        timestamp=datetime.now()
    )

    rag_chunks = [
        (
            "Box breathing helps reduce anxiety.",
            {
                "category": "breathing"
            }
        ),
        (
            "Study planning reduces exam stress.",
            {
                "category": "academic"
            }
        )
    ]

    builder = ContextBuilder()

    messages = builder.build(
        session=session,
        emotion_result=emotion_result,
        rag_chunks=rag_chunks
    )

    # Messages array exists
    assert isinstance(messages, list)

    # Should contain multiple messages
    assert len(messages) > 0

    # OpenAI/Groq format validation
    for message in messages:

        assert "role" in message
        assert "content" in message

    # Conversation history included
    all_content = " ".join(
        msg["content"]
        for msg in messages
    )

    assert (
        "I feel anxious about exams."
        in all_content
    )

    assert (
        "Can you tell me more about it?"
        in all_content
    )

    # Emotion context included
    assert (
        emotion_result.label.value
        in all_content.lower()
    )

    # RAG context included
    assert (
        "Box breathing helps reduce anxiety."
        in all_content
    )

    assert (
        "Study planning reduces exam stress."
        in all_content
    )