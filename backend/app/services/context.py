from pathlib import Path

from app.models.db_models import Session


class ContextBuilder:
    """
    Builds the complete conversation context
    that is sent to the LLM.
    """

    def build(
        self,
        session: Session,
        emotion_result,
        rag_chunks
    ):

        # ----------------------------------
        # Load System Prompt
        # ----------------------------------

        prompt_path = (
            Path(__file__).parent.parent
            / "prompts"
            / "system.txt"
        )

        system_prompt = (
            prompt_path.read_text(
                encoding="utf-8"
            )
        )

        messages = [
            {
                "role": "system",
                "content": system_prompt
            }
        ]

        # ----------------------------------
        # Emotion Context
        # ----------------------------------

        emotion_context = f"""
Detected Emotion:
{emotion_result.label.value}

Intensity:
{emotion_result.intensity.value}
"""

        messages.append(
            {
                "role": "system",
                "content": emotion_context
            }
        )

        # ----------------------------------
        # RAG Context
        # ----------------------------------

        rag_context = ""

        for doc, meta in rag_chunks:

            meta = meta or {}

            category = meta.get(
                "category",
                "unknown"
            )

            rag_context += (
                f"\nRelevant Coping Strategy "
                f"({category}):\n"
                f"{doc}\n"
            )

        if rag_context:

            messages.append(
                {
                    "role": "system",
                    "content": rag_context
                }
            )

        # ----------------------------------
        # Conversation History
        # ----------------------------------

        conversation = sorted(
            session.messages,
            key=lambda message: message.turn_number
        )

        # Keep only the last 10 messages
        conversation = conversation[-10:]

        for message in conversation:

            messages.append(
                {
                    "role": message.role,
                    "content": message.content
                }
            )

        return messages