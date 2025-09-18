from sqlalchemy.orm import Session
from app.schema.users_schema import UsersRegister,UserDisplay
from app.database.models import UserData
from app.auth.hash import Hash
from app.services.interface import UserAuth

class DatabaseUser(UserAuth):
    def register(self, db: Session, request: UsersRegister):
        new_user = UserData(
            first_name=request.first_name,
            last_name=request.last_name,
            email=request.email,
            password=Hash.bcrypt(request.password)  
        )
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return UserDisplay(
            username=f"{new_user.first_name} {new_user.last_name}",
            email=new_user.email
        )

    def _get_user(self, db:Session):
        return db.query(UserData).all()

    def _delete_user(self,db:Session,id:int,):  
        user = db.query(UserData).filter(UserData.id == id).first()
        if not user:
            return "User not found"
        db.delete(user)
        db.commit()
        return "ok"

    def login(self,db: Session, email: str,password: str):
        user = db.query(UserData).filter(UserData.email == email).first()
        if not user or not Hash.verify(user.password,password):
            raise ValueError("Invalid Credentials")
        return Hash.create_token(str(user.id))
  
