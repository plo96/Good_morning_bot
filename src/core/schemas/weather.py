from dataclasses import dataclass
from datetime import time

from src.core.models import User


@dataclass
class WeatherDTO:
    time: time
    temperature: float
    feels_like: float
    humidity: int
    weather: list[str]
    wind: float
