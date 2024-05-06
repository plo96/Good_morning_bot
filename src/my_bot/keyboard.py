from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

menu = [
	[InlineKeyboardButton(text="Удалить пользователя", callback_data="/delete"),
	 InlineKeyboardButton(text="Настроить пользователя", callback_data="/config")],
]

kb = InlineKeyboardMarkup(inline_keyboard=menu)
