from pydantic import BaseModel

class CharacterByEpisodeBase(BaseModel):
    character_id: int
    episode_id: int

class CharacterByEpisdeCreate(CharacterByEpisodeBase):
    pass

class CharacterByEpisode(CharacterByEpisodeBase):
    character_id: int
    episode_id: int

    class Config:
        orm_mode = True
