# app/api/endpoints/auth

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, UserLogin
from app.crud import user as crud_user
from app.db.database import get_db
from app.db.models.user import User
from app.core.security import verify_password, create_access_token
from pydantic import BaseModel
from datetime import timedelta

router = APIRouter()

class ForgotPasswordRequest(BaseModel):
    email: str

@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    db_user = crud_user.get_user_by_username(db, user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already exists")
    new_user = crud_user.create_user(db, user)
    return {"message": "User registered", "user": new_user.username}

@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    # Check username or email
    db_user = crud_user.get_user_by_username(db, user.username)
    if not db_user:
        db_user = db.query(User).filter(User.email == user.username).first()
    if not db_user or not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    
    access_token = create_access_token(
        data={"sub": db_user.username},
        expires_delta=timedelta(minutes=60)
    )
    return {"access_token": access_token, "token_type": "bearer"}
    

@router.post("/forgot-password")
def forgot_password(request: ForgotPasswordRequest, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == request.email).first()
    if not user:
        raise HTTPException(status_code=404, detail="Email not found")
    return {"message": "Reset link sent to your email (simulated for demo)"}
