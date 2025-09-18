
from app.database.db import Base
from sqlalchemy import Column
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import Integer,String,Boolean
from sqlalchemy.sql.schema import ForeignKey

class UserData(Base):
    __tablename__ ="users"
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String, unique=True)
    password = Column(String)