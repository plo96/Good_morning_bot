from abc import ABC, abstractmethod


class BotInterface(ABC):
	
	@abstractmethod
	async def new_user_register(self):
		...
	
	@abstractmethod
	async def user_delete(self):
		...
	
	@abstractmethod
	async def say_good_morning(self):
		...
	
	@abstractmethod
	async def say_weather_predict(self):
		...
