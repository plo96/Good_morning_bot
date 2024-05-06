from datetime import datetime

import httpx

from src.project.config import settings
from src.core.schemas import WeatherDTO


OPENWEATHERMAP_URL = "http://api.openweathermap.org/data/2.5/forecast"


class WeatherWorker:
    def __init__(
            self,
            url: str,
            token: str,
    ):
        self._url = url
        self._token = token

    async def get_weather_prediction(
            self,
            lat: float,
            lon: float,
    ) -> list:
        
        async with httpx.AsyncClient() as client:
            response = await client.get(
                url=self._url,
                params={
                    "lat": lat,
                    "lon": lon,
                    "appid": self._token,
                }
            )
        
        weather_prediction: list = []
        
        for one_weather_predict in response.json()['list'][0:4]:
            weather = WeatherDTO(
                time=datetime.fromtimestamp(one_weather_predict['dt']).time(),
                temperature=one_weather_predict['main']['temp'],
                feels_like=one_weather_predict['main']['feels_like'],
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
