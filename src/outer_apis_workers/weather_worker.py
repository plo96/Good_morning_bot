"""
	Создание и инициализация экзмепляра класса, ответственного за взаимодействие с API прогноза погоды.
"""
from datetime import datetime

import aiohttp

from src.project.config import settings
from src.core.schemas import WeatherDTO
from src.project.exceptions import WeatherApiException
from src.outer_apis_workers.multiply_triying import multiply_trying

OPENWEATHERMAP_URL = "http://api.openweathermap.org/data/2.5/forecast"


class WeatherWorker:
	"""Класс для обеспечения взаимодействия с API прогноза погоды."""
	
	def __init__(
			self,
			url: str,
			token: str,
	):
		"""
        :param url: URL по которому доступно API.
        :param token: Персональный токен доступа к API.
        """
		self._url = url
		self._token = token
	
	@multiply_trying
	async def get_weather_prediction(
			self,
			lat: float,
			lon: float,
	) -> str:
		"""
        Получение прогноза погоды по внешнему API. Выделение нужных параметров, составление текста прогноза погоды.
        :param lat: Географическая широта для прогноза.
        :param lon: Географическая долгота для прогноза.
        :return: Строка с отформатированным по Markdown текстом прогноза погоды.
                 WeatherApiException в случае bad request.
        """
		async with aiohttp.ClientSession() as client:
			async with client.get(
					url=self._url,
					params={
						"lat": lat,
						"lon": lon,
						"appid": self._token,
					},
					timeout=5,
			) as response:
				status_code = response.status
				if status_code != 200:
					raise WeatherApiException
				weather_predictions_list: list = []
				for one_weather_predict in (await response.json())['list'][0:4]:
					weather = WeatherDTO(
						time=datetime.fromtimestamp(one_weather_predict['dt']).time(),
						temperature=one_weather_predict['main']['temp'] - 273.15,
						feels_like=one_weather_predict['main']['feels_like'] - 273.15,
						humidity=one_weather_predict['main']['humidity'],
						weather_type=[weather['main'] for weather in one_weather_predict['weather']],
						wind=one_weather_predict['wind']['speed'],
					)
					weather_predictions_list.append(weather)
		
		weather_prediction = self.weather_prediction_formatting(weather_predictions_list)
		
		return weather_prediction
	
	@staticmethod
	def weather_prediction_formatting(
			weather_predictions_list: list[WeatherDTO],
	) -> str:
		"""
       Форматирование результата
       :param weather_predictions_list: Список WeatherDTO, полученный от weather_worker.
       :return: Строка с отформатированным по Markdown текстом прогноза погоды.
       """
		weather_predictions_text = [
			f"""*{w.time.strftime("%H:%M")}* : Тип погоды - **{', '.join([w_type for w_type in w.weather_type])}**,
                Температура {round(w.temperature)}°C (ощущается {round(w.feels_like)}°С),
                Влажность {w.humidity}%, Ветер {round(w.wind, 1)}м/с""" for w in weather_predictions_list]
		
		weather_text = 'Погода на сегодня:\n'.__add__('\n'.join(weather_predictions_text))
		
		return weather_text


weather_worker = WeatherWorker(
	url=OPENWEATHERMAP_URL,
	token=settings.weather_token,
)
