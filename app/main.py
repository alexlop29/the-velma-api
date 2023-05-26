from fastapi import FastAPI
from routers import characters, episodes, locations, characters_appearances_by_episodes, locations_visited_by_characters
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware
from fastapi.responses import RedirectResponse

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

@app.get("/", include_in_schema=False)
async def root():
    return RedirectResponse(url='/docs')
