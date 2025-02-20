from aiogram import Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from core.config import settings


def get_bot() -> Bot:
    return Bot(
        token=settings.bot_token,
        default=DefaultBotProperties(
            link_preview_is_disabled=True,
            parse_mode=ParseMode.HTML,
        ),
    )
