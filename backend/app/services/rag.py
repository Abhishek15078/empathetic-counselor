from pathlib import Path
import chromadb

from sentence_transformers import (
    SentenceTransformer
)
class RAGService:

    def __init__(self):

        self.model = (
            SentenceTransformer(
                "all-MiniLM-L6-v2"
            )
        )
        db_path = (
            Path(__file__)
            .resolve()
            .parent.parent.parent.parent
            / "chroma_db"
            )

        self.client = (
            chromadb.PersistentClient(
                path=str(db_path)
            )
        )

        self.collection = (
            self.client.get_collection(
                "counseling_kb"
            )
        )

    def retrieve(
        self,
        query: str,
        emotion_label: str,
        n_results: int = 3
    ):

        search_query = (
            f"{emotion_label} "
            f"{query}"
        )

        results = self.collection.query(
            query_texts=[
                search_query
            ],
            n_results=n_results
        )

        documents = (
            results["documents"][0]
        )

        metadatas = (
            results["metadatas"][0]
        )

        return list(
            zip(
                documents,
                metadatas
            )
        )

    def get_context(
        self,
        query: str,
        emotion_label: str,
        n_results: int = 3
    ):

        retrieved_docs = (
            self.retrieve(
                query,
                emotion_label,
                n_results
            )
        )

        context_parts = []

        for doc, _ in retrieved_docs:

            context_parts.append(
                doc
            )

        return "\n\n".join(
            context_parts
        )