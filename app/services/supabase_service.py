from supabase import AsyncClient, create_async_client
from app.core.settings import settings


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
