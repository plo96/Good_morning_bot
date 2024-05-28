"""
    Реализация класса, выполняющего задачи при запуске приложения.
"""
from src.scheduler import Scheduler
from aiogram import Bot

from src.outer_apis_workers.timezone_worker import timezone_worker, ITimezoneWorker
from src.database import UserRepositoryMongo as UserRepository
from src.events.startup_events.i_startup_events import IStartupEvents
from src.project.logger import init_logger


class StartupEvents(IStartupEvents):
    _timezone_worker: ITimezoneWorker = timezone_worker

    @classmethod
    async def do_all_startup_events(
            cls,
            bot: Bot,
    ):
        init_logger(name='main', bot=bot)
        Scheduler.start()
        await cls._refresh_all_time_shift()
        await cls._add_all_jobs_from_database(bot=bot)

    @classmethod
    async def _add_all_jobs_from_database(
            cls,
            bot: Bot,
    ) -> None:
        """
		Добавление в расписание задач для всех пользователей из базы данных. Обновление данных по job_id в базе.
		:param bot: Telegram бот, с которого будут отсылаться уведомления (Экземпляр класса Bot библиотеки aiogram).
		"""
        users = await UserRepository.select_all_users()
        for user in users:
            job_id = Scheduler.add_new_good_morning_job(
                bot=bot,
                user=user,
            )
            if user.job_id != job_id:
                await UserRepository.update_user(user_id=user.id, job_id=job_id)

    @classmethod
    async def _refresh_all_time_shift(cls) -> None:
        """
		Обновление данных в БД по текущему сдвигу времени для всех пользователей (для учёта зимнего времени).
		"""
        users = await UserRepository.select_all_users()
        for user in users:
            time_shift = await cls._timezone_worker.get_time_shift(
                latitude=user.city.lat,
                longitude=user.city.lon,
            )
            await UserRepository.update_user(user_id=user.id, time_shift=time_shift.seconds)
