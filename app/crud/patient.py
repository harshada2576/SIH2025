# app/crud/patient.py
from sqlalchemy.orm import Session
from app.db.models.patient import Patient
from app.db.models.user import User
from app.core.security import get_password_hash

def create_patient(db: Session, patient_data):
    # Create user
    user = User(
        username=patient_data.email,
        email=patient_data.email,
        hashed_password=get_password_hash(patient_data.password),
        is_doctor=False
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    # Create patient
    db_patient = Patient(
        user_id=user.id,
        first_name=patient_data.first_name,
        last_name=patient_data.last_name,
        date_of_birth=patient_data.date_of_birth,
        gender=patient_data.gender,
        blood_group=patient_data.blood_group,
        address=patient_data.address,
        allergies=patient_data.allergies,
        current_medications=patient_data.current_medications,
        medical_conditions=patient_data.medical_conditions,
        consent_terms=patient_data.consent_terms,
        consent_accuracy=patient_data.consent_accuracy
    )
    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)
    return db_patient
