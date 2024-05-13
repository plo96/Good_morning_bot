from datetime import datetime

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from aiogram import Bot

from src.core.schemas import UserDTO
from src.scheduler.schedule_jobs import say_good_morning
from src.database import UserRepositoryMongo as UserRepository


async_scheduler = AsyncIOScheduler(timezone="Europe/Moscow")


def add_new_async_schedule_job(
		bot: Bot,
		user: UserDTO,
) -> str:
	new_job = async_scheduler.add_job(
		say_good_morning,
		trigger='cron',
		hour=user.wake_up_time.hour,
		minute=user.wake_up_time.minute,
		start_date=datetime.now(),
		kwargs={'bot': bot, 'user_id': user.id},
	)
	return new_job.id


def del_async_schedule_job(
		job_id: str,
):
	async_scheduler.remove_job(job_id=job_id)


async def add_all_jobs_from_database(
		bot: Bot,
):
	users = await UserRepository.select_all_users()
	for user in users:
		job_id = add_new_async_schedule_job(
			bot=bot,
			user=user,
		)
		
		await UserRepository.update_user(user_id=user.id, job_id=job_id)
		
		
		
	
