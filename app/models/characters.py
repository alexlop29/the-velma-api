from sqlalchemy import Column, Integer, VARCHAR

from config.db import Base

class Character(Base):
    __tablename__ = "characters"

    character_id = Column(Integer, primary_key=True)
    first_name = Column(VARCHAR)
    last_name = Column(VARCHAR)
    species = Column(VARCHAR)
    gender = Column(VARCHAR)

