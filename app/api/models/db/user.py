from sqlalchemy import Column, String
from models.db.base import BaseModel


class User(BaseModel):
    __tablename__ = 'user'

    first_name = Column(String(length=255), nullable=False)
    last_name = Column(String(length=255), nullable=False)
    email = Column(String(length=255), nullable=False)
    phone_number = Column(String(length=12), nullable=False)
    password = Column(String(length=255), nullable=False)

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return f"{self.full_name}"
