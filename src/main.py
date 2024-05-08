import asyncio

from src.my_bot import init_bot


async def main():
	await init_bot()

if __name__ == "__main__":
	asyncio.run(main())
