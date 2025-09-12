# app/crud/pharmacy.py
from sqlalchemy.orm import Session
from app.db.models.pharmacy import Pharmacy
from app.db.models.user import User
from app.core.security import get_password_hash

def create_pharmacy(db: Session, pharmacy_data):
    user = User(
        username=pharmacy_data.email,
        email=pharmacy_data.email,
        hashed_password=get_password_hash(pharmacy_data.password),
        is_doctor=False
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    db_pharmacy = Pharmacy(
        user_id=user.id,
        pharmacy_name=pharmacy_data.pharmacy_name,
        drug_license_number=pharmacy_data.drug_license_number,
        registration_id=pharmacy_data.registration_id,
        address=pharmacy_data.address,
        city=pharmacy_data.city,
        state=pharmacy_data.state,
        pin_code=pharmacy_data.pin_code,
        contact_number=pharmacy_data.contact_number,
        email=pharmacy_data.email,
        pharmacist_name=pharmacy_data.pharmacist_name,
        qualification=pharmacy_data.qualification,
        pharmacist_registration_number=pharmacy_data.pharmacist_registration_number,
        experience=pharmacy_data.experience,
        additional_certifications=pharmacy_data.additional_certifications,
        gps_location=pharmacy_data.gps_location,
        services=pharmacy_data.services,
        operating_hours=pharmacy_data.operating_hours,
        additional_notes=pharmacy_data.additional_notes,
        consent_terms=pharmacy_data.consent_terms,
        consent_data=pharmacy_data.consent_data,
        consent_marketing=pharmacy_data.consent_marketing
    )
    db.add(db_pharmacy)
    db.commit()
    db.refresh(db_pharmacy)
    return db_pharmacy
