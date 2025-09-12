# app/schemas/patient.py
from pydantic import BaseModel, EmailStr
from datetime import date
from typing import List, Optional

class PatientCreate(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    password: str
    date_of_birth: date
    gender: str
    blood_group: str
    address: Optional[str] = None
    allergies: List[str] = []
    current_medications: List[str] = []
    medical_conditions: List[str] = []
    consent_terms: bool
    consent_accuracy: bool

class PatientOut(BaseModel):
    id: int
    user_id: int
    first_name: str
    last_name: str
    email: str
    date_of_birth: date
    gender: str
    blood_group: str
    address: Optional[str]
    allergies: List[str]
    current_medications: List[str]
    medical_conditions: List[str]

    class Config:
        orm_mode = True
