from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.settings import settings
from app.api.main import api_router
from app.services.supabase_service import SupabaseService

supabase: SupabaseService | None = None


@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.supabase = await SupabaseService.init()
    yield


def register_router(app: FastAPI) -> None:
    app.include_router(api_router, prefix=settings.API_VERSION)


def register_middleware(app: FastAPI) -> None:
    if settings.all_cors_origins:
        app.add_middleware(
            CORSMiddleware,
            allow_origins=settings.all_cors_origins,
            allow_credentials=settings.ALLOWED_CREDENTIALS,
            allow_methods=["*"],
            allow_headers=["*"],
        )


def register_app() -> FastAPI:
    app = FastAPI(
        title=settings.PROJECT_NAME,
        version=settings.PROJECT_VERSION,
        debug=settings.DEBUG,
        lifespan=lifespan,
    )
    register_middleware(app)
    register_router(app)
    return app
