from pydantic import BaseModel


class CharacterByEpisodeBase(BaseModel):
    character_id: int
    episode_id: int


class CharacterByEpisodeCreate(CharacterByEpisodeBase):
    pass


class CharacterByEpisode(CharacterByEpisodeBase):
    id: int

    class Config:
        orm_mode = True
