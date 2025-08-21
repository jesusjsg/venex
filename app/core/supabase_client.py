from supabase import create_async_client
from app.core.settings import settings


class SupabaseClient:
    def __init__(self, client) -> None:
        self.client = client

    @classmethod
    async def create(cls):
        cls = await create_async_client(
            settings.SUPABASE_URL, settings.SUPABASE_API_KEY
        )
        return cls
