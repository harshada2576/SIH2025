# app/db/models/patient.py
from sqlalchemy import Column, Integer, String, Date, JSON, Boolean, ForeignKey
from app.db.database import Base

class Patient(Base):
    __tablename__ = "patients"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    date_of_birth = Column(Date)
    gender = Column(String)
    blood_group = Column(String)
    address = Column(String)
    allergies = Column(JSON)  # Store as list, e.g., ["peanuts", "penicillin"]
    current_medications = Column(JSON)  # Store as list
    medical_conditions = Column(JSON)  # Store as list
    consent_terms = Column(Boolean, default=False)
    consent_accuracy = Column(Boolean, default=False)
