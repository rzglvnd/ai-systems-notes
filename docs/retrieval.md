# Retrieval & RAG

This section explains retrieval-augmented generation (RAG) patterns, vector stores, and strategies for serving retrieval layers.

Topics covered

- Document ingestion and normalization
- Embeddings and vector stores
- Retrieval strategies (BM25, TF-IDF, vector nearest-neighbor)
- Chunking, metadata, and filters
- Caching and freshness

## FAISS and Dense Retrieval

For denser, semantic retrieval at scale, use FAISS + sentence-transformers for embeddings. See the `local-llm-chat-engine` `docs/faiss_runbook.md` for installation and endpoints to interact with a FAISS store.


Notes and sample code live in the `examples/` folder. For a lightweight retrieval demo, see the `local-llm-chat-engine` repository that accompanies these notes.
