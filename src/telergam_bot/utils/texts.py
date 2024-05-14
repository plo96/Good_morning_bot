from abc import ABC
from datetime import time

from src.core.schemas import CityDTO, UserDTO


class BotTexts(ABC):
	
	@staticmethod
	def welcome_text(
			user_name: str,
	) -> str:
		return f"""
		Приветствую, {user_name}!
		Данный бот будет ежедневно желать тебе доброго утра и рассказывать о прогнозе погоды на сегодня.
		Осталось только провести несколько настроек. Для этого вызовите меню и выберите пункт 'Настройки пользователя'.
		"""
	
	@staticmethod
	def menu_text() -> str:
		return """
		Выберите нужный пункт меню.
		"""
	
	@staticmethod
	def delete_acceptance_text() -> str:
		return """
		Вы точно желаете удалить настройки вашего аккаунта в данном боте?
		"""
	
	@staticmethod
	def user_not_found_text() -> str:
		return """
		Вы не зарегистрированы в данном боте.
		"""
	
	@staticmethod
	def success_delete_text() -> str:
		return """
		Настройки пользователя успешно удалены.
		"""
	
	@staticmethod
	def config_already_exists(user: UserDTO) -> str:
		return f"""
		Для вашего профиля сохранены настройки:
		Ваше время подъёма: {user.wake_up_time}
		Ваш город: {user.city.name}({user.city.state}, {user.city.country})
		Ваш пол: {user.sex}
		Для удаления можете воспользоваться коммандой 'Удаление пользователя'.
		"""
	
	@staticmethod
	def config_start_text() -> str:
		return """
		Итак, приступим к настройке.
		"""

	@staticmethod
	def config_hours_text() -> str:
		return """
		Выберите промежуток времени, когда вы встаёте по утрам:
		"""

	@staticmethod
	def config_hours_accept_text(hour) -> str:
		return f"""
		Вы выбрали промежуток с {hour}:00 до {hour}:59.
		"""

	@staticmethod
	def config_minutes_text() -> str:
		return """
		Давайте уточним это время:
		"""
	
	@staticmethod
	def config_time_accept_text(hour, minutes) -> str:
		return f"""
		Выбрано время {hour}:{minutes}.
		"""
	
	@staticmethod
	def config_city_text() -> str:
		return """
		Введите название вашего города (например: 'Moscow' или 'Новгород').
		"""
	
	@staticmethod
	def config_wrong_city_text() -> str:
		return """
		К сожалению, вашего города не найдено, попробуйте ввести название по-другому или использовать соседний город.
		"""
	
	@staticmethod
	def config_choose_city_text(city: CityDTO) -> str:
		return f"""
		Вы имеете ввиду город {city.name}, который находится в {city.state} страны {city.country}?
		"""
	
	@staticmethod
	def config_city_accept_text(city: CityDTO) -> str:
		return f"""
		Вы выбрали город "{city.name}({city.state}, {city.country})".
		"""
	
	@staticmethod
	def config_choose_sex_text() -> str:
		return """
		Выберите ваш пол.
		"""
	
	@staticmethod
	def config_accept_sex_text(sex: str) -> str:
		return f"""
		Вы выбрали пол {sex}.
		"""
	
	@staticmethod
	def config_done_text(
		wake_up_time: time,
	) -> str:
		return f"""
		Ваше настройки успешно сохранены.
		Вам будут отправляться автоматические сообщения в {wake_up_time}.
		Подробные настройки аккаунта можно посмотреть в разделе "Настройки пользователя".
		Удалить пользователя можно в разделе "Удаление пользователя".
		"""
	
	@staticmethod
	def a_lot_of_users_text() -> str:
		return """
			К сожалению, в настоящий момент превышено максимальное число пользователей.
			"""
	