"""
    Задачи по расписанию.
"""
from aiogram import Bot

from src.database import UserRepositoryMongo as UserRepository
from src.outer_apis_workers.weather_worker import weather_worker
from src.outer_apis_workers.gpt_worker import gpt_worker


async def say_good_morning(
        bot: Bot,
        user_id: int,
) -> None:
    """
    Получение пожелания доброго утра и прогноза погоды от внешних API и их отправка пользователю.
    :param bot: Telegram бот с которого будут отправлятсья сообщения.
    :param user_id: id пользователя, которому отправляется сообщение.
    :return: None
    """
    
    user = await UserRepository.select_user(user_id=user_id)
    if not user:
        return
    good_morning = await gpt_worker.get_good_morning(sex=user.sex, name=user.name)
    weather_prediction = await weather_worker.get_weather_prediction(lat=user.city.lat, lon=user.city.lon)
    
    await bot.send_message(user_id, good_morning)
    await bot.send_message(user_id, weather_prediction, parse_mode='Markdown')



