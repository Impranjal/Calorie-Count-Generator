from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.db import get_db
from app.database.db_user import DatabaseUser
from app.schema.users_schema import UsersRegister,UserLogin

router = APIRouter()
db_user = DatabaseUser()

@router.post("/register")
def register(user: UsersRegister, db: Session = Depends(get_db)):
    try:
        return db_user.register(db, user)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    try:
        token = db_user.login(db, user.email, user.password)
        return {"access_token": token, "token_type": "bearer"}
    except ValueError as e:
        raise HTTPException(status_code=401, detail=str(e))
