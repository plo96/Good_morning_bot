from dataclasses import dataclass
from datetime import time

from src.core.models import User


@dataclass
class UserDTO:
	_id: int
	name: str
	lat: float
	lon: float
	wake_up_time: time
	job_id: str
	
	@staticmethod
	def from_model(model: User):
		return UserDTO(
			_id=model.id,
			name=model.name,
			lat=model.lat,
			lon=model.lon,
			wake_up_time=model.wake_up_time,
			job_id=model.job_id,
		)
	