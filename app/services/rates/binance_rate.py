from app.core.settings import settings
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class BinanceRate:
    BINANCE_API_URL = settings.BINANCE_RATES_USDT_URL

    def __init__(self, timeout: int = 10) -> None:
        options = Options()
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

        self.driver = webdriver.Chrome(options=options)
        self.wait = WebDriverWait(self.driver, timeout)

    def get_binance_rate(self):
        self.driver.get(self.BINANCE_API_URL)

        try:
            self.wait.until(
                EC.visibility_of_element_located((By.CLASS_NAME, "headline5"))
            )
            elements = self.driver.find_elements(By.CLASS_NAME, "headline5")
            rates = [element.text for element in elements]
            return rates
        except Exception as e:
            print(f"Error while getting binance rate: {e}")
            return []
