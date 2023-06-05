import strawberry
from gql_api.schemas.characters import Character as Schema_Char
from models.characters import Character
from config.db import SessionLocal
from enum import Enum
from strawberry.scalars import JSON
from gql_api.fragments.pagination import PaginationWindow, get_pagination_window

db = SessionLocal()


@strawberry.enum
class SelectCharacterSearchField(Enum):
    first_name = "first_name"
    last_name = "last_name"


@strawberry.input
class SearchCharacterPath:
    search_field: SelectCharacterSearchField
    search_string: str


@strawberry.type
class Character_GQL:
    @strawberry.field
    def get_characters(self, limit: int, offset: int = 0,) -> PaginationWindow[Schema_Char]:
        count = db.query(Character).count()
        return get_pagination_window(dataset=db.query(Character).order_by(Character.first_name),
                                     ItemType=Character,
                                     limit=limit,
                                     offset=offset,
                                     total=count)

    @strawberry.field
    def search_for_character(self, search_options: SearchCharacterPath) -> list[Schema_Char]:
        print(search_options.search_field, search_options.search_string)
        match search_options.search_field:
            case SelectCharacterSearchField.first_name:
                return db.query(Character).filter(
                    Character.first_name.ilike(f'%{search_options.search_string}%')
                ).all()
            case SelectCharacterSearchField.last_name:
                return db.query(Character).filter(
                    Character.last_name.ilike(f'%{search_options.search_string}%')
                ).all()

    @strawberry.field
    def count_of_characters(self) -> JSON:
        return {"count": db.query(Character).count()}
