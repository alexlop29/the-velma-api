""" Queries the Episodes table """

from fastapi import Depends, APIRouter, Response, status, HTTPException
from fastapi.security import HTTPBearer
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from schemas.episodes import EpisodeCreate as EpisodeCreate
from models.episodes import Episode as Episode
from config.db import SessionLocal, engine
from internal.validate import VerifyToken
import sentry_sdk
from pydantic import ValidationError

router = APIRouter()
token_auth_scheme  = HTTPBearer()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get(
    "/episodes",
    tags=["episodes"],
    responses={
        500: {"description": "Internal server error"}
    },
    response_model=list[EpisodeCreate]
)
async def get_episodes(response: Response, db: Session = Depends(get_db)):
    """ Returns a list of all episodes """
    try:
        episodes = db.query(Episode).all()
    except Exception as error:
        sentry_sdk.capture_message(error)
        response.status_code = 500
        return  HTTPException(status_code=500, detail="Internal server error")
    return JSONResponse(content=jsonable_encoder(episodes))

@router.get(
    "/episodes/count",
    tags=["episodes"],
    responses={
        500: {"description": "Internal server error"}
    }
)
async def get_count_of_episodes(response: Response, db: Session = Depends(get_db)):
    try:
        count = db.query(Episode).count()
    except Exception as error:
        sentry_sdk.capture_message(error)
        response.status_code = 500
        return HTTPException(status_code=500, detail="Internal server error")
    count_to_json = {
        'count':count
    }
    return JSONResponse(content=jsonable_encoder(count_to_json))

@router.post(
    "/episodes",
    tags=["episodes"],
    responses={
        500: {"description": "Internal server error"}
    },
    response_model=list[EpisodeCreate]
)
async def create_episode(
        response: Response,
        episode: EpisodeCreate, 
        db: Session = Depends(get_db),
        token: str = Depends(token_auth_scheme)
    ):
    result = VerifyToken(token.credentials).verify()
    if result.get("status"):
        response.status_code = status.HTTP_400_BAD_REQUEST
        return result
    try:
        episode_info = Episode(
            name=episode.name, 
            air_date=episode.air_date
        )
    except ValidationError as error:
        sentry_sdk.capture_message(error)
        response.status_code=422
        return {"status": "error", "msg": error.__str__()}
    db.add(episode_info)
    db.commit()
    db.refresh(episode_info)
    return episode_info
