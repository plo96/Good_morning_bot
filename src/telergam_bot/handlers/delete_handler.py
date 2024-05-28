"""
	Handlers для процесса удаления пользователя.
"""
from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext

from src.telergam_bot.utils import BotTexts, StepsForm, BotKeyboards
from src.database.user_repository_mongo import UserRepositoryMongo as UserRepository
from src.scheduler import Scheduler

router = Router()


@router.callback_query(F.data == "delete")
async def delete_acceptance(
		callback: CallbackQuery,
		state: FSMContext,
):
	user_id = callback.from_user.id
	user = await UserRepository.select_user(user_id=user_id)
	
	if not user:
		new_message = await callback.message.answer(
			text=BotTexts.user_not_found_text(),
			reply_markup=BotKeyboards.get_menu_kb(),
		)
	else:
		await state.set_state(StepsForm.DELETION_ACCEPT)
		new_message = await callback.message.answer(
			text=BotTexts.delete_acceptance_text(),
			reply_markup=BotKeyboards.get_accept_kb(),
		)
	
	await state.update_data(last_kb=new_message.message_id)


@router.callback_query(StateFilter(StepsForm.DELETION_ACCEPT), F.data == "yes")
async def delete_accept(
		callback: CallbackQuery,
		state: FSMContext,
):
	user_id = callback.from_user.id
	user = await UserRepository.select_user(user_id=user_id)
	await UserRepository.del_user(user_id=user_id)
	Scheduler.delete_job_for_user(user=user)
	await state.clear()
	new_message = await callback.message.answer(
		text=BotTexts.success_delete_text(),
		reply_markup=BotKeyboards.get_menu_kb(),
	)
	await state.update_data(last_kb=new_message.message_id)


@router.callback_query(StateFilter(StepsForm.DELETION_ACCEPT), F.data == "no")
async def delete_confirm(
		callback: CallbackQuery,
		state: FSMContext,
):
	await state.clear()
	new_message = await callback.message.answer(
		text=BotTexts.menu_text(),
		reply_markup=BotKeyboards.get_menu_kb(),
	)
	await state.update_data(last_kb=new_message.message_id)
	