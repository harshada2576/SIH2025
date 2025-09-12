# app/api/endpoints/register.py
from fastapi import APIRouter, UploadFile, File, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.schemas.doctor import RegisterDoctorRequest
from app.db.models.doctor import Doctor
from app.core.security import get_password_hash
import os
from datetime import datetime, date

router = APIRouter()

@router.post("/register")
async def register_doctor(
    doctor_data: RegisterDoctorRequest,
    certificate: UploadFile = File(None),  # Optional file upload
    db: Session = Depends(get_db)
):
    if db.query(Doctor).filter(Doctor.email == doctor_data.email).first():
        raise HTTPException(status_code=400, detail="Email already registered")
    if db.query(Doctor).filter(Doctor.phone == doctor_data.phone).first():
        raise HTTPException(status_code=400, detail="Phone already registered")
    
    dob = doctor_data.date_of_birth
    if isinstance(dob, str):
        dob_date = datetime.strptime(dob, "%Y-%m-%d").date()
    else:
        dob_date = dob

    hashed_password = get_password_hash(doctor_data.password)

    # Save certificate if provided
    certificate_path = None
    if certificate:
        certificate_path = f"uploads/{certificate.filename}"
        with open(certificate_path, "wb") as f:
            f.write(await certificate.read())

    doctor = Doctor(
        first_name=doctor_data.first_name,
        middle_name=doctor_data.middle_name,
        last_name=doctor_data.last_name,
        gender=doctor_data.gender,
        date_of_birth=dob_date,
        phone=doctor_data.phone,
        email=doctor_data.email,
        hashed_password=hashed_password,

        registration_number=doctor_data.registration_number,
        medical_council=doctor_data.medical_council,
        specialization=doctor_data.specialization,
        sub_specialization=doctor_data.sub_specialization,
        experience=doctor_data.experience,
        qualifications=doctor_data.qualifications,
        
        hospital_name=doctor_data.hospital_name,
        consultation_type=doctor_data.consultation_type,
        hospital_address=doctor_data.hospital_address,
        consultation_fee=doctor_data.consultation_fee,
        online_fee=doctor_data.online_fee,
        
        available_timings=doctor_data.available_timings,
        account_holder_name=doctor_data.account_holder_name,
        account_number=doctor_data.account_number,
        ifsc_code=doctor_data.ifsc_code,
        bank_name=doctor_data.bank_name,
        pan_number=doctor_data.pan_number,
        gst_number=doctor_data.gst_number,
        
        upi_id=doctor_data.upi_id,
        languages=doctor_data.languages,
        emergency_contact=doctor_data.emergency_contact,
        bio=doctor_data.bio,

        certificate_path=certificate_path,  # Add to Doctor model if needed

        confirm_details=doctor_data.confirm_details,
        agree_terms=doctor_data.agree_terms,
    )

    db.add(doctor)
    db.commit()
    db.refresh(doctor)

    return {"message": "Registration successful, pending verification", "doctor_id": doctor.id}

