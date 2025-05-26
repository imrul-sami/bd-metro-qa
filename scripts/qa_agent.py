from sentence_transformers import SentenceTransformer
import chromadb

model = SentenceTransformer("all-MiniLM-L6-v2")
chroma_client = chromadb.PersistentClient(path="./chroma_db")
collection = chroma_client.get_or_create_collection("metro_docs")

while True:
    query = input("❓ প্রশ্ন করুন: ")
    if query.lower() in ["exit", "quit"]:
        break

    query_embedding = model.encode([query])[0]
    results = collection.query(query_embeddings=[query_embedding], n_results=3)
    contexts = results["documents"][0]

    print("\n🔍 Relevant Information from Metro Rail Docs:\n")
    for i, context in enumerate(contexts, 1):
        print(f"[{i}] {context}\n")

