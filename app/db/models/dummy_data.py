# app/db/models/dummy_data
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../..')))

from app.db.database import SessionLocal, engine, Base
from app.db.models.user import User
from app.db.models.doctor import Doctor
from app.db.models.patient import Patient
from app.db.models.appointment import Appointment
from app.core.security import get_password_hash  # Import password hashing
from datetime import datetime, date

# Create tables if not exist
Base.metadata.create_all(bind=engine)

db = SessionLocal()

# Generate a hashed password for dummy data (e.g., password: "password123")
hashed_password = get_password_hash("password123")

# --- Dummy Patients (Users) ---
patients = [
    User(username="ramesh123", email="ramesh.patil@example.com", hashed_password=hashed_password, is_doctor=False),
    User(username="geeta456", email="geeta.sharma@example.com", hashed_password=hashed_password, is_doctor=False),
    User(username="sunita789", email="sunita.yadav@example.com", hashed_password=hashed_password, is_doctor=False),
    User(username="akash321", email="akash.kumar@example.com", hashed_password=hashed_password, is_doctor=False),
    User(username="meena654", email="meena.joshi@example.com", hashed_password=hashed_password, is_doctor=False),
]

# --- Dummy Doctors (Users) ---
doctor_users = [
    User(username="anil.verma@clinic.com", email="anil.verma@clinic.com", hashed_password=hashed_password, is_doctor=True),
    User(username="savita.patil@clinic.com", email="savita.patil@clinic.com", hashed_password=hashed_password, is_doctor=True),
    User(username="rajesh.kumar@clinic.com", email="rajesh.kumar@clinic.com", hashed_password=hashed_password, is_doctor=True),
    User(username="meera.joshi@clinic.com", email="meera.joshi@clinic.com", hashed_password=hashed_password, is_doctor=True),
    User(username="irfan.shaikh@clinic.com", email="irfan.shaikh@clinic.com", hashed_password=hashed_password, is_doctor=True),
]

# --- Dummy Doctors ---
doctors = [
    Doctor(
        first_name="Anil", last_name="Verma", gender="Male",
        date_of_birth=date(1978, 5, 14), phone="9876543210", email="anil.verma@clinic.com",
        hashed_password=hashed_password, registration_number="DOC1001",
        medical_council="MCI", specialization="General Physician", sub_specialization="",
        experience=15, qualifications="MBBS", hospital_name="Gram Panchayat Clinic",
        consultation_type="Offline", hospital_address="Village Clinic, Maharashtra",
        consultation_fee=200, online_fee=100, available_timings={"Monday": ["9-12"], "Tuesday": ["2-5"]},
        account_holder_name="Anil Verma", account_number="1234567890", ifsc_code="SBIN000111",
        bank_name="SBI", pan_number="ABCDE1234F", gst_number="29ABCDE1234F1Z5", upi_id="anilverma@upi",
        languages=["Marathi", "Hindi"], emergency_contact="9123456789", bio="Village doctor serving since 2005.",
        confirm_details=True, agree_terms=True, is_verified=True, is_active=True
    ),
    Doctor(
        first_name="Savita", last_name="Patil", gender="Female",
        date_of_birth=date(1985, 3, 22), phone="9123456789", email="savita.patil@clinic.com",
        hashed_password=hashed_password, registration_number="DOC1002",
        medical_council="MCI", specialization="Gynecology", sub_specialization="",
        experience=12, qualifications="MBBS, DGO", hospital_name="Rural Health Center",
        consultation_type="Both", hospital_address="Health Center, Karnataka",
        consultation_fee=300, online_fee=150, available_timings={"Wednesday": ["10-1"], "Friday": ["3-6"]},
        account_holder_name="Savita Patil", account_number="1234567891", ifsc_code="SBIN000222",
        bank_name="SBI", pan_number="BCDEF2345G", gst_number="29BCDEF2345G1Z6", upi_id="savitapatil@upi",
        languages=["Kannada", "Hindi"], emergency_contact="9345678901", bio="Focused on women’s healthcare.",
        confirm_details=True, agree_terms=True, is_verified=True, is_active=True
    ),
    Doctor(
        first_name="Rajesh", last_name="Kumar", gender="Male",
        date_of_birth=date(1980, 9, 10), phone="9345678901", email="rajesh.kumar@clinic.com",
        hashed_password=hashed_password, registration_number="DOC1003",
        medical_council="MCI", specialization="Pediatrics", sub_specialization="",
        experience=18, qualifications="MBBS, MD Pediatrics", hospital_name="Block Hospital",
        consultation_type="Offline", hospital_address="Community Hospital, Bihar",
        consultation_fee=250, online_fee=120, available_timings={"Monday": ["8-11"], "Thursday": ["2-4"]},
        account_holder_name="Rajesh Kumar", account_number="1234567892", ifsc_code="SBIN000333",
        bank_name="SBI", pan_number="CDEFG3456H", gst_number="29CDEFG3456H1Z7", upi_id="rajeshkumar@upi",
        languages=["Hindi", "Bhojpuri"], emergency_contact="9456789012", bio="Helping children in rural areas.",
        confirm_details=True, agree_terms=True, is_verified=True, is_active=True
    ),
    Doctor(
        first_name="Meera", last_name="Joshi", gender="Female",
        date_of_birth=date(1990, 6, 5), phone="9456789012", email="meera.joshi@clinic.com",
        hashed_password=hashed_password, registration_number="DOC1004",
        medical_council="MCI", specialization="Dermatology", sub_specialization="",
        experience=8, qualifications="MBBS, DDVL", hospital_name="Primary Health Center",
        consultation_type="Both", hospital_address="PHC, Uttar Pradesh",
        consultation_fee=350, online_fee=200, available_timings={"Tuesday": ["11-2"], "Saturday": ["9-12"]},
        account_holder_name="Meera Joshi", account_number="1234567893", ifsc_code="SBIN000444",
        bank_name="SBI", pan_number="DEFGH4567I", gst_number="29DEFGH4567I1Z8", upi_id="meerajoshi@upi",
        languages=["Hindi"], emergency_contact="9567890123", bio="Dermatologist with rural outreach programs.",
        confirm_details=True, agree_terms=True, is_verified=True, is_active=True
    ),
    Doctor(
        first_name="Irfan", last_name="Shaikh", gender="Male",
        date_of_birth=date(1983, 11, 18), phone="9567890123", email="irfan.shaikh@clinic.com",
        hashed_password=hashed_password, registration_number="DOC1005",
        medical_council="MCI", specialization="Orthopedics", sub_specialization="",
        experience=14, qualifications="MBBS, MS Ortho", hospital_name="District Hospital",
        consultation_type="Offline", hospital_address="District Hospital, Rajasthan",
        consultation_fee=400, online_fee=220, available_timings={"Monday": ["10-1"], "Friday": ["4-6"]},
        account_holder_name="Irfan Shaikh", account_number="1234567894", ifsc_code="SBIN000555",
        bank_name="SBI", pan_number="EFGHI5678J", gst_number="29EFGHI5678J1Z9", upi_id="irfanshaikh@upi",
        languages=["Hindi", "Rajasthani"], emergency_contact="9678901234", bio="Orthopedic specialist in rural care.",
        confirm_details=True, agree_terms=True, is_verified=True, is_active=True
    ),
]

patients_data = [
    Patient(
        user_id=1,  # ramesh123
        first_name="Ramesh", last_name="Patil",
        date_of_birth=date(1990, 1, 1),
        gender="Male", blood_group="A+",
        address="123 Village Road, Maharashtra",
        allergies=["none"], current_medications=["none"],
        medical_conditions=["none"],
        consent_terms=True, consent_accuracy=True
    ),
    Patient(
        user_id=2,  # geeta456
        first_name="Geeta", last_name="Sharma",
        date_of_birth=date(1985, 5, 15),
        gender="Female", blood_group="B+",
        address="456 Rural Lane, Karnataka",
        allergies=["pollen"], current_medications=["antihistamine"],
        medical_conditions=["asthma"],
        consent_terms=True, consent_accuracy=True
    ),
]

appointments = [
    Appointment(
        patient_id=1,  # ramesh123
        doctor_id=1,  # Anil Verma
        appointment_time=datetime(2025, 9, 13, 10, 0),
        consultation_type="online",
        status="scheduled"
    ),
    Appointment(
        patient_id=2,  # geeta456
        doctor_id=2,  # Savita Patil
        appointment_time=datetime(2025, 9, 14, 14, 0),
        consultation_type="offline",
        status="scheduled"
    ),
]

# Insert patients, doctor users, doctors, appointments, and patients
db.add_all(patients + doctor_users + doctors + appointments + patients_data)
db.commit()
db.close()

print("✅ Inserted 5 dummy patients and 5 dummy doctors, and 2 dummy appointments (Indian villagers).")
