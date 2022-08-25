from fastapi_users.db import SQLAlchemyBaseUserTableUUID
from sqlalchemy import Column, Integer, String
from sqlalchemy_utils import PhoneNumberType

from database import Base

class User(SQLAlchemyBaseUserTableUUID, Base):
    __tablename__ = 'user'

    def __repr__(self):
        return f'{self.id} {self.name}'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    phone = Column(PhoneNumberType())
