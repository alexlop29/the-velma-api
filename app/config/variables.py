from pydantic import BaseSettings
import os

class Settings(BaseSettings):
    DATABASE_URL=os.getenv("DATABASE_URL")
    DOMAIN = os.getenv("DOMAIN")
    API_AUDIENCE = os.getenv("API_AUDIENCE")
    ISSUER = os.getenv("ISSUER")
    ALGORITHMS = "RS256"

settings = Settings()
