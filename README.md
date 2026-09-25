# AI Systems Notes

A versioned AI engineering handbook covering LLM system architecture, RAG, evaluation, security, and operations. It organizes design decisions and trade-offs so readers can connect model behavior to the software that operates it.

## Problem and structure

AI system design spans retrieval, generation, APIs, evaluation, and operational controls. This repository brings those concerns into a navigable technical reference, with documentation built through MkDocs and checked in CI.

**Architecture:** Markdown chapters and examples feed a MkDocs Material static site. `serve.py` provides an alternative lightweight viewer. Diagrams in the handbook describe reference architectures, not deployed infrastructure.

**Design choices:** Documentation is versioned alongside examples; architecture, evaluation, and operations are separate chapters with explicit links. This is an engineering reference rather than an executable agent platform.

**Status:** The roadmap marks the core v0.1 handbook complete. Reproducible benchmarks and deployment recipes are in progress; reference local LLM pipelines remain planned. No measured accuracy, latency, or production adoption is claimed.

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
mkdocs build --strict
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


## Evaluation and limitations

A successful documentation build checks navigation and rendering, not the empirical correctness of every architecture recommendation. The handbook does not establish benchmark results or deployed-system reliability. Treat reference patterns as starting points to validate in a specific system.

See [evaluation](docs/evaluation.md), [experiments](docs/experiments.md), and the [roadmap](docs/roadmap.md) for the distinction between guidance, in-progress benchmarks, and planned implementations.

## License

See [LICENSE](LICENSE) for the repository license.
