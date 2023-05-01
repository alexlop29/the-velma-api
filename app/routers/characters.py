from fastapi import Depends, APIRouter

router = APIRouter()

# class Character(BaseModel):
#     name: str
#     status: str
#     species: str
#     gender: str
#     first_seen_at: str
#     last_seen_at: str
#     episodes: str

@router.get("/characters/", tags=["characters"])
async def get_characters():
    return [{"name": "Velma"}]
