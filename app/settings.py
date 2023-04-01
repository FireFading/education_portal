from dotenv import load_dotenv
from pydantic import BaseSettings, Field, PostgresDsn

load_dotenv(dotenv_path="../.env")


class Settings(BaseSettings):
    database_url: PostgresDsn = Field(env="DATABASE_URL")

    class Config:
        env_file = "../.env"

