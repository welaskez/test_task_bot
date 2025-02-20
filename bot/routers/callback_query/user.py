import message_texts
from aiogram import F, Router, types
from keyboards.inline import common
from services.response import ResponseService

router = Router(name=__name__)


@router.callback_query(F.data == "main")
async def handle_main(callback: types.CallbackQuery):
    await callback.message.edit_text(text=message_texts.START, reply_markup=common.start_kb)
    await callback.answer()


@router.callback_query(F.data == "services")
async def handle_services(callback: types.CallbackQuery):
    await callback.message.edit_text(text=message_texts.SERVICES, reply_markup=common.services_and_prices_kb)
    await callback.answer()


@router.callback_query(F.data == "prices")
async def handle_prices(callback: types.CallbackQuery):
    await callback.message.edit_text(text=message_texts.PRICES, reply_markup=common.services_and_prices_kb)
    await callback.answer()


@router.callback_query(F.data == "contact")
async def handle_contacts(callback: types.CallbackQuery):
    await callback.message.edit_text(text=message_texts.CONTACTS, reply_markup=common.to_main_kb)
    await callback.answer()


@router.callback_query(F.data == "tarot")
async def handle_tarot(callback: types.CallbackQuery, response_service: ResponseService):
    await response_service.handle_tarot(callback)


@router.callback_query(F.data == "finance")
async def handle_finance(callback: types.CallbackQuery, response_service: ResponseService):
    await response_service.handle_finance(callback)
