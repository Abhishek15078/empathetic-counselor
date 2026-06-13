from pathlib import Path

from app.models.emotion import EmotionResult


class ResponseFormatter:

    TEMPLATE_PATH = (
        Path(__file__)
        .parent.parent
        / "prompts"
        / "emotion_context.txt"
    )

    @classmethod
    def format_emotion_context(
        cls,
        emotion: EmotionResult
    ) -> str:

        template = cls.TEMPLATE_PATH.read_text(
            encoding="utf-8"
        )

        return template.format(
            emotion=emotion.label.value,
            intensity=emotion.intensity.value,
            is_concerning=emotion.is_concerning
        )