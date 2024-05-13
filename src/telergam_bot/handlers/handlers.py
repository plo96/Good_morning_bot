# from datetime import time
#
# from aiogram import Router, F, Bot
# from aiogram.types import Message, CallbackQuery
# from aiogram.filters import Command, StateFilter
# from aiogram.fsm.context import FSMContext
# from aiogram.exceptions import TelegramBadRequest
#
# from src.core.schemas import CityDTO, UserDTO
# from src.telergam_bot.utils import BotTexts, StepsForm
# from src.telergam_bot.keyboards import BotKeyboards
# from src.database.user_repository_mongo import UserRepositoryMongo as UserRepository
# from src.outer_apis_workers import geoposition_worker
# from src.project import settings
# from src.scheduler import add_new_async_schedule_job, del_async_schedule_job
#
# router = Router()
#
#
# @router.message(Command("start"))
# async def start(
# 		message: Message,
# ):
# 	await message.answer(
# 		text=BotTexts.welcome_text(
# 			user_name=message.from_user.first_name,
# 		),
# 	)
#
#
# @router.message(Command("menu"))
# async def menu(
# 		message: Message,
# 		bot: Bot,
# 		state: FSMContext
# ):
# 	state_data = await state.get_data()
# 	if 'last_kb' in state_data.keys():
# 		last_kb = (await state.get_data()).__getitem__('last_kb')
# 		if last_kb:
# 			try:
# 				await bot.edit_message_reply_markup(chat_id=message.chat.id, message_id=last_kb, reply_markup=None)
# 			except TelegramBadRequest:
# 				pass
# 	await state.clear()
# 	new_message = await message.answer(
# 		text=BotTexts.menu_text(),
# 		reply_markup=BotKeyboards.get_menu_kb(),
# 	)
# 	await state.update_data(last_kb=new_message.message_id)
#
#
# @router.callback_query(F.data == "delete")
# async def delete_acceptance(
# 		callback: CallbackQuery,
# 		state: FSMContext,
# ):
# 	user_id = callback.from_user.id
# 	user = await UserRepository.select_user(user_id=user_id)
#
# 	if not user:
# 		new_message = await callback.message.answer(
# 			text=BotTexts.user_not_found_text(),
# 			reply_markup=BotKeyboards.get_menu_kb(),
# 		)
# 	else:
# 		await state.set_state(StepsForm.DELETION_ACCEPT)
# 		new_message = await callback.message.answer(
# 			text=BotTexts.delete_acceptance_text(),
# 			reply_markup=BotKeyboards.get_accept_kb(),
# 		)
#
# 	await state.update_data(last_kb=new_message.message_id)
#
#
# @router.callback_query(StateFilter(StepsForm.DELETION_ACCEPT), F.data == "yes")
# async def delete_accept(
# 		callback: CallbackQuery,
# 		state: FSMContext,
# ):
# 	user_id = callback.from_user.id
# 	user = await UserRepository.select_user(user_id=user_id)
# 	job_id = user.job_id
# 	await UserRepository.del_user(user_id=user_id)
# 	del_async_schedule_job(job_id)
# 	await state.clear()
# 	new_message = await callback.message.answer(
# 		text=BotTexts.success_delete_text(),
# 		reply_markup=BotKeyboards.get_menu_kb(),
# 	)
# 	await state.update_data(last_kb=new_message.message_id)
#
#
# @router.callback_query(StateFilter(StepsForm.DELETION_ACCEPT), F.data == "no")
# async def delete_confirm(
# 		callback: CallbackQuery,
# 		state: FSMContext,
# ):
# 	await state.clear()
# 	new_message = await callback.message.answer(
# 		text=BotTexts.menu_text(),
# 		reply_markup=BotKeyboards.get_menu_kb(),
# 	)
# 	await state.update_data(last_kb=new_message.message_id)
#
#
# @router.callback_query(F.data == "config")
# async def config_start(
# 		callback: CallbackQuery,
# 		state: FSMContext,
# ):
# 	user_id = callback.from_user.id
# 	user = await UserRepository.select_user(user_id=user_id)
# 	if user:
# 		new_message = await callback.message.answer(
# 			text=BotTexts.config_already_exists(),
# 			reply_markup=BotKeyboards.get_menu_kb(),
# 		)
# 	else:
# 		await state.set_state(StepsForm.GET_HOUR)
# 		await callback.message.answer(
# 			text=BotTexts.config_start_text(),
# 		)
# 		new_message = await callback.message.answer(
# 			text=BotTexts.config_hours_text(),
# 			reply_markup=BotKeyboards.get_hours_choose_kb(),
# 		)
#
# 	await state.update_data(last_kb=new_message.message_id)
#
#
# @router.callback_query(StateFilter(StepsForm.GET_HOUR), F.data.startswith("/hour_"))
# async def config_minutes(
# 		callback: CallbackQuery,
# 		state: FSMContext,
# ):
# 	hour = callback.data.lstrip('/hour_')
# 	await state.set_state(StepsForm.GET_MINUTES)
# 	await callback.message.answer(
# 		text=BotTexts.config_hours_accept_text(hour=hour),
# 	)
# 	new_message = await callback.message.answer(
# 		text=BotTexts.config_minutes_text(),
# 		reply_markup=BotKeyboards.get_minutes_choose_kb(hour=hour),
# 	)
# 	await state.update_data(last_kb=new_message.message_id)
#
#
# @router.callback_query(StateFilter(StepsForm.GET_MINUTES), F.data.startswith("/time_"))
# async def config_city(
# 		callback: CallbackQuery,
# 		state: FSMContext,
# ):
# 	hour, minutes = callback.data.split('_')[1: 3]
# 	await state.update_data(time=time(int(hour), int(minutes)).isoformat())
# 	await state.set_state(StepsForm.GET_CITY)
# 	await callback.message.answer(
# 		text=BotTexts.config_time_accept_text(hour=hour, minutes=minutes),
# 	)
# 	await callback.message.answer(
# 		text=BotTexts.config_city_text(),
# 	)
# 	await state.update_data(last_kb=None)
#
#
# @router.message(StateFilter(StepsForm.GET_CITY))
# async def config_city(
# 		message: Message,
# 		state: FSMContext,
# ):
# 	user_city = message.text
# 	list_of_cities = await geoposition_worker.get_list_of_cities(city_name=user_city)
# 	if not list_of_cities:
# 		await message.answer(
# 			text=BotTexts.config_wrong_city_text(),
# 		)
# 	else:
# 		await state.set_state(StepsForm.CHOOSE_CITY)
# 		await state.update_data(list_of_cities=[city.__dict__ for city in list_of_cities])
# 		await state.update_data(current_city_index=0)
# 		probable_city = list_of_cities[0]
# 		new_message = await message.answer(
# 			text=BotTexts.config_choose_city_text(city=probable_city),
# 			reply_markup=BotKeyboards.get_accept_kb(),
# 		)
# 		await state.update_data(last_kb=new_message.message_id)
#
#
# @router.callback_query(StateFilter(StepsForm.CHOOSE_CITY), F.data == 'yes')
# async def config_choose_city(
# 		callback: CallbackQuery,
# 		state: FSMContext,
# ):
# 	current_city_index = (await state.get_data())['current_city_index']
# 	list_of_cities_serialized = (await state.get_data())['list_of_cities']
# 	list_of_cities = [CityDTO.from_dict(city) for city in list_of_cities_serialized]
# 	await state.set_state(StepsForm.CHOOSE_SEX)
# 	city = list_of_cities[current_city_index]
# 	await state.update_data(city=city.__dict__)
# 	await callback.message.answer(
# 		text=BotTexts.config_city_accept_text(city=city),
# 	)
# 	new_message = await callback.message.answer(
# 		text=BotTexts.config_choose_sex_text(),
# 		reply_markup=BotKeyboards.get_choose_sex_kb(),
# 	)
# 	await state.update_data(last_kb=new_message.message_id)
#
#
# @router.callback_query(StateFilter(StepsForm.CHOOSE_CITY), F.data == 'no')
# async def config_choose_city(
# 		callback: CallbackQuery,
# 		state: FSMContext,
# ):
# 	current_city_index = (await state.get_data())['current_city_index']
# 	list_of_cities_serialized = (await state.get_data())['list_of_cities']
# 	list_of_cities = [CityDTO.from_dict(city) for city in list_of_cities_serialized]
# 	current_city_index += 1
# 	if current_city_index == len(list_of_cities):
# 		await state.set_state(StepsForm.GET_CITY)
# 		await callback.message.answer(
# 			text=BotTexts.config_wrong_city_text(),
# 		)
# 	else:
# 		await state.update_data(current_city_index=current_city_index)
# 		probable_city = list_of_cities[current_city_index]
# 		new_message = await callback.message.answer(
# 			text=BotTexts.config_choose_city_text(city=probable_city),
# 			reply_markup=BotKeyboards.get_accept_kb(),
# 		)
# 		await state.update_data(last_kb=new_message.message_id)
#
#
# @router.callback_query(StateFilter(StepsForm.CHOOSE_SEX), (F.data == 'male' or F.data == 'female'))
# async def choose_sex(
# 		callback: CallbackQuery,
# 		bot: Bot,
# 		state: FSMContext,
# ):
# 	await callback.message.answer(
# 		text=BotTexts.config_accept_sex_text(sex=callback.data)
# 	)
# 	users_now = await UserRepository.count_users()
# 	if users_now >= settings.max_number_of_users:
# 		await state.clear()
# 		await callback.message.answer(
# 			text=BotTexts.a_lot_of_users_text(),
# 			reply_markup=None,
# 		)
#
# 	else:
# 		user_data: dict = await state.get_data()
# 		user_data['time'] = time.fromisoformat(user_data['time'])
# 		user_data['city'] = CityDTO.from_dict(user_data['city'])
#
# 		job_id = add_new_async_schedule_job(
# 			bot=bot,
# 			user_id=callback.from_user.id,
# 			wake_up_time=user_data.__getitem__('time'),
# 		)
#
# 		new_user = UserDTO(
# 			_id=callback.from_user.id,
# 			name=callback.from_user.first_name,
# 			city=user_data.__getitem__('city'),
# 			sex=callback.data,
# 			wake_up_time=user_data.__getitem__('time').isoformat(),
# 			job_id=job_id,
# 		)
# 		await UserRepository.add_user(new_user=new_user)
#
# 		await state.clear()
# 		await callback.message.answer(
# 			text=BotTexts.config_done_text(wake_up_time=user_data.__getitem__('time')),
# 			reply_markup=None,
# 		)
