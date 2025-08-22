from fastapi import APIRouter
from app.api.routes import help

api_router = APIRouter()

api_router.include_router(help.router, tags=["Help"])
