from unittest.mock import AsyncMock

import pytest
from aiogram.types import CallbackQuery, Message
from core.enums import ResponseEnum
from core.models import Response
from crud.response import ResponseCRUD
from keyboards.inline import builders
from services.response import ResponseService


@pytest.fixture
def mock_crud():
    return AsyncMock(spec=ResponseCRUD)


@pytest.fixture
def response_service(mock_crud):
    service = ResponseService(session=AsyncMock())
    service.crud = mock_crud
    return service


@pytest.fixture
def mock_callback():
    callback = AsyncMock(spec=CallbackQuery)
    callback.message = AsyncMock(spec=Message)
    callback.answer = AsyncMock()
    callback.message.answer = AsyncMock()
    return callback


@pytest.mark.asyncio
async def test_get_random_response_text(response_service, mock_crud):
    mock_crud.get_random_response.return_value = Response(id=1, text="Ответ", type=ResponseEnum.TAROT)

    text = await response_service.get_random_response_text(ResponseEnum.TAROT)

    assert text == "Ответ"
    mock_crud.get_random_response.assert_called_once_with(ResponseEnum.TAROT)


@pytest.mark.asyncio
async def test_handle_response(response_service, mock_crud, mock_callback):
    mock_crud.get_random_response.return_value = Response(
        id=1, text="Тестовый ответ", type=ResponseEnum.TAROT
    )

    await response_service.handle_response(mock_callback, ResponseEnum.TAROT)

    mock_callback.message.answer.assert_any_call(text="🔮 Перемешиваю карты...")

    mock_crud.get_random_response.assert_called_once_with(ResponseEnum.TAROT)

    mock_callback.message.answer.assert_any_call(
        text="Тестовый ответ", reply_markup=builders.response_kb(ResponseEnum.TAROT)
    )

    mock_callback.answer.assert_called_once()


@pytest.mark.asyncio
async def test_handle_tarot(response_service, mock_callback):
    response_service.handle_response = AsyncMock()

    await response_service.handle_tarot(mock_callback)

    response_service.handle_response.assert_called_once_with(mock_callback, ResponseEnum.TAROT)


@pytest.mark.asyncio
async def test_handle_finance(response_service, mock_callback):
    response_service.handle_response = AsyncMock()

    await response_service.handle_finance(mock_callback)

    response_service.handle_response.assert_called_once_with(mock_callback, ResponseEnum.FINANCE)
