from pickletools import int4
from typing import List, Optional

from sqlmodel import select

from stuart.database import get_session
from stuart.models import Stuart


def add_event_source(
    max_capacity: int,
    capacity_required: int,


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