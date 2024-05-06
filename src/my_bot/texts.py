from abc import ABC


class BotTexts(ABC):
	
	@staticmethod
	def welcome_text(
			user_name: str,
	) -> str:
		return f"""
		Приветствую, {user_name}!
		Данный бот будет ежедневно желать тебе доброго утра и рассказывать о прогнозе погоды на сегодня.
		Осталось только провести несколько настроек. Для этого введи команду '/config'.
		"""
	
	@staticmethod
	def delete_acceptance_text() -> str:
		return """
		Вы точно желаете удалить настройки вашего аккаунта в данном боте?
		"""
	
	@staticmethod
	def config_already_exists() -> str:
		return """
		Похоже, в моей базе данных уже имеются настройки для вашего аккаунта!
		Для повторной настройки необходимо сначала удалить старые данные.
		Для удаления можете воспользоваться коммандой '/delete'.
		"""
	
	@staticmethod
	def config_text() -> str:
		return """
		Итак, приступим к найстройке.
		"""
