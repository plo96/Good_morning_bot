from datetime import time, datetime

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from aiogram import Bot

from src.scheduler.schedule_jobs import say_good_morning

async_scheduler = AsyncIOScheduler(timezone="Europe/Moscow")


def add_new_async_schedule_job(
		bot: Bot,
		user_id: int,
		wake_up_time: time,
) -> str:
	new_job = async_scheduler.add_job(
		say_good_morning,
		trigger='cron',
		hour=wake_up_time.hour,
		minute=wake_up_time.minute,
		start_date=datetime.now(),
		kwargs={'bot': bot, 'user_id': user_id},
	)
	return new_job.id


def del_async_schedule_job(
		job_id: str,
):
	async_scheduler.remove_job(job_id=job_id)
