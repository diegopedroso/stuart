from pickletools import int4
from typing import List, Optional
from sqlmodel import select
from stuart.database import get_session
from stuart.models import Stuart
from fastapi.encoders import jsonable_encoder
from sqlmodel import Session, create_engine, select
from stuart.models import Stuart

def add_event_source(
    max_capacity: int,

) -> bool:
    with get_session() as session:
        stuart = Stuart(**locals())
        session.add(stuart)
        session.commit()

    return True

def get_event_source(style: Optional[str] = None) -> List[Stuart]:
    with get_session() as session:
        sql = select(Stuart)
        if style:
            sql = sql.where(Stuart.style == style)
        return list(session.exec(sql))

def get_event_source_by_max_capacity(max_capacity, style: Optional[str] = None) -> Stuart:
    with get_session() as session:
        sql = select(Stuart)
        if (max_capacity):
            sql = sql.where(Stuart.max_capacity >= max_capacity)
        if style:
            sql = sql.where(Stuart.style == style)
        return list(session.exec(sql))

def update_stuart(id, stuart_in):
    stuart = Stuart(**stuart_in.dict())
    with get_session() as session:
        statement = select(Stuart).where(Stuart.id == id)
        results = session.exec(statement)
        _stuart = results.one()
        _stuart.max_capacity = stuart.max_capacity
        session.add(_stuart)
        session.commit()
        session.refresh(_stuart)
        return _stuart