from fastapi import HTTPException, status, Path

from app.enum.rate_enum import RateBinanceCurrency, RateBcvCurrency


def get_currency(currency: str = Path(...)) -> RateBinanceCurrency | RateBcvCurrency:
    try:
        if currency.upper() in RateBinanceCurrency.__members__:
            return RateBinanceCurrency(currency.upper())
        else:
            return RateBcvCurrency(currency.upper())
    except ValueError:
        raise HTTPException(
            status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Invalid currency"
        )
