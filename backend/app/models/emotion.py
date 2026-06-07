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


@dataclass
class EmotionResult:
    label: EmotionLabel
    score: float
    intensity: IntensityLevel
    is_concerning: bool
    timestamp: datetime