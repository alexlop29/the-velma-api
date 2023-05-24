from sqlalchemy import Column, Integer, VARCHAR, DATE
from sqlalchemy.orm import relationship
from config.db import Base

class Episode(Base):
    __tablename__ = "episodes"

    episode_id = Column(Integer, primary_key=True)
    name = Column(VARCHAR)
    air_date = Column(DATE)

    characters = relationship(
        'Character', 
        secondary = 'character_appearances_by_episode',
        back_populates="episodes"
    )
