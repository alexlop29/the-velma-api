""" Uses Pydantic to validate the LocationBase model """
from pydantic import BaseModel


class LocationBase(BaseModel):
    """ Requires the input in the LocationBase model to conform to the field values """
    name: str


class LocationCreate(LocationBase):
    """ Inherits attributes and data from LocationBase """


class Location(LocationBase):
    """ References fields unknown until after creation"""
    location_id: int

    class Config:
        # pylint: disable=too-few-public-methods
        """ Enables ORM mode """
        orm_mode = True
