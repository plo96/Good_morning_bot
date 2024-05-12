from datetime import time

from aiogram import Router, F, Bot
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.exceptions import TelegramBadRequest

from src.core.schemas import CityDTO, UserDTO
from src.telergam_bot.utils import BotTexts, StepsForm
from src.telergam_bot.keyboards import BotKeyboards
from src.database.user_repository_mongo import UserRepositoryMongo as UserRepository
from src.outer_apis_workers import geoposition_worker
from src.project import settings
from src.scheduler import add_new_async_schedule_job, del_async_schedule_job

router = Router()


@router.callback_query(F.data == "config")
async def config_start(
		callback: CallbackQuery,
		state: FSMContext,
):
	user_id = callback.message.from_user.id
	user = await UserRepository.select_user(user_id=user_id)
	if user:
		await callback.message.answer(
			text=BotTexts.config_already_exists(),
			reply_markup=BotKeyboards.get_menu_kb(),
		)
	else:
		await state.set_state(StepsForm.GET_HOUR)
		await callback.message.answer(
			text=BotTexts.config_start_text(),
		)
		await callback.message.answer(
			text=BotTexts.config_hours_text(),
			reply_markup=BotKeyboards.get_hours_choose_kb(),
		)


@router.callback_query(StepsForm.GET_HOUR and F.data.startswith("/hour_"))
async def config_minutes(
		callback: CallbackQuery,
		state: FSMContext,
):
	hour = callback.data.lstrip('/hour_')
	await state.set_state(StepsForm.GET_MINUTES)
	await callback.message.answer(
		text=BotTexts.config_minutes_text(),
		reply_markup=BotKeyboards.get_minutes_choose_kb(hour=hour),
	)


@router.callback_query(StepsForm.GET_MINUTES and F.data.startswith("/time_"))
async def config_city(
		callback: CallbackQuery,
		state: FSMContext,
):
	hour, minutes = callback.data.split('_')[1: 3]
	await state.update_data(time=time(int(hour), int(minutes)))
	await state.set_state(StepsForm.GET_CITY)
	await callback.message.answer(
		text=BotTexts.config_city_text(),
	)


@router.message(StepsForm.GET_CITY)
async def config_city(
		message: Message,
		state: FSMContext,
):
	user_city = message.text
	list_of_cities = await geoposition_worker.get_list_of_cities(city_name=user_city)
	if not list_of_cities:
		await message.answer(
			text=BotTexts.config_wrong_city_text(),
		)
	else:
		await state.set_state(StepsForm.CHOOSE_CITY)
		await state.update_data(list_of_cities=list_of_cities)
		await state.update_data(current_city_index=0)
		probable_city = list_of_cities[0]
		await message.answer(
			text=BotTexts.config_choose_city_text(city=probable_city),
			reply_markup=BotKeyboards.get_accept_kb(),
		)


@router.callback_query(StepsForm.CHOOSE_CITY and F.data in ('yes', 'no'))
async def choose_city(
		callback: CallbackQuery,
		state: FSMContext,
):
	current_city_index = (await state.get_data())['current_city_index']
	list_of_cities = (await state.get_data())['list_of_cities']
	if F.data == 'no':
		current_city_index += 1
		if current_city_index == len(list_of_cities):
			await callback.message.answer(
				text=BotTexts.config_wrong_city_text(),
			)
		else:
			await state.update_data(current_city_index=current_city_index)
			probable_city = list_of_cities[current_city_index]
			await callback.message.answer(
				text=BotTexts.config_choose_city_text(city=probable_city),
				reply_markup=BotKeyboards.get_accept_kb(),
			)
	elif F.data == 'yes':
		await state.set_state(StepsForm.CHOOSE_SEX)
		city = list_of_cities[current_city_index]
		await state.update_data(lat=city.lat, lon=city.lon)
		await callback.message.answer(
			text=BotTexts.config_choose_sex_text(),
			reply_markup=BotKeyboards.get_choose_sex_kb(),
		)


@router.callback_query(StepsForm.CHOOSE_SEX and F.data in ('male', 'female'))
async def choose_sex(
		bot: Bot,
		callback: CallbackQuery,
		state: FSMContext,
):
	users_now = await UserRepository.count_users()
	if users_now >= settings.max_number_of_users:
		await state.clear()
		await callback.message.answer(
			text=BotTexts.a_lot_of_users_text(),
			reply_markup=BotKeyboards.get_menu_kb(),
		)
	else:
		user_data: dict = await state.get_data()
		new_user = User(
			id=callback.message.from_user.id,
			name=callback.message.from_user.first_name,
			lat=user_data.__getitem__('lat'),
			lon=user_data.__getitem__('lon'),
			sex=F.data,
			wake_up_time=user_data.__getitem__('time'),
		)
		await UserRepository.add_user(new_user=new_user)
		
		add_new_async_schedule_job(
			bot=bot,
			user_id=new_user.id,
			wake_up_time=new_user.wake_up_time,
		)
		
		await state.clear()
		await callback.message.answer(
			text=BotTexts.config_done_text(wake_up_time=user_data.__getitem__('time')),
			reply_markup=BotKeyboards.get_menu_kb(),
		)
