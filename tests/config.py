from tests.settings import Settings

settings = Settings(_env_file="../.env.example")

test_user = {"name": "Name", "surname": "Surname", "email": "new_user@google.com"}

show_test_user = {
    "name": "Name",
    "surname": "Surname",
    "email": "new_user@google.com",
    "is_active": True,
}
