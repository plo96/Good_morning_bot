"""
	Интерфейс для работы с задачами по расписанию.
"""
from abc import ABC
from logging import getLogger
from datetime import datetime

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from aiogram import Bot

from src.core.schemas import UserDTO
from src.scheduler.schedule_jobs import say_good_morning
from src.database import UserRepositoryMongo as UserRepository


class SchedulerHelper(ABC):
	"""Абстрактный класс для управления задачами по расписанию"""
	_logger = getLogger('main.scheduler')
	_async_scheduler = AsyncIOScheduler(timezone="Europe/Moscow")
	
	@classmethod
	def add_new_async_schedule_job(
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
		job_id = user.job_id
		new_job = cls._async_scheduler.add_job(
			say_good_morning,
			id=job_id,
			trigger='cron',
			hour=user.wake_up_time.hour,
			minute=user.wake_up_time.minute,
			start_date=datetime.now(),
			kwargs={'bot': bot, 'user_id': user.id},
		)
		cls._logger.warning(f'new scheduler job for {user} added.')
		return new_job.id
	
	@classmethod
	def del_async_schedule_job(
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
	async def add_all_jobs_from_database(
			cls,
			bot: Bot,
	) -> None:
		"""
		Добавление в расписание задач для всех пользователей из базы данных. Обновление данных по job_id в базе.
		:param bot: Telegram бот, с которого будут отсылаться уведомления.
		:return: None
		"""
		users = await UserRepository.select_all_users()
		for user in users:
			job_id = cls.add_new_async_schedule_job(
				bot=bot,
				user=user,
			)
			
			await UserRepository.update_user(user_id=user.id, job_id=job_id)
		
	@classmethod
	def start_scheduler(cls):
		"""Запуск обработки задач по расписанию."""
		cls._async_scheduler.start()
