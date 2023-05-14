from sqlalchemy import Column, Integer, VARCHAR, DATE

from config.db import Base

class Episode(Base):
    __tablename__ = "episodes"

    episode_id = Column(Integer, primary_key=True)
    name = Column(VARCHAR)
    air_date = Column(DATE, primary_key=True)
