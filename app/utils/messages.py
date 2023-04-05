from dataclasses import dataclass


@dataclass
class Messages:
    USER_NOT_FOUND = "User not found"
    USER_ALREADY_EXISTS = "User already exists"
    USER_LOGOUT = "User logout"

    WRONG_PASSWORD = "Wrong password"


messages = Messages()
