from fastapi import FastAPI
from app.database import models
from app.database.db import engine
from slowapi.middleware import SlowAPIMiddleware
from slowapi.errors import RateLimitExceeded
from fastapi.responses import JSONResponse
from app.api import auth,calories_entry
from app.services.rate_limiter import limiter
app = FastAPI()
app.state.limiter = limiter
app.add_middleware(SlowAPIMiddleware)
@app.exception_handler(RateLimitExceeded)
def rate_limit_handler(request, exc):
    return JSONResponse(
        status_code=429,
        content={"detail": "Too many requests. Please slow down."}
    )

app.include_router(auth.router)
app.include_router(calories_entry.router)

models.Base.metadata.create_all(bind=engine)