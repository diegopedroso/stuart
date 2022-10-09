from datetime import datetime
from statistics import mean
from typing import Optional

from pydantic import validator
from sqlmodel import Field, SQLModel


class Stuart(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True, default=None, index=True)
    max_capacity: int
    capacity_required: int
    date: datetime = Field(default_factory=datetime.now)

    @validator("max_capacity")
    def validate_max_capacity(cls, v, field):
        if v < 0:
            raise RuntimeError(f"{field.name} must be > 0 value")
        return v

    @validator("capacity_required")
    def validate_capacity_required(cls, v, field):
        if v < 0:
            raise RuntimeError(f"{field.name} must be > 0 value")
        return v