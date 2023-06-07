""" Contains HTTP methods to interact with the `locations` table  """
from fastapi import Depends, APIRouter, Response, status, HTTPException
from fastapi.security import HTTPBearer
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from sqlalchemy import exc
from schemas.locations import LocationCreate
from models.locations import Location
from config.db import get_db
from internal.validate import VerifyToken
import sentry_sdk

router = APIRouter()
token_auth_scheme = HTTPBearer()


@router.get(
    "/locations",
    tags=["locations"],
    responses={
        500: {"description": "Internal server error"}
    },
    response_model=list[LocationCreate]
)
async def get_locations(response: Response, velma_db: Session = Depends(get_db)):
    """ Returns a list of all episodes """
    try:
        locations = velma_db.query(Location).all()
    except exc.SQLAlchemyError as error:
        sentry_sdk.capture_message(error)
        response.status_code = 500
        return HTTPException(status_code=500, detail="Internal server error")
    return JSONResponse(content=jsonable_encoder(locations))


@router.get(
    "/locations/count",
    tags=["locations"],
    responses={
        500: {"description": "Internal server error"}
    }
)
async def get_count_of_locations(response: Response, velma_db: Session = Depends(get_db)):
    """ Returns a count of locations """
    try:
        count = velma_db.query(Location).count()
    except exc.SQLAlchemyError as error:
        sentry_sdk.capture_message(error)
        response.status_code = 500
        return HTTPException(status_code=500, detail="Internal server error")
    count_to_json = {
        'count': count
    }
    return JSONResponse(content=jsonable_encoder(count_to_json))


@router.get(
        "/locations/search",
        tags=["locations"],
        responses={
            500: {"description": "Internal server error"}
        },
        response_model=list[LocationCreate]
    )
async def search_locations(query: str, velma_db: Session = Depends(get_db)):
    """ Returns a list of locations matching the search string """
    try:
        location_search = velma_db.query(Location).filter(
          Location.name.ilike(f'%{query}%')
        ).all()
    except exc.SQLAlchemyError as err:
        sentry_sdk.capture_message(type(err))
        raise HTTPException(status_code=500, detail="Internal Server Error") from err
    return JSONResponse(content=jsonable_encoder(location_search))


@router.post("/locations", tags=["locations"])
async def create_location(
        response: Response,
        location: LocationCreate,
        velma_db: Session = Depends(get_db),
        token: str = Depends(token_auth_scheme)):
    """ Creates a new location """
    result = VerifyToken(token.credentials).verify()
    if result.get("status"):
        response.status_code = status.HTTP_400_BAD_REQUEST
        return result

    location_info = Location(
        name=location.name
    )
    velma_db.add(location_info)
    velma_db.commit()
    velma_db.refresh(location_info)
    return location_info
