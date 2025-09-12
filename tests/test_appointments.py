# tests/test_appointments.py

from fastapi.testclient import TestClient
from app.main import app
from app.core.security import create_access_token

client = TestClient(app)

def test_book_appointment():
    token = create_access_token(data={"sub": "ramesh123"})
    response = client.post(
        "/appointments/book",
        json={
            "doctor_id": 1,
            "appointment_time": "2025-09-15T10:00:00",
            "consultation_type": "online"
        },
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 200
    assert response.json()["consultation_type"] == "online"
    assert response.json()["status"] == "scheduled"

def test_get_patient_appointments():
    token = create_access_token(data={"sub": "ramesh123"})
    response = client.get(
        "/appointments/patient",
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_doctor_appointments():
    token = create_access_token(data={"sub": "anil.verma@clinic.com"})
    response = client.get(
        "/appointments/doctor",
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_cancel_appointment():
    token = create_access_token(data={"sub": "ramesh123"})
    book_response = client.post(
        "/appointments/book",
        json={
            "doctor_id": 1,
            "appointment_time": "2025-09-15T11:00:00",
            "consultation_type": "offline"
        },
        headers={"Authorization": f"Bearer {token}"}
    )
    appointment_id = book_response.json()["id"]
    response = client.post(
        f"/appointments/cancel/{appointment_id}",
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 200
    assert response.json() == {"message": "Appointment canceled"}
