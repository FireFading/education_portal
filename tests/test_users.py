from app.utils.messages import messages
from fastapi import status
from pytest_mock import MockerFixture

from tests.config import show_test_user, test_user


class TestRegister:
    async def test_register_user(self, client, mocker: MockerFixture):
        mocker.patch("uuid.uuid4", return_value="00000000-0000-0000-0000-000000000000")
        response = client.post("/users/register/", json=test_user)
        assert response.status_code == status.HTTP_201_CREATED
        result = response.json()
        assert "id" in result
        del result["id"]
        assert result == show_test_user


class TestLogin:
    async def test_login_user(self, register_user, client):
        response = client.post(
            "/users/login",
            json={"email": test_user.email, "password": test_user.password},
        )
        assert response.status_code == status.HTTP_200_OK
        assert "access_token" in response.json()
        assert "refresh_token" in response.json()

    async def test_wrong_password_login(self, register_user, client):
        response = client.post(
            "/users/login",
            json={"email": test_user.email, "password": test_user.wrong_password},
        )
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
        assert response.json().get("detail") == messages.WRONG_PASSWORD
