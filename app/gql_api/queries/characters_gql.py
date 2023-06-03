import strawberry
from gql_api.schemas.characters import Character as Schema_Char
from models.characters import Character
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

@strawberry.enum
class SelectCharacterSearchField(Enum):
    first_name = "first_name"
    last_name = "last_name"

@strawberry.input
class SearchCharacterPath:
    search_field: SelectCharacterSearchField
    search_string : str

@strawberry.type
class Character_GQL:
    @strawberry.field
    def get_characters(self) -> list[Schema_Char]:
        return db.query(Character).order_by(Character.first_name)
    @strawberry.field
    def search_for_character(self, search_options: SearchCharacterPath) -> list[Schema_Char]:
        print(search_options.search_field, search_options.search_string)
        match search_options.search_field:
            case SelectCharacterSearchField.first_name:
                return db.query(Character).filter(Character.first_name.ilike(f'%{search_options.search_string}%')).all()
            case SelectCharacterSearchField.last_name:
                return db.query(Character).filter(Character.last_name.ilike(f'%{search_options.search_string}%')).all()
    @strawberry.field
    def count_of_characters(self) -> JSON:
        return {"count": db.query(Character).count()} 
