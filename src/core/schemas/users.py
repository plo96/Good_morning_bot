from dataclasses import dataclass
from datetime import time
from typing import Optional
from uuid import UUID

from src.core.models import User


@dataclass
class UserDTO:
	id: Optional[UUID]
	name: str
	city: str
	wake_up_time: time
	
	@staticmethod
	def from_model(model: User):
		return UserDTO(
			id=model.id,
			name=model.name,
			city=model.city,
			wake_up_time=model.wake_up_time,
		)
	