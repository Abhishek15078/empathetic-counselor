from app.services.orchestrator import (
    AIOrchestrator
)


def test_normal_pipeline():

    orchestrator = (
        AIOrchestrator()
    )

    session = (
        orchestrator.memory_manager
        .create_session()
    )

    result = (
        orchestrator.process_message(
            session.session_id,
            "I feel anxious about exams"
        )
    )

    assert result.safety_triggered is False
    assert result.response_text is not None
    assert result.emotion_result is not None
    assert result.processing_time_ms >= 0


def test_crisis_pipeline():

    orchestrator = (
        AIOrchestrator()
    )

    session = (
        orchestrator.memory_manager
        .create_session()
    )

    result = (
        orchestrator.process_message(
            session.session_id,
            "I want to kill myself"
        )
    )

    assert result.safety_triggered is True
    assert result.response_text is not None


def test_emotion_populated():

    orchestrator = (
        AIOrchestrator()
    )

    session = (
        orchestrator.memory_manager
        .create_session()
    )

    result = (
        orchestrator.process_message(
            session.session_id,
            "I feel very sad today"
        )
    )

    assert result.emotion_result is not None


def test_rag_documents_exist():

    orchestrator = (
        AIOrchestrator()
    )

    session = (
        orchestrator.memory_manager
        .create_session()
    )

    result = (
        orchestrator.process_message(
            session.session_id,
            "I am overwhelmed by exams"
        )
    )

    assert isinstance(
        result.rag_documents_used,
        list
    )


def test_processing_time():

    orchestrator = (
        AIOrchestrator()
    )

    session = (
        orchestrator.memory_manager
        .create_session()
    )

    result = (
        orchestrator.process_message(
            session.session_id,
            "I feel anxious"
        )
    )

    assert (
        result.processing_time_ms
        >= 0
    )


def test_turn_count_increases():

    orchestrator = (
        AIOrchestrator()
    )

    session = (
        orchestrator.memory_manager
        .create_session()
    )

    orchestrator.process_message(
        session.session_id,
        "I feel anxious"
    )

    result = (
        orchestrator.process_message(
            session.session_id,
            "Still feeling anxious"
        )
    )

    assert (
        result.turn_number >= 2
    )