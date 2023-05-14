from sqlalchemy import Column, Integer, VARCHAR
from sqlalchemy import ForeignKey

from config.db import Base

class Character(Base):
    __tablename__ = "character_appearances_by_episodes"

    character_id = Column(Integer, ForeignKey('characters.character_id'))
    episode_id = Column(Integer, ForeignKey('episodes.episode_id'))
