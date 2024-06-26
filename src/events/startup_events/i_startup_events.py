"""
    Интерфейс для класса, выполняющего задачи при запуске приложения.
"""
from abc import ABC, abstractmethod


class IStartupEvents(ABC):

    @classmethod
    @abstractmethod
    async def do_all_startup_events(cls, **kwargs):
        pass
