from pathlib import Path
import chromadb

DB_PATH = (
    Path(__file__).parent.parent
    / "chroma_db"
)

print("Database Path:")
print(DB_PATH)

client = chromadb.PersistentClient(
    path=str(DB_PATH)
)

print("\nCollections:")
print(client.list_collections())

collection = client.get_collection(
    "counseling_kb"
)

print(
    "\nDocuments:",
    collection.count()
)