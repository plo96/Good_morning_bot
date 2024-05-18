"""
	Описание интерфейса класса,, ответственного за взаимодействие с API часовых поясов.
"""
from abc import ABC, abstractmethod
from datetime import timedelta

from src.project.exceptions import TimezoneApiException


class ITimezoneWorker(ABC):
    """Интерфейс для взаимодействия с API часового пояса."""

    @abstractmethod
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
        pass
