import requests

from app.core.settings import settings


class BinanceRate:
    BINANCE_API_URL = settings.BINANCE_RATES_USDT_URL

    def get_rates(self, headers: dict, payload: dict) -> dict:
        try:
            response = requests.post(
                self.BINANCE_API_URL, headers=headers, json=payload
            )
            if response.status_code != 200:
                print("Error in the response:", response.status_code)
                return {"data": []}
            return response.json()
        except Exception as e:
            print("Error in the request:", e)
            return {"data": []}
