from datetime import time, datetime

from apscheduler.schedulers.asyncio import AsyncIOScheduler
# from apscheduler.jobstores.redis import RedisJobStore
# from apscheduler_di import ContextSchedulerDecorator
from aiogram import Bot

from src.scheduler.schedule_jobs import say_good_morning

# job_store = {
# 	'default': RedisJobStore(
# 		jobs_key='dispatched_trips_jobs',
# 		from_times_key=' dispatched_trips_running',
# 		host='localhost',
# 		db=2,
# 		port=6379,
# 	)
# }

# async_scheduler = ContextSchedulerDecorator(AsyncIOScheduler(timezone="Europe/Moscow", jobstores=job_store))
async_scheduler = AsyncIOScheduler(timezone="Europe/Moscow")


def add_new_async_schedule_job(
		bot: Bot,
		user_id: int,
		wake_up_time: time,
):
	async_scheduler.add_job(
		say_good_morning,
		trigger='cron',
		hour=wake_up_time.hour,
		minute=wake_up_time.minute,
		start_date=datetime.now,
		kwargs={'bot': bot, 'user_id': user_id},
	)


def del_async_schedule_job():
	...
