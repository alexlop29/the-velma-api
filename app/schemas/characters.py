from pydantic import BaseModel

class CharacterBase(BaseModel):
    first_name: str
    last_name: str
    species: str
    gender: str

class CharacterCreate(CharacterBase):
    pass

class Character(CharacterBase):
    character_id: int

    class Config:
        orm_mode = True


