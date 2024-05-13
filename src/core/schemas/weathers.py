"""
	Схемы для работы с сущностями погоды.
"""
from dataclasses import dataclass
from datetime import time


@dataclass
class WeatherDTO:
    """
    Класс для описания состояния погоды.
    """
    time: time
    temperature: float
    feels_like: float
    humidity: int
    weather_type: list[str]
    wind: float
