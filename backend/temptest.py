from app.services.emotion import EmotionClassifier

classifier = EmotionClassifier()

result = classifier.classify(
    "I feel extremely anxious and overwhelmed today"
)

print(result)