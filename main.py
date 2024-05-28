from logging import basicConfig, INFO
import asyncio

from src.telergam_bot import init_bot
from src.events import StartupEvents, ShutdownEvents


async def main():
	basicConfig(level=INFO)
	bot, dp = await init_bot()

	try:
		await StartupEvents.do_all_startup_events(bot=bot)
		await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
	finally:
		await ShutdownEvents.do_all_shutdown_events()
		await bot.session.close()


if __name__ == "__main__":
	asyncio.run(main())
