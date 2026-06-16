from dataclasses import dataclass
from datetime import datetime
from enum import Enum


class EmotionLabel(Enum):
    JOY = "joy"
    SADNESS = "sadness"
    ANGER = "anger"
    FEAR = "fear"
    LOVE = "love"
    SURPRISE = "surprise"
    NEUTRAL = "neutral"


class IntensityLevel(Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"

class TrajectoryLabel(Enum):

    IMPROVING = "improving"

    STABLE = "stable"

    WORSENING = "worsening"


@dataclass
class EmotionResult:
    label: EmotionLabel
    score: float
    intensity: IntensityLevel
    is_concerning: bool
    timestamp: datetime