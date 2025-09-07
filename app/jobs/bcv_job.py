import asyncio

from starlette.concurrency import run_in_threadpool

from app.services.rates.bcv_rate import BcvRate
from app.services.rate_service import RateService
from app.enum.rate_enum import RateCurrency, RateSource


async def get_bcv_rates():
    try:
        bcv_service = BcvRate()
        data = await run_in_threadpool(bcv_service.get_rates)

        rate_service = RateService()
        for currency, rate in data.items():
            enum_currency = getattr(RateCurrency, currency)
            await rate_service.save_rates(
                RateSource.BANCO_CENTRAL, enum_currency, [rate]
            )

        print("Successfully saved BCV rates")

    except Exception as e:
        print("Error in the request:", e)


if __name__ == "__main__":
    asyncio.run(get_bcv_rates())
