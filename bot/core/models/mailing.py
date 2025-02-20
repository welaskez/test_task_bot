from datetime import datetime

from sqlalchemy import DateTime, Enum
from sqlalchemy.orm import Mapped, mapped_column

from ..enums import MailingStatus
from .base import Base
from .mixins import CreatedAtMixin, UpdatedAtMixin, UuidPkMixin


class Mailing(UuidPkMixin, CreatedAtMixin, UpdatedAtMixin, Base):
    time: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    text: Mapped[str]
    status: Mapped[MailingStatus] = mapped_column(Enum(MailingStatus))
