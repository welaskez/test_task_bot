import pytest
from unittest.mock import AsyncMock
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext
import message_texts
from keyboards.inline import common
from routers.callback_query.user import (
    handle_main,
    handle_services,
    handle_prices,
    handle_contacts,
    handle_consultation,
)
from states.consultation import ConsultationState


@pytest.fixture
def mock_callback():
    callback = AsyncMock(spec=CallbackQuery)
    callback.message = AsyncMock(spec=Message)
    callback.message.edit_text = AsyncMock()
    callback.message.answer = AsyncMock()
    callback.answer = AsyncMock()
    return callback


@pytest.fixture
def mock_state():
    return AsyncMock(spec=FSMContext)


@pytest.mark.asyncio
async def test_handle_main(mock_callback):
    await handle_main(mock_callback)

    mock_callback.message.edit_text.assert_called_once_with(
        text=message_texts.START, reply_markup=common.start_kb
    )

    mock_callback.answer.assert_called_once()


@pytest.mark.asyncio
async def test_handle_services(mock_callback):
    await handle_services(mock_callback)

    mock_callback.message.edit_text.assert_called_once_with(
        text=message_texts.SERVICES, reply_markup=common.services_and_prices_kb
    )

    mock_callback.answer.assert_called_once()


@pytest.mark.asyncio
async def test_handle_prices(mock_callback):
    await handle_prices(mock_callback)

    mock_callback.message.edit_text.assert_called_once_with(
        text=message_texts.PRICES, reply_markup=common.services_and_prices_kb
    )

    mock_callback.answer.assert_called_once()


@pytest.mark.asyncio
async def test_handle_contacts(mock_callback):
    await handle_contacts(mock_callback)

    mock_callback.message.edit_text.assert_called_once_with(
        text=message_texts.CONTACTS, reply_markup=common.to_main_kb
    )

    mock_callback.answer.assert_called_once()


@pytest.mark.asyncio
async def test_handle_consultation(mock_callback, mock_state):
    await handle_consultation(mock_callback, mock_state)

    mock_state.set_state.assert_called_once_with(ConsultationState.name)

    mock_callback.message.answer.assert_called_once_with(text="Введите ваше имя")
