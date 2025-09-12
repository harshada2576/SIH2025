# tests/test_doctor.py
from fastapi.testclient import TestClient
from app.main import app
from app.core.security import create_access_token

client = TestClient(app)

def test_get_doctor_dashboard():
    # Login as a doctor (using dummy data: anil.verma@clinic.com)
    token = create_access_token(data={"sub": "anil.verma@clinic.com"})
    response = client.get(
        "/doctor/dashboard",
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 200
    assert "doctor" in response.json()
    assert "appointments" in response.json()

def test_get_doctor_list():
    response = client.get("/doctor/list")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) > 0
    assert "name" in response.json()[0]
    assert "specialization" in response.json()[0]
