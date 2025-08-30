from typing import Any, Literal
from pydantic import BeforeValidator, computed_field
from typing_extensions import Annotated
from pydantic.networks import AnyHttpUrl
from pydantic_settings import BaseSettings, SettingsConfigDict


def parse_cors(v: Any) -> list[str] | str:
    if isinstance(v, str) and not v.startswith("["):
        return [i.strip() for i in v.split(",")]
    elif isinstance(v, list | str):
        return v
    else:
        raise ValueError("Invalid CORS configuration")


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_prefix="APP_",
        env_file_encoding="utf-8",
        case_sensitive=True,
        env_ignore_empty=True,
    )

    DEBUG: bool
    SUPABASE_URL: str
    SUPABASE_API_KEY: str
    SUPABASE_TABLE: str
    ENVIRONMENT: Literal["development", "production"] = "development"
    PROJECT_NAME: str
    PROJECT_VERSION: str
    FRONTEND_HOST: str
    API_VERSION: str
    BINANCE_RATES_USDT_URL: str
    BINANCE_PAGE: int
    BINANCE_ROWS: int

    ALLOWED_CREDENTIALS: bool
    ALLOWED_ORIGINS: Annotated[list[AnyHttpUrl] | str, BeforeValidator(parse_cors)]
    ALLOWED_METHODS: list[str]

    @computed_field
    @property
    def all_cors_origins(self) -> list[str]:
        return [str(origin) for origin in self.ALLOWED_ORIGINS] + [self.FRONTEND_HOST]


settings = Settings()
