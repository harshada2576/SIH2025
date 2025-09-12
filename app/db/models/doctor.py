# app/db/models/doctor

from sqlalchemy import Column, Integer, String, Boolean, Date, LargeBinary, JSON
from app.db.database import Base

class Doctor(Base):
    __tablename__ = "doctors"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    middle_name = Column(String)
    last_name = Column(String, nullable=False)
    gender = Column(String)
    date_of_birth = Column(Date)
    phone = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)

    # Professional info
    registration_number = Column(String)
    medical_council = Column(String)
    specialization = Column(String)
    sub_specialization = Column(String)
    experience = Column(Integer)
    qualifications = Column(String)

    # app/db/models/doctor.py
    certificate_path = Column(String, nullable=True)
    
    # Practice info
    hospital_name = Column(String)
    consultation_type = Column(String)
    hospital_address = Column(String)
    consultation_fee = Column(Integer)
    online_fee = Column(Integer)
    available_timings = Column(JSON)  # store as JSON: {"Monday": ["9-11", "2-4"], ...}
    
    # Banking info
    account_holder_name = Column(String)
    account_number = Column(String)
    ifsc_code = Column(String)
    bank_name = Column(String)
    pan_number = Column(String)
    gst_number = Column(String)
    upi_id = Column(String)

    # Additional info
    languages = Column(JSON)  # store list of languages as JSON
    emergency_contact = Column(String)
    bio = Column(String)

    # Agreements
    confirm_details = Column(Boolean, default=False)
    agree_terms = Column(Boolean, default=False)

    # Status and verification
    is_verified = Column(Boolean, default=False)
    is_active = Column(Boolean, default=True)

