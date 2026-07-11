from app.services.llm import LLMCaller


class BaselineSystem:
    """
    Baseline system.

    Uses only the conversation history.

    No:

    - Emotion Detection
    - RAG
    - Trajectory
    """

    def __init__(self):

        self.llm = LLMCaller()

    def build_messages(

        self,

        user_message: str,

        history: list[dict] | None = None

    ):

        messages = [

            {

                "role": "system",

                "content": (
                    "You are a helpful AI assistant."
                    "Answer naturally."
                )

            }

        ]

        if history:

            for message in history:

                messages.append(

                    {

                        "role": message["role"],

                        "content": message["content"]

                    }

                )

        messages.append(

            {

                "role": "user",

                "content": user_message

            }

        )

        return messages

    def generate_response(

        self,

        user_message: str,

        history: list[dict] | None = None

    ) -> str:

        messages = self.build_messages(

            user_message,

            history

        )

        return self.llm.generate_from_messages(

            messages

        )