from fastapi import Depends, APIRouter

router = APIRouter()

@router.get("/locations/", tags=["locations"])
async def get_locations():
    return [{"location": "Velma's House"}]
