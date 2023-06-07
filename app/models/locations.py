""" Uses SQLAlchemy to connect to the locations table """
from sqlalchemy import Column, Integer, VARCHAR
from sqlalchemy.orm import relationship
from config.db import Base


class Location(Base):
    # pylint: disable=too-few-public-methods
    """ Creates attributes corresponding to each column in its corresponding database table """
    __tablename__ = "locations"

    location_id = Column(Integer, primary_key=True)
    name = Column(VARCHAR)

    characters = relationship(
        'Character',
        secondary='locations_visited_by_characters',
        back_populates="locations"
    )
