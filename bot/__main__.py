import asyncio
import logging

from aiogram import Dispatcher
from aiogram.enums import ChatType
from core.config import settings
from core.models import session_pool
from filters import ChatTypeFilter
from middlewares import (
    ConsultationServiceMiddleware,
    DatabaseMiddleware,
    ResponseServiceMiddleware,
    UserServiceMiddleware,
)
from routers import router
from utils.bot import get_bot


async def main():
    bot = get_bot()
    dp = Dispatcher()

    await bot.delete_webhook(drop_pending_updates=True)

    dp.include_router(router)
    dp.update.middleware(DatabaseMiddleware(session_pool=session_pool))
    dp.update.middleware(UserServiceMiddleware())
    dp.update.middleware(ResponseServiceMiddleware())
    dp.update.middleware(ConsultationServiceMiddleware())
    dp.message.filter(ChatTypeFilter(chat_types=[ChatType.PRIVATE]))
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(
        level=settings.logging.level,
        format=settings.logging.format,
        handlers=[logging.StreamHandler()],
    )
    asyncio.run(main())
