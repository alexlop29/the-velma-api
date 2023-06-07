""" Contains HTTP methods to interact with the `character_appearances_by_episode` table """
from fastapi import Depends, APIRouter, Response, status, HTTPException
from fastapi.security import HTTPBearer
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from sqlalchemy import exc
from schemas.character_appearances_by_episode import CharacterByEpisodeCreate
from models.character_appearances_by_episode import CharacterByEpisode
from models.characters import Character
from models.episodes import Episode
from config.db import get_db
from internal.validate import VerifyToken
import sentry_sdk


router = APIRouter()
token_auth_scheme = HTTPBearer()


@router.get(
    "/episode_appearances",
    tags=["episode_appearances"],
    responses={
        500: {"description": "Internal server error"},
        404: {"description": "Not found"}
    }
)
async def get_episode_appearances_by_character(
        input_character_id: int,
        response: Response,
        velma_db: Session = Depends(get_db)):
    """Queries a list of episodes in which a character appears

    Args:
        id (int): Expects a provided character_id
        response (Response): References the Response object to improve error handling
        db (Session, optional): Establishes a connection to the database

    Returns:
        (JSON): {
            'character_id': 'value',
            'first_name': 'value',
            'last_name': 'value',
            'episode_id': 'value',
            'episode_name': 'value'
        }
    """
    try:
        characters_by_episode = velma_db.query(
            Character.character_id,
            Character.first_name,
            Character.last_name,
            CharacterByEpisode.episode_id,
            Episode.name
        ) \
          .join(Character, Character.character_id == CharacterByEpisode.character_id) \
          .join(Episode, CharacterByEpisode.episode_id == Episode.episode_id) \
          .filter(Character.character_id == input_character_id) \
          .all()
        if not characters_by_episode:
            response.status_code = 404
            return HTTPException(status_code=404, detail="Not found")
    except exc.SQLAlchemyError as error:
        sentry_sdk.capture_message(error)
        response.status_code = 500
        return HTTPException(status_code=500, detail="Internal server error")
    results = [tuple(row) for row in characters_by_episode]
    dict_of_results = []
    for row in results:
        dict_of_results.append({
            'character_id': row[0],
            'first_name': row[1],
            'last_name': row[2],
            'episode_id': row[3],
            'episode_name': row[4]
        })
    return JSONResponse(content=jsonable_encoder(dict_of_results))


@router.post(
    "/episode_appearances",
    tags=["episode_appearances"],
    responses={
        500: {"description": "Internal server error"},
        404: {"description": "Not found"}
    }
)
async def create_episode_appearances_by_character(
        response: Response,
        character_by_episode: CharacterByEpisodeCreate,
        velma_db: Session = Depends(get_db),
        token: str = Depends(token_auth_scheme)):
    """ Creates a relationship between a Character and an Episode in the association table

    Args:
        response (Response): References the Response object to improve error handling
        character_by_episode (CharacterByEpisodeCreate): References the Pydantic schema
        velma_db (Session, optional): Establishes a connection to the database
        token (str, optional): References the provided HTTPBearer() token

    Returns:
        CharacterByEpisode (model)
            character_id: int
            episode_id: int
    """
    result = VerifyToken(token.credentials).verify()
    if result.get("status"):
        response.status_code = status.HTTP_400_BAD_REQUEST
        return result
    try:
        character_info = velma_db.query(Character).filter(
            Character.character_id == character_by_episode.character_id
        ).one()
        episode_info = velma_db.query(Episode).filter(
            Episode.episode_id == character_by_episode.episode_id
        ).one()
    except exc.NoResultFound as error:
        sentry_sdk.capture_message(error)
        response.status_code = 404
        return HTTPException(status_code=404, detail="Not found")
    character_info.episodes.append(episode_info)
    velma_db.add(character_info)
    velma_db.commit()
    velma_db.refresh(character_info)
    return velma_db.query(CharacterByEpisode).filter(
        CharacterByEpisode.character_id == character_by_episode.character_id
    ).all()
