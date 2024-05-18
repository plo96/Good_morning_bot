"""
	Создание и инициализация экзмепляра класса, ответственного за взаимодействие с API геопозиции.
"""
from datetime import timedelta

import aiohttp

from src.outer_apis_workers.multiply_triying import multiply_trying
from src.project.exceptions import TimezoneApiException

from .i_timezone_worker import ITimezoneWorker

TIMEZONE_URL = "https://timeapi.io/api/TimeZone/coordinate"


class TimeapiTimezoneWorker(ITimezoneWorker):
    """Класс для взаимодействия с API часового пояса."""

    def __init__(
            self,
            url: str,
    ):
        self._url = url

    @multiply_trying
    async def get_time_shift(
            self,
            latitude: float,
            longitude: float,
    ) -> timedelta:
        """
		Получение сдвига времени для конкретных координат.
        :param latitude: Искомая широта.
        :param longitude: Искомая долгота.
        :return: Сдвиг времени по UTC.
                 TimezoneApiException в случае bad request.
		"""
        async with aiohttp.ClientSession() as client:
            async with client.get(
                    url=self._url,
                    params={
                        "latitude": latitude,
                        "longitude": longitude,
                    },
                    timeout=5,
            ) as response:
                status_code = response.status
                if status_code != 200:
                    raise TimezoneApiException
                response = await response.json()

        time_shift = response['currentUtcOffset']['seconds']

        return timedelta(seconds=time_shift)


timeapi_timezone_worker = TimeapiTimezoneWorker(
    url=TIMEZONE_URL,
)
