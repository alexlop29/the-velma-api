from fastapi import FastAPI
from routers import characters, episodes, locations, characters_appearances_by_episodes

description = """
Query informatiom about HBO Max's Velma
"""

app = FastAPI(
    title="the Velma API",
    description=description,
    version="0.0.1",
    contact={
        "name": "Alexander Lopez",
        "email": "alexander.lopez@owasp.org",
    },
)

app.include_router(characters.router)
app.include_router(episodes.router)
app.include_router(locations.router)
app.include_router(characters_appearances_by_episodes.router)

@app.get("/")
async def root():
    return {"message": "the-velma-api"}
