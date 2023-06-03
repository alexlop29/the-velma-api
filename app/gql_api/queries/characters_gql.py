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
from typing import List, TypeVar
from strawberry.scalars import JSON

db = SessionLocal()

GenericType = TypeVar("GenericType")

@strawberry.type
class PaginationWindow(List[GenericType]):
    items: List[GenericType] = strawberry.field(
        description="The list of items in this pagination window."
    )

    total_items_count: int = strawberry.field(
        description="Total number of items in the filtered dataset."
    )

def get_pagination_window(
        dataset: List[GenericType],
        ItemType: type,
        limit: int,
        offset: int = 0,
        filters: dict[str, str] = {}) -> PaginationWindow:
    """
    Get one pagination window on the given dataset for the given limit
    and offset, ordered by the given attribute and filtered using the
    given filters
    """

    if limit <= 0 or limit > 100:
        raise Exception(f'limit ({limit}) must be between 0-100')

    if offset != 0 and not 0 <= offset < len(dataset):
        raise Exception(f'offset ({offset}) is out of range '
                        f'(0-{len(dataset) - 1})')

    items = dataset[offset:offset + limit]

    items = [ItemType.from_row(x) for x in items]

    return PaginationWindow(items=items)

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
    def get_characters(self, limit: int, offset: int = 0,) -> PaginationWindow[Schema_Char]:
        return get_pagination_window(dataset=db.query(Character).order_by(Character.first_name), \
                                    ItemType=Character, \
                                    limit=limit, \
                                    offset=offset,)
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

