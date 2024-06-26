from typing import Callable, Any, Awaitable, Dict

from aiogram import BaseMiddleware
from aiogram.types import CallbackQuery


class ClearPreviousKeyboard(BaseMiddleware):
	"""
	Middleware для очистки любой inline-клавиатуры при нажатии на ней некоторой кнопки.
	"""
	async def __call__(
			self,
			handler: Callable[[CallbackQuery, Dict[str, Any]], Awaitable[Any]],
			event: CallbackQuery,
			data: Dict[str, Any],
	) -> Any:
		await event.message.edit_reply_markup(None)
		return await handler(event, data)
	