"""
    Взаимодействие с API сервиса определения часового пояса по координатам.
"""
__all__ = (
    "timezone_worker",
)

from .timeapi_timezone_worker import timeapi_timezone_worker as timezone_worker
