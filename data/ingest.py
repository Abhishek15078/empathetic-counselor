from pathlib import Path

import chromadb

from sentence_transformers import (
    SentenceTransformer
)

DATA_DIR = Path(
    "data/processed"
)

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

DB_PATH = (
    Path(__file__).resolve().parents[1]
    / "backend"
    / "chroma_db"
)

print("Saving Chroma DB to:")
print(DB_PATH)

client = chromadb.PersistentClient(
    path=str(DB_PATH)
)

collection = client.get_or_create_collection(
    name="counseling_kb"
)

files = list(
    DATA_DIR.rglob("*.txt")
)
print(
    f"Found {len(files)} files"
)

for f in files:
    print(f)

for file in files:

    text = file.read_text(
        encoding="utf-8"
    )

    embedding = model.encode(
        text
    ).tolist()

    collection.add(
        ids=[file.stem],
        documents=[text],
        embeddings=[embedding],
        metadatas=[
            {
                "source": file.name,
                "category": file.parent.name            }
        ]
    )

    print(
        f"Added {file.name}"
    )

print(
    "\nKnowledge Base Ready!"
)