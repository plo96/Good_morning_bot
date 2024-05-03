"""
    ОРМ-модель User для пользователей
"""
from datetime import time
from uuid import UUID, uuid4

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Uuid

from .base import Base


class User(Base):
	"""ОРМ-класс с декларативным объявлением с помощью SQLAlchemy для пользователей"""
	__tablename__ = 'users'
	
	id: Mapped[UUID] = mapped_column(
		Uuid,
		primary_key=True,
		default=uuid4,
	)
	name: Mapped[str]
	city: Mapped[str]
	wake_up_time: Mapped[time]
