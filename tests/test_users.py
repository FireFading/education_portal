import json

import pytest
from fastapi import status
from pytest_mock import MockerFixture

from tests.config import show_test_user, test_user


class TestRegister:
    @pytest.mark.asyncio
    async def test_register_user(self, client, mocker: MockerFixture):
        mocker.patch("uuid.uuid4", return_value="00000000-0000-0000-0000-000000000000")
        response = client.post("/users/register/", json=test_user)
        assert response.status_code == status.HTTP_201_CREATED
        result = response.json()
        assert "id" in result
        del result["id"]
        assert result == show_test_user
