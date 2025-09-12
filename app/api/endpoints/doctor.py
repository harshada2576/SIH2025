# app/api/endpoint/doctor.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.api.deps import get_current_doctor
from app.db.models.doctor import Doctor
from app.crud.appointment import get_appointments_by_doctor
from app.db.models.user import User


router = APIRouter()

@router.get("/dashboard")
def get_doctor_dashboard(
    current_doctor: Doctor = Depends(get_current_doctor),
    db: Session = Depends(get_db)
):
    appointments = get_appointments_by_doctor(db, doctor_id=current_doctor.id)
    return {
        "doctor": f"{current_doctor.first_name} {current_doctor.last_name}",
        "appointments": [
            {
                "id": appt.id,
                "patient_id": appt.patient_id,
                "time": appt.appointment_time.isoformat(),
                "status": appt.status,
                "type": appt.consultation_type
            } for appt in appointments
        ]
    }

@router.get("/list", response_model=list[dict])
def get_doctors_list(db: Session = Depends(get_db)):
    doctors = db.query(Doctor).filter(Doctor.is_verified == True, Doctor.is_active == True).all()
    return [
        {
            "id": doctor.id,
            "name": f"{doctor.first_name} {doctor.last_name}",
            "specialization": doctor.specialization,
            "hospital_name": doctor.hospital_name,
            "consultation_fee": doctor.consultation_fee,
            "online_fee": doctor.online_fee,
            "available_timings": doctor.available_timings
        } for doctor in doctors
    ]

