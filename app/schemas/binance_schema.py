from datetime import date
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class BinanceSchema(BaseModel):
    currency: str
    rate: float
    source: str
    date: date
