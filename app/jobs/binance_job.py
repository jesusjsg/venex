import asyncio

from starlette.concurrency import run_in_threadpool
from app.core.settings import settings
from app.services.rates.binance_rate import BinanceRate
from app.services.rate_service import RateService
from app.enum.rate_enum import RateBinanceCurrency, RateSource

currency = RateBinanceCurrency.USDT
url = settings.BINANCE_RATES_USDT_URL
headers = {"Content-Type": "application/json"}
payload = {
    "proMerchantAds": False,
    "page": settings.BINANCE_PAGE,
    "rows": settings.BINANCE_ROWS,
    "fiat": "VES",
    "tradeType": "BUY",
    "asset": currency.value,
}


async def get_binance_rates():
    try:
        binance_service = BinanceRate()
        data = await run_in_threadpool(binance_service.get_rates, headers, payload)
        rates = [adv["adv"]["price"] for adv in data.get("data", [])]

        rate_service = RateService()
        await rate_service.save_rates(
            RateSource.BINANCE, RateBinanceCurrency.USDT, rates
        )
        print("Successfully saved Binance rates")

    except Exception as e:
        print("Error in the request:", e)


if __name__ == "__main__":
    asyncio.run(get_binance_rates())
