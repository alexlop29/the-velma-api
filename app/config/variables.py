""" Configures the environment variables """
import os
from pydantic import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL = os.getenv("DATABASE_URL")
    DOMAIN = os.getenv("DOMAIN")
    API_AUDIENCE = os.getenv("API_AUDIENCE")
    ISSUER = os.getenv("ISSUER")
    ALGORITHMS = "RS256"
    SENTRY_DSN = os.getenv("SENTRY_DSN")
    SENTRY_ENVIRONMENT = os.getenv("SENTRY_ENVIRONMENT")
    TRACES_SAMPLE_RATE = os.getenv("TRACES_SAMPLE_RATE")


settings = Settings()
