import asyncio
from collections.abc import AsyncGenerator

import pytest
import pytest_asyncio

from app.database import Base, get_session
from app.main import app as main_app
from fastapi import FastAPI, status
from fastapi.testclient import TestClient
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from tests.config import settings, test_user


engine = create_async_engine(
    settings.test_database_url,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)

Session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


@pytest_asyncio.fixture()
async def app() -> AsyncGenerator:
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield main_app
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


@pytest_asyncio.fixture
async def client(app: FastAPI, db_session: Session) -> AsyncGenerator | TestClient:
    async def _get_test_db():
        yield db_session

    app.dependency_overrides[get_session] = _get_test_db
    with TestClient(app) as client:
        yield client


@pytest.fixture(scope="session")
def event_loop():
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest_asyncio.fixture
async def db_session(app: FastAPI) -> AsyncGenerator:
    connection = await engine.connect()
    transaction = await connection.begin()
    session = Session(bind=connection)
    yield session
    await session.close()
    await transaction.rollback()
    await connection.close()


@pytest_asyncio.fixture
async def register_user(client: AsyncGenerator | TestClient) -> AsyncGenerator:
    response = client.post("/users/register", json=test_user)
    assert response.status_code == status.HTTP_201_CREATED
