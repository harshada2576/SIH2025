# app/crud/user

from sqlalchemy.orm import Session
from app.db.models.user import User
from app.core.security import get_password_hash, verify_password

def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()

def create_user(db: Session, user_data):
    hashed_pw = get_password_hash(user_data.password)
    db_user = User(
        username=user_data.username,
        email=user_data.email,
        hashed_password=hashed_pw,
        is_doctor=user_data.is_doctor
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

