# app/api/endpoints/prescriptions.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.schemas.prescription import PrescriptionOut
from app.db.models.prescription import Prescription
from app.api.deps import get_current_user
from app.db.models.user import User

router = APIRouter()

@router.get("/pharmacy", response_model=list[PrescriptionOut])
def get_pharmacy_prescriptions(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    pharmacy = db.query(Pharmacy).filter(Pharmacy.email == current_user.email).first()
    if not pharmacy:
        raise HTTPException(status_code=403, detail="Not authorized as pharmacy")
    prescriptions = db.query(Prescription).filter(Prescription.pharmacy_id == pharmacy.id).all()
    return prescriptions
