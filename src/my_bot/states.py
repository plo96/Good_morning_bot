from aiogram.fsm.state import StatesGroup, State


class StepsForm(StatesGroup):
	GET_HOUR = State()
	GET_MINUTES = State()
	GET_CITY = State()
