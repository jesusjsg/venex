from fastapi import APIRouter

from app.core.supabase_client import SupabaseClient

router = APIRouter(prefix="/help", tags=["Help"])


@router.get("/")
async def get_help() -> bool:
    return True


@router.get("/status")
async def get_status_supabase():
    supabase = await SupabaseClient.create()
    connection = await supabase.test_connection()

    if connection:
        return {"status": "ok"}
    return {"status": "failed", "error": connection}
