# AI Systems Notes

Mission
> Become one of GitHub's best open-source knowledge bases on practical AI engineering.

Contents: LLMs, RAG, Embeddings, Vector DBs, LangChain, LangGraph, Agentic AI, Evaluation, Serving.

## Getting started

- Read `docs/getting-started.md`
- Explore architecture and retrieval sections in `docs/`
- Build docs locally via MkDocs

## Run locally

Install dependencies and run the docs server:

```bash
cd ai-systems-notes
python -m pip install -r requirements.txt
mkdocs serve
```

Alternative lightweight viewer using built-in server:

```bash
python serve.py
# open http://127.0.0.1:8000
```

Build static docs output:

```bash
mkdocs build
```

## Documentation map

- `docs/architecture.md`
- `docs/retrieval.md`
- `docs/evaluation.md`
- `docs/security.md`
- `docs/operations.md`
- `docs/deployment.md`
- `docs/experiments.md`
- `docs/roadmap.md`

## Quality checks

- GitHub Actions validates MkDocs build for push/PR.
- Keep examples runnable and update docs when APIs evolve.

