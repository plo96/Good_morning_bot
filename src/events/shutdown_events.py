from src.database import UserRepositoryMongo as UserRepository
from src.scheduler import SchedulerHelper


async def del_all_jobs_from_database() -> None:
	"""
	Удаление задач по расписанию для всех пользователей из базы данных.
	:return: None
	"""
	users = await UserRepository.select_all_users()
	for user in users:
		SchedulerHelper.del_async_schedule_job(
			user=user,
		)
		