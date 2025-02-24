from admin.models import ConsultationAdmin, MailingAdmin
from core.models import engine
from fastapi import FastAPI
from sqladmin import Admin


def create_admin_panel(app: FastAPI):
    admin = Admin(
        app=app,
        engine=engine,
    )
    admin.add_view(ConsultationAdmin)
    admin.add_view(MailingAdmin)
