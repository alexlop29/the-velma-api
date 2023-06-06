""" Uses Pydantic to validate the EpisodeBase model """

from datetime import date
from pydantic import BaseModel


class EpisodeBase(BaseModel):
    """ Requires the input in the EpisodeBase model to conform to the field values """
    name: str
    air_date: date


class EpisodeCreate(EpisodeBase):
    """ Inherits attributes and data from EpisodeBase """


class Episode(EpisodeBase):
    """ References fields unknown until after creation"""
    episode_id: int

    class Config:
        # pylint: disable=too-few-public-methods
        """ Enables ORM mode """
        orm_mode = True
