# 🔍 Local RAG: Retrieval-Augmented Generation with Multiple File Types

> A local, file-based Retrieval-Augmented Generation (RAG) system using LangChain, FAISS, and HuggingFace embeddings.  
> Supports `.txt`, `.pdf`, `.md`, `.csv`, and `.docx` files out of the box — no internet, no APIs required!

---

## 📘 What is Retrieval-Augmented Generation?

**Retrieval-Augmented Generation (RAG)** combines the power of document retrieval with the language generation abilities of LLMs.

Instead of relying on the model's internal knowledge alone, RAG enables the model to **search through local documents** and use them to answer queries.  
This ensures:
- Better factual accuracy
- Domain-specific responses
- Custom QA for internal documents

---

## 📂 Supported File Types

This RAG system can load and chunk the following formats:

| File Type | Description              |
|-----------|--------------------------|
| `.txt`    | Plain text files         |
| `.md`     | Markdown files           |
| `.csv`    | Structured tabular data  |
| `.pdf`    | PDF documents            |
| `.docx`   | Microsoft Word documents |

All files should be placed inside the `data/` directory.

---

## 🛠️ Setup Instructions

1. **Clone this repository**
```bash
git clone https://github.com/your-username/local-rag.git
cd local-rag
```

2. **Create a virtual environment**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

> If `.docx` support fails, install this manually:
```bash
pip install docx2txt
```

---

## 📁 Add Your Data

Place your files into the `data/` folder. For example:
```
data/
├── notes.md
├── faq.csv
├── rag.pdf
├── intro_to_rag.docx
├── applications.txt
```

---

## ⚙️ Run the Ingestion Script

This script loads documents and saves the vectorstore.

```bash
python3 src/ingest.py
```

✅ Output example:
```
[.txt/.md] ✅ Loaded: data/notes.md
[.pdf]     ✅ Loaded: data/rag.pdf
[.csv]     ✅ Loaded: data/faq.csv
[.docx]    ✅ Loaded: data/intro_to_rag.docx
Chunks created: 173
Vectorstore saved at: vectorstore
```

---

## 💬 Ask Questions (RAG in Action)

Run your RAG chain (example script):

```bash
python3 src/rag_chain.py
```

Sample prompt:
```
> What is Retrieval-Augmented Generation?
```

📌 The system will respond with a grounded answer pulled from your documents.

---

## 🖼️ Example Output

### 🔡 Ingestion Output
![RAG QA Success Output](https://github.com/ShamamahFirdous/Rag-Q-A-System/blob/main/assets/sucess%20output.png?raw=true)


### 🤖 RAG QA Output
![RAG Demo Output](https://github.com/ShamamahFirdous/Rag-Q-A-System/blob/main/assets/answer.png?raw=true)


---

## ✨ Highlights

- 💻 100% Local — No API keys required
- 🧠 Accurate — Answers grounded in your files
- 🧩 Modular — Easy to extend with new loaders
- 📁 Multi-format — Supports 5+ file types

---

## 🧩 Future Ideas

- Add support for `.json` and `.html`
- Streamlit or Gradio frontend for chatting
- Web search + file retrieval hybrid RAG

---

## 🙌 Credits

- LangChain
- HuggingFace Embeddings
- FAISS for vector indexing
- `docx2txt`, `PyMuPDF`, and `pandas` for parsing

---

## 📎 License

MIT License. Feel free to fork, use, and extend!

