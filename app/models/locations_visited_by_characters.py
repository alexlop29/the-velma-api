from sqlalchemy import Column, Integer, VARCHAR
from sqlalchemy import ForeignKey

from config.db import Base

class LocationsByCharacters(Base):
    __tablename__ = "locations_visited_by_characters"

    id = Column(Integer, primary_key=True)
    character_id = Column(Integer, ForeignKey('characters.character_id'))
    location_id = Column(Integer, ForeignKey('locations.location_id'))
