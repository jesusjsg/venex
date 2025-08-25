from fastapi import APIRouter
from starlette.concurrency import run_in_threadpool

from app.services.rates.binance_rate import BinanceRate
from app.utils import get_average_rate


router = APIRouter(prefix="/rates")


@router.get("/binance")
async def get_binance_rate():
    binance_rate = BinanceRate()
    rates = await run_in_threadpool(binance_rate.get_binance_rate)
    avg_rate = await run_in_threadpool(get_average_rate, rates)
    return {"avg_rate": avg_rate}
