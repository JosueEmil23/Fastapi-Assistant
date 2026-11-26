from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict 

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file = ".env",
        env_file_encoding= "utf-8",
        extra= "ignore",
    )

    app_name: str = "FastAPI Expense Assistant"
    app_version: str = "0.1.0"
    environment: str = "development"
    debug: bool = True

    database_url: str = "sqlite:///./finance.db"

    llm_provider: str = "fallback"
    llm_api_key: str | None = None
    llm_model: str = "gpt-4o-mini"

    cors_origins: list[str] = ["http://localhost:3000", "http://localhost:5173"]


@lru_cache
def get_settings() -> Settings:
    return Settings()