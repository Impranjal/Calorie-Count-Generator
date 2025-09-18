from pydantic import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str
    API_KEY: str
    JWT_SECERT_KEY: str
    JWT_ALGORITHM: str = "HS256"
    JWT_EXPIRY_MIN: int = 60
    RATE_LIMIT_REQ: int = 15
    RATE_LIMIT_WINDOW_SEC: int = 60
    
    class Config:
        env_file = ".env"

settings = Settings()
        

