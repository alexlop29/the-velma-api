""" Queries the Episodes table """

from fastapi import Depends, APIRouter, Response, status
from fastapi.security import HTTPBearer
from sqlalchemy.orm import Session
from schemas.episodes import EpisodeCreate as EpisodeCreate
from models.episodes import Episode as Episode
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

@router.get("/episode_count/", tags=["episodes"])
async def get_episode_count(db: Session = Depends(get_db)):
    return db.query(Episode).count()

@router.get("/episodes/", tags=["episodes"])
async def get_episodes(db: Session = Depends(get_db)):
    return db.query(Episode).all()

@router.post("/episode/", tags=["episodes"])
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

    episode_info = Episode(
        name=episode.name, 
        air_date=episode.air_date
    )
    db.add(episode_info)
    db.commit()
    db.refresh(episode_info)
    return episode_info
