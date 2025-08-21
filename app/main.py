from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.main import api_router
from app.core.settings import settings


app = FastAPI(
    title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION, debug=settings.DEBUG
)

if settings.all_cors_origins:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.all_cors_origins,
        allow_credentials=settings.ALLOWED_CREDENTIALS,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.include_router(api_router)
