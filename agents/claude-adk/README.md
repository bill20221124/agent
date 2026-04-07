# Claude ADK Agent (Python)

## Quick Start

```bash
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -e .[dev]
python -m src.main
python -m pytest
```

## Clean Workspace

```bash
rm -rf .pytest_cache __pycache__
find . -type f -name '*.pyc' -delete
find . -type f -name '.DS_Store' -delete
```

## Notes

- Set `ANTHROPIC_API_KEY` in project `.env` before integrating real model calls.
- Keep secrets out of Git.
- If `python-dotenv` is unavailable in the active interpreter, the app still starts and falls back to OS env vars.
