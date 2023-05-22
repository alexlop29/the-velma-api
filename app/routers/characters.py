from fastapi import Depends, APIRouter, Response, status
from fastapi.security import HTTPBearer
from sqlalchemy.orm import Session
from schemas.characters import CharacterCreate as CharacterCreate
from models.characters import Character as Character
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

@router.get("/characters/", tags=["characters"])
async def get_characters(
        db: Session = Depends(get_db),
        skip: int = 0, 
        limit: int = 100,
    ):

    return db.query(Character).offset(skip).limit(limit).all()

@router.get("/character/", tags=["characters"])
async def get_character(query: str, db: Session = Depends(get_db)):
    return db.query(Character).filter(
        Character.first_name.like(query),
        Character.last_name.like(query)
    )

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

    db_user = Character(
        first_name=character.first_name, 
        last_name=character.last_name,
        species=character.species,
        gender=character.gender
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
