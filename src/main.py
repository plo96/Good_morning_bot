import asyncio

from src.my_bot import init_bot

from src.project.logger import init_logger


async def main():
	await init_bot()

if __name__ == "__main__":
	asyncio.run(main())
