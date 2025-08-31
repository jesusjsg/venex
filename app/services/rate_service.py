from datetime import date
import uuid
from starlette.concurrency import run_in_threadpool

from app.enum.rate_enum import RateCurrency, RateSource
from app.models.rate_model import Rate, RatePublic
from app.services.supabase_service import SupabaseService
from app.utils import get_average_rate


class RateService:
    async def save_rates(
        self, source: RateSource, currency: RateCurrency, rates: list[str]
    ) -> Rate:
        avg_rate = await run_in_threadpool(get_average_rate, rates)

        supabase_service = await SupabaseService.init()

        data = Rate(
            id=uuid.uuid4(),
            currency=currency.value,
            rate=avg_rate,
            source=source.value,
            date=date.today(),
        )
        payload = data.model_dump(mode="json", exclude={"created_at"})
        await supabase_service.save(payload)
        return data

    async def get_all(self, currency: RateCurrency) -> list[RatePublic]:
        supabase_service = await SupabaseService.init()
        data = await supabase_service.all(currency)
        return [RatePublic(**rate) for rate in data]
