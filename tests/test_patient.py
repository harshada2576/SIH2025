from fastapi.testclient import TestClient
from app.main import app
from app.core.security import create_access_token

client = TestClient(app)

def test_register_patient():
    response = client.post(
        "/patient/register",
        json={
            "first_name": "Jane",
            "last_name": "Doe",
            "email": "jane.doe@example.com",
            "password": "testpass123",
            "date_of_birth": "1995-01-01",
            "gender": "Female",
            "blood_group": "O+",
            "address": "456 Main St",
            "allergies": ["none"],
            "current_medications": ["none"],
            "medical_conditions": ["none"],
            "consent_terms": True,
            "consent_accuracy": True
        }
    )
    assert response.status_code == 200
    assert response.json()["email"] == "jane.doe@example.com"

def test_get_patient_dashboard():
    client.post(
        "/patient/register",
        json={
            "first_name": "Jane",
            "last_name": "Doe",
            "email": "jane.doe@example.com",
            "password": "testpass123",
            "date_of_birth": "1995-01-01",
            "gender": "Female",
            "blood_group": "O+",
            "address": "456 Main St",
            "allergies": ["none"],
            "current_medications": ["none"],
            "medical_conditions": ["none"],
            "consent_terms": True,
            "consent_accuracy": True
        }
    )
    token = create_access_token(data={"sub": "jane.doe@example.com"})
    response = client.get(
        "/patient/dashboard",
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 200
    assert "patient" in response.json()
    assert "appointments" in response.json()
