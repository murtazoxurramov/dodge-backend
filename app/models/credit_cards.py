from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

from app.config.database import Base
from .base import BaseMixin


class CreditCard(Base, BaseMixin):
    __tablename__ = 'credit_cards'

    card_number = Column(String(16), nullable=False)
    expiration_month = Column(String(2), nullable=False)
    expiration_year = Column(String(4), nullable=False)
    user_id = Column(String(36), ForeignKey('users.id'))
    user = relationship("User", back_populates="credit_cards")
