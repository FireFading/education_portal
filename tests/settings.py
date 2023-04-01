from dotenv import load_dotenv
from pydantic import BaseSettings, Field, PostgresDsn

load_dotenv(dotenv_path=".env.example")


class Settings(BaseSettings):
    test_database_url: PostgresDsn | str = Field(env="TEST_DATABASE_URL")

    class Config:
        env_file = "../.env.example"
