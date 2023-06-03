import strawberry
from gql_api.schemas.locations import Location as Location_Schema
from models.locations import Location
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
class Location_GQL:
    @strawberry.field
    def get_locations(self) -> list[Location_Schema]:
        return db.query(Location).order_by(Location.name)
    @strawberry.field
    def count_of_locations(self) -> JSON:
        return {"count": db.query(Location).count()} 

