from supabase import AsyncClient, create_async_client
from app.core.settings import settings
from app.enum.rate_enum import RateBcvCurrency, RateBinanceCurrency


class SupabaseService:
    def __init__(self, client: AsyncClient) -> None:
        self._client = client

    @classmethod
    async def init(cls) -> "SupabaseService":
        client = await create_async_client(
            settings.SUPABASE_URL, settings.SUPABASE_API_KEY
        )
        return cls(client)

    @property
    def client(self) -> AsyncClient:
        return self._client

    async def save(self, data: dict):
        response = (
            await self.client.table(settings.SUPABASE_TABLE).insert(data).execute()
        )
        return response

    async def get_last(self, currency: RateBinanceCurrency | RateBcvCurrency):
        response = (
            await self.client.table(settings.SUPABASE_TABLE)
            .select("rate")
            .eq("currency", currency.value)
            .order("created_at", desc=True)
            .limit(1)
            .execute()
        )
        return response.data

    async def get_all(
        self,
        currency: RateBinanceCurrency | RateBcvCurrency,
        start_date: str | None,
        end_date: str | None,
    ):
        query = self.client.table(settings.SUPABASE_TABLE).select(
            "id, currency, rate, source, date, diff, percent"
        )
        query = query.eq("currency", currency.value)

        if start_date:
            query = query.gte("date", start_date)

        if end_date:
            query = query.lte("date", end_date)

        query = query.not_.is_("diff", "null")
        query = query.order("date", desc=True)

        response = await query.execute()
        return response.data
