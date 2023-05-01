from fastapi import Depends, APIRouter

router = APIRouter()

# class Locations(BaseModel):
#     name: str

@router.get("/locations/", tags=["locations"])
async def get_locations():
    return [{"location": "Velma's House"}]
