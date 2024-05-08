from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder


class BotKeyboards:
    
    @staticmethod
    def get_empty_kb():
        empty_kb = InlineKeyboardMarkup(inline_keyboard=[])
        return empty_kb
    
    @staticmethod
    def get_menu_kb():
        menu = [
            [InlineKeyboardButton(text="Удалить пользователя", callback_data="delete"),
             InlineKeyboardButton(text="Настроить пользователя", callback_data="config")],
        ]
        menu = InlineKeyboardMarkup(inline_keyboard=menu)
        return menu
    
    @staticmethod
    def get_accept_kb():
        accept_del = [
            [InlineKeyboardButton(text="Да", callback_data="yes"),
             InlineKeyboardButton(text="Нет", callback_data="no")],
        ]
        accept_del = InlineKeyboardMarkup(inline_keyboard=accept_del)
        return accept_del
    
    @staticmethod
    def get_hours_choose_kb():
        hours_choose_kb = InlineKeyboardBuilder()
        for hour in range(5, 11):
            hours_choose_kb.button(
                text=f"{hour}:00-{hour}:59",
                callback_data=f"/hour_{hour}",
            )
        hours_choose_kb.adjust(2)
        hours_choose_kb = hours_choose_kb.as_markup()
        return hours_choose_kb
    
    @staticmethod
    def get_minutes_choose_kb(hour: str):
        minutes_choose_kb = InlineKeyboardBuilder()
        for minutes in range(0, 60, 10):
            minutes_choose_kb.button(
                text=f"{hour}:{minutes if minutes != 0 else '00'}",
                callback_data=f"/time_{hour}_{minutes}",
            )
        minutes_choose_kb.adjust(2)
        minutes_choose_kb = minutes_choose_kb.as_markup()
        return minutes_choose_kb

    @staticmethod
    def get_choose_sex_kb():
        choose_sex_kb = [
            [InlineKeyboardButton(text="Мужской", callback_data="male")],
            [InlineKeyboardButton(text="Женский", callback_data="female")],
        ]
        choose_sex_kb = InlineKeyboardMarkup(inline_keyboard=choose_sex_kb)
        return choose_sex_kb
