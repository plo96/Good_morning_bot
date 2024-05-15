from logging import Logger, getLogger

from typing import Callable, Any, Awaitable, Dict

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject


class LoggingUserDeal(BaseMiddleware):
	def __init__(self, logger: Logger = getLogger('main.middleware_logger')):
		self.logger = logger
	
	async def __call__(
			self,
			handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
			event: TelegramObject,
			data: Dict[str, Any],
	) -> Any:
		self.logger.info(event)
		return await handler(event, data)
