from sentence_transformers import SentenceTransformer
import chromadb

def load_metro_docs(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read().split('\n\n')

docs = load_metro_docs("data/metro_rail_docs.txt")

chroma_client = chromadb.PersistentClient(path="./chroma_db")
collection = chroma_client.get_or_create_collection("metro_docs")

embedder = SentenceTransformer("all-MiniLM-L6-v2")

for chunk in docs:
    if chunk.strip():
        embedding = embedder.encode(chunk)
        collection.add(documents=[chunk], embeddings=[embedding])

print("✅ Metro Rail Docs Embedded Successfully!")

