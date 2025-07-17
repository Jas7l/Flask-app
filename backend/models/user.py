from sqlalchemy import Column, String, Boolean, Integer, LargeBinary
from flask_login import UserMixin
from ..database import Base


class User(Base, UserMixin):
    __tablename__ = "users"
    orbis_id = Column(Integer, autoincrement=True, primary_key=True, unique=True)
    login = Column(String(100), nullable=False, unique=True)
    password = Column(LargeBinary(60), nullable=False)
    active = Column(Boolean, default=True)

    def get_id(self):
        return str(self.orbis_id)
