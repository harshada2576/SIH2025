# app/api/deps.py

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from sqlalchemy.orm import Session  # Import Session directly from sqlalchemy.orm
from app.core.security import ALGORITHM, SECRET_KEY
from app.db.database import get_db
from app.db.models.user import User
from app.db.models.doctor import Doctor

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = db.query(User).filter(User.username == username).first()
    if user is None:
        raise credentials_exception
    return user

def get_current_doctor(current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    if not current_user.is_doctor:
        raise HTTPException(status_code=403, detail="Not authorized as doctor")
    doctor = db.query(Doctor).filter(Doctor.email == current_user.email).first()
    if not doctor:
        raise HTTPException(status_code=404, detail="Doctor not found")
    return doctor
