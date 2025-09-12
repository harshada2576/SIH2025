# app/api/endpoints/pharmacy.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.schemas.pharmacy import PharmacyCreate, PharmacyOut
from app.crud.pharmacy import create_pharmacy
from app.db.models.user import User

router = APIRouter()

@router.post("/register", response_model=PharmacyOut)
def register_pharmacy(pharmacy: PharmacyCreate, db: Session = Depends(get_db)):
    if db.query(User).filter(User.email == pharmacy.email).first():
        raise HTTPException(status_code=400, detail="Email already registered")
    return create_pharmacy(db, pharmacy)
