# tests/test_auth.py

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_register_user():
    response = client.post(
        "/auth/register",
        json={
            "username": "testuser",
            "email": "testuser@example.com",
            "password": "testpass123",
            "is_doctor": False
        }
    )
    assert response.status_code == 200
    assert response.json() == {"message": "User registered", "user": "testuser"}

def test_login_user():
    client.post(
        "/auth/register",
        json={
            "username": "testlogin",
            "email": "testlogin@example.com",
            "password": "testpass123",
            "is_doctor": False
        }
    )
    response = client.post(
        "/auth/login",
        json={"username": "testlogin@example.com", "password": "testpass123"}
    )
    assert response.status_code == 200
    assert "access_token" in response.json()
    assert response.json()["token_type"] == "bearer"

def test_login_invalid_credentials():
    response = client.post(
        "/auth/login",
        json={"username": "nonexistent", "password": "wrongpass"}
    )
    assert response.status_code == 400
    assert response.json() == {"detail": "Invalid credentials"}

def test_forgot_password():
    client.post(
        "/auth/register",
        json={
            "username": "testforgot",
            "email": "testforgot@example.com",
            "password": "testpass123",
            "is_doctor": False
        }
    )
    response = client.post(
        "/auth/forgot-password",
        json={"email": "testforgot@example.com"}
    )
    assert response.status_code == 200
    assert response.json() == {"message": "Reset link sent to your email (simulated for demo)"}
