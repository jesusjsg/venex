from fastapi import APIRouter
from starlette.concurrency import run_in_threadpool

from app.enum.rate_enum import RateCurrency, RateSource
from app.services.rate_service import RateService


router = APIRouter(prefix="/binance")
