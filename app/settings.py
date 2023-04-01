from dotenv import load_dotenv
from pydantic import BaseSettings, Field

load_dotenv(dotenv_path="../.env")


class Settings(BaseSettings):
    database_url: str = Field(env="DATABASE_URL")

    class Config:
        env_file = "../.env"

