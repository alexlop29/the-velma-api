import strawberry
from graphql.schemas.episodes import Episode

@strawberry.type
class EpisoderNotFound:
    message: str = "Couldn't find an episode with the supplied name"

AddEpisodeResponse = strawberry.union(
    "AddEpisoderResponse", 
    (Episode, EpisoderNotFound)
)
