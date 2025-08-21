from fastapi import APIRouter

router = APIRouter(prefix="/help", tags=["Help"])


@router.get("/")
async def get_help() -> bool:
    return True
