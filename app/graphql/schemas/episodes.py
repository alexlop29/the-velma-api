from models.episodes import Episode
import strawberry
import datetime

@strawberry.type
class Episode:
    episode_id: strawberry.ID
    name: str
    air_date: datetime.date

    @classmethod
    def marshal(cls, model: Episode) -> "Episode":
        return cls(
            episode_id=strawberry.ID(str(Episode.episode_id)),
            name=Episode.name,
            air_date=Episode.air_date
        )
