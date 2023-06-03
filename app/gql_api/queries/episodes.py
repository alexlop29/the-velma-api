import strawberry
from gql_api.schemas.episodes import Episode as Episode_Schema
from models.episodes import Episode
from config.db import SessionLocal
import strawberry
from sqlalchemy.orm import Session
from sqlalchemy import or_
from fastapi import Depends
from typing import Optional
from enum import Enum
import typing
from strawberry.scalars import JSON

db = SessionLocal()

@strawberry.type
class Episode:
    @strawberry.field
    def get_episodes(self) -> list[Episode_Schema]:
        return db.query(Episode).order_by(Episode.air_date)
    @strawberry.field
    def count_of_episodes(self) -> JSON:
        return {"count": db.query(Episode).count()} 

