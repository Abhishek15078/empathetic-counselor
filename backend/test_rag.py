from app.services.rag import (
    RAGService
)

rag = RAGService()

results = rag.retrieve(
    "I feel anxious and overwhelmed"
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
        "I feel anxious and overwhelmed"
    )
)