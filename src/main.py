from logging import basicConfig, INFO
import asyncio

from src.project.logger import init_logger
from src.telergam_bot import init_bot
from src.scheduler import SchedulerHelper
from src.events import starup_events, shutdown_events


async def main():
	basicConfig(level=INFO)
	SchedulerHelper.start_scheduler()
	bot, dp = await init_bot()
	logger = init_logger(name='main', bot=bot)
	try:
		await starup_events.refresh_all_time_shift()
		await starup_events.add_all_jobs_from_database(bot=bot)
		logger.info('startup tasks done.')
		await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
	finally:
		await shutdown_events.del_all_jobs_from_database()
		await bot.session.close()


if __name__ == "__main__":
	asyncio.run(main())
