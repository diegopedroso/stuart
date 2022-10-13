import warnings

from sqlalchemy.exc import SAWarning
from sqlmodel import Session, create_engine
from sqlmodel.sql.expression import Select, SelectOfScalar
from sqlmodel import Session, create_engine, select
from stuart.models import Stuart
from stuart import models
from stuart.config import settings

warnings.filterwarnings("ignore", category=SAWarning)
SelectOfScalar.inherit_cache = True
Select.inherit_cache = True

engine = create_engine(settings.database.url, echo=False)
models.SQLModel.metadata.create_all(engine)

def get_session():
    return Session(engine)

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