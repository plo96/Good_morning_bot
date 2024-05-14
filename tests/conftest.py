import pytest
from aiogram import Bot, types
from aiogram.contrib.testing.bot import InlineQueryBot


@pytest.fixture
async def bot():
    # Создаем объект бота для тестирования
    bot = Bot(token="your_bot_token")
    return bot


@pytest.mark.asyncio
async def test_send_message(bot):
    chat_id = "your_chat_id"
    message_text = "Hello, World!"

    # Отправляем сообщение от бота
    await bot.send_message(chat_id, message_text)

    # Получаем информацию о последнем отправленном сообщении
    last_message = await bot.send_message.last_call.args[1]

    # Проверяем, что текст сообщения совпадает с ожидаемым
    assert last_message.text == message_text
