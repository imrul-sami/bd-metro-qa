# BD Metro Rail Q&A Agent

A simple question-answering agent for Bangladesh Metro Rail information using semantic search with vector embeddings.

## Features

- Loads BD Metro Rail documentation
- Embeds into vector database (ChromaDB)
- Query any question in Bangla or English and get relevant answers

## Project Structure

bd-metro-qa/
├── data/ # Metro Rail Docs
├── scripts/ # Core scripts
├── chroma_db/ # Vector Database (auto-generated)
├── venv/ # Virtual Environment (not uploaded)
├── README.md
├── requirements.txt
└── .gitignore

## ⚙️ Installation & Setup

```bash
git clone <your-github-repo-url>
cd bd-metro-qa
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt