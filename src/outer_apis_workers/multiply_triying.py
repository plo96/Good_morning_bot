"""
	Общий для работы со всеми внешними API декоратор для повторного запроса при неудаче.
"""
from logging import getLogger
from asyncio import sleep as asleep
from functools import wraps

from src.project.exceptions import OuterAPIExceptions

MAX_TRYING = 3

logger = getLogger('main.outer_apis_workers')


def multiply_trying(func):
	"""Обеспечивает повторный запрос к внешнему API в случае неудачи. Повторяется до MAX_TRYING раз."""
	@wraps(func)
	async def wrapper(*args, **kwargs):
		for trying in range(MAX_TRYING):
			try:
				logger.info(f"{func}: trying №{trying} - started with {args=} {kwargs=}.")
				result = await func(*args, **kwargs)
				logger.info(f"{func}: trying №{trying} - return {result=}.")
				return result
			except OuterAPIExceptions as _ex:
				logger.info(f"{func}: trying №{trying} - OuterAPIExceptions. Retrying...")
				await asleep(2)
		logger.warning(f"{func}: Max trying. OuterAPIExceptions.")
		
	return wrapper
