import strawberry
from graphql.schemas.characters import Character

@strawberry.type
class CharacterNotFound:
    message: str = "Couldn't find a character with the supplied name"

@strawberry.type
class CharacterNameMissing:
    message: str = "Please supply a character name"

AddCharacterResponse = strawberry.union(
    "AddCharacterResponse", 
    (Character, CharacterNotFound, CharacterNameMissing)
)
