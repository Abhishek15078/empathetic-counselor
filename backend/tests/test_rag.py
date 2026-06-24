from app.services.rag import (
    RAGService
)


def test_rag_retrieval():

    rag = RAGService()

    results = rag.retrieve(
        query="I feel anxious and overwhelmed",
        emotion_label="fear"
    )

    assert len(results) > 0

    for doc, meta in results:

        assert len(doc) > 0
        assert isinstance(meta, dict)