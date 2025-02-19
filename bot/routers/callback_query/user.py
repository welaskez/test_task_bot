import message_texts
from aiogram import F, Router, types
from keyboards.inline import common

router = Router(name=__name__)


@router.callback_query(F.data == "main")
async def handle_main(callback: types.CallbackQuery):
    await callback.message.edit_text(text=message_texts.START, reply_markup=common.start_kb)
    await callback.answer()


@router.callback_query(F.data == "services")
async def handle_services(callback: types.CallbackQuery):
    await callback.message.edit_text(text=message_texts.SERVICES, reply_markup=common.services_kb)
    await callback.answer()
