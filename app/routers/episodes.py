from fastapi import Depends, APIRouter

router = APIRouter()

@router.get("/episodes/", tags=["episodes"])
async def get_episodes():
    return [{"id": "1"}]
