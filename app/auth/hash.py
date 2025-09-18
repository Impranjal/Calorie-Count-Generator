import os
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from typing import Optional
from datetime import datetime, timedelta
from jose import jwt
pwd_cxt = CryptContext(schemes="bcrypt",deprecated='auto')
oauth_scheme = OAuth2PasswordBearer(tokenUrl="token")

SECRET_KEY = os.getenv("JWT_SECERT_KEY", "supersecret")
ALGORITHM = os.getenv("JWT_ALGORITHM", "HS256")
JWT_EXPIRY_MIN = int(os.getenv("JWT_EXPIRY_MIN", "60"))

class Hash():
    def bcrypt(password:str):
        return pwd_cxt.hash(password)

    def verify(hashed_password,plain_password):
        return pwd_cxt.verify(plain_password,hashed_password)
    
    def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=JWT_EXPIRY_MIN)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt