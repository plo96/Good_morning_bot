"""
	'Сборка' и инициализация бота, а также все сопутствующие действия.
"""
from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand, BotCommandScopeDefault
from aiogram.fsm.storage.redis import RedisStorage

from src.project import settings
from src.telergam_bot.handlers import router
from src.telergam_bot.middlewares import ClearPreviousKeyboard, LoggingUserDeal


async def start_bot(bot: Bot):
	"""Выполнение команд сразу после запуска бота."""
	await bot.send_message(
		settings.admin_id,
		text='Bot started.'
	)


async def stop_bot(bot: Bot):
	"""Выполнение команд непосредственно перед остановкой бота."""
	await bot.send_message(
		settings.admin_id,
		text='Bot stopped.'
	)


async def init_bot() -> tuple[Bot, Dispatcher]:
	"""
	Инициализация бота. Регистрация startup- и shutdown- функций, middleware и router, а также установка комманд.
	Запуск функции для добавления в задачи по расписанию оповещений для всех пользователей из базы данных.
	В качестве хранилища данных используется Redis.
	:return: Bot - экзмепляр класса бота, Dispatcher - диспетчер для отслеживания событий данного бота.
	"""
	bot = Bot(token=settings.bot_token)
	await bot.set_my_commands(
		[
			BotCommand(
				command='start',
				description='Приветственное сообщение.',
			),
			BotCommand(
				command='menu',
				description='Вызов меню.',
			)
		],
		BotCommandScopeDefault(),
	)
	
	storage = RedisStorage.from_url(settings.redis_url)
	
	dp = Dispatcher(storage=storage)
	
	dp.include_router(router)
	dp.startup.register(start_bot)
	dp.shutdown.register(stop_bot)
	dp.callback_query.middleware.register(ClearPreviousKeyboard())
	dp.callback_query.middleware.register(LoggingUserDeal())
	
	await bot.delete_webhook(drop_pending_updates=True)
	
	return bot, dp
