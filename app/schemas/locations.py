from pydantic import BaseModel

class EpisodeBase(BaseModel):
    name: str

class EpisodeCreate(EpisodeBase):
    pass

class Episode(EpisodeBase):
    location_id: int

    class Config:
        orm_mode = True


