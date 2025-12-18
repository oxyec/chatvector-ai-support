import os
from pathlib import Path
from dotenv import load_dotenv
import logging

logger = logging.getLogger(__name__)

# Load environment variables from a .env file located next to this config module
dotenv_path = Path(__file__).resolve().parent / ".env"
if dotenv_path.exists():
    load_dotenv(dotenv_path)
    logger.debug(f"Loaded environment variables from {dotenv_path}")
else:
    # Fall back to the default behavior (cwd .env or system envs)
    load_dotenv()
    logger.debug("No local .env found next to config.py; falling back to default load_dotenv()")


class Settings:
    SUPABASE_URL: str = os.getenv("SUPABASE_URL")
    SUPABASE_KEY: str = os.getenv("SUPABASE_KEY")
    GEN_AI_KEY: str = os.getenv("GEN_AI_KEY")
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO").upper()  # Log level with default
    # Whether to use UTC timestamps for logs. Set LOG_USE_UTC=true in .env to enable UTC.
    LOG_USE_UTC: bool = os.getenv("LOG_USE_UTC", "false").lower() in ("1", "true", "yes")

    # Backwards-compatible lowercase properties (some modules referenced these)
    @property
    def supabase_url(self) -> str:
        return self.SUPABASE_URL

    @property
    def supabase_key(self) -> str:
        return self.SUPABASE_KEY


# Create a single config object that other files can import
config = Settings()
