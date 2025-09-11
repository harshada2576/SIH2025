from fastapi import APIRouter

router = APIRouter()

@router.get("/dashboard")
def get_patient_dashboard():
    return {"upcoming": ["Dr. X - 10AM", "Dr. Y - 5PM"]}

