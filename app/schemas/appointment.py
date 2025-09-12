# app/schemas/appointment.py
from pydantic import BaseModel
from datetime import datetime

class AppointmentCreate(BaseModel):
    doctor_id: int
    appointment_time: datetime
    consultation_type: str

class AppointmentOut(BaseModel):
    id: int
    patient_id: int
    doctor_id: int
    appointment_time: datetime
    status: str
    consultation_type: str
    created_at: datetime

    class Config:
        orm_mode = True
