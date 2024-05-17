"""
	Кастомные ислючения для данного приложения.
"""


class OuterAPIExceptions(Exception):
	"""Ошибки при обращении к внешним API."""


class WeatherApiException(OuterAPIExceptions):
	"""Ошибка при обращении к API прогноза погоды."""
	pass


class GptApiException(OuterAPIExceptions):
	"""Ошибка при обращении к API llm-нейросети."""
	pass


class GeopositionalApiException(OuterAPIExceptions):
	"""Ошибка при обращении к API поиска геопозиции."""
	pass


class TimezoneApiException(OuterAPIExceptions):
	"""Ошибка при обращении к API определения часового пояса."""
	pass
