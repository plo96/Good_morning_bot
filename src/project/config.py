"""
	Основные настройки проекта. Получение из файла .env.
"""
from dataclasses import dataclass
import os
from pathlib import Path
from typing import Optional

HOME_DIR = Path(__file__).parent.parent.parent


@dataclass
class Settings:
	"""Класс, содержащий основные настройки приложения."""
	bot_token: str
	weather_token: str
	geopositional_token: str
	gpt_token: str
	gpt_identification: str
	home_dir: Path
	admin_id: Optional[int]
	max_number_of_users: int

	_mongo_user: str
	_mongo_pwd: str
	_mongo_host: str
	_mongo_port: int

	_redis_pwd: str
	_redis_host: str
	_redis_port: int

	def __post_init__(self):
		"""
			'Cборка' url для подключения к сторонним сервисам после основной инициализации объекта класса.
		"""
		self.db_url_mongodb: str = f"mongodb://{self._mongo_user}:{self._mongo_pwd}@{self._mongo_host}:{self._mongo_port}"
		self.redis_url: str = f"redis://:{self._redis_pwd}@{self._redis_host}:{self._redis_port}/0"


settings = Settings(
	bot_token=os.getenv("BOT_TOKEN"),
	weather_token=os.getenv("OPENWEATHERMAP_API_KEY"),
	geopositional_token=os.getenv("GEOPOSITIONAL_OPENWEATHERMAP_API_KEY"),
	gpt_identification=os.getenv("YANDEX_GPT_IDENTIFICATION"),
	gpt_token=os.getenv("YANDEX_GPT_API_KEY"),
	home_dir=HOME_DIR,
	admin_id=int(os.getenv('ADMIN_ID')) if os.getenv('ADMIN_ID') else None,
	max_number_of_users=int(os.getenv('MAX_NUMBER_OF_USERS')),
	_mongo_user=os.getenv("MONGO_USER"),
	_mongo_pwd=os.getenv("MONGO_PWD"),
	_mongo_host=os.getenv("MONGO_HOST"),
	_mongo_port=int(os.getenv("MONGO_PORT")),
	_redis_pwd=os.getenv("REDIS_PWD"),
	_redis_host=os.getenv("REDIS_HOST"),
	_redis_port=int(os.getenv("REDIS_PORT")),
)
