"""
	Классы, отвечающие за реализацию машины состояний в боте.
"""
from aiogram.fsm.state import StatesGroup, State


class StepsForm(StatesGroup):
	"""
		Класс, хранящий солстояния стадии заполнения анкеты (при настройке пользователя).
	"""
	DELETION_ACCEPT = State()
	GET_HOUR = State()
	GET_MINUTES = State()
	GET_CITY = State()
	CHOOSE_CITY = State()
	CHOOSE_SEX = State()
	