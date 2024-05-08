from datetime import time

from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from src.database.user_repository import UserRepository
from src.my_bot.texts import BotTexts
from src.my_bot import keyboards as kb
from src.my_bot.states import StepsForm

router = Router()


@router.message(Command("id"))
async def get_id(message: Message):
	await message.reply(
		text=str(message.from_user.id),
	)


@router.message(Command("start"))
async def start(message: Message, state: FSMContext):
	await state.clear()
	await message.answer(
		text=BotTexts.welcome_text(
			user_name=message.from_user.full_name,
		),
		reply_markup=kb.menu,
	)


@router.callback_query(F.data == "menu")
async def menu(
		callback: CallbackQuery,
		state: FSMContext
):
	await state.clear()
	await callback.message.edit_text(
		text=callback.message.text,
		reply_markup=kb.InlineKeyboardMarkup(inline_keyboard=[]),
	)
	await callback.message.answer(
		text='Выберите нужный пункт меню.',
		reply_markup=kb.menu,
	)


@router.callback_query(F.data == "delete")
async def delete_acceptance(
		callback: CallbackQuery,
	):
	user_id = callback.message.from_user.id
	user = await UserRepository.select_user(user_id=user_id)
	if not user:
		await callback.message.answer(
			text=BotTexts.user_not_found_text(),
			reply_markup=kb.menu,
		)
	else:
		await callback.message.answer(
			text=BotTexts.delete_acceptance_text(),
			reply_markup=kb.accept_del,
		)
	
		
@router.callback_query(F.data == "delete_yes")
async def delete_accept(
		callback: CallbackQuery,
	):
	user_id = callback.message.from_user.id				# TODO: Проверить чей id вылезет - бота или пользователя
	print(user_id)
	user = await UserRepository.select_user(user_id=user_id)
	await UserRepository.del_user(user)
	await callback.message.answer(
		text=BotTexts.success_delete_text(),
		reply_markup=kb.menu,
	)


@router.callback_query(F.data == "delete_no")
async def delete_confirm(
		callback: CallbackQuery,
	):
	await callback.message.answer(
		reply_markup=kb.menu,
	)


@router.callback_query(F.data == "config")
async def config_start(
	callback: CallbackQuery,
	state: FSMContext,
	):
	user_id = callback.message.from_user.id
	user = await UserRepository.select_user(user_id=user_id)
	if user:
		await callback.message.answer(
			text=BotTexts.config_already_exists()
		)
	else:
		await state.set_state(StepsForm.GET_HOUR)
		await callback.message.answer(
			text=BotTexts.config_start_text(),
			reply_markup=kb.InlineKeyboardMarkup(inline_keyboard=[])
		)
		await callback.message.answer(
			text=BotTexts.config_hours_text(),
			reply_markup=kb.hours_choose_kb,
		)
	
	
@router.callback_query((StepsForm.GET_HOUR and F.data.startswith("/hour_")))
async def config_minutes(
	callback: CallbackQuery,
	state: FSMContext,
):
	hour = callback.data.lstrip('/hour_')
	await state.set_state(StepsForm.GET_MINUTES)
	await callback.message.answer(
		text=BotTexts.config_minutes_text(),
		reply_markup=kb.get_minutes_choose_kb(hour=hour),
	)

	
@router.callback_query((StepsForm.GET_MINUTES and F.data.startswith("/time_")))
async def config_city(
	callback: CallbackQuery,
	state: FSMContext,
):
	hour, minutes = callback.data.split('_')[1: 3]
	await state.update_data(time=time(int(hour), int(minutes)))
	await state.set_state(StepsForm.GET_CITY)
	await callback.message.answer(
		text=BotTexts.config_city_text(),
		# reply_markup=kb.get_location_kb(),
	)


@router.message(StepsForm.GET_CITY)
async def config_city(
		message: Message,
		state: FSMContext,
):
	time = (await state.get_data())['time']
	await message.answer(
		text=f'Твоё время: {time}. Твой введённый город: {message.text}',
	)
