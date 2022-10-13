from datetime import datetime

from fastapi import HTTPException, status
from pydantic import BaseModel, validator


class StuartOut(BaseModel):
    id: int
    max_capacity: int
    date: datetime

class StuartIn(BaseModel):
    max_capacity: int

    @validator("max_capacity")
    def validate_max_capacity(cls, v, field):
        if v < 0:
            raise HTTPException(
                detail=f"{field.name} must be > 0",
                status_code=status.HTTP_400_BAD_REQUEST,
            )
        return v