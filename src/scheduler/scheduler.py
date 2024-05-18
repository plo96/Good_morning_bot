"""
	Интерфейс для работы с задачами по расписанию.
"""
from abc import ABC
from logging import getLogger
from datetime import datetime

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from aiogram import Bot
from pytz import utc

from src.core.schemas import UserDTO
from src.scheduler.schedule_jobs import say_good_morning


class Scheduler(ABC):
	"""Абстрактный класс для управления задачами по расписанию"""
	_logger = getLogger('main.scheduler')
	_async_scheduler = AsyncIOScheduler(timezone=utc)
	
	@classmethod
	def add_new_good_morning_job(
			cls,
			bot: Bot,
			user: UserDTO,
	) -> str:
		"""
		Добавление в расписание новой задачи 'say_good_morning' для определённого пользователя.
		:param bot: Telegram бот, с которого будут отсылаться уведомления.
		:param user: Пользователь, для которого добавляется задача.
		:return: Строка с идентификатором job_id.
		"""
		today = datetime.today().date()
		actual_wake_up_time = (datetime(
			year=today.year,
			month=today.month,
			day=today.day,
			hour=user.wake_up_time.hour,
			minute=user.wake_up_time.minute,
		) - user.time_shift).time()
		
		job_id = user.job_id
		new_job = cls._async_scheduler.add_job(
			say_good_morning,
			id=job_id,
			trigger='cron',
			hour=actual_wake_up_time.hour,
			minute=actual_wake_up_time.minute,
			start_date=datetime.now(utc),
			kwargs={'bot': bot, 'user_id': user.id},
		)
		cls._logger.warning(f'new scheduler job for {user} added.')
		return new_job.id
	
	@classmethod
	def delete_job_for_user(
			cls,
			user: UserDTO,
	) -> None:
		"""
		Удаление из расписания задачи 'say_good_morning' для определённого пользователя.
		:param user: Пользователь, для которого удаляется задача.
		:return: None
		"""
		cls._async_scheduler.remove_job(job_id=user.job_id)
		cls._logger.warning(f'scheduler job for {user} removed.')

	@classmethod
	def start(cls):
		"""Запуск обработки задач по расписанию."""
		cls._async_scheduler.start()

	@classmethod
	def stop(cls):
		"""Остановка обработки задач по расписанию."""
		cls._async_scheduler.shutdown(wait=False)

	@classmethod
	def delete_all_jobs(cls):
		"""Удаление всех активных задач по расписанию."""
		cls._async_scheduler.remove_all_jobs()
