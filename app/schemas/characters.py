""" Uses Pydantic to validate the CharacterBase model """
from pydantic import BaseModel


class CharacterBase(BaseModel):
    """ Requires the input in the CharacterBase model to conform to the field values """
    first_name: str
    last_name: str
    species: str
    gender: str


class CharacterCreate(CharacterBase):
    """ Inherits attributes and data from CharacterBase """


class Character(CharacterBase):
    """ References fields unknown until after creation"""
    character_id: int

    class Config:
        # pylint: disable=too-few-public-methods
        """ Enables ORM mode """
        orm_mode = True
