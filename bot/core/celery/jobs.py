import asyncio

from aiogram.exceptions import TelegramBadRequest, TelegramForbiddenError
from celery import shared_task
from crud.mailing import MailingCRUD
from crud.user import UserCRUD
from utils.bot import get_bot

from core.enums import MailingStatus
from core.models import session_pool
from core.schemas.mailings import MailingUpdate


async def send_scheduled_mailings():
    bot = get_bot()
    async with session_pool() as session:
        mailing_crud = MailingCRUD(session)
        user_crud = UserCRUD(session)

    mailings = await mailing_crud.get_scheduled_mailings()
    if mailings:
        for mailing in mailings:
            if mailing.status == MailingStatus.PENDING:
                for user in await user_crud.get_all():
                    try:
                        await bot.send_message(text=mailing.text, chat_id=user.tg_id)
                        await asyncio.sleep(0.03)
                    except TelegramBadRequest:
                        continue
                    except TelegramForbiddenError:
                        continue

            await mailing_crud.update(mailing, MailingUpdate(status=MailingStatus.SENT))

    await bot.session.close()


@shared_task()
def start_mailing():
    asyncio.run(send_scheduled_mailings())
