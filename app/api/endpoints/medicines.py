# app/api/endpoints/medicines.py
from fastapi import APIRouter

router = APIRouter()

@router.get("/compare")
def compare_medicines():
    return {
        "message": "Medicine comparison (simulated for demo)",
        "medicines": [
            {"name": "Paracetamol", "price": 50},
            {"name": "Ibuprofen", "price": 75}
        ]
    }
