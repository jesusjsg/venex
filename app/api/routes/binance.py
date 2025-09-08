from datetime import date

from typing import List
from fastapi import APIRouter, Depends, HTTPException, Query, status

from app.api.deps import get_currency
from app.enum.rate_enum import RateBinanceCurrency
from app.models.rate_model import RatePublic
from app.services.rate_service import RateService

router = APIRouter(prefix="/binance")


@router.get(
    "/{currency}", response_model=List[RatePublic], summary="Get all rates by currency"
)
async def get_rates_by_currency(
    currency: RateBinanceCurrency = Depends(get_currency),
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
