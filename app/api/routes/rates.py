from fastapi import APIRouter
from starlette.concurrency import run_in_threadpool

from app.enum.rate_enum import RateCurrency, RateSource
from app.services.rate_service import RateService
from app.services.rates.binance_rate import BinanceRate


router = APIRouter(prefix="/rates")


@router.post("/binance")
async def save_binance_rate():
    binance_rate = BinanceRate()
    rates = await run_in_threadpool(binance_rate.get_binance_rate)
    rate_service = RateService()

    data = await rate_service.save_rates(
        source=RateSource.BINANCE, currency=RateCurrency.USDT, rates=rates
    )

    return data
