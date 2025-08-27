from starlette.concurrency import run_in_threadpool
from app.enum.rate_enum import RateCurrency, RateSource
from app.services.rate_service import RateService
from app.services.scrapers.binance_scraper import BinanceScraper


async def run_binance_scraping():
    try:
        scraper = BinanceScraper()
        rates = await run_in_threadpool(scraper.get_binance_rate)

        rate_service = RateService()

        await rate_service.save_rates(
            source=RateSource.BINANCE, currency=RateCurrency.USDT, rates=rates
        )
        print("Successfully scraped Binance")

    except Exception as e:
        print(f"Error while scraping Binance: {e}")
