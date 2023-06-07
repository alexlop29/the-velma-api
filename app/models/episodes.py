""" Uses SQLAlchemy to connect to the characters """
from sqlalchemy import Column, Integer, VARCHAR, DATE
from sqlalchemy.orm import relationship
from config.db import Base


class Episode(Base):
    # pylint: disable=too-few-public-methods
    """ Creates attributes corresponding to each column in its corresponding database table """
    __tablename__ = "episodes"

    episode_id = Column(Integer, primary_key=True)
    name = Column(VARCHAR)
    air_date = Column(DATE)

    characters = relationship(
        'Character',
        secondary='character_appearances_by_episode',
        back_populates="episodes"
    )
