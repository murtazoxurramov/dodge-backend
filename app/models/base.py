import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime


class BaseMixin:
    id = Column(String(36), primary_key=True, default=str(uuid.uuid4()))

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow,
                        onupdate=datetime.utcnow)
