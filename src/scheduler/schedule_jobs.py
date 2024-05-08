from aiogram import Bot

from src.database import UserRepository
from src.outer_apis_workers import weather_worker, gpt_worker


async def say_good_morning(
		bot: Bot,
		user_id: int,
):
	user = await UserRepository.select_user(user_id=user_id)
	if not user:
		return
	good_morning = await gpt_worker.get_good_morning(sex=user.sex, user=user.name)
	weather_predict = await weather_worker.get_weather_prediction(lat=user.lat, lon=user.lon)
	
	weather_predict = [f"""{w.time.hour}:{w.time.minute} : Тип погоды - {', '.join([w_type for w_type in w.weather_type])},
								  Температура {w.temperature}°C (по ощущениям {w.feels_like}°С),
					 			  Влажность {w.humidity}%, скорость ветра {w.wind}м/с""" for w in weather_predict]
	
	weather_text = 'Погода на сегодня:\n'.__add__('\n'.join(weather_predict))
	
	await bot.send_message(user_id, good_morning)
	await bot.send_message(user_id, weather_text)
	