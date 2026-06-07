from datetime import datetime, UTC

from transformers import pipeline

from app.models.emotion import (
    EmotionLabel,
    IntensityLevel,
    EmotionResult
)


class EmotionClassifier:

    def __init__(self):

        self.pipeline = pipeline(
            task="text-classification",
            model="j-hartmann/emotion-english-distilroberta-base",
            top_k=1
        )

    def _get_intensity(
        self,
        score: float
    ) -> IntensityLevel:

        if score >= 0.70:
            return IntensityLevel.HIGH

        if score >= 0.40:
            return IntensityLevel.MEDIUM

        return IntensityLevel.LOW

    def _is_concerning(
        self,
        label: EmotionLabel,
        score: float
    ) -> bool:

        concerning_emotions = {
            EmotionLabel.SADNESS,
            EmotionLabel.FEAR,
            EmotionLabel.ANGER
        }

        return (
            label in concerning_emotions
            and score >= 0.70
        )

    def classify(
        self,
        text: str
    ) -> EmotionResult:

        if not text.strip():

            return EmotionResult(
                label=EmotionLabel.NEUTRAL,
                score=0.0,
                intensity=IntensityLevel.LOW,
                is_concerning=False,
                timestamp=datetime.now(UTC)
            )

        result = self.pipeline(
            text,
            truncation=True
        )

        prediction = result[0][0]

        label = EmotionLabel(
            prediction["label"].lower()
        )

        score = float(
            prediction["score"]
        )

        intensity = self._get_intensity(
            score
        )

        is_concerning = self._is_concerning(
            label,
            score
        )

        return EmotionResult(
            label=label,
            score=score,
            intensity=intensity,
            is_concerning=is_concerning,
            timestamp=datetime.now(UTC)
        )