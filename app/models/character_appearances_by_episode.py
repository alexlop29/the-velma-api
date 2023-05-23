from sqlalchemy import Column, Integer, VARCHAR
from sqlalchemy import ForeignKey

from config.db import Base

class CharacterByEpisode(Base):
    __tablename__ = "character_appearances_by_episode"

    id = Column(Integer, primary_key=True)
    character_id = Column(Integer, ForeignKey('characters.character_id'))
    episode_id = Column(Integer, ForeignKey('episodes.episode_id'))
