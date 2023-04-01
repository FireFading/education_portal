from app.schemas.base import CustomConfig, LETTER_NAME_PATTERN
from pydantic import BaseModel, EmailStr, validator
import re
from fastapi import HTTPException, status
from uuid import UUID


class CreateUser(BaseModel):
    name: str
    surname: str
    email: EmailStr

    @validator("name", "surname")
    def validate_name_fields(cls, value):
        if not re.match(pattern=LETTER_NAME_PATTERN, string=value):
            raise HTTPException(status=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Name should contains only letters")
        return value


class ShowUser(CustomConfig):
    id: UUID
    name: str
    surname: str
    email: EmailStr
    is_active: bool
