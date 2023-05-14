from pydantic import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL="postgresql://velma-api:velma-api@postgres:5432/velma-api"
    OKTA_CLIENT_ID = "0oa9jluw5i8uSQ7J45d7"
    OKTA_CLIENT_SECRET = "OkMmRX7-eB_77bpFsLpeOQBR5iMNlwoaK0PQrk_-"
    OKTA_ISSUER = "Hrxc5wCk5cHA5S4cyUZVc8CSA65BfBkEVjpCtOb6"

settings = Settings()
