from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def add_bot():
    keyboard = [
        [InlineKeyboardButton(text="➕ Добавить Moderator в группу", url="https://t.me/moderator_chanel_mikeInTech_bot?startgroup")],
    ] 
    return InlineKeyboardMarkup(inline_keyboard=keyboard)
