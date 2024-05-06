from dataclasses import dataclass
from datetime import time


@dataclass
class WeatherDTO:
    time: time
    temperature: float
    feels_like: float
    humidity: int
    weather_type: list[str]
    wind: float
