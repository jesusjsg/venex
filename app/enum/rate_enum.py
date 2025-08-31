from enum import Enum


class RateSource(Enum):
    BINANCE = "binance"
    BANCO_CENTRAL = "banco central de venezuela"


class RateCurrency(Enum):
    USDT = "USDT"
    USD = "USD"
    EUR = "EUR"
    CNY = "CNY"
