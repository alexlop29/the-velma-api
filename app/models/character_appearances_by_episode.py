""" Uses SQLAlchemy to connect to the character_appearances_by_episode table """
from sqlalchemy import Column, Integer
from sqlalchemy import ForeignKey
from config.db import Base


class CharacterByEpisode(Base):
    # pylint: disable=too-few-public-methods
    """ Creates attributes corresponding to each column in its corresponding database table """
    __tablename__ = "character_appearances_by_episode"

    id = Column(Integer, primary_key=True)
    character_id = Column(Integer, ForeignKey('characters.character_id'))
    episode_id = Column(Integer, ForeignKey('episodes.episode_id'))
