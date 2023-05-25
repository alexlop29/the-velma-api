from pydantic import BaseSettings
import os

class Settings(BaseSettings):
    DATABASE_URL=os.getenv("DATABASE_URL")
    DATABASE_URL_2=os.getenv("DATABASE_URL_2")
    DOMAIN = os.getenv("DOMAIN")
    API_AUDIENCE = os.getenv("API_AUDIENCE")
    ISSUER = os.getenv("ISSUER")
    ALGORITHMS = "RS256"

settings = Settings()
