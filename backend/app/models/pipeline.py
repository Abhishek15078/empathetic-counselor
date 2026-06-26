from dataclasses import dataclass

from app.models.emotion import EmotionResult
from app.models.emotion import TrajectoryLabel


@dataclass
class PipelineResult:

    response_text: str

    emotion_result: EmotionResult

    trajectory: TrajectoryLabel

    rag_documents_used: list[str]

    safety_triggered: bool

    turn_number: int

    processing_time_ms: int