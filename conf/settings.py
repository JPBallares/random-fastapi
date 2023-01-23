from pydantic import BaseSettings


class Settings(BaseSettings):
    split_key: str = "localhost"

    class Config:
        env_file = ".env"
