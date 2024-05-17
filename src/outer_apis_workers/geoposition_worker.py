"""
	Создание и инициализация экзмепляра класса, ответственного за взаимодействие с API геопозиции.
"""
import aiohttp

from src.outer_apis_workers.multiply_triying import multiply_trying
from src.project.config import settings
from src.project.exceptions import GeopositionalApiException
from src.core.schemas import CityDTO


GEOPOSITION_URL = "http://api.openweathermap.org/geo/1.0/direct"


class GeopositionWorker:
    """Класс для взаимодействия с API геопозиции."""
    def __init__(
            self,
            url: str,
            token: str,
    ):
        self._url = url
        self._token = token
    
    @multiply_trying
    async def get_list_of_cities(
            self,
            city_name: str,
    ) -> list[CityDTO]:
        """
        Получение списка возможных городов, соответствующих названию.
        :param city_name: Искомый город.
        :return: Список моделей CityDTO городов, совпадающих по названию с искомым.
                 GeopositionalApiException в случае bad request.
        """
        async with aiohttp.ClientSession() as client:
            async with client.get(
                url=self._url,
                params={
                    "q": city_name,
                    "appid": self._token,
                    "limit": 100,
                },
                timeout=5,
            ) as response:
                status_code = response.status
                if status_code != 200:
                    raise GeopositionalApiException
                response = await response.json()
                list_of_cities: list = []
                for result in response:
                    city = CityDTO.from_dict(result)
                    list_of_cities.append(city)
                    
        return list_of_cities


geoposition_worker = GeopositionWorker(
    url=GEOPOSITION_URL,
    token=settings.weather_token,
)
