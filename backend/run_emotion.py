from app.services.emotion import EmotionClassifier

classifier = EmotionClassifier()

result = classifier.classify(
    "I am worried about my exams"
)

print(result)