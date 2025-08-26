from datetime import datetime
from starlette.concurrency import run_in_threadpool

from app.enum.rate_enum import RateCurrency, RateSource
from app.models.rate_model import RateModel
from app.services.supabase_service import SupabaseService
from app.utils import get_average_rate


class RateService:
    async def save_rates(
        self, source: RateSource, currency: RateCurrency, rates: list[str]
    ) -> RateModel:
        avg_rate = await run_in_threadpool(get_average_rate, rates)

        supabase_service = await SupabaseService.init()

        data = RateModel(
            currency=currency.value,
            rate=avg_rate,
            source=source.value,
            date=datetime.today().isoformat(),
            created_at=datetime.now().isoformat(),
        )

        await supabase_service.save(data.model_dump())

        return data
