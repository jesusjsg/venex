from typing_extensions import Annotated
from pydantic.networks import Url, UrlConstraints
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DEBUG: bool = True
    SUPABASE_URL: Annotated[Url, UrlConstraints(allowed_schemes=["https"])] = (
        "https://test.supabase.com"
    )
    SUPABASE_API_KEY: str = "test"
    ENVIRONMENT: str = "development"
    PROJECT_NAME: str = "venex"
    PROJECT_VERSION: str = "0.1.0"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_prefix="APP_",
        env_file_encoding="utf-8",
        case_sensitive=True,
        env_ignore_empty=True,
    )


settings = Settings()
