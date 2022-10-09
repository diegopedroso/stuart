from datetime import datetime

from fastapi import HTTPException, status
from pydantic import BaseModel, validator


class StuartOut(BaseModel):
    id: int
    max_capacity: int
    capacity_required: int
    date: datetime


class StuartIn(BaseModel):
    max_capacity: int
    capacity_required: int

    @validator("max_capacity")
    def validate_max_capacity(cls, v, field):
        if v < 0:
            raise HTTPException(
                detail=f"{field.name} must be > 0",
                status_code=status.HTTP_400_BAD_REQUEST,
            )
        return v

    @validator("capacity_required")
    def validate_capacity_required(cls, v, field):
        if v < 0:
            raise HTTPException(
                detail=f"{field.name} must be > 0",
                status_code=status.HTTP_400_BAD_REQUEST,
            )
        return v