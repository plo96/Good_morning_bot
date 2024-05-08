

@router.message(Command("id"))
async def get_id(message: Message):
	print(message.from_user)
	await message.reply(
		text=str(message.from_user.id),
	)


@router.message(Command("start"))
async def start(
		message: Message,
):
	await message.answer(
		text=BotTexts.welcome_text(
			user_name=message.from_user.first_name,
		),
	)


@router.callback_query(F.data == "menu")
async def menu(
		callback: CallbackQuery,
		state: FSMContext
):
	await state.clear()
	await callback.message.answer(
		text=BotTexts.menu_text(),
		reply_markup=BotKeyboards.get_menu_kb(),
	)
