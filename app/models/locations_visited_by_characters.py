""" Uses SQLAlchemy to connect to the locations_visited_by_characters table """
from sqlalchemy import Column, Integer
from sqlalchemy import ForeignKey
from config.db import Base


class LocationsByCharacters(Base):
    # pylint: disable=too-few-public-methods
    """ Creates attributes corresponding to each column in its corresponding database table """
    __tablename__ = "locations_visited_by_characters"

    id = Column(Integer, primary_key=True)
    character_id = Column(Integer, ForeignKey('characters.character_id'))
    location_id = Column(Integer, ForeignKey('locations.location_id'))
