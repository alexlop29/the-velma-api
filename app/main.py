from fastapi import FastAPI
from routers import characters, episodes, locations, characters_appearances_by_episodes, locations_visited_by_characters
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware
from fastapi.responses import RedirectResponse
from config.variables import settings
import sentry_sdk
from sentry_sdk.integrations.starlette import StarletteIntegration
from sentry_sdk.integrations.fastapi import FastApiIntegration
from sentry_sdk.integrations.sqlalchemy import SqlalchemyIntegration
import strawberry
from strawberry.fastapi import GraphQLRouter
from graphql.queries.characters import Query

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

# @strawberry.type
# class Query:
#     @strawberry.field
#     def hello(self) -> str:
#         return "Hello World"
schema = strawberry.Schema(query=Query)
graphql_app = GraphQLRouter(schema)

description = """
Query information about HBO Max's Velma
"""

app = FastAPI(
    title="the Velma API",
    description=description,
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
    return RedirectResponse(url='/docs')
