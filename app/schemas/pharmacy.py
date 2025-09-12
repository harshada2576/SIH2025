# app/schemas/pharmacy.py
from pydantic import BaseModel, EmailStr
from typing import List, Optional, Dict

class PharmacyCreate(BaseModel):
    pharmacy_name: str
    drug_license_number: str
    registration_id: Optional[str] = None
    address: str
    city: str
    state: str
    pin_code: str
    contact_number: str
    email: EmailStr
    password: str
    pharmacist_name: str
    qualification: str
    pharmacist_registration_number: str
    experience: str
    additional_certifications: List[str] = []
    gps_location: Optional[str] = None
    services: List[str] = []
    operating_hours: Dict[str, str] = {}
    additional_notes: Optional[str] = None
    consent_terms: bool
    consent_data: bool
    consent_marketing: bool

class PharmacyOut(BaseModel):
    id: int
    user_id: int
    pharmacy_name: str
    email: EmailStr
    city: str
    state: str

    class Config:
        orm_mode = True
