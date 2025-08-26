from pydantic import BaseModel


class RateModel(BaseModel):
    currency: str
    rate: float
    source: str
    date: str
    created_at: str
