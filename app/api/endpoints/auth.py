from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app import models

# Create router for login/register
router = APIRouter()

# Request body models
class UserLogin(BaseModel):
    email: str
    password: str
    role: str   # 👈 role is required



class UserLogin(BaseModel):
    email: str
    password: str
    role: str

# Register endpoint
@router.post("/api/register")
def register(user: UserRegister):
    existing = models.get_user_by_email(user.email)
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")

    models.create_user(user.username, user.email, user.password, user.role)
    return {"message": "User registered successfully", "email": user.email}

# Login endpoint
@router.post("/api/login")
def login(user: UserLogin):
    db_user = models.get_user_by_email(user.email)
    if not db_user:
        raise HTTPException(status_code=401, detail="Invalid email or password")

    if not models.verify_password(user.password, db_user["password_hash"]):
        raise HTTPException(status_code=401, detail="Invalid email or password")

    if db_user["role"] != user.role:
        raise HTTPException(status_code=403, detail="Role mismatch")

    models.update_last_login(db_user["user_id"])
    return {
        "message": "Login successful",
        "token": f"fake-token-for-{db_user['email']}",  # replace with JWT later
        "role": db_user["role"],
        "email": db_user["email"]
    }
