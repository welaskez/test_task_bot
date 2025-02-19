from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="🔮 Услуги", callback_data="services")],
        [InlineKeyboardButton(text="💰 Цены", callback_data="prices")],
        [InlineKeyboardButton(text="📞 Контакты", callback_data="contact")],
    ]
)

services_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="🃏 Гадание на Таро", callback_data="tarot")],
        [InlineKeyboardButton(text="🔮 Консультация", callback_data="consultation")],
        [InlineKeyboardButton(text="💰 Финансы", callback_data="finance")],
        [InlineKeyboardButton(text="🔙 Назад", callback_data="main")],
    ]
)
