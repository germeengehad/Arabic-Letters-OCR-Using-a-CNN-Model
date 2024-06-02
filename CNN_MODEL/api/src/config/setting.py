from typing import Any, Dict, Optional

from pydantic import BaseSettings, PostgresDsn, validator


from pydantic import BaseSettings
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    APP_NAME: str = os.getenv("APP_NAME")
    DOMAIN: str = os.getenv("DOMAIN")
    DEBUG_MODE: bool = os.getenv("DEBUG_MODE", "").lower() in ("yes", "true", "1")
    BACKEND_PORT: int = int(os.getenv("BACKEND_PORT", 8080))

    @validator("BACKEND_PORT", pre=True)
    def set_port_default(cls, v: int) -> int:
        if v:
            return v
        return 8080  # Default port set to 8080

settings = Settings()

