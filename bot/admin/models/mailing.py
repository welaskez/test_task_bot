from core.models import Mailing
from sqladmin import ModelView


class MailingAdmin(ModelView, model=Mailing):
    column_list = [Mailing.time, Mailing.text, Mailing.status]
    form_excluded_columns = [Mailing.created_at, Mailing.updated_at]
