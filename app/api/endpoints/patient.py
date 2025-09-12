# app/api/endpoint/patient

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.schemas.patient import PatientCreate, PatientOut
from app.crud.patient import create_patient
from app.api.deps import get_current_user
from app.db.models.user import User
from app.db.models.doctor import Doctor
from app.db.models.patient import Patient
from app.db.models.appointment import Appointment

router = APIRouter()

@router.post("/register", response_model=PatientOut)
def register_patient(patient: PatientCreate, db: Session = Depends(get_db)):
    if db.query(User).filter((User.email == patient.email) | (User.username == patient.email)).first():
        raise HTTPException(status_code=400, detail="Email or username already registered")
    return create_patient(db, patient)

@router.get("/dashboard")
def get_patient_dashboard(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    if current_user.is_doctor:
        raise HTTPException(status_code=403, detail="Doctors cannot view patient dashboard")
    appointments = db.query(Appointment).filter(Appointment.patient_id == current_user.id).all()
    return {
        "patient": current_user.username,
        "appointments": [
            {
                "id": appt.id,
                "doctor": f"{db.query(Doctor).filter(Doctor.id == appt.doctor_id).first().first_name} {db.query(Doctor).filter(Doctor.id == appt.doctor_id).first().last_name}",
                "time": appt.appointment_time.isoformat(),
                "status": appt.status,
                "type": appt.consultation_type
            } for appt in appointments
        ]
    }

@router.get("/info")
def get_patient_info(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    if current_user.is_doctor:
        raise HTTPException(status_code=403, detail="Doctors cannot view patient info")
    patient = db.query(Patient).filter(Patient.user_id == current_user.id).first()
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    return {
        "patient_id": patient.id,
        "name": f"{patient.first_name} {patient.last_name}",
        "blood_group": patient.blood_group,
        "last_updated": patient.date_of_birth,  # Placeholder, update if you add a timestamp
        "allergies": patient.allergies,
        "medical_conditions": patient.medical_conditions,
        "current_medications": patient.current_medications
    }

