from fastapi import APIRouter, Request
from app.services.supabase_service import SupabaseService


router = APIRouter(prefix="/help")


@router.get("/")
async def get_status_server() -> bool:
    return True


@router.get("/status/db")
async def get_status_db(request: Request):
    supabase: SupabaseService = request.app.state.supabase
    response = await supabase.client.table("currency_rates").select("*").execute()
    return response
