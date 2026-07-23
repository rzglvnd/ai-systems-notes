# Evaluation

Evaluation should cover both retrieval and generation quality.

Core metrics

- Retrieval: precision@k, recall@k, MRR.
- Generation: groundedness, factuality, task success.
- Operations: p95 latency, timeout rate, error rate.

Evaluation workflow

1. Define task-oriented query set.
2. Label relevant retrieval context for each query.
3. Run baseline and candidate systems.
4. Compare metrics and failure cases.
5. Capture trade-offs (cost, latency, quality).

Practical guidance

- Evaluate with production-like payloads.
- Include adversarial and out-of-domain queries.
- Track regressions across model or prompt updates.
