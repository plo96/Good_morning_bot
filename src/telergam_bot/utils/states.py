from aiogram.fsm.state import StatesGroup, State


class StepsForm(StatesGroup):
	DELETION_ACCEPT = State()
	GET_HOUR = State()
	GET_MINUTES = State()
	GET_CITY = State()
	CHOOSE_CITY = State()
	CHOOSE_SEX = State()
	