from pathlib import Path

import chromadb
from sentence_transformers import SentenceTransformer


class RAGService:

    def __init__(self):

        self.model = SentenceTransformer(
            "all-MiniLM-L6-v2"
        )

        db_path = (
            Path(__file__)
            .resolve()
            .parents[2]
            / "chroma_db"
        )

        print("=" * 60)
        print("RAG DATABASE PATH")
        print(db_path)
        print("=" * 60)

        self.client = chromadb.PersistentClient(
            path=str(db_path)
        )

        print("=" * 60)
        print("AVAILABLE COLLECTIONS")
        print(self.client.list_collections())
        print("=" * 60)

        self.collection = self.client.get_collection(
            name="counseling_kb"
        )

    def retrieve(
        self,
        query: str,
        emotion_label: str,
        n_results: int = 3
    ):

        search_query = f"{emotion_label} {query}"

        results = self.collection.query(
            query_texts=[search_query],
            n_results=n_results
        )

        documents = results["documents"][0]
        metadatas = results["metadatas"][0]

        return list(zip(documents, metadatas))

    def get_context(
        self,
        query: str,
        emotion_label: str,
        n_results: int = 3
    ):

        retrieved = self.retrieve(
            query,
            emotion_label,
            n_results
        )

        return "\n\n".join(
            doc for doc, _ in retrieved
        )