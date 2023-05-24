""" Queries the Locations table """

from fastapi import Depends, APIRouter, Response, status
from fastapi.security import HTTPBearer
from sqlalchemy.orm import Session
from schemas.locations import LocationCreate as LocationCreate
from models.locations import Location as Location
from config.db import SessionLocal, engine
from internal.validate import VerifyToken

router = APIRouter()
token_auth_scheme  = HTTPBearer()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/location_count/", tags=["locations"])
async def get_location_count(db: Session = Depends(get_db)):
    return db.query(Location).count()

@router.get("/locations/", tags=["locations"])
async def get_locations(db: Session = Depends(get_db)):
    return db.query(Location).all()

@router.post("/location/", tags=["locations"])
async def create_location(
        response: Response,
        location: LocationCreate, 
        db: Session = Depends(get_db),
        token: str = Depends(token_auth_scheme)
    ):

    result = VerifyToken(token.credentials).verify()
    if result.get("status"):
        response.status_code = status.HTTP_400_BAD_REQUEST
        return result

    location_info = Location(
        name=location.name
    )
    db.add(location_info)
    db.commit()
    db.refresh(location_info)
    return location_info
