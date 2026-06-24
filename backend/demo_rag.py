from app.services.rag import (
    RAGService
)

rag = RAGService()

results = rag.retrieve(
    query="I feel anxious and overwhelmed",
    emotion_label="fear"
)

for doc, meta in results:

    print("\nMetadata:")
    print(meta)

    print("\nDocument Preview:")
    print(doc[:200])

print("\n" + "=" * 50)

print("\nCombined Context:\n")

print(
    rag.get_context(
        query="I feel anxious and overwhelmed",
        emotion_label="fear"
    )
)