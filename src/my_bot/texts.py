from abc import ABC


class BotTexts(ABC):
	
	@staticmethod
	def welcome_text(
			user_name: str,
	) -> str:
		return f"""
		Приветствую, {user_name}!
		Данный бот будет ежедневно желать тебе доброго утра и рассказывать о прогнозе погоды на сегодня.
		Осталось только провести несколько настроек. Для этого выберите пункт 'Настроить пользователя'.
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
	def config_already_exists() -> str:
		return """
		Похоже, в моей базе данных уже имеются настройки для вашего аккаунта!
		Для повторной настройки необходимо сначала удалить старые данные.
		Для удаления можете воспользоваться коммандой 'Удалить пользователя'.
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
	def config_minutes_text() -> str:
		return """
		Давайте уточним это время:
		"""
	
	@staticmethod
	def config_city_text() -> str:
		return """
			Введите название вашего города на латинице (например: 'Moscow').
			Или нажмите на кнопку ниже, чтобы предоставить доступ к вашей геолокации.
			"""
