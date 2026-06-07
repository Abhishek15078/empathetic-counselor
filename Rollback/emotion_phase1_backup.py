from transformers import pipeline


class EmotionClassifier:

    def __init__(self):

        self.pipeline = pipeline(
            task="text-classification",
            model="j-hartmann/emotion-english-distilroberta-base",
            top_k=1
        )

    def classify(self, text: str) -> dict:

        if not text.strip():
            return {
                "label": "neutral",
                "score": 0.0
            }

        result = self.pipeline(
            text,
            truncation=True
        )

        prediction = result[0][0]

        return {
            "label": prediction["label"],
            "score": float(prediction["score"])
        }