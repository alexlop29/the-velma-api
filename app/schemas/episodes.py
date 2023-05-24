from pydantic import BaseModel
from datetime import date

class EpisodeBase(BaseModel):
    name: str
    air_date: date

class EpisodeCreate(EpisodeBase):
    pass

class Episode(EpisodeBase):
    episode_id: int

    class Config:
        orm_mode = True

