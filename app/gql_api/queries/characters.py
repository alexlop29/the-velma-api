import strawberry
from gql_api.schemas.characters import Character as Schema_Char
from models.characters import Character
from config.db import SessionLocal
import strawberry
from sqlalchemy.orm import Session
from sqlalchemy import or_
from fastapi import Depends
from typing import Optional

db = SessionLocal()

@strawberry.input
class SearchCharacter:
    first_name: Optional[str] = strawberry.UNSET
    last_name: Optional[str] = strawberry.UNSET

@strawberry.type
class Query:
    @strawberry.field
    def characters(self) -> list[Schema_Char]:
        return db.query(Character).order_by(Character.first_name)
    @strawberry.field
    def character(self, search_char: SearchCharacter) -> list[Schema_Char]:
        return db.query(Character).filter(or_(
        Character.first_name.ilike(f'%{search_char}%'),
        Character.last_name.ilike(f'%{search_char}%'))
        ).all()
