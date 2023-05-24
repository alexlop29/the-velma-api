from fastapi import APIRouter, Response, Depends, status
from fastapi.security import HTTPBearer
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from schemas.locations_visited_by_characters import LocationsByCharactersCreate as LocationsByCharactersCreate
from models.locations_visited_by_characters import LocationsByCharacters as LocationsByCharacters 
from models.characters import Character as Character
from models.locations import Location as Location
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

@router.get("/location_by_character/", tags=["location_by_character"])
async def get_location_by_character(
        query: int,
        db: Session = Depends(get_db),
    ):

    locations_by_character = db.query(
        Character.character_id, 
        Character.first_name, 
        Character.last_name, 
        LocationsByCharacters.location_id,
        Location.name
        ) \
        .join(Character, Character.character_id == LocationsByCharacters.character_id) \
        .join(Location, LocationsByCharacters.location_id == Location.location_id) \
        .filter(Character.character_id == query) \
        .all()
    
    results = [tuple(row) for row in locations_by_character]

    dict_of_results = []

    for row in results:
        dict_of_results.append({
            'character_id':row[0],
            'first_name':row[1],
            'last_name':row[2],
            'location_id':row[3],
            'location_name':row[4]
        })
    
    return JSONResponse(content=jsonable_encoder(dict_of_results))

@router.post("/location_by_character/", tags=["location_by_character"])
async def create_location_by_character(
        response: Response,
        location_by_character: LocationsByCharactersCreate, 
        db: Session = Depends(get_db),
        token: str = Depends(token_auth_scheme)
    ):

    result = VerifyToken(token.credentials).verify()
    if result.get("status"):
        response.status_code = status.HTTP_400_BAD_REQUEST
        return result

    character_info = db.query(Character).filter(Character.character_id==location_by_character.character_id).first()
    location_info = db.query(Location).filter(Location.location_id==location_by_character.location_id).first()

    character_info.locations.append(location_info)
    db.add(character_info)
    db.commit()
    db.refresh(character_info)

    return db.query(LocationsByCharacters).filter(
        LocationsByCharacters.character_id==location_by_character.character_id
    ).all()
