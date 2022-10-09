from typing import List, Optional
from stuart.serializers import StuartIn
from fastapi import FastAPI, Response, status
from stuart.core import get_event_source
from stuart.database import get_session
from stuart.models import Stuart
from stuart.serializers import StuartIn, StuartOut

api = FastAPI(title="stuart ")


@api.get("/stuart", response_model=List[StuartOut])
async def list_events(style: Optional[str] = None):
    """Stuart Couriers max Capacity (in liters)"""
    stuart = get_event_source(style)
    return stuart


@api.post("/stuart", response_model=StuartOut)
async def add_parameters(StuartIn: StuartIn, response: Response):
    stuart = stuart(**stuart_in.dict())
    with get_session() as session:
        session.add(stuart)
        session.commit()
        session.refresh(stuart)

    response.status_code = status.HTTP_201_CREATED
    return stuart
