from typing import List
from fastapi import APIRouter

from app.enum.rate_enum import RateCurrency
from app.schemas.binance_schema import BinanceSchema
from app.services.rate_service import RateService

router = APIRouter(prefix="/binance")


@router.get("/usdt", response_model=List[BinanceSchema])
async def get_usdt():
    service = RateService()
    data = await service.get_all(RateCurrency.USDT)
    return data
