import uuid

from sqlalchemy import Boolean, Column, String
from sqlalchemy_utils import UUIDType

from app.crud import CRUD
from app.database import Base


class User(Base, CRUD):
    __tablename__ = "users"

    id = Column(UUIDType(binary=False), primary_key=True, index=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    is_active = Column(Boolean, nullable=False, default=True)
    password = Column(String, nullable=False)
