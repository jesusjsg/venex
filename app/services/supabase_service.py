from supabase import AsyncClient, create_async_client
from app.core.settings import settings
from app.enum.rate_enum import RateCurrency


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

    async def all(self, currency: RateCurrency):
        response = (
            await self.client.table(settings.SUPABASE_TABLE)
            .select("id, currency, rate, source, date")
            .eq("currency", currency.value)
            .execute()
        )
        return response.data
