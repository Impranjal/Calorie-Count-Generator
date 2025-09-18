from fastapi import FastAPI
from app.database import models
from app.database.db import engine
from app.api import auth
app = FastAPI()
app.include_router(auth.router)
models.Base.metadata.create_all(bind=engine)