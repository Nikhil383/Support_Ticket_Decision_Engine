from pathlib import Path

import chromadb

from sentence_transformers import (
    SentenceTransformer
)


class KnowledgeBase:

    def __init__(
        self,
        knowledge_dir="data/knowledge",
    ):

        self.knowledge_dir = Path(
            knowledge_dir
        )

        self.embedder = (
            SentenceTransformer(
                "all-MiniLM-L6-v2"
            )
        )

        self.client = (
            chromadb.PersistentClient(
                path=".chroma"
            )
        )

        self.collection = (
            self.client.get_or_create_collection(
                "support_knowledge"
            )
        )

        self._index_documents()

    def _index_documents(self):

        documents = []
        ids = []
        metadata = []

        for path in sorted(
            self.knowledge_dir.glob("*.md")
        ):

            documents.append(
                path.read_text(
                    encoding="utf-8"
                )
            )

            ids.append(
                path.name
            )

            metadata.append(
                {
                    "source": path.name
                }
            )

        if documents:

            embeddings = (
                self.embedder
                .encode(documents)
                .tolist()
            )

            self.collection.upsert(
                ids=ids,
                documents=documents,
                embeddings=embeddings,
                metadatas=metadata,
            )

    def search(
        self,
        query: str,
        top_k: int = 3,
    ):

        embedding = (
            self.embedder
            .encode([query])
            .tolist()
        )

        result = (
            self.collection.query(
                query_embeddings=embedding,
                n_results=top_k,
            )
        )

        documents = result.get(
            "documents",
            [[]],
        )[0]

        metadatas = result.get(
            "metadatas",
            [[]],
        )[0]

        return list(
            zip(
                documents,
                metadatas,
            )
        )