""" Queries the Characters table """

from fastapi import Depends, APIRouter, Response, status
from fastapi.security import HTTPBearer
from sqlalchemy.orm import Session
from sqlalchemy import or_
from schemas.characters import CharacterCreate
from models.characters import Character
from config.db import SessionLocal, engine
from internal.validate import VerifyToken

router = APIRouter()
token_auth_scheme  = HTTPBearer()

def get_db():
    """ Establishes a connection to the database """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/sentry-debug")
async def trigger_error():
    division_by_zero = 1 / 0

@router.get("/character_count/", tags=["characters"])
async def get_character_count(db: Session = Depends(get_db)):
    return db.query(Character).count()

@router.get("/characters/", tags=["characters"])
async def get_characters(
        db: Session = Depends(get_db),
        skip: int = 0,
        limit: int = 100,
    ):

    return db.query(Character).offset(skip).limit(limit).all()

@router.get("/character/", tags=["characters"])
async def get_character(query: str, db: Session = Depends(get_db)):
    return db.query(Character).filter(or_(
        Character.first_name.like(query),
        Character.last_name.like(query))
    ).all()

@router.post("/character/", tags=["characters"])
async def create_character(
        response: Response,
        character: CharacterCreate,
        db: Session = Depends(get_db),
        token: str = Depends(token_auth_scheme)
    ):

    result = VerifyToken(token.credentials).verify()
    if result.get("status"):
        response.status_code = status.HTTP_400_BAD_REQUEST
        return result

    character_info = Character(
        first_name=character.first_name,
        last_name=character.last_name,
        species=character.species,
        gender=character.gender
    )
    db.add(character_info )
    db.commit()
    db.refresh(character_info)
    return character_info
