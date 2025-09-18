import os
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from typing import Optional
from datetime import datetime, timedelta
from jose import jwt
from app.config_loader import settings
pwd_cxt = CryptContext(schemes="bcrypt",deprecated='auto')
oauth_scheme = OAuth2PasswordBearer(tokenUrl="token")


class Hash():
    def bcrypt(password:str):
        return pwd_cxt.hash(password)

    def verify(hashed_password,plain_password):
        return pwd_cxt.verify(plain_password,hashed_password)
    
    def create_token(data, expires_delta: Optional[timedelta] = None):
        if isinstance(data, str):
            to_encode = {"user_id": data}
        else:
            to_encode = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=settings.JWT_EXPIRY_MIN)

        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, settings.JWT_SECERT_KEY, algorithm=settings.JWT_ALGORITHM)
        return encoded_jwt
