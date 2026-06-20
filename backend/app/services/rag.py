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

        self.client = (
            chromadb.PersistentClient(
                path="../chroma_db"
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
        n_results: int = 3
    ):

        results = (
            self.collection.query(
                query_texts=[query],
                n_results=n_results
            )
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
        n_results: int = 3
    ):

        retrieved_docs = (
            self.retrieve(
                query,
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