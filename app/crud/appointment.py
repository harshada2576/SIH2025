# app/crud/appointment.py
from sqlalchemy.orm import Session
from app.db.models.appointment import Appointment

def create_appointment(db: Session, appointment_data, patient_id: int):
    db_appointment = Appointment(
        patient_id=patient_id,
        doctor_id=appointment_data.doctor_id,
        appointment_time=appointment_data.appointment_time,
        consultation_type=appointment_data.consultation_type
    )
    db.add(db_appointment)
    db.commit()
    db.refresh(db_appointment)
    return db_appointment

def get_appointments_by_patient(db: Session, patient_id: int):
    return db.query(Appointment).filter(Appointment.patient_id == patient_id).all()

def get_appointments_by_doctor(db: Session, doctor_id: int):
    return db.query(Appointment).filter(Appointment.doctor_id == doctor_id).all()

def cancel_appointment(db: Session, appointment_id: int):
    appointment = db.query(Appointment).filter(Appointment.id == appointment_id).first()
    if appointment:
        appointment.status = "canceled"
        db.commit()
        db.refresh(appointment)
    return appointment
