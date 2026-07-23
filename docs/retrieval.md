# Retrieval & RAG

This section explains retrieval-augmented generation (RAG) patterns, vector stores, and strategies for serving retrieval layers.

Topics covered

- Document ingestion and normalization
- Embeddings and vector stores
- Retrieval strategies (BM25, TF-IDF, vector nearest-neighbor)
- Chunking, metadata, and filters
- Caching and freshness

Production retrieval strategy

1. Start with lexical baseline (TF-IDF/BM25) for explainability.
2. Add dense embeddings for semantic recall.
3. Use hybrid retrieval where both precision and recall matter.
4. Rerank top candidates before generation when latency budget allows.

Chunking guidance

- Use chunk sizes that preserve semantic boundaries.
- Keep overlap minimal but sufficient for context continuity.
- Store source metadata (document id, section, timestamp) for traceability.

Evaluation essentials

- Retrieval quality: precision@k, recall@k, MRR.
- End-to-end quality: groundedness and answer correctness.
- Operational quality: p95 latency, index update lag, error rates.

## FAISS and Dense Retrieval

For denser, semantic retrieval at scale, use FAISS + sentence-transformers for embeddings. See the `local-llm-chat-engine` `docs/faiss_runbook.md` for installation and endpoints to interact with a FAISS store.


Notes and sample code live in the `examples/` folder. For a lightweight retrieval demo, see the `local-llm-chat-engine` repository that accompanies these notes.
