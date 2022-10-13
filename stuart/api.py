from typing import List, Optional
from stuart.serializers import StuartIn
from fastapi import FastAPI, Response, status
from stuart.core import get_event_source
from stuart.core import get_event_source_by_max_capacity
from stuart.database import get_session
from stuart.models import Stuart
from stuart.serializers import StuartIn, StuartOut
from fastapi.encoders import jsonable_encoder
from stuart.database import get_session, update_stuart

api = FastAPI(title="stuart")

@api.get("/capacity_required", response_model=List[StuartOut])
async def list_events(max_capacity: int, style: Optional[str] = None):
    """Stuart Couriers max Capacity (in liters)"""
    stuart = get_event_source_by_max_capacity(max_capacity)
    return stuart

@api.post("/stuart", response_model=StuartOut)
async def add_parameters(stuart_in: StuartIn, response: Response):
    stuart = Stuart(**stuart_in.dict())
    with get_session() as session:
        session.add(stuart)
        session.commit()
        session.refresh(stuart)

    response.status_code = status.HTTP_201_CREATED
    return stuart

@api.put("/update_capacity/{item_id}", response_model=StuartOut)
async def update_item(item_id: str, stuart_in: StuartIn, response: Response):
    stuart = update_stuart(item_id, stuart_in)
    response.status_code = status.HTTP_200_OK
    return stuart