from pydantic import BaseModel


class LocationBase(BaseModel):
    name: str


class LocationCreate(LocationBase):
    pass


class Location(LocationBase):
    location_id: int

    class Config:
        orm_mode = True
