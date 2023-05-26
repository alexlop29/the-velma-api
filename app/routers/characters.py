""" Queries the Characters table """

from fastapi import Depends, APIRouter, Response, status, HTTPException
from fastapi.security import HTTPBearer
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from sqlalchemy import or_
from sqlalchemy import exc
from schemas.characters import CharacterCreate
from models.characters import Character
from config.db import SessionLocal, engine
from internal.validate import VerifyToken
import sentry_sdk

router = APIRouter()
token_auth_scheme  = HTTPBearer()

def get_db():
    """ Establishes a connection to the database """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/characters", tags=["characters"])
async def get_characters(db: Session = Depends(get_db)):
    try:
        characters = db.query(Character).all()
    except exc.SQLAlchemyError as err:
        sentry_sdk.capture_message(type(err))
        raise HTTPException(status_code=500, detail="Internal Server Error")
    return JSONResponse(content=jsonable_encoder(characters))

@router.get("/characters/count", tags=["characters"], status_code=200)
async def get_count_of_characters(db: Session = Depends(get_db)):
    """ Returns a count of characters """
    try:
      count = db.query(Character).count()
    except exc.SQLAlchemyError as err:
        sentry_sdk.capture_message(type(err))
        raise HTTPException(status_code=500, detail="Internal Server Error")
    count_to_json = {
        'count':count
    }
    return JSONResponse(content=jsonable_encoder(count_to_json))

@router.get("/characters/search", tags=["characters"])
async def get_character(query: str, db: Session = Depends(get_db)):
    try:
        character_search = db.query(Character).filter(or_(
        Character.first_name.ilike(f'%{query}%'),
        Character.last_name.ilike(f'%{query}%'))
        ).all()
    except exc.SQLAlchemyError as err:
        sentry_sdk.capture_message(type(err))
        raise HTTPException(status_code=500, detail="Internal Server Error")
    return JSONResponse(content=jsonable_encoder(character_search))

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
