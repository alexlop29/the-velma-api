""" Queries the Locations table """

from fastapi import Depends, APIRouter, Response, status, HTTPException
from fastapi.security import HTTPBearer
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from schemas.locations import LocationCreate as LocationCreate
from models.locations import Location as Location
from config.db import SessionLocal, engine
from internal.validate import VerifyToken
import sentry_sdk

router = APIRouter()
token_auth_scheme  = HTTPBearer()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get(
    "/locations/",
    tags=["locations"],
    responses={
        500: {"description": "Internal server error"}
    },
    response_model=list[LocationCreate]
)
async def get_locations(response: Response, db: Session = Depends(get_db)):
    """ Returns a list of all episodes """
    try:
        locations = db.query(Location).all()
    except Exception as error:
        sentry_sdk.capture_message(error)
        response.status_code = 500
        return  HTTPException(status_code=500, detail="Internal server error")
    return JSONResponse(content=jsonable_encoder(locations))

@router.get(
    "/locations/count",
    tags=["locations"],
    responses={
        500: {"description": "Internal server error"}
    }
)
async def get_count_of_locations(response: Response, db: Session = Depends(get_db)):
    """ Returns a count of locations """
    try:
        count =  db.query(Location).count()
    except Exception as error:
        sentry_sdk.capture_message(error)
        response.status_code = 500
        return HTTPException(status_code=500, detail="Internal server error")
    count_to_json = {
        'count':count
    }
    return JSONResponse(content=jsonable_encoder(count_to_json))

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
