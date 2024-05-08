

@router.callback_query(F.data == "delete")
async def delete_acceptance(
		callback: CallbackQuery,
		state: FSMContext,
):
	user_id = callback.message.from_user.id  # TODO: Проверить чей id вылезет - бота или пользователя
	user = await UserRepository.select_user(user_id=user_id)
	
	if not user:
		await callback.message.answer(
			text=BotTexts.user_not_found_text(),
			reply_markup=BotKeyboards.get_menu_kb(),
		)
	else:
		await state.set_state(StepsForm.DELETION_ACCEPT)
		await callback.message.answer(
			text=BotTexts.delete_acceptance_text(),
			reply_markup=BotKeyboards.get_accept_kb(),
		)


@router.callback_query(StepsForm.DELETION_ACCEPT and F.data == "yes")
async def delete_accept(
		callback: CallbackQuery,
		state: FSMContext,
):
	user_id = callback.message.from_user.id  # TODO: Проверить чей id вылезет - бота или пользователя
	print(user_id)
	user = await UserRepository.select_user(user_id=user_id)
	await UserRepository.del_user(user)
	await state.clear()
	await callback.message.answer(
		text=BotTexts.success_delete_text(),
		reply_markup=BotKeyboards.get_menu_kb(),
	)
	del_async_schedule_job()  # TODO: Разобраться с удалением тасок по расписанию


@router.callback_query(StepsForm.DELETION_ACCEPT and F.data == "no")
async def delete_confirm(
		callback: CallbackQuery,
		state: FSMContext,
):
	await state.clear()
	await callback.message.answer(
		text=BotTexts.menu_text(),
		reply_markup=BotKeyboards.get_menu_kb(),
	)