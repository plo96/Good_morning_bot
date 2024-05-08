from logging import getLogger, INFO

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from src.project.config import settings
from src.my_bot.handlers import router

logger = getLogger()
logger.setLevel(INFO)


async def start_bot(bot: Bot):
	await bot.send_message(
		settings.admin_id,
		text='Bot started.'
	)


async def stop_bot(bot: Bot):
	await bot.send_message(
		settings.admin_id,
		text='Bot stopped.'
	)


async def init_bot():
	bot = Bot(token=settings.bot_token)
	dp = Dispatcher(storage=MemoryStorage())
	dp.include_router(router)
	
	dp.startup.register(start_bot)
	dp.shutdown.register(stop_bot)
	
	try:
		await bot.delete_webhook(drop_pending_updates=True)
		await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
	finally:
		await bot.session.close()
		