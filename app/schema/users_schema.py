from pydantic import BaseModel, EmailStr, validator, Field
from typing import Optional
import re

class UsersRegister(BaseModel):
    first_name: str = Field(...,min_length=2,max_length=100)
    last_name:str=Field(...,min_length=2,max_length=100)
    email:EmailStr
    password:str = Field(...,min_length=8,max_length=100)

    @validator("first_name","last_name")
    def validate_name(cls,v):
        if not v or len(v.strip()) < 2:
            raise ValueError("Name must be 2 characters long")
        if not re.match(r'^[a-zA-Z\s\'-]+$',v):
            raise ValueError("Name can have letters ,spaces and extra characters")
        
    @validator("password")
    def validate_password(cls,v):
        if not len(v) >8:
            raise ValueError("The password should be minimium 8 characters long")
        if not re.search(r'[A-Z]',v):
            raise ValueError("Password must contain atleast one uppercase character")
        if not re.search(r'[a-z]',v):
            raise ValueError("Password must contain atleast one lowercase character")
        if not re.search(r'\d', v):
            raise ValueError('Password must contain atleast one digit')
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', v):
            raise ValueError('Password must contain atleast one special character')
        return v

class UserLogin(BaseModel):
    email: EmailStr
    password:str = Field(...,min_length=8,max_length=100)
