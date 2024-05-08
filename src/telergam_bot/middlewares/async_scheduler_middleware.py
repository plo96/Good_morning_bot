# from typing import Callable, Any, Awaitable, Dict
#
# from aiogram import BaseMiddleware
# from aiogram.types import TelegramObject
# from apscheduler.schedulers.asyncio import AsyncIOScheduler
#
#
# class AsyncSchedulerMiddleware(BaseMiddleware):
# 	def __init__(self, async_scheduler: AsyncIOScheduler):
# 		self.async_scheduler = async_scheduler
#
# 	async def __call__(
# 			self,
# 			handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
# 			event: TelegramObject,
# 			data: Dict[str, Any],
# 	) -> Any:
# 		data['async_scheduler'] = self.async_scheduler
# 		return await handler(event, data)
#
