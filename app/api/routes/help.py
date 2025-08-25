from fastapi import APIRouter, Request
from app.services.supabase_service import SupabaseService
from app.core.settings import settings

router = APIRouter(prefix="/help")


@router.get("/")
async def get_status_server() -> dict:
    return {"status": "ok"}


if settings.ENVIRONMENT == "development":

    @router.get("/status/db")
    async def get_status_db(request: Request):
        supabase: SupabaseService = request.app.state.supabase
        response = (
            await supabase.client.table(settings.SUPABASE_TABLE).select("*").execute()
        )
        return response
