from typing import Callable, Any, Awaitable, Dict

from aiogram import BaseMiddleware
from aiogram.types import CallbackQuery

from src.my_bot.keyboards import BotKeyboards


class ClearPreviousKeyboard(BaseMiddleware):
	async def __call__(
			self,
			handler: Callable[[CallbackQuery, Dict[str, Any]], Awaitable[Any]],
			event: CallbackQuery,
			data: Dict[str, Any],
	) -> Any:
		await event.message.edit_text(
			text=event.message.text,
			reply_markup=BotKeyboards.get_empty_kb(),
		)
		return await handler(event, data)
	
