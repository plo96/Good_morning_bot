from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder

exit_button_conf = {
    'text': "◀️ Выйти в меню",
    'callback_data': "menu",
}

menu = [
    [InlineKeyboardButton(text="Удалить пользователя", callback_data="delete"),
     InlineKeyboardButton(text="Настроить пользователя", callback_data="config")],
    [InlineKeyboardButton(**exit_button_conf)],
]
menu = InlineKeyboardMarkup(inline_keyboard=menu)

accept_del = [
    [InlineKeyboardButton(text="Да", callback_data="delete_yes"),
     InlineKeyboardButton(text="Нет", callback_data="delete_no")],
    [InlineKeyboardButton(**exit_button_conf)],
]
accept_del = InlineKeyboardMarkup(inline_keyboard=accept_del)

hours_choose_kb = InlineKeyboardBuilder()
for hour in range(5, 11):
    hours_choose_kb.button(
        text=f"{hour}:00-{hour}:59",
        callback_data=f"/hour_{hour}",
    )
hours_choose_kb.button(**exit_button_conf)
hours_choose_kb.adjust(2, 2, 2, 1)

hours_choose_kb = hours_choose_kb.as_markup()


def get_minutes_choose_kb(hour: str):
    minutes_choose_kb = InlineKeyboardBuilder()
    for minutes in range(0, 60, 10):
        minutes_choose_kb.button(
            text=f"{hour}:{minutes if minutes != 0 else '00'}",
            callback_data=f"/time_{hour}_{minutes}",
        )
    minutes_choose_kb.button(**exit_button_conf)
    minutes_choose_kb.adjust(2, 2, 2, 1)
    minutes_choose_kb = minutes_choose_kb.as_markup()
    return minutes_choose_kb


def get_location_kb():
    # location_kb = ReplyKeyboardBuilder()
    #
    # location_kb.button(text='Предоставить текущую геолокацию', request_location=True)
    # location_kb.button(text=exit_button_conf['text'])
    # location_kb = location_kb.adjust(1)
    # location_kb = location_kb.as_markup(resize_keyboard=True)

    location_kb = InlineKeyboardBuilder()
    location_kb.button(**exit_button_conf)

    location_kb = location_kb.as_markup()

    return location_kb
