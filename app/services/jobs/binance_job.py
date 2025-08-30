from app.core.settings import settings
from app.services.rates.binance_rate import BinanceRate

url = settings.BINANCE_RATES_USDT_URL
headers = {"Content-Type": "application/json"}
payload = {
    "proMerchantAds": False,
    "page": 1,
    "rows": 10,
    "fiat": "VES",
    "tradeType": "BUY",
    "countries": [],
    "payTypes": [],
    "asset": "USDT",
}


def get_binance_rates():
    try:
        service = BinanceRate()
        data = service.get_rates(headers, payload)
        rates = [adv["adv"]["price"] for adv in data.get("data", [])]
        print(rates)
        return rates

    except Exception as e:
        print("Error in the request:", e)


if __name__ == "__main__":
    get_binance_rates()
