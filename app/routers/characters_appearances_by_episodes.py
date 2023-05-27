from fastapi import Depends, APIRouter, Response, status, HTTPException
from fastapi.security import HTTPBearer
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from sqlalchemy import and_
from sqlalchemy import exc
from schemas.character_appearances_by_episode import CharacterByEpisodeCreate as CharacterByEpisodeCreate
from models.character_appearances_by_episode import CharacterByEpisode as CharacterByEpisode
from models.characters import Character as Character
from models.episodes import Episode as Episode
from config.db import SessionLocal, engine
from internal.validate import VerifyToken
from sqlalchemy import select
import json
from fastapi.responses import JSONResponse
import sentry_sdk

router = APIRouter()
token_auth_scheme  = HTTPBearer()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/episode_appearances/{character_id}", tags=["episode_appearances"])
async def get_episode_by_character(
        id: int,
        response: Response, 
        db: Session = Depends(get_db),
    ):
    try:
        characters_by_episode = db.query(
            Character.character_id, 
            Character.first_name, 
            Character.last_name, 
            CharacterByEpisode.episode_id,
            Episode.name
        ) \
        .join(Character, Character.character_id == CharacterByEpisode.character_id) \
        .join(Episode, CharacterByEpisode.episode_id == Episode.episode_id) \
        .filter(Character.character_id == id) \
        .all()
        if not characters_by_episode:
            response.status_code = 404
            return HTTPException(status_code=404, detail="Not found")
    except exc.SQLAlchemyError as error:
        sentry_sdk.capture_message(error)
        response.status_code=500
        return HTTPException(status_code=500, detail="Internal server")
    results = [tuple(row) for row in characters_by_episode]
    dict_of_results = []
    for row in results:
        dict_of_results.append({
            'character_id':row[0],
            'first_name':row[1],
            'last_name':row[2],
            'episode_id':row[3],
            'episode_name':row[4]
        })
    return JSONResponse(content=jsonable_encoder(dict_of_results))

@router.post("/episode_by_character/", tags=["episode_appearances"])
async def create_episode_by_character(
        response: Response,
        character_by_episode: CharacterByEpisodeCreate, 
        db: Session = Depends(get_db),
        token: str = Depends(token_auth_scheme)
    ):

    result = VerifyToken(token.credentials).verify()
    if result.get("status"):
        response.status_code = status.HTTP_400_BAD_REQUEST
        return result

    character_info = db.query(Character).filter(Character.character_id==character_by_episode.character_id).first()
    episode_info = db.query(Episode).filter(Episode.episode_id==character_by_episode.episode_id).first()

    character_info.episodes.append(episode_info)
    db.add(character_info)
    db.commit()
    db.refresh(character_info)

    return db.query(CharacterByEpisode).filter(
        CharacterByEpisode.character_id==character_by_episode.character_id
    ).all()
