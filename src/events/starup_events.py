from src.scheduler import SchedulerHelper
from aiogram import Bot

from src.outer_apis_workers import timezone_worker
from src.database import UserRepositoryMongo as UserRepository


async def add_all_jobs_from_database(
		bot: Bot,
) -> None:
	"""
	Добавление в расписание задач для всех пользователей из базы данных. Обновление данных по job_id в базе.
	:param bot: Telegram бот, с которого будут отсылаться уведомления.
	:return: None
	"""
	users = await UserRepository.select_all_users()
	for user in users:
		job_id = SchedulerHelper.add_new_async_schedule_job(
			bot=bot,
			user=user,
		)
		if user.job_id != job_id:
			await UserRepository.update_user(user_id=user.id, job_id=job_id)


async def refresh_all_time_shift() -> None:
	"""
	Обновление всех данных по сдвигу времени для всех пользователей
	(чтобы перезапуском бота можно было учитывать летнее время).
	:return: None
	"""
	users = await UserRepository.select_all_users()
	for user in users:
		time_shift = await timezone_worker.get_time_shift(
			latitude=user.city.lat,
			longitude=user.city.lon,
		)
		await UserRepository.update_user(user_id=user.id, time_shift=time_shift)
		