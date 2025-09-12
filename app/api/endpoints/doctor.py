from fastapi import APIRouter

router = APIRouter()

@router.get("/dashboard")
def get_doctor_dashboard():
    return {"appointments": ["Patient A - 10AM", "Patient B - 2PM"]}

