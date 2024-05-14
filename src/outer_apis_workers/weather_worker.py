from datetime import datetime

import aiohttp

from src.project.config import settings
from src.core.schemas import WeatherDTO
from src.project.exceptions import WeatherApiException
from src.outer_apis_workers.multiply_triying import multiply_trying


OPENWEATHERMAP_URL = "http://api.openweathermap.org/data/2.5/forecast"


class WeatherWorker:
    def __init__(
            self,
            url: str,
            token: str,
    ):
        self._url = url
        self._token = token
    
    @multiply_trying
    async def get_weather_prediction(
            self,
            lat: float,
            lon: float,
    ) -> list[WeatherDTO]:
        
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
                weather_prediction: list = []
                for one_weather_predict in (await response.json())['list'][0:4]:
                    weather = WeatherDTO(
                        time=datetime.fromtimestamp(one_weather_predict['dt']).time(),
                        temperature=one_weather_predict['main']['temp'] - 273.15,
                        feels_like=one_weather_predict['main']['feels_like'] - 273.15,
                        humidity=one_weather_predict['main']['humidity'],
                        weather_type=[weather['main'] for weather in one_weather_predict['weather']],
                        wind=one_weather_predict['wind']['speed'],
                    )
                    weather_prediction.append(weather)
        return weather_prediction


weather_worker = WeatherWorker(
    url=OPENWEATHERMAP_URL,
    token=settings.weather_token,
)
