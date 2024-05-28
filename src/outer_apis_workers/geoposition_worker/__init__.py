"""
    Взаимодействие с API геопозиционирования.
"""
__all__ = (
    "geoposition_worker",
)

from .openweathermap_geoposition_worker import openweathermap_geoposition_worker as geoposition_worker
