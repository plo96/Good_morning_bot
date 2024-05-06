"""
    ОРМ-модель User для пользователей
"""
from datetime import time

from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class User(Base):
	"""ОРМ-класс с декларативным объявлением с помощью SQLAlchemy для пользователей"""
	__tablename__ = 'users'
	
	id: Mapped[int] = mapped_column(
		primary_key=True,
	)
	chat_id: Mapped[int]
	name: Mapped[str]
	lat: Mapped[float]
	lon: Mapped[float]
	wake_up_time: Mapped[time]
