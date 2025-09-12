# app/db/models/pharmacy.py
from sqlalchemy import Column, Integer, String, JSON, Boolean, ForeignKey
from app.db.database import Base

class Pharmacy(Base):
    __tablename__ = "pharmacies"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    pharmacy_name = Column(String, nullable=False)
    drug_license_number = Column(String, nullable=False)
    registration_id = Column(String)
    address = Column(String, nullable=False)
    city = Column(String, nullable=False)
    state = Column(String, nullable=False)
    pin_code = Column(String, nullable=False)
    contact_number = Column(String, nullable=False)
    email = Column(String, nullable=False)
    pharmacist_name = Column(String, nullable=False)
    qualification = Column(String, nullable=False)
    pharmacist_registration_number = Column(String, nullable=False)
    experience = Column(String, nullable=False)
    additional_certifications = Column(JSON)
    gps_location = Column(String)
    services = Column(JSON)  # e.g., ["Home Delivery", "24/7 Service"]
    operating_hours = Column(JSON)  # e.g., {"open": "09:00", "close": "21:00"}
    additional_notes = Column(String)
    consent_terms = Column(Boolean, default=False)
    consent_data = Column(Boolean, default=False)
    consent_marketing = Column(Boolean, default=False)
