import os
from pathlib import Path
from datetime import datetime

from dotenv import load_dotenv
from groq import Groq

from app.models.emotion import (
    EmotionResult,
    EmotionLabel,
    IntensityLevel
)

# -------------------------------------------------
# Load .env
# -------------------------------------------------

env_path = (
    Path(__file__).parent.parent.parent
    / ".env"
)

load_dotenv(env_path)


class LLMCaller:
    """
    Handles all communication with Groq LLM.
    """

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

        self.model_name = (
            "llama-3.3-70b-versatile"
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

    # -------------------------------------------------
    # Build Prompt
    # -------------------------------------------------

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

    # -------------------------------------------------
    # Standard LLM Response
    # -------------------------------------------------

    def generate_response(
        self,
        emotion_result: EmotionResult,
        user_message: str
    ):

        messages = self.build_messages(
            emotion_result,
            user_message
        )

        response = (
            self.client.chat.completions.create(
                model=self.model_name,
                messages=messages,
                temperature=0.6,
                max_tokens=250
            )
        )

        return (
            response
            .choices[0]
            .message
            .content
        )

    # -------------------------------------------------
    # Phase 9
    # Used by AIOrchestrator
    # -------------------------------------------------

    def generate_from_messages(
        self,
        messages
    ):
        """
        Generates a response from an already
        prepared message list.
        """

        response = (
            self.client.chat.completions.create(
                model=self.model_name,
                messages=messages,
                temperature=0.6,
                max_tokens=250
            )
        )

        return (
            response
            .choices[0]
            .message
            .content
        )

    # -------------------------------------------------
    # Phase 8
    # Semantic Crisis Detection
    # -------------------------------------------------

    def classify_crisis(
        self,
        message: str
    ) -> bool:

        app_dir = (
            Path(__file__).parent.parent
        )

        crisis_prompt_path = (
            app_dir
            / "prompts"
            / "crisis_classifier.txt"
        )

        prompt_template = (
            crisis_prompt_path.read_text(
                encoding="utf-8"
            )
        )

        prompt = (
            prompt_template.replace(
                "{message}",
                message
            )
        )

        response = (
            self.client.chat.completions.create(
                model=self.model_name,
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=0,
                max_tokens=5
            )
        )

        result = (
            response
            .choices[0]
            .message
            .content
            .strip()
            .upper()
        )

        return result == "YES"


# -------------------------------------------------
# Manual Testing
# -------------------------------------------------

if __name__ == "__main__":

    test_emotion = EmotionResult(
        label=EmotionLabel.FEAR,
        score=0.91,
        intensity=IntensityLevel.HIGH,
        is_concerning=True,
        timestamp=datetime.now()
    )

    llm = LLMCaller()

    print("=" * 60)
    print("STANDARD RESPONSE")
    print("=" * 60)

    reply = llm.generate_response(
        emotion_result=test_emotion,
        user_message=(
            "I have been feeling overwhelmed "
            "and unable to focus on work."
        )
    )

    print(reply)

    print("\n" + "=" * 60)
    print("CRISIS CLASSIFIER")
    print("=" * 60)

    crisis = llm.classify_crisis(
        "I don't know if I can keep going anymore."
    )

    print(crisis)

    print("\n" + "=" * 60)
    print("MESSAGE LIST API")
    print("=" * 60)

    messages = [
        {
            "role": "system",
            "content": "You are a helpful assistant."
        },
        {
            "role": "user",
            "content": "Hello"
        }
    ]

    print(
        llm.generate_from_messages(
            messages
        )
    )