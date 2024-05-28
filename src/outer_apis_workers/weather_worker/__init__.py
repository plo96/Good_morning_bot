"""
    Взаимодействие с API сервиса прогноза погоды.
"""
__all__ = (
    "weather_worker",
)

from .openweathermap_weather_worker import openweathermap_weather_worker as weather_worker
