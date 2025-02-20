from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardMarkup
from core.enums import ResponseEnum


def response_kb(response_type: ResponseEnum) -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()

    kb.button(text="Еще раз", callback_data="tarot" if response_type == ResponseEnum.TAROT else "finance")

    return kb.as_markup()
