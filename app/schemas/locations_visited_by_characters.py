""" Uses Pydantic to validate the LocationsByCharacterBase model """
from pydantic import BaseModel


class LocationsByCharactersBase(BaseModel):
    """ Requires the input in the LocationsByCharacterBase model to conform to the field values """
    character_id: int
    location_id: int


class LocationsByCharactersCreate(LocationsByCharactersBase):
    """ Inherits attributes and data from LocationsByCharactersBase """


class LocationsByCharacters(LocationsByCharactersBase):
    """ References fields unknown until after creation"""
    id: int

    class Config:
        # pylint: disable=too-few-public-methods
        """ Enables ORM mode """
        orm_mode = True
