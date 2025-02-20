from unittest.mock import AsyncMock

import pytest
from aiogram.types import Message
from aiogram.types import User as AiogramUser
from core.models import User
from core.schemas.user import UserCreate
from crud.user import UserCRUD
from services.user import UserService


@pytest.fixture
def mock_user_crud():
    return AsyncMock(spec=UserCRUD)


@pytest.fixture
def user_service(mock_user_crud):
    service = UserService(session=AsyncMock())
    service.crud = mock_user_crud
    return service


@pytest.fixture
def mock_message():
    msg = AsyncMock(spec=Message)
    msg.from_user = AiogramUser(id=123456, is_bot=False, first_name="asdf")
    msg.answer = AsyncMock()
    return msg


@pytest.mark.asyncio
async def test_handle_start_creates_user(user_service, mock_user_crud, mock_message):
    mock_user_crud.get_one_by_expression.return_value = None
    mock_user_crud.create.return_value = User(id=1, tg_id=123456)

    await user_service.handle_start(mock_message)

    mock_user_crud.create.assert_called_once_with(UserCreate(tg_id=123456))
    mock_message.answer.assert_called_once()
