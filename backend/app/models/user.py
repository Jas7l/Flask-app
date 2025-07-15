from sqlalchemy import Column, String, Boolean, Integer, LargeBinary
from ..database import Base


class User(Base):
    __tablename__ = "users"
    orbis_id = Column(Integer, autoincrement=True, primary_key=True)
    login = Column(String(100), nullable=False)
    password = Column(LargeBinary(60), nullable=False)
    active = Column(Boolean, default=False)
