from sqlalchemy.orm.session import Session
from app.schema.users_schema import UsersRegister
from app.database.models import UserData
from app.auth.hash import Hash
from app.services.interface import UserAuth

class DatabaseUser(UserAuth):
    def register(self,db: Session, request: UsersRegister):
        new_user = UserData(
            first_name=request.first_name,
            last_name=request.last_name,
            email=request.email,
            password=Hash.bcrypt(request.password)
        )
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user

    def _get_user(self,db: Session):
        return db.query(UserData).all()
    
    def _delete_user(self,id:int,db=Session):
        user = db.query(UserData).filter(UserData.id == id).first()
        db.delete(user)
        db.commit()
        return "ok"
    
    def login(self,email:str,password:str,db=Session):
        user = db.query(UserData).filter(UserData.email == email).first()
        if not user or not Hash.verify(password,UserData.password):
            raise ValueError("Invalid Credentials")
        return Hash.create_token(str(UserData.id))