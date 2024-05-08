from logging import basicConfig, INFO
import asyncio

from src.telergam_bot import init_bot
from src.scheduler import async_scheduler


async def main():
	basicConfig(level=INFO)
	await async_scheduler.start()
	await init_bot()


if __name__ == "__main__":
	asyncio.run(main())
