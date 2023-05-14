from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from schemas.characters import CharacterCreate as CharacterCreate
from models.characters import Character as Character
from config.db import SessionLocal, engine

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/characters/", tags=["characters"])
async def get_characters():
    return [{"name": "Velma"}]

@router.post("/character/", tags=["characters"])
async def create_character(character: CharacterCreate, db: Session = Depends(get_db)):
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
