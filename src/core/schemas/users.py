from dataclasses import dataclass
from datetime import time
from typing import Optional, Type
from uuid import UUID

from src.core.models import User


@dataclass
class UserDTO:
	id: int
	chat_id: int
	name: str
	lat: float
	lon: float
	wake_up_time: time
	
	@staticmethod
	def from_model(model: User):
		return UserDTO(
			id=model.id,
			chat_id=model.chat_id,
			name=model.name,
			lat=model.lat,
			lon=model.lon,
			wake_up_time=model.wake_up_time,
		)
	