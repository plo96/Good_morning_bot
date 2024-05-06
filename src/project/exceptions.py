"""
	Кастомные ислючения для данного приложения.
"""


class WeatherApiError(Exception):
	"""Ошибка при обращении к API прогноза погоды."""
	pass


class GptApiError(Exception):
	"""Ошибка при обращении к API llm-нейросети."""
	pass


class GeopositionalApiError(Exception):
	"""Ошибка при обращении к API поиска геопозиции."""
	pass
