# app/schemas/prescription.py
from pydantic import BaseModel
from datetime import datetime

class PrescriptionOut(BaseModel):
    id: int
    patient_id: int
    doctor_id: int
    pharmacy_id: int | None
    medications: str
    created_at: datetime
    status: str

    class Config:
        orm_mode = True
