from enum import StrEnum, auto


class MailingStatus(StrEnum):
    PENDING = auto()
    SENT = auto()
