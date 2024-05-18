"""
	Модуль для работы с внешними API.
"""
__all__ = (
    "geoposition_worker",
    "gpt_worker",
    "timezone_worker",
    "weather_worker",
)

from . import geoposition_worker, gpt_worker, timezone_worker, weather_worker
