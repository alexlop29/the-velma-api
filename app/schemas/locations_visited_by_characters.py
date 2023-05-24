from pydantic import BaseModel

class LocationsByCharactersBase(BaseModel):
    character_id: int
    location_id: int

class LocationsByCharactersCreate(LocationsByCharactersBase):
    pass

class LocationsByCharacters(LocationsByCharactersBase):
    id: int

    class Config:
        orm_mode = True
