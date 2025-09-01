import uuid
import datetime

from starlette.concurrency import run_in_threadpool

from app.enum.rate_enum import RateCurrency, RateSource
from app.models.rate_model import LastRate, Rate, RatePublic
from app.services.supabase_service import SupabaseService
from app.utils import get_average_rate, get_diff, get_percent_change


class RateService:
    async def get_all_rates(self, currency: RateCurrency) -> list[RatePublic]:
        supabase_service = await SupabaseService.init()
        data = await supabase_service.all(currency)
        return [RatePublic(**rate) for rate in data]

    async def get_last_rate(self, currency: RateCurrency) -> LastRate | None:
        supabase_service = await SupabaseService.init()
        data = await supabase_service.get_last(currency)
        if not data:
            return None
        return LastRate(**data[0])

    async def save_rates(
        self, source: RateSource, currency: RateCurrency, rates: list[str]
    ) -> Rate:
        avg_rate = await run_in_threadpool(get_average_rate, rates)

        last_data = await self.get_last_rate(currency)
        last_rate = last_data.rate if last_data else None

        diff = await run_in_threadpool(get_diff, avg_rate, last_rate)
        percent = await run_in_threadpool(get_percent_change, avg_rate, last_rate)

        supabase_service = await SupabaseService.init()

        data = Rate(
            id=uuid.uuid4(),
            currency=currency.value,
            rate=avg_rate,
            source=source.value,
            diff=diff,
            percent=percent,
            date=datetime.datetime.now(),
        )
        payload = data.model_dump(mode="json", exclude={"created_at"})
        await supabase_service.save(payload)
        return data
