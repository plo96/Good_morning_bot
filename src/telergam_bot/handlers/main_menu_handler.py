from aiogram import Router, Bot
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.exceptions import TelegramBadRequest

from src.telergam_bot.utils import BotTexts
from src.telergam_bot.keyboards import BotKeyboards

router = Router()


@router.message(Command("start"))
async def start(
		message: Message,
):
	await message.answer(
		text=BotTexts.welcome_text(
			user_name=message.from_user.first_name,
		),
	)


@router.message(Command("menu"))
async def menu(
		message: Message,
		bot: Bot,
		state: FSMContext
):
	state_data = await state.get_data()
	if 'last_kb' in state_data.keys():
		last_kb = (await state.get_data()).__getitem__('last_kb')
		if last_kb:
			try:
				await bot.edit_message_reply_markup(chat_id=message.chat.id, message_id=last_kb, reply_markup=None)
			except TelegramBadRequest:
				pass
	await state.clear()
	new_message = await message.answer(
		text=BotTexts.menu_text(),
		reply_markup=BotKeyboards.get_menu_kb(),
	)
	await state.update_data(last_kb=new_message.message_id)

