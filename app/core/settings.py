from typing import Any
from pydantic import BeforeValidator, computed_field
from typing_extensions import Annotated
from pydantic.networks import AnyHttpUrl, Url, UrlConstraints
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

    DEBUG: bool = True
    SUPABASE_URL: Annotated[Url, UrlConstraints(allowed_schemes=["https"])] = (
        "https://test.supabase.com"
    )
    SUPABASE_API_KEY: str = "test"
    ENVIRONMENT: str = "development"
    PROJECT_NAME: str = "venex"
    PROJECT_VERSION: str = "0.1.0"
    FRONTEND_HOST: str = "http://localhost:3000"

    ALLOWED_CREDENTIALS: bool = False
    ALLOWED_ORIGINS: Annotated[list[AnyHttpUrl] | str, BeforeValidator(parse_cors)] = []

    @computed_field
    @property
    def all_cors_origins(self) -> list[str]:
        return [str(origin) for origin in self.ALLOWED_ORIGINS] + [self.FRONTEND_HOST]


settings = Settings()
