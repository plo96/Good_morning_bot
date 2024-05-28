"""
    Интерфейс для класса, выполняющего задачи при выключении приложения.
"""
from abc import ABC, abstractmethod


class IShutdownEvents(ABC):

    @classmethod
    @abstractmethod
    async def do_all_shutdown_events(cls, **kwargs):
        pass
