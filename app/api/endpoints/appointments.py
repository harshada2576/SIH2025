# app/api/endpoints/appointments.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.schemas.appointment import AppointmentCreate, AppointmentOut
from app.crud.appointment import create_appointment, get_appointments_by_patient, get_appointments_by_doctor, cancel_appointment
from app.api.deps import get_current_user
from app.db.models.user import User

router = APIRouter()

@router.post("/book", response_model=AppointmentOut)
def book_appointment(
    appointment: AppointmentCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    if current_user.is_doctor:
        raise HTTPException(status_code=403, detail="Doctors cannot book appointments")
    return create_appointment(db, appointment, patient_id=current_user.id)

@router.get("/patient", response_model=list[AppointmentOut])
def get_patient_appointments(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    if current_user.is_doctor:
        raise HTTPException(status_code=403, detail="Doctors cannot view patient appointments")
    return get_appointments_by_patient(db, patient_id=current_user.id)

@router.get("/doctor", response_model=list[AppointmentOut])
def get_doctor_appointments(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    if not current_user.is_doctor:
        raise HTTPException(status_code=403, detail="Only doctors can view their appointments")
    doctor = db.query(Doctor).filter(Doctor.email == current_user.email).first()
    if not doctor:
        raise HTTPException(status_code=404, detail="Doctor not found")
    return get_appointments_by_doctor(db, doctor_id=doctor.id)

@router.post("/cancel/{appointment_id}")
def cancel_appointment_endpoint(
    appointment_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    appointment = cancel_appointment(db, appointment_id)
    if not appointment:
        raise HTTPException(status_code=404, detail="Appointment not found")
    return {"message": "Appointment canceled"}
