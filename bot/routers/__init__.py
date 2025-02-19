__all__ = ("router",)

from aiogram import Router

from .message import router as message_router

router = Router(name=__name__)
router.include_router(message_router)
