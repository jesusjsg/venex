from fastapi import APIRouter
from app.services.rates.binance_rate import BinanceRate

router = APIRouter(prefix="/rates")


@router.get("/binance")
async def get_binance_rate():
    binance_rate = BinanceRate()
    return binance_rate.get_binance_rate()
