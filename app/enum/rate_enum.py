from enum import Enum


class RateSource(Enum):
    BINANCE = "binance"
    BANCO_CENTRAL = "banco central de venezuela"


class RateCurrency(Enum):
    USDT = "usdt"
    EUR = "eur"
