import os

def load_metro_docs(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

if __name__ == "__main__":
    docs = load_metro_docs("data/metro_rail_docs.txt")
    print("📄 BD Metro Rail Docs Loaded Successfully!")
    print(docs[:500])  # প্রথম 500 অক্ষর প্রিন্ট করবে
