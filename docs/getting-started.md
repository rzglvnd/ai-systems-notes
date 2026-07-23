# Getting Started

This quick-start will get you reading the notes locally and building the static site.

Prerequisites

- Python 3.9+
- `pip` or a virtual environment

Install dependencies (recommended in a venv):

```bash
cd ai-systems-notes
python -m pip install -r requirements.txt
```

Serve the docs locally:

```bash
mkdocs serve
# open http://127.0.0.1:8000
```

Build a static site:

```bash
mkdocs build
# preview in site/
```

Run quality check:

```bash
mkdocs build --strict
```
