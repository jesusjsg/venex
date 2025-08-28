"""import asyncio

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


if __name__ == "__main__":
    asyncio.run(run_binance_scraping())"""

import requests

url = "https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search"

headers = {
    "Accept": "*/*",
    "Content-Type": "application/json",
    "Origin": "https://p2p.binance.com",
    "User-Agent": "Mozilla/5.0",
}

payload = {
    "proMerchantAds": False,
    "page": 1,
    "rows": 5,
    "payTypes": [],
    "countries": [],
    "fiat": "VES",
    "tradeType": "BUY",
    "asset": "USDT",
}

try:
    response = requests.post(url, headers=headers, json=payload)
    response.raise_for_status()
    data = response.json()

    for adv in data.get("data", []):
        price = adv["adv"]["price"]
        nickname = adv["advertiser"]["nickName"]
        print(f"{nickname}: {price} VES/USDT")

except requests.exceptions.RequestException as e:
    print("Error en la solicitud:", e)
except ValueError:
    print("La respuesta no es JSON válido.")
