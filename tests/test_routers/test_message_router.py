import pytest
from unittest.mock import AsyncMock
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from services.consultation import ConsultationService
from states.consultation import ConsultationState
import message_texts
from keyboards.inline import common
from routers.message.user import handle_help, handle_name, handle_time, handle_message


@pytest.fixture
def mock_message():
    msg = AsyncMock(spec=Message)
    msg.from_user = AsyncMock()
    msg.from_user.id = 123456
    msg.text = "Тестовое сообщение"
    msg.answer = AsyncMock()
    return msg


@pytest.fixture
def mock_state():
    state = AsyncMock(spec=FSMContext)
    state.get_data.return_value = {"name": "Иван"}
    return state


@pytest.fixture
def mock_consultation_service():
    return AsyncMock(spec=ConsultationService)


@pytest.mark.asyncio
async def test_handle_help(mock_message):
    await handle_help(mock_message)

    mock_message.answer.assert_called_once_with(text=message_texts.HELP)


@pytest.mark.asyncio
async def test_handle_name(mock_message, mock_state):
    await handle_name(mock_message, mock_state)

    mock_state.update_data.assert_called_once_with(name="Тестовое сообщение")

    mock_state.set_state.assert_called_once_with(ConsultationState.time)

    mock_message.answer.assert_called_once_with(text="Введите желаемое время")


@pytest.mark.asyncio
async def test_handle_time(mock_message, mock_state, mock_consultation_service):
    await handle_time(mock_message, mock_state, mock_consultation_service)

    mock_consultation_service.add_consultation.assert_called_once_with(mock_message, mock_state)


@pytest.mark.asyncio
async def test_handle_message(mock_message):
    await handle_message(mock_message)

    mock_message.answer.assert_called_once_with(text=message_texts.START, reply_markup=common.start_kb)
