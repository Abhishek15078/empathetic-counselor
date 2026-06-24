from datetime import datetime

from app.models.emotion import (
    EmotionResult,
    EmotionLabel,
    IntensityLevel
)

from app.services.memory import (
    SessionManager,
    TrajectoryTracker
)

from app.services.rag import (
    RAGService
)

from app.services.context import (
    ContextBuilder
)


def main():

    manager = SessionManager()

    tracker = TrajectoryTracker()

    rag = RAGService()

    context_builder = ContextBuilder()

    # Create Session

    session = manager.create_session()

    # Simulated Emotion Detection Output

    emotion = EmotionResult(
        label=EmotionLabel.FEAR,
        score=0.91,
        intensity=IntensityLevel.HIGH,
        is_concerning=True,
        timestamp=datetime.now()
    )

    # Save Emotion

    session.add_emotion(
        emotion
    )

    # User Message

    message = (
        "I cannot stop worrying "
        "about my exams."
    )

    # Save Conversation

    session.add_message(
        "user",
        message
    )

    # Trajectory

    trajectory = tracker.analyze(
        session.emotion_log
    )

    print(
        "\nTrajectory:",
        trajectory.value
    )

    # RAG Retrieval

    rag_chunks = rag.retrieve(
        query=message,
        emotion_label=emotion.label.value
    )

    print(
        "\nRetrieved Chunks:"
    )

    for doc, meta in rag_chunks:

        print(
            "\nCategory:",
            meta.get(
                "category",
                "unknown"
            )
        )

        print(
            doc[:150]
        )

    # Context Building

    messages = context_builder.build(
        session=session,
        emotion_result=emotion,
        rag_chunks=rag_chunks
    )

    print(
        "\nFinal Messages Array:"
    )

    for msg in messages:

        print(
            "\nROLE:",
            msg["role"]
        )

        print(
            msg["content"][:300]
        )


if __name__ == "__main__":

    main()