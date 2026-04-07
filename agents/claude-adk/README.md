# Claude ADK Agent (Python)

## Run locally in dev container terminal

```bash
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -e .[dev]
python -m src.main
python -m pytest
```

## Notes

- Set `ANTHROPIC_API_KEY` in project `.env` before integrating real model calls.
- Keep secrets out of Git.
- If `python-dotenv` is unavailable in the active interpreter, the app still starts and falls back to OS env vars.
