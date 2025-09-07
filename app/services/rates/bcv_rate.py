import httpx

from bs4 import BeautifulSoup

from app.core.settings import settings
from app.enum.rate_enum import RateCurrency


class BcvRate:
    BCV_RATES_URL = settings.BCV_RATES_URL

    def get_rates(self) -> dict:
        try:
            with httpx.Client(verify=settings.CERT_BCV, timeout=10) as client:
                response = client.get(self.BCV_RATES_URL)
                response.raise_for_status()

            soup = BeautifulSoup(response.text, "html.parser")

            rates = {}
            for row in soup.select("div.field-content"):
                currency_span = row.select_one("span")
                rate_strong = row.select_one("strong")

                if currency_span and rate_strong:
                    currency = currency_span.get_text(strip=True)
                    rate = rate_strong.get_text(strip=True)

                    try:
                        enum_currency = RateCurrency(currency.upper())
                    except ValueError:
                        continue

                    if enum_currency in (RateCurrency.USD, RateCurrency.EUR):
                        clean_rate = rate.replace(",", ".").replace(",", ".")
                        rates[currency] = float(clean_rate)

            return rates

        except Exception as e:
            print("Error in the request:", e)
            return {}
