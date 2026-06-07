from transformers import pipeline

classifier = pipeline(
    "text-classification",
    model="j-hartmann/emotion-english-distilroberta-base"
)

print(
    classifier(
        "I am anxious about my exams"
    )
)