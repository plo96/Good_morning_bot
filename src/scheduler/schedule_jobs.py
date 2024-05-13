from aiogram import Bot

from src.database import UserRepositoryMongo as UserRepository
from src.outer_apis_workers import weather_worker, gpt_worker


async def say_good_morning(
        bot: Bot,
        user_id: int,
):
    user = await UserRepository.select_user(user_id=user_id)
    if not user:
        return
    good_morning = await gpt_worker.get_good_morning(sex=user.sex, name=user.name)
    weather_predict = await weather_worker.get_weather_prediction(lat=user.city.lat, lon=user.city.lon)

    weather_predict = [
        f"""*{w.time.strftime("%H:%M")}* : Тип погоды - **{', '.join([w_type for w_type in w.weather_type])}**,
			  Температура {round(w.temperature), 1}°C (по ощущениям {round(w.feels_like, 1)}°С),
			  Влажность {w.humidity}%, скорость ветра {round(w.wind, 1)}м/с""" for w in weather_predict]

    weather_text = 'Погода на сегодня:\n'.__add__('\n'.join(weather_predict))

    await bot.send_message(user_id, good_morning)
    await bot.send_message(user_id, weather_text, parse_mode='Markdown')
