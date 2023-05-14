from pydantic import BaseModel, datetime

class EpisodeBase(BaseModel):
    name: str
    air_date: datetime.date

class EpisodeCreate(EpisodeBase):
    pass

class Episode(EpisodeBase):
    episode_id: int

    class Config:
        orm_mode = True


