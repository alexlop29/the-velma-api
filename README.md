# the-velma-api
Contains an API to query the Velma TV show, using Python's FastAPI

# Local Developemnt
```
docker-compose build
docker-compose up -d
docker-compose down
docker-compose up --build (To Relaunch with Updates)
```

NOTE TO SELF:
- Remediate the pylint errors
- Need to return to finish error handling in /characters
- Need to test passing invalid token
- non existing character in /characters/search should produce 404 - not found (check all)
- function to check for duplicate records


https://stackoverflow.com/questions/65982681/how-to-access-the-database-from-unit-test-in-fast-api
