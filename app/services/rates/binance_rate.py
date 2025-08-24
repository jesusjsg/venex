import requests
from app.core.settings import settings
from bs4 import BeautifulSoup


class BinanceRate:
    BINANECE_API_URL = settings.BINANCE_RATES_USDT_URL

    def get_binance_rate(self):
        response = requests.get(self.BINANECE_API_URL)
        soup = BeautifulSoup(response.text, "html.parser")
        quotes = [
            quote for quote in soup.find_all("div", class_="headline5 text-primaryText")
        ]
        print(quotes)
        return quotes
