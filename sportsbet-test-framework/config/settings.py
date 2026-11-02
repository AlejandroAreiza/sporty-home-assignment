import os
from pathlib import Path

from dotenv import load_dotenv

PROJECT_ROOT = Path(__file__).resolve().parents[1]

load_dotenv(PROJECT_ROOT / ".env")


def _load(name: str) -> str:
    value = os.getenv(name)
    if not value:
        raise RuntimeError(f"Missing env var '{name}'")
    return value


class EnvVariables:
    QA_BASE_URL = _load("QA_BASE_URL")
    QA_USER_ID = _load("QA_USER_ID")
