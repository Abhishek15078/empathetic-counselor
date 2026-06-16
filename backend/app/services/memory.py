import uuid

from datetime import datetime

from app.models.emotion import (
    EmotionResult,
    EmotionLabel,
    TrajectoryLabel
)


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
    
class TrajectoryTracker:

    VALENCE_MAP = {

    EmotionLabel.JOY: 2,

    EmotionLabel.LOVE: 1,

    EmotionLabel.SURPRISE: 0,

    EmotionLabel.NEUTRAL: 0,

    EmotionLabel.SADNESS: -1,

    EmotionLabel.ANGER: -1,

    EmotionLabel.FEAR: -2
}

    @classmethod
    def emotion_to_score(
        cls,
        emotion_label: EmotionLabel
    ):

        return cls.VALENCE_MAP[
            emotion_label
        ]

    @classmethod
    def analyze(
        cls,
        emotion_log: list
    ):

        # Need at least 6 emotions
        # (3 prior + 3 recent)

        if len(emotion_log) < 6:

            return (
                TrajectoryLabel.STABLE
            )

        prior_window = emotion_log[
            -6:-3
        ]

        recent_window = emotion_log[
            -3:
        ]

        prior_scores = [

            cls.emotion_to_score(
                emotion.label
            )

            for emotion in prior_window
        ]

        recent_scores = [

            cls.emotion_to_score(
                emotion.label
            )

            for emotion in recent_window
        ]

        mean_prior = (

            sum(prior_scores)

            /

            len(prior_scores)

        )

        mean_recent = (

            sum(recent_scores)

            /

            len(recent_scores)

        )

        difference = (

            mean_recent

            -

            mean_prior

        )

        if difference > 0.3:

            return (
                TrajectoryLabel.IMPROVING
            )

        if difference < -0.3:

            return (
                TrajectoryLabel.WORSENING
            )

        return (
            TrajectoryLabel.STABLE
        )    