from fastapi import Depends, APIRouter

router = APIRouter()

# class Episodes(BaseModel):
#     name: str
#     status: str
#     species: str
#     gender: str
#     first_seen_at: str
#     last_seen_at: str
#     episodes: str

@router.get("/episodes/", tags=["episodes"])
async def get_episodes():
    return [{"id": "1"}]
