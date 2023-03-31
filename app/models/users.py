from app.database import Base
import uuid
from sqlalchemy import Column, Date, Float, Integer, String, Boolean
from sqlalchemy_utils import UUIDType


class User(Base):
    __tablename__ = "users"

    id = Column(
        UUIDType(binary=False), primary_key=True, index=True, default=uuid.uuid4
    )
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    is_active = Column(Boolean, nullable=False, default=True)