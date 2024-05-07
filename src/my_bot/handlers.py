from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command

from src.database.user_repository import UserRepository
from src.my_bot.texts import BotTexts
from src.my_bot.keyboard import kb

router = Router()


@router.message(Command("start"))
async def echo_message(message: Message):
	await message.answer(
		text=BotTexts.welcome_text(
			user_name=message.from_user.name,
		),
		reply_markup=kb,
	)


@router.message(Command("config"))
async def echo_message(message: Message):
	user_id = message.from_user.id
	user = await UserRepository.select_user(user_id=user_id)
	if user:
		await message.answer(
			text=BotTexts.config_already_exists()
		)
	else:
		...
		user = await UserRepository.add_user(new_user_dict=...)


@router.message(Command("config"))
async def echo_message(message: Message):
	user_id = message.from_user.id
	user = await UserRepository.select_user(user_id=user_id)
	if user:
		await message.answer(
			text=BotTexts.config_already_exists()
		)
	else:
		...
		user = await UserRepository.add_user(new_user_dict=...)


