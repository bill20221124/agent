from __future__ import annotations

import os
from dataclasses import dataclass

try:
    from dotenv import load_dotenv
except ModuleNotFoundError:
    def load_dotenv() -> bool:
        # Keep startup/test flow working when optional local env tooling is missing.
        return False


@dataclass
class AppConfig:
    app_env: str
    log_level: str
    has_api_key: bool


def load_config() -> AppConfig:
    load_dotenv()
    return AppConfig(
        app_env=os.getenv("APP_ENV", "development"),
        log_level=os.getenv("LOG_LEVEL", "INFO"),
        has_api_key=bool(os.getenv("ANTHROPIC_API_KEY")),
    )


def main() -> None:
    cfg = load_config()
    print("Claude ADK Python dev environment is ready.")
    print(f"APP_ENV={cfg.app_env}, LOG_LEVEL={cfg.log_level}")
    if not cfg.has_api_key:
        print("Warning: ANTHROPIC_API_KEY is not set yet.")


if __name__ == "__main__":
    main()
