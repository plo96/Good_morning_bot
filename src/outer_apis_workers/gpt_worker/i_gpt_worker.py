"""
	Описание интерфейса класса, ответственного за взаимодействие с API llm-модели.
"""
from abc import ABC, abstractmethod

from src.project.exceptions import GptApiException


class IGptWorker(ABC):
    """Интерфейс для обеспечания взаимодействия с llm-моделью по её API."""

    @abstractmethod
    async def get_good_morning(
            self,
            sex: str,
            name: str,
    ) -> str:
        """
        Получение от llm-модели сгенерированного пожелания доброго утра.
        :param sex: Пол пользователя.
        :param name: Имя пользователя.
        :return: Сгенерированная нейросетью строка с индивидуальными пожеланиями.
                 GptApiException в случае bad request.
        """
        pass
