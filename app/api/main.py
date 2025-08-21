from fastapi import APIRouter
from app.api.routes import health, help

api_router = APIRouter()

api_router.include_router(health.router, prefix="/v1")
api_router.include_router(help.router, prefix="/v1")

