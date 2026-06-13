import os
from pathlib import Path

from dotenv import load_dotenv
from groq import Groq

from datetime import datetime

from app.models.emotion import (
    EmotionResult,
    EmotionLabel,
    IntensityLevel
)

env_path = (
    Path(__file__).parent.parent.parent
    / ".env"
)

load_dotenv(env_path)


class LLMCaller:

    def __init__(self):

        self.api_key = os.getenv(
    "GROQ_API_KEY"
)

        if not self.api_key:

            raise ValueError(
                "GROQ_API_KEY not found"
            )

        self.client = Groq(
            api_key=self.api_key
        )

        app_dir = (
            Path(__file__).parent.parent
        )

        system_prompt_path = (
            app_dir
            / "prompts"
            / "system.txt"
        )

        emotion_prompt_path = (
            app_dir
            / "prompts"
            / "emotion_context.txt"
        )

        self.system_prompt = (
            system_prompt_path.read_text(
                encoding="utf-8"
            )
        )

        self.emotion_template = (
            emotion_prompt_path.read_text(
                encoding="utf-8"
            )
        )

    def build_messages(
        self,
        emotion_result: EmotionResult,
        user_message: str
    ):

        emotion_context = (
            self.emotion_template.format(
                emotion=emotion_result.label.value,
                intensity=emotion_result.intensity.value,
                is_concerning=emotion_result.is_concerning
            )
        )

        messages = [
            {
                "role": "system",
                "content": self.system_prompt
            },
            {
                "role": "user",
                "content": (
                    emotion_context
                    + "\n\n"
                    + user_message
                )
            }
        ]

        return messages

    def generate_response(
        self,
        emotion_result: EmotionResult,
        user_message: str
    ):

        messages = self.build_messages(
            emotion_result=emotion_result,
            user_message=user_message
        )

        response = self.client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=messages,
            temperature=0.6,
            max_tokens=250
        )

        return (
            response
            .choices[0]
            .message
            .content
        )


if __name__ == "__main__":

    test_emotion = EmotionResult(
        label=EmotionLabel.FEAR,
        score=0.91,
        intensity=IntensityLevel.HIGH,
        is_concerning=True,
        timestamp=datetime.now()
    )

    llm = LLMCaller()

    reply = llm.generate_response(
        emotion_result=test_emotion,
        user_message=(
            "I have been feeling overwhelmed "
            "and unable to focus on my work lately."
        )
    )

    print(reply)