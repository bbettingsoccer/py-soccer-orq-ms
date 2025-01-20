from fastapi import FastAPI
from .routes import process_router


app = FastAPI()
app.include_router(process_router.router, tags=["Soccer-Match-Domain"], prefix="/soccer/process")
