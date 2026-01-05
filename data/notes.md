# Notes on Retrieval-Augmented Generation (RAG)

## 🔍 What is RAG?

RAG combines a retriever and a generator model. It fetches relevant chunks from a document store and then uses a language model (e.g., GPT) to generate answers based on that retrieved knowledge.

## 🧠 Why use RAG?

- It reduces hallucinations.
- Makes language models grounded in real knowledge.
- Enables querying of private datasets.

## ⚙️ Architecture Overview

1. **Retriever**: Finds top-k relevant chunks (e.g., FAISS or BM25).
2. **Generator**: Uses retrieved chunks + question to answer.
3. **Reranker (optional)**: Improves quality by re-scoring chunks.
