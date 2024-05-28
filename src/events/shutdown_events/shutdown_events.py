"""
    Реализация класса, выполняющего задачи при выключении приложения.
"""
from src.database import UserRepositoryMongo as UserRepository
from src.scheduler import Scheduler

from src.events.shutdown_events.i_shutdown_events import IShutdownEvents


class ShutdownEvents(IShutdownEvents):

    @classmethod
    async def do_all_shutdown_events(
            cls,
    ):
        Scheduler.delete_all_jobs()
        Scheduler.stop()
        UserRepository.close_connection()
        