from pydantic import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL="postgresql://velma-api:velma-api@postgres:5432/velma-api"
    DOMAIN = "dev-xxn2763opsyx3347.us.auth0.com"
    API_AUDIENCE = "https://the-velma-api.com"
    ISSUER = "https://dev-xxn2763opsyx3347.us.auth0.com/"
    ALGORITHMS = "RS256"

settings = Settings()
