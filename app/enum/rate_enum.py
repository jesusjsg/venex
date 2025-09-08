from enum import Enum


class RateSource(Enum):
    BINANCE = "binance"
    BANCO_CENTRAL = "banco central de venezuela"


class RateBinanceCurrency(Enum):
    USDT = "USDT"


class RateBcvCurrency(Enum):
    USD = "USD"
    EUR = "EUR"
    CNY = "CNY"
