from sqlalchemy import Column, Integer, VARCHAR, ARRAY
from sqlalchemy.orm import relationship
from config.db import Base

class Location(Base):
    __tablename__ = "locations"

    location_id = Column(Integer, primary_key=True)
    name = Column(VARCHAR)

    characters = relationship(
        'Character', 
        secondary = 'locations_visited_by_characters',
        back_populates="locations"
    )
