from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand, BotCommandScopeDefault
from aiogram.fsm.storage.redis import RedisStorage

from src.project.config import settings
from src.my_bot.handlers import router
from src.my_bot.middlewares import ClearPreviousKeyboard


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
	
	storage = RedisStorage.from_url(settings.redis_url)
	
	dp = Dispatcher(storage=storage)
	
	dp.include_router(router)
	
	dp.startup.register(start_bot)
	dp.shutdown.register(stop_bot)
	
	dp.callback_query.middleware.register(ClearPreviousKeyboard())
	
	try:
		await bot.set_my_commands(
			[
				BotCommand(
					command='start',
					description='Приветственное сообщение.'
				),
				BotCommand(
					command='menu',
					description='Вызов меню.'
				)
			],
			BotCommandScopeDefault(),
		)
		await bot.delete_webhook(drop_pending_updates=True)
		await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
	finally:
		await bot.session.close()
