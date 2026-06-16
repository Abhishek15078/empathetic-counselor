import uuid

from datetime import datetime

from app.models.emotion import EmotionResult


class ConversationSession:

    def __init__(self):

        self.session_id = str(
            uuid.uuid4()
        )

        self.created_at = (
            datetime.now()
        )

        self.messages = []

        self.emotion_log = []

    def add_message(
        self,
        role: str,
        content: str
    ):

        self.messages.append(
            {
                "role": role,
                "content": content
            }
        )

    def add_emotion(
        self,
        emotion_result: EmotionResult
    ):

        self.emotion_log.append(
            emotion_result
        )

    def get_history(
        self,
        max_turns: int = 20
    ):

        return self.messages[
            -max_turns:
        ]

    def get_emotion_log(self):

        return self.emotion_log


class SessionManager:

    def __init__(self):

        self.sessions = {}

    def create_session(self):

        session = (
            ConversationSession()
        )

        self.sessions[
            session.session_id
        ] = session

        return session

    def get_session(
        self,
        session_id: str
    ):

        if (
            session_id
            not in self.sessions
        ):

            raise ValueError(
                f"Session '{session_id}' not found"
            )

        return self.sessions[
            session_id
        ]

    def delete_session(
        self,
        session_id: str
    ):

        if (
            session_id
            not in self.sessions
        ):

            raise ValueError(
                f"Session '{session_id}' not found"
            )

        del self.sessions[
            session_id
        ]

    def get_all_sessions(self):

        return self.sessions