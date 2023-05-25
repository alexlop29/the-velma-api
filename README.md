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


# Many-to-Many Relationships
- https://stackoverflow.com/questions/25668092/flask-sqlalchemy-many-to-many-insert-data

NOTE TO SELF:
- Add filter to disregard case in query (get_character by name)
- Remediate the pylint errors
- https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/PostgreSQL.Procedural.Importing.EC2.html
- Missing two girls in the shower scene in episode 1 / also appear in spooner's malt shop / lola & becca 
- May want to create baby velma and baby daphne
- BUG: post location_by_character returns all locations, as opposed to the newly created row 

- Dynamically query DB URL from Heroku

# Helpful SQL Queries
```
select C.character_id, C.first_name, C.last_name, CA.episode_id from characters as C join character_appearances_by_episode CA on C.character_id = CA.character_id;
```


```
SELECT * FROM characters JOIN character_appearances_by_episode ON characters.character_id = character_appearances_by_episode.character_id JOIN episodes ON character_appearances_by_episode.episode_id = episodes.episode_id ORDER BY characters.character_id

select * from characters as C join character_appearances_by_episode CA on C.character_id = CA.character_id;

select C.character_id, C.first_name, C.last_name, CA.episode_id from characters as C join character_appearances_by_episode CA on C.character_id = CA.character_id join episodes E on E.episode_id = CA.episode_id;

select C.character_id, C.first_name, C.last_name, CA.episode_id from characters as C join character_appearances_by_episode CA on C.character_id = CA.character_id;
```
