from pydantic import BaseModel

from core.enums import MailingStatus


class MailingUpdate(BaseModel):
    status: MailingStatus | None = None
