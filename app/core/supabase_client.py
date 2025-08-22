from supabase import create_async_client
from app.core.settings import settings


class SupabaseClient:
    def __init__(self, client) -> None:
        self.client = client

    @classmethod
    async def create(cls):
        client = await create_async_client(
            settings.SUPABASE_URL, settings.SUPABASE_API_KEY
        )
        return cls(client)

    async def test_connection(self) -> bool:
        try:
            response = await self.client.from_("currency_rates").select("*").execute()

            if response.status_code == 200:
                print("Connection to Supabase successful")
                return True
            else:
                print("Connection to Supabase failed")
                return False
        except Exception as e:
            print(e)
            return False
