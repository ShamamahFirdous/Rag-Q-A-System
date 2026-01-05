from pathlib import Path
import os
from langchain_community.document_loaders import Docx2txtLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader, PyMuPDFLoader, CSVLoader
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from config import *

# 🧠 Load .txt, .pdf, .md, .csv documents
documents = []
for root, _, files in os.walk(DATA_PATH):
    for file in files:
        filepath = os.path.join(root, file)
        ext = os.path.splitext(file)[-1].lower()
        try:
            if ext in [".txt", ".md"]:
                documents.extend(TextLoader(filepath).load())
                print(f"\033[92m[.txt/.md] ✅ Loaded: {filepath}\033[0m")

            elif ext == ".docx":
                 documents.extend(Docx2txtLoader(filepath).load())
                 print(f"\033[96m[.docx]\033[0m Loaded: {filepath}")
    
            elif ext == ".pdf":
                documents.extend(PyMuPDFLoader(filepath).load())
                print(f"\033[94m[.pdf] ✅ Loaded: {filepath}\033[0m")
            elif ext == ".csv":
                documents.extend(CSVLoader(filepath).load())
                print(f"\033[93m[.csv] ✅ Loaded: {filepath}\033[0m")
            
        except Exception as e:
            print(f"\033[91m❌ Failed to load {filepath}: {e}\033[0m")

print(f"\n📄 Total documents loaded: \033[93m{len(documents)}\033[0m")

# ✂️ Split into chunks
splitter = RecursiveCharacterTextSplitter(chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP)
chunks = splitter.split_documents(documents)
print(f"🔪 Chunks created: \033[96m{len(chunks)}\033[0m")

# 🔗 Embed and save vectorstore
embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)
db = FAISS.from_documents(chunks, embeddings)
db.save_local(VECTOR_DB_PATH)
print("✅ Vectorstore saved at:", VECTOR_DB_PATH)
