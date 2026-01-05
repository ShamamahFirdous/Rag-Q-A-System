from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA

from config import *
from llm import get_llm
from colorama import Fore, Style, init
init(autoreset=True)


def ask(question: str):
    # 1) Same embeddings as ingest.py
    embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)

    # 2) Load FAISS (allow pickle load)
    db = FAISS.load_local(
        VECTOR_DB_PATH,
        embeddings,
        allow_dangerous_deserialization=True
    )

    # 3) Retriever
    retriever = db.as_retriever(search_kwargs={"k": 3})

    # 4) LLM (Ollama)
    llm = get_llm()

    # 5) RetrievalQA with sources enabled
    qa = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type="stuff",
        return_source_documents=True
    )

    # IMPORTANT: use invoke to get docs back
    result = qa.invoke({"query": question})

    answer = result["result"]
    docs = result.get("source_documents", [])

    # Build nice citations
    sources = []
    for i, d in enumerate(docs, start=1):
        src = d.metadata.get("source", "unknown")
        snippet = d.page_content[:160].replace("\n", " ")
        sources.append(f"[{i}] {src} — \"{snippet}...\"")

    return answer, sources


if __name__ == "__main__":
    while True:
        question = input("\nAsk a question (or type 'exit' to quit): ")
        if question.lower() == "exit":
            break

        answer, sources = ask(question)

        print(Fore.CYAN + "\nAnswer:\n" + Style.BRIGHT + answer)
print(Fore.MAGENTA + "\nSources:")
for s in sources:
    print(Fore.YELLOW + "- " + s)
