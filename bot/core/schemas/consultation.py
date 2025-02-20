from pydantic import BaseModel


class ConsultationCreate(BaseModel):
    username: str
    name: str
    time: str
