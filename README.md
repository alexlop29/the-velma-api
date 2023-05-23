# the-velma-api
Contains an API to query the Velma TV show, using Python's FastAPI

# To Do
- Transfer database to AWS
- Remove hardcoded credentials in the `alembic-ini` file. 

```
docker-compose build
docker-compose up -d
docker-compose down
docker-compose up --build (To Relaunch with Updates)
```

# Environment Variables Documentation
- https://itsjoshcampos.codes/fast-api-environment-variables#heading-read-environment-variables-in-fastapi
- https://fastapi.tiangolo.com/advanced/settings/

NOTE TO SELF:
- Add filter to disregard case in query (get_character by name)
- Left off fixing the following error in the character_appearances_by_episodes
```
There is an entry for table "character_appearances_by_episode", but it cannot be referenced from this part of the query.
Examples:
- https://fastapi.tiangolo.com/tutorial/sql-databases/
- https://www.tutorialspoint.com/sqlalchemy/sqlalchemy_orm_building_relationship.htm
```
