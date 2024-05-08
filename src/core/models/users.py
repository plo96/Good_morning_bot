"""
    ОРМ-модель User для пользователей
"""
from datetime import time
from enum import Enum

from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class Sex(Enum):
	male = "male"
	female = "female"


class User(Base):
	"""ОРМ-класс с декларативным объявлением с помощью SQLAlchemy для пользователей"""
	__tablename__ = 'users'
	
	id: Mapped[int] = mapped_column(
		primary_key=True,
	)
	name: Mapped[str]
	lat: Mapped[float]
	lon: Mapped[float]
	sex: Mapped[Sex]
	wake_up_time: Mapped[time]
