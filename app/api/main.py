from fastapi import APIRouter
from app.api.routes import help
from app.api.routes import rates

api_router = APIRouter()

api_router.include_router(help.router, tags=["Help"])
api_router.include_router(rates.router, tags=["Rates"])
