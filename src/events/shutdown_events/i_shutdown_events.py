from abc import ABC, abstractmethod


class IShutdownEvents(ABC):

    @classmethod
    @abstractmethod
    async def do_all_shutdown_events(cls, **kwargs):
        pass
