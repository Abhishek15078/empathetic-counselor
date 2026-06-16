from datetime import datetime

from app.models.emotion import (
    EmotionResult,
    EmotionLabel,
    IntensityLevel
)

from app.services.memory import (
    TrajectoryTracker
)


emotion_log = [

    EmotionResult(
        label=EmotionLabel.FEAR,
        score=0.95,
        intensity=IntensityLevel.HIGH,
        is_concerning=True,
        timestamp=datetime.now()
    ),

    EmotionResult(
        label=EmotionLabel.FEAR,
        score=0.92,
        intensity=IntensityLevel.HIGH,
        is_concerning=True,
        timestamp=datetime.now()
    ),

    EmotionResult(
        label=EmotionLabel.SADNESS,
        score=0.88,
        intensity=IntensityLevel.HIGH,
        is_concerning=True,
        timestamp=datetime.now()
    ),

    EmotionResult(
        label=EmotionLabel.NEUTRAL,
        score=0.70,
        intensity=IntensityLevel.MEDIUM,
        is_concerning=False,
        timestamp=datetime.now()
    ),

    EmotionResult(
        label=EmotionLabel.JOY,
        score=0.93,
        intensity=IntensityLevel.HIGH,
        is_concerning=False,
        timestamp=datetime.now()
    ),

    EmotionResult(
        label=EmotionLabel.JOY,
        score=0.96,
        intensity=IntensityLevel.HIGH,
        is_concerning=False,
        timestamp=datetime.now()
    )
]


trajectory = TrajectoryTracker.analyze(
    emotion_log
)

print("\nEmotion Sequence:")

for emotion in emotion_log:

    print(
        emotion.label.value
    )

print("\nTrajectory:")

print(
    trajectory.value
)