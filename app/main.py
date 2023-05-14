from fastapi import FastAPI
from routers import characters, episodes, locations, login

app = FastAPI()

app.include_router(characters.router)
app.include_router(episodes.router)
app.include_router(locations.router)
app.include_router(login.router)

@app.get("/")
async def root():
    return {"message": "the-velma-api"}
