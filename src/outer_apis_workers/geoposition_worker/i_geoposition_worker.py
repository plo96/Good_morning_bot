"""
	Описание интерфейса класса, ответственного за взаимодействие с API геопозиции.
"""
from abc import ABC, abstractmethod

import aiohttp

from src.project.exceptions import GeopositionalApiException
from src.core.schemas import CityDTO


class IGeopositionWorker(ABC):
    """Интерфейс для взаимодействия с API геопозиции."""

    @abstractmethod
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
        pass
