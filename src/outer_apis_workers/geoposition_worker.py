import aiohttp

from src.project.config import settings
from src.project.exceptions import GeopositionalApiError
from src.core.schemas import CityDTO


OPENWEATHERMAP_URL = "http://api.openweathermap.org/data/2.5/forecast"


class GeopositionWorker:
    def __init__(
            self,
            url: str,
            token: str,
    ):
        self._url = url
        self._token = token
    
    async def get_list_of_cities(
            self,
            city_name: str,
    ) -> list[CityDTO]:
        
        async with aiohttp.ClientSession() as client:
            async with client.get(
                url=self._url,
                params={
                    "city": city_name,
                    "appid": self._token,
                }
            ) as response:
                response = await response.json()
                if not response or not isinstance(response, list):
                    raise GeopositionalApiError

                list_of_cities: list = []
                for result in response:
                    city = CityDTO.from_dict(result)
                    list_of_cities.append(city)
        return list_of_cities


geoposition_worker = GeopositionWorker(
    url=OPENWEATHERMAP_URL,
    token=settings.weather_token,
)
