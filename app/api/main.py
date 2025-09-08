from fastapi import APIRouter
from app.api.routes import bcv, help, binance

api_router = APIRouter()

api_router.include_router(help.router, tags=["Help"])
api_router.include_router(binance.router, tags=["Binance"])
api_router.include_router(bcv.router, tags=["BCV"])
