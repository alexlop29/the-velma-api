""" Contains the configuration to launch FastAPI """

from fastapi import FastAPI
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware
from fastapi.responses import RedirectResponse
from routers import characters, episodes, locations
from routers import characters_appearances_by_episodes, locations_visited_by_characters
from config.variables import settings
import sentry_sdk
from sentry_sdk.integrations.starlette import StarletteIntegration
from sentry_sdk.integrations.fastapi import FastApiIntegration
from sentry_sdk.integrations.sqlalchemy import SqlalchemyIntegration
import strawberry
from strawberry.fastapi import GraphQLRouter
from strawberry.tools import merge_types
from gql_api.queries import characters_gql, episodes_gql, locations_gql


sentry_sdk.init(
    dsn=settings.SENTRY_DSN,
    environment=settings.SENTRY_ENVIRONMENT,
    traces_sample_rate=settings.TRACES_SAMPLE_RATE,
    integrations=[
        StarletteIntegration(transaction_style="endpoint"),
        FastApiIntegration(transaction_style="endpoint"),
        SqlalchemyIntegration()
    ]
)

ComboQuery = merge_types("ComboQuery", (
                          characters_gql.Character_GQL,
                          episodes_gql.Episode_GQL,
                          locations_gql.Location_GQL
                        ))
schema = strawberry.Schema(query=ComboQuery)
graphql_app = GraphQLRouter(schema)

DESCRIPTION = """
Query information about HBO Max's Velma
"""

app = FastAPI(
    title="the Velma API",
    description=DESCRIPTION ,
    version="1.0.0",
    contact={
        "name": "Alexander Lopez",
        "email": "alexander.lopez@owasp.org",
    },
)

app.add_middleware(HTTPSRedirectMiddleware)

app.include_router(characters.router)
app.include_router(episodes.router)
app.include_router(locations.router)
app.include_router(characters_appearances_by_episodes.router)
app.include_router(locations_visited_by_characters.router)
app.include_router(graphql_app, prefix="/graphql", include_in_schema=False)


@app.get("/", include_in_schema=False)
async def root():
    """ Launches the application and redirects the user to the Swagger Docs """
    return RedirectResponse(url='/docs')
