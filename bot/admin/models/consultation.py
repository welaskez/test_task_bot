from core.models import Consultation
from sqladmin import ModelView


class ConsultationAdmin(ModelView, model=Consultation):
    column_list = [Consultation.name, Consultation.username, Consultation.time]
