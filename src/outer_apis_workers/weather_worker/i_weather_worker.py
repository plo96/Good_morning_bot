"""
	Создание интерфейса класса, ответственного за взаимодействие с API прогноза погоды.
"""
from abc import abstractmethod, ABC

from src.project.exceptions import WeatherApiException


class IWeatherWorker(ABC):
    """Интерфейс для обеспечения взаимодействия с API прогноза погоды."""

    @abstractmethod
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
        pass
