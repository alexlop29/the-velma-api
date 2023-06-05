from models.locations import Location
import strawberry


@strawberry.type
class Location:
    location_id: strawberry.ID
    name: str

    @classmethod
    def marshal(cls, model: Location) -> "Location":
        return cls(
            episode_id=strawberry.ID(str(Location.location_id)),
            name=Location.name
        )
