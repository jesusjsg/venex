from datetime import date
from typing import List

from fastapi import APIRouter, Depends, HTTPException, status

from app.api.deps import get_currency
from app.enum.rate_enum import RateBcvCurrency
from app.models.rate_model import RatePublic
from app.services.rate_service import RateService

router = APIRouter(prefix="/bcv")


@router.get(
    "/{currency}", response_model=List[RatePublic], summary="Get all rates by currency"
)
async def get_rates_by_currency(
    currency: RateBcvCurrency = Depends(get_currency),
    start_date: date | None = None,
    end_date: date | None = None,
) -> List[RatePublic]:
    service = RateService()
    data = await service.get_all_rates(currency, start_date, end_date)
    if not data:
        raise HTTPException(
            status.HTTP_404_NOT_FOUND,
            detail="The data for the currency provided is not found",
        )
    return data

