from typing import List
from fastapi import APIRouter, Depends, HTTPException, status

from app.api.deps import get_currency
from app.enum.rate_enum import RateCurrency
from app.models.rate_model import RatePublic
from app.services.rate_service import RateService

router = APIRouter(prefix="/binance")


@router.get(
    "/{currency}", response_model=List[RatePublic], summary="Get all rates by currency"
)
async def get_rates_by_currency(
    currency: RateCurrency = Depends(get_currency),
    start_date: str | None = None,
    end_date: str | None = None,
) -> List[RatePublic]:
    service = RateService()
    data = await service.get_all_rates(currency, start_date, end_date)
    if not data:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Currency not found")
    return data
