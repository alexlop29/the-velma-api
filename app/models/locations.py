from sqlalchemy import Column, Integer, VARCHAR, ARRAY

from config.db import Base

class Location(Base):
    __tablename__ = "locations"

    location_id = Column(Integer, primary_key=True)
    name = Column(VARCHAR)
