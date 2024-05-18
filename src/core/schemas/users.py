"""
	Схемы для работы с сущностями пользователей.
"""
from datetime import time, timedelta

from dataclasses import dataclass
from typing import Optional, Mapping, Any

from .cities import CityDTO


@dataclass
class UserDTO:
    """
    Класс для пользователей приложения.
    """
    id: int                         # id в телеграм
    name: str                       # имя пользователя
    city: CityDTO                   # город
    sex: str                        # пол
    wake_up_time: time              # Время пробуждения
    time_shift: timedelta           # Сдвиг временного пояса
    job_id: Optional[str] = None    # id привязанной хадачи по расписанию
    
    
    def to_serialised_mongo_dict(self) -> dict:
        """
        Сериализация данных и представление их в словаре для записи в базу данных mongodb.
        :return: dict
        """
        return dict(
            _id=self.id,
            name=self.name,
            city=self.city.__dict__,
            sex=self.sex,
            wake_up_time=self.wake_up_time.isoformat(),
            time_shift=self.time_shift.seconds,
            job_id=self.job_id,
        )
    
    @staticmethod
    def from_serialised_mongo_dict(mongo_dict: dict | Mapping[str, Any]):
        """
        Создание экземпляра класса UserDTO из сериализованного словаря после чтения из базы данных mongodb.
        :param mongo_dict: Словарь, полученный из базы данных mongodb.
        :return: UserDTO
        """
        return UserDTO(
            id=mongo_dict.__getitem__('_id'),
            name=mongo_dict.__getitem__('name'),
            city=CityDTO(**mongo_dict.__getitem__('city')),
            sex=mongo_dict.__getitem__('sex'),
            wake_up_time=time.fromisoformat(mongo_dict.__getitem__('wake_up_time')),
            time_shift=timedelta(seconds=mongo_dict.__getitem__('time_shift')),
            job_id=mongo_dict.__getitem__('job_id'),
        )