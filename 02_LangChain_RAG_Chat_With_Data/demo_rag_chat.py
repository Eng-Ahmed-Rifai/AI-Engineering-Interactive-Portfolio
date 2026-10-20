"""
Interactive CLI for RAG Chat over Data
Author: Ahmed Mohamed Abdullatif Rifai
"""

from rag_pipeline import RAGPipeline

def main():
    rag = RAGPipeline(chunk_size=160, chunk_overlap=30)
    
    knowledge_base = (
        "ChromaDB is the open-source embedding database. Chroma makes it easy to build LLM apps by making knowledge, "
        "facts, and skills pluggable for LLMs. It comes with everything you need: embeddings, vector search, document "
        "storage, and filtering. You can install Chroma using pip install chromadb. When combined with LangChain, "
        "Chroma serves as an optimal persistence store for RAG applications."
    )
    rag.ingest_text(knowledge_base, source_name="chromadb_overview.md")

    print("==================================================================")
    print("   LangChain Production RAG Engine CLI Demonstration")
    print("   Engineer: Ahmed Mohamed Abdullatif Rifai")
    print("==================================================================\n")

    queries = [
        "What is ChromaDB and how is it installed?",
        "How does Chroma combine with LangChain?"
    ]

    for q in queries:
        print(f"\nUser Query: {q}")
        res = rag.query(q, k=2)
        print(f"Agent Response:\n{res['answer']}")
        print("Retrieved Passages:")
        for idx, (chunk, score) in enumerate(res["retrieved_chunks"]):
            print(f"  [{idx+1}] (Cosine: {score:.3f}): {chunk}")

if __name__ == "__main__":
    main()
