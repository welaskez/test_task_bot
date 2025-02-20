from typing import Any, Awaitable, Callable, Coroutine

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject
from services.response import ResponseService


class ResponseServiceMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[TelegramObject, dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: dict[str, Any],
    ) -> Coroutine[Any, Any, Any]:
        data["response_service"] = ResponseService(session=data["session"])
        return await handler(event, data)
