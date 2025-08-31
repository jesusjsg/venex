from typing import Optional
import uuid

from sqlmodel import Field, SQLModel
from datetime import datetime, date


class RateBase(SQLModel):
    currency: str
    rate: float
    source: str
    date: date


class RateCreate(RateBase):
    pass  # don't need to pass the id and created_at fields


class Rate(RateBase, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    created_at: Optional[datetime] = None  # This field is auto-filled by Supabase


class RatePublic(RateBase):
    id: uuid.UUID
