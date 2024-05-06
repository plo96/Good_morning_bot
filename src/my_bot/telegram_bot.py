from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from src.project.config import settings
from handlers import router


async def init_bot():
	bot = Bot(token=settings.bot_token)
	await bot.delete_webhook(drop_pending_updates=True)
	
	dp = Dispatcher(storage=MemoryStorage())
	dp.include_router(router)
	
	await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
