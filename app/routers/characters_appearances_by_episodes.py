from fastapi import Depends, APIRouter, Response, status
from fastapi.security import HTTPBearer
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from sqlalchemy import and_
from schemas.character_appearances_by_episode import CharacterByEpisodeCreate as CharacterByEpisodeCreate
from models.character_appearances_by_episode import CharacterByEpisode as CharacterByEpisode
from models.characters import Character as Character
from models.episodes import Episode as Episode
from config.db import SessionLocal, engine
from internal.validate import VerifyToken
from sqlalchemy import select
import json
from fastapi.responses import JSONResponse


router = APIRouter()
token_auth_scheme  = HTTPBearer()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/character_by_episode/", tags=["character_by_episode"])
async def get_character_by_episode(
        query: int,
        db: Session = Depends(get_db),
    ):

    characters_by_episode = db.query(
        Character.character_id, 
        Character.first_name, 
        Character.last_name, 
        CharacterByEpisode.episode_id,
        Episode.name
        ) \
        .join(Character, Character.character_id == CharacterByEpisode.character_id) \
        .join(Episode, CharacterByEpisode.episode_id == Episode.episode_id) \
        .filter(Character.character_id == query) \
        .all()
    
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

@router.post("/character_by_episode/", tags=["character_by_episode"])
async def create_character_by_episode(
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
