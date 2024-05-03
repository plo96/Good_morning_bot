from telebot import Telebot
from sqlalchemy.ext.asyncio import async_sessionmaker

from src.core.schemas import UserDTO
from src.my_bot.interface import BotInterface
from src.outer_apis_workers import weather_worker, llm_worker
from src.project.config import settings
from src.database import UserRepository, db_helper


class MyBot(Telebot, BotInterface):
	def __init__(self, token: str, session_factory: async_sessionmaker):
		self._token = token
		self._session_factory = session_factory
	
	async def new_user_register(self):
		async with self._session_factory() as session:
			res = await UserRepository.add_user(
				session=session,
				new_user=...,
			)
			new_user = UserDTO.from_model(res)
	
	async def user_delete(self):
		async with self._session_factory() as session:
			user = await UserRepository.select_user(
				session=session,
				user_id=...
			)
			await UserRepository.del_user(
				session=session,
				user=user,
			)
			await session.commit()
	
	async def say_good_morning(self):
		good_morning = await llm_worker.get_good_morning()
		print(good_morning)
	
	async def say_weather_predict(self):
		weather_predict = await weather_worker.get_weather()
		print(weather_predict)


my_bot = MyBot(
	token=settings.bot_token,
	session_factory=db_helper.get_session_factory(),
)
