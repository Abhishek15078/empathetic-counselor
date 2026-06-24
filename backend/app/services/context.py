from pathlib import Path


class ContextBuilder:

    def build(
        self,
        session,
        emotion_result,
        rag_chunks
    ):

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

        messages.append(
            {
                "role": "system",
                "content": rag_context
            }
        )

        messages.extend(
            session.get_history(
                max_turns=10
            )
        )

        return messages