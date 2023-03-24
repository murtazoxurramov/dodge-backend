from sqlalchemy import Column, DateTime, func, BigInteger
from sqlalchemy.orm import declarative_base


Base = declarative_base()
metadata = Base.metadata


class BaseModel(Base):
    __abstract__ = True

    id = Column(BigInteger, nullable=False,
                autoincrement=True, primary_key=True)

    created_at = Column(DateTime(True), server_default=func.now())
    updaed_at = Column(DateTime(True), server_default=func.now(),
                       onupdate=func.now(), default=func.now())
