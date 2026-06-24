import chromadb

client = chromadb.PersistentClient(
    path="chroma_db"
)

print("Collections:")

for collection in client.list_collections():
    print(collection.name)