from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schema import UsersRegister,UserLogin
from app.services.auth_service import AuthService

router = APIRouter()
auth_service = AuthService()

@router.post("/register")
def register(user: UsersRegister, db: Session = Depends(get_db)):
    try:
        return auth_service.register(db, user)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    try:
        token = auth_service.login(db, user.email, user.password)
        return {"access_token": token, "token_type": "bearer"}
    except ValueError as e:
        raise HTTPException(status_code=401, detail=str(e))
