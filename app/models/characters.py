from sqlalchemy import Column, Integer, VARCHAR
from sqlalchemy.orm import relationship
from config.db import Base

class Character(Base):
    __tablename__ = "characters"

    character_id = Column(Integer, primary_key=True)
    first_name = Column(VARCHAR)
    last_name = Column(VARCHAR)
    species = Column(VARCHAR)
    gender = Column(VARCHAR)

    episodes = relationship(
        'Episode', 
        secondary = 'character_appearances_by_episode',
        back_populates="characters"
    )

    locations = relationship(
        'Location', 
        secondary = 'locations_visited_by_characters',
        back_populates="characters"
    )


