# Retrieval Examples

This page links to small retrieval experiments and example code used in the `local-llm-chat-engine` demo. It explains the TF-IDF fallback, vectorization notes, and how to evaluate retrieval precision/recall.

Suggested experiments

1. Lexical baseline
	- Ingest a small corpus.
	- Run representative queries and record precision@3.
2. Dense retrieval
	- Enable embeddings.
	- Compare recall@5 against lexical baseline.
3. FAISS backend
	- Ingest same corpus with FAISS.
	- Compare latency and retrieval consistency.

Reporting checklist

- Dataset provenance
- Query set description
- Metrics and definitions
- Failure cases and mitigations
