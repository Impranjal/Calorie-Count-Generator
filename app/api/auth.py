from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.db import get_db
from app.database.db_user import DatabaseUser
from app.schema.users_schema import UsersRegister,UserLogin,UserDisplay

router = APIRouter(
    prefix="/auth",
    tags= ["Authentication"]
)
@router.post("/register",response_model=UserDisplay)
def register(user: UsersRegister, db: Session = Depends(get_db)):
    service = DatabaseUser()
    try:
        return service.register(db, user)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    service = DatabaseUser()
    try:
        token = service.login(db, user.email, user.password)
        return {"access_token": token, "token_type": "bearer"}
    except ValueError as e:
        raise HTTPException(status_code=401, detail=str(e))
