from pydantic import BaseModel


LETTER_NAME_PATTERN = "^[a-zA-Z]+$"


class CustomConfig(BaseModel):
    class Config:
        orm_mode = True

