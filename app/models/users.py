import uuid
from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import TIMESTAMP
from sqlalchemy.orm import relationship
from sqlalchemy.sql import expression
from sqlalchemy_utils import EmailType, PhoneNumberType, PasswordType

from app.config.database import Base
from .base import BaseMixin


class User(Base, BaseMixin):
    __tablename__ = 'users'

    id = Column(String(36), primary_key=True, default=str(uuid.uuid4()))
    first_name = Column(String(50))
    last_name = Column(String(50))
    image = Column(String(255))
    email = Column(EmailType, unique=True, nullable=False)
    phone_number = Column(PhoneNumberType, unique=True, nullable=False)
    auth_type = Column(String(10), default='email')
    password = Column(PasswordType(
        schemes=[
            'pbkdf2_sha512',
            'md5_crypt'
        ],
        deprecated=['md5_crypt']
    ), nullable=False)

    credit_cards = relationship("CreditCard", back_populates="user")
