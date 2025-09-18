from fastapi import APIRouter,Depends,HTTPException,Form,status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from database.database import get_db
from database import models
from app.auth.hash import Hash
from auth import oauth2
router = APIRouter(
    tags =['authentication']

)

@router.post('/token')
def get_token(request:OAuth2PasswordRequestForm=Depends(),db: Session=Depends(get_db)):
    user =db.query(models.UserData).filter(models.UserData.username == request.username).first()
    if not user:
        raise HTTPException(status_code=404)
    if not Hash.verify(user.password,request.password):
        raise HTTPException(status_code=401)
    access_token = oauth2.create_access_token(data={'sub':user.username})

    return{
        'access_token':access_token,
        'token_type':'bearer',
        'user_id':user.id,
        'username':user.username
    }