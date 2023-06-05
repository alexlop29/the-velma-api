import strawberry
from gql_api.schemas.episodes import Episode as Episode_Schema
from models.episodes import Episode
from config.db import SessionLocal
from strawberry.scalars import JSON


db = SessionLocal()


@strawberry.type
class Episode_GQL:
    @strawberry.field
    def get_episodes(self) -> list[Episode_Schema]:
        return db.query(Episode).order_by(Episode.air_date)

    @strawberry.field
    def count_of_episodes(self) -> JSON:
        return {"count": db.query(Episode).count()}
