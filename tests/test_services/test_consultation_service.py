from unittest.mock import AsyncMock

import pytest
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.types import User as AiogramUser
from core.schemas.consultation import ConsultationCreate
from crud.consultation import ConsultationCRUD
from services.consultation import ConsultationService


@pytest.fixture
def mock_crud():
    return AsyncMock(spec=ConsultationCRUD)


@pytest.fixture
def consultation_service(mock_crud):
    service = ConsultationService(session=AsyncMock())
    service.crud = mock_crud
    return service


@pytest.fixture
def mock_message():
    msg = AsyncMock(spec=Message)
    msg.from_user = AiogramUser(id=123456, is_bot=False, first_name="asdf", username="testuser")
    msg.text = "10:00"
    msg.answer = AsyncMock()
    return msg


@pytest.fixture
def mock_state():
    state = AsyncMock(spec=FSMContext)
    state.get_data.return_value = {"name": "Иван", "time": "10:00"}
    return state


@pytest.mark.asyncio
async def test_add_consultation_creates_entry(consultation_service, mock_crud, mock_message, mock_state):
    await consultation_service.add_consultation(mock_message, mock_state)

    mock_state.update_data.assert_called_once_with(time="10:00")

    mock_state.get_data.assert_called_once()

    mock_state.clear.assert_called_once()

    mock_crud.create.assert_called_once_with(
        ConsultationCreate(name="Иван", username="@testuser", time="10:00")
    )

    mock_message.answer.assert_called_once_with("Заявка создана, пожалуйста ожидайте, вам напишут")
