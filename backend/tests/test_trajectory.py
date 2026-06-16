from datetime import datetime

from app.models.emotion import (
    EmotionResult,
    EmotionLabel,
    IntensityLevel,
    TrajectoryLabel
)

from app.services.memory import (
    TrajectoryTracker
)


def create_emotion(
    label: EmotionLabel
):

    return EmotionResult(
        label=label,
        score=0.9,
        intensity=IntensityLevel.HIGH,
        is_concerning=False,
        timestamp=datetime.now()
    )


def test_improving():

    emotion_log = [

        create_emotion(
            EmotionLabel.FEAR
        ),

        create_emotion(
            EmotionLabel.FEAR
        ),

        create_emotion(
            EmotionLabel.SADNESS
        ),

        create_emotion(
            EmotionLabel.NEUTRAL
        ),

        create_emotion(
            EmotionLabel.JOY
        ),

        create_emotion(
            EmotionLabel.JOY
        )
    ]

    trajectory = (
        TrajectoryTracker.analyze(
            emotion_log
        )
    )

    assert (
        trajectory
        ==
        TrajectoryLabel.IMPROVING
    )


def test_worsening():

    emotion_log = [

        create_emotion(
            EmotionLabel.JOY
        ),

        create_emotion(
            EmotionLabel.JOY
        ),

        create_emotion(
            EmotionLabel.NEUTRAL
        ),

        create_emotion(
            EmotionLabel.FEAR
        ),

        create_emotion(
            EmotionLabel.SADNESS
        ),

        create_emotion(
            EmotionLabel.FEAR
        )
    ]

    trajectory = (
        TrajectoryTracker.analyze(
            emotion_log
        )
    )

    assert (
        trajectory
        ==
        TrajectoryLabel.WORSENING
    )


def test_stable():

    emotion_log = [

        create_emotion(
            EmotionLabel.SADNESS
        ),

        create_emotion(
            EmotionLabel.SADNESS
        ),

        create_emotion(
            EmotionLabel.SADNESS
        ),

        create_emotion(
            EmotionLabel.SADNESS
        ),

        create_emotion(
            EmotionLabel.SADNESS
        ),

        create_emotion(
            EmotionLabel.SADNESS
        )
    ]

    trajectory = (
        TrajectoryTracker.analyze(
            emotion_log
        )
    )

    assert (
        trajectory
        ==
        TrajectoryLabel.STABLE
    )


def test_insufficient_history():

    emotion_log = [

        create_emotion(
            EmotionLabel.FEAR
        ),

        create_emotion(
            EmotionLabel.SADNESS
        )
    ]

    trajectory = (
        TrajectoryTracker.analyze(
            emotion_log
        )
    )

    assert (
        trajectory
        ==
        TrajectoryLabel.STABLE
    )