from fastapi import FastAPI
from .router import soccer_orq_router as SoccerRouter

app = FastAPI()
app.include_router(SoccerRouter.router, tags=["Soccer"], prefix="/soccer/process")


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this SheduleMatch domain !"}
