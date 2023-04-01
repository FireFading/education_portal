import re
from uuid import UUID

from fastapi import HTTPException, status
from pydantic import BaseModel, EmailStr, validator

from app.schemas.base import LETTER_NAME_PATTERN, CustomConfig


class CreateUser(BaseModel):
    name: str
    surname: str
    email: EmailStr

    @validator("name", "surname")
    def validate_name_fields(cls, value):
        if not re.match(pattern=LETTER_NAME_PATTERN, string=value):
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail="Name should contains only letters",
            )
        return value


class ShowUser(CustomConfig):
    id: UUID
    name: str
    surname: str
    email: EmailStr
    is_active: bool
