from functools import lru_cache
from fastapi import FastAPI, Depends
from faker import Faker

from conf.settings import Settings
from core.split import SplitSDK

app = FastAPI()
fake = Faker()


@lru_cache()
def get_settings():
    return Settings()


@app.get("/user/random")
async def generate_user(settings: Settings = Depends(get_settings)):
    email = fake.email()
    full_name = fake.name()

    return {
        "email": email,
        "full_name": full_name,
    }
