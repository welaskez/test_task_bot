import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ChatType, ParseMode
from core.config import settings
from core.models import session_pool
from filters import ChatTypeFilter
from middlewares import DatabaseMiddleware, UserServiceMiddleware
from routers import router


async def main():
    bot = Bot(
        token=settings.bot_token,
        default=DefaultBotProperties(
            link_preview_is_disabled=True,
            parse_mode=ParseMode.HTML,
        ),
    )
    dp = Dispatcher()

    await bot.delete_webhook(drop_pending_updates=True)

    dp.include_router(router)
    dp.update.middleware(DatabaseMiddleware(session_pool=session_pool))
    dp.update.middleware(UserServiceMiddleware())
    dp.message.filter(ChatTypeFilter(chat_types=[ChatType.PRIVATE]))
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(
        level=settings.logging.level,
        format=settings.logging.format,
        handlers=[logging.StreamHandler()],
    )
    asyncio.run(main())
