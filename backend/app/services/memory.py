from app.models.emotion import (
    EmotionLabel,
    TrajectoryLabel
)


class TrajectoryTracker:
    """
    Tracks whether the user's emotional
    trajectory is improving, worsening,
    or remaining stable.
    """

    VALENCE_MAP = {
        EmotionLabel.JOY: 2,
        EmotionLabel.LOVE: 1,
        EmotionLabel.SURPRISE: 0,
        EmotionLabel.NEUTRAL: 0,
        EmotionLabel.SADNESS: -1,
        EmotionLabel.ANGER: -1,
        EmotionLabel.FEAR: -2,
    }

    @classmethod
    def emotion_to_score(
        cls,
        emotion_label
    ):
        """
        Convert an emotion label
        into its numerical score.
        """

        if isinstance(emotion_label, str):
            emotion_label = EmotionLabel(
                emotion_label
            )

        return cls.VALENCE_MAP[
            emotion_label
        ]

    @classmethod
    def analyze(
        cls,
        emotion_log: list
    ):
        """
        Analyze emotional trajectory
        using the last six emotions.
        """

        # Need at least six emotions
        if len(emotion_log) < 6:
            return TrajectoryLabel.STABLE

        prior_window = emotion_log[-6:-3]

        recent_window = emotion_log[-3:]

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
            / len(prior_scores)
        )

        mean_recent = (
            sum(recent_scores)
            / len(recent_scores)
        )

        difference = (
            mean_recent
            - mean_prior
        )

        if difference > 0.3:
            return TrajectoryLabel.IMPROVING

        if difference < -0.3:
            return TrajectoryLabel.WORSENING

        return TrajectoryLabel.STABLE