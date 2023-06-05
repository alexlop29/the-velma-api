import strawberry
from gql_api.schemas.locations import Location as Location_Schema
from models.locations import Location
from config.db import SessionLocal
from strawberry.scalars import JSON
from gql_api.fragments.pagination import PaginationWindow, get_pagination_window


db = SessionLocal()


@strawberry.type
class Location_GQL:
    @strawberry.field
    def get_locations(self, limit: int, offset: int = 0,) -> PaginationWindow[Location_Schema]:
        count = db.query(Location).count()
        return get_pagination_window(dataset=db.query(Location).order_by(Location.name),
                                     ItemType=Location,
                                     limit=limit,
                                     offset=offset,
                                     total=count)

    @strawberry.field
    def count_of_locations(self) -> JSON:
        return {"count": db.query(Location).count()}
