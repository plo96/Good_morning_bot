from asyncio import sleep as asleep
from functools import wraps

from src.project.exceptions import OuterAPIExceptions

MAX_TRYING = 3


def multiply_trying(func):
	@wraps(func)
	async def wrapper(*args, **kwargs):
		for _ in range(MAX_TRYING):
			try:
				result = await func(*args, **kwargs)
				return result
			except OuterAPIExceptions as _ex:
				print(_ex)
				await asleep(2)
	
	return wrapper
