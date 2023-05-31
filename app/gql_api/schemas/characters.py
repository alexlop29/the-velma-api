from models.characters import Character as Character_Model
import strawberry

@strawberry.type
class Character:
    character_id: strawberry.ID
    first_name: str
    last_name: str
    species: str
    gender: str

    @classmethod
    def marshal(cls, model: Character_Model) -> "Character":
        return cls(
            character_id=strawberry.ID(str(Character_Model.character_id)),
            first_name=Character_Model.first_name,
            last_name=Character_Model.last_name,
            species=Character_Model.species,
            gender=Character_Model.gender
        )
