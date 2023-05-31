import strawberry
from gql_api.schemas.characters import Character as Schema_Char
from models.characters import Character
from config.db import SessionLocal
import strawberry
from sqlalchemy.orm import Session
from fastapi import Depends

def get_db():
    """ Establishes a connection to the database """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# @strawberry.type
# class Query:
#     @strawberry.field
#     async def books(self) -> list[Book]:
#         async with models.get_session() as s:
#             sql = select(models.Book).order_by(models.Book.name)
#             db_books = (await s.execute(sql)).scalars().unique().all()
#         return [Book.marshal(book) for book in db_books]


# @strawberry.type
# class Query:
#     @strawberry.field
#     async def characters(self) -> list[Schema_Char]:
#         async with get_db() as db:
#             sql = db.query(Character).order_by(Character.first_name)
#             db_chars = (await db.execute(sql)).scalars().unique().all()
#         return [Schema_Char.marshal(Character) for character in db_chars]
    

@strawberry.type
class Query:
    @strawberry.field
    async def characters(self) -> list[Schema_Char]:
        db: Session = Depends(get_db)
        return db.query(Character).order_by(Character.first_name)
        return [Schema_Char.marshal(Character) for character_item in list_of_chars]
