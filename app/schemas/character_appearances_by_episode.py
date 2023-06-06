""" Uses Pydantic to validate the CharacterByEpisodeBase model """
from pydantic import BaseModel


class CharacterByEpisodeBase(BaseModel):
    """ Requires the input in the CharacterByEpisode model to conform to the field values """

    character_id: int
    episode_id: int


class CharacterByEpisodeCreate(CharacterByEpisodeBase):
    """ Inherits attributes and data from CharacterByEpisodeBase"""


class CharacterByEpisode(CharacterByEpisodeBase):
    """ References fields unknown until after creation"""
    id: int

    class Config:
        # pylint: disable=too-few-public-methods
        """ Enables ORM mode """
        orm_mode = True
