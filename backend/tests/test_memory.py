import pytest

from app.services.memory import (
    ConversationSession,
    SessionManager
)


def test_unique_session_ids():

    manager = SessionManager()

    session1 = manager.create_session()

    session2 = manager.create_session()

    assert (
        session1.session_id
        != session2.session_id
    )


def test_history_sliding_window():

    session = ConversationSession()

    for i in range(25):

        session.add_message(
            role="user",
            content=f"message {i}"
        )

    history = session.get_history(
        max_turns=20
    )

    assert len(history) == 20


def test_message_order_preserved():

    session = ConversationSession()

    session.add_message(
        role="user",
        content="msg1"
    )

    session.add_message(
        role="assistant",
        content="msg2"
    )

    session.add_message(
        role="user",
        content="msg3"
    )

    history = session.get_history()

    assert (
        history[0]["content"]
        == "msg1"
    )

    assert (
        history[1]["content"]
        == "msg2"
    )

    assert (
        history[2]["content"]
        == "msg3"
    )


def test_invalid_session_id():

    manager = SessionManager()

    with pytest.raises(
        ValueError
    ):

        manager.get_session(
            "fake-id"
        )