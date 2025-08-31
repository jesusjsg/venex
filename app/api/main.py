from fastapi import APIRouter
from app.api.routes import help
from app.api.routes import binance

api_router = APIRouter()

api_router.include_router(help.router, tags=["Help"])
api_router.include_router(binance.router, tags=["Binance"])
