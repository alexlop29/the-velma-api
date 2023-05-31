from models.characters import Character
import strawberry

@strawberry.type
class Character:
    character_id: strawberry.ID
    first_name: str
    last_name: str
    species: str
    gender: str

    @classmethod
    def marshal(cls, model: Character) -> "Character":
        return cls(
            character_id=strawberry.ID(str(Character.character_id)),
            first_name=Character.first_name,
            last_name=Character.last_name,
            species=Character.species,
            gender=Character.gender
        )
