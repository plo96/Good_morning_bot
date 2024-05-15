from logging import basicConfig, INFO
import asyncio

from src.project.logger import init_logger
from src.telergam_bot import init_bot
from src.scheduler import SchedulerHelper


async def main():
	basicConfig(level=INFO)
	SchedulerHelper.start_scheduler()
	bot, dp = await init_bot()
	logger = init_logger(name='main', bot=bot)
	try:
		await SchedulerHelper.add_all_jobs_from_database(bot=bot)
		logger.info('Previous tasks running.')
		await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
	finally:
		await bot.session.close()


if __name__ == "__main__":
	asyncio.run(main())
