from fastapi import HTTPException, status, Path

from app.enum.rate_enum import RateCurrency


def get_currency(currency: str = Path(...)) -> RateCurrency:
    try:
        print(currency)
        return RateCurrency(currency.upper())
    except ValueError:
        raise HTTPException(
            status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Invalid currency"
        )
