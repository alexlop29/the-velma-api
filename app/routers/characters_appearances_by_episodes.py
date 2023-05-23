from fastapi import Depends, APIRouter, Response, status
from fastapi.security import HTTPBearer
from sqlalchemy.orm import Session
from schemas.character_appearances_by_episode import CharacterByEpisdeCreate as CharacterByEpisdeCreate
from models.character_appearances_by_episode import CharacterByEpisode as CharacterByEpisode
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

@router.post("/characterbyepisode/", tags=["characterbyepisode"])
async def create_character_by_episode(
        response: Response,
        character: CharacterByEpisdeCreate, 
        db: Session = Depends(get_db),
        token: str = Depends(token_auth_scheme)
    ):

    result = VerifyToken(token.credentials).verify()
    if result.get("status"):
        response.status_code = status.HTTP_400_BAD_REQUEST
        return result

    character_by_episode_info = CharacterByEpisode(
        character_id=CharacterByEpisode.character_id, 
        episode_id=CharacterByEpisode.episode_id
    )
    db.add(character_by_episode_info)
    db.commit()
    db.refresh(character_by_episode_info)
    return character_by_episode_info
