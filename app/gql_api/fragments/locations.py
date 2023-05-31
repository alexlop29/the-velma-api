import strawberry
from gql_api.schemas.locations import Location

@strawberry.type
class LocationNotFound:
    message: str = "Couldn't find a location with the supplied name"

@strawberry.type
class LocationNameMissing:
    message: str = "Please supply a location name"

AddLocationResponse = strawberry.union(
    "AddLocationResponse", 
    (Location, LocationNotFound, LocationNameMissing)
)
