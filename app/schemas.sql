CREATE TABLE users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    phone TEXT UNIQUE,
    role TEXT NOT NULL CHECK(role IN ('patient', 'doctor', 'pharmacist', 'organization_admin')),
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    last_login DATETIME
);

-- PATIENTS: Patient-specific info, linked 1:1 with users
CREATE TABLE patients (
    patient_id INTEGER PRIMARY KEY,
    user_id INTEGER UNIQUE NOT NULL REFERENCES users(user_id) ON DELETE CASCADE,
    full_name TEXT NOT NULL,
    dob DATE,
    gender TEXT CHECK(gender IN ('male', 'female', 'other')),
    address TEXT,
    emergency_contact_name TEXT,
    emergency_contact_phone TEXT
);

-- DOCTORS: Doctor-specific info
CREATE TABLE doctors (
    doctor_id INTEGER PRIMARY KEY,
    user_id INTEGER UNIQUE NOT NULL REFERENCES users(user_id) ON DELETE CASCADE,
    full_name TEXT NOT NULL,
    specialization TEXT,
    license_number TEXT UNIQUE,
    clinic_address TEXT,
    available BOOLEAN DEFAULT TRUE
);

-- PHARMACISTS: Pharmacist-specific info
CREATE TABLE pharmacists (
    pharmacist_id INTEGER PRIMARY KEY,
    user_id INTEGER UNIQUE NOT NULL REFERENCES users(user_id) ON DELETE CASCADE,
    full_name TEXT NOT NULL,
    pharmacy_id INTEGER NOT NULL REFERENCES pharmacies(pharmacy_id) ON DELETE SET NULL
);

-- ORGANIZATIONS: Hospitals, Blood Banks, Pharmacies
CREATE TABLE organizations (
    organization_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    type TEXT NOT NULL CHECK(type IN ('hospital', 'blood_bank', 'pharmacy')),
    address TEXT,
    phone TEXT,
    email TEXT
);

-- LINK ORGANIZATION ADMINS TO ORGANIZATIONS
CREATE TABLE organization_admins (
    admin_id INTEGER PRIMARY KEY,
    user_id INTEGER UNIQUE NOT NULL REFERENCES users(user_id) ON DELETE CASCADE,
    organization_id INTEGER NOT NULL REFERENCES organizations(organization_id) ON DELETE CASCADE
);

-- PHARMACIES: Subset of organizations with type = 'pharmacy'
CREATE TABLE pharmacies (
    pharmacy_id INTEGER PRIMARY KEY,
    organization_id INTEGER UNIQUE NOT NULL REFERENCES organizations(organization_id) ON DELETE CASCADE
);

-- BLOOD BANKS: Subset of organizations with type = 'blood_bank'
CREATE TABLE blood_banks (
    blood_bank_id INTEGER PRIMARY KEY,
    organization_id INTEGER UNIQUE NOT NULL REFERENCES organizations(organization_id) ON DELETE CASCADE,
    blood_type TEXT NOT NULL, -- example: "A+", "O-", etc.
    units_available INTEGER DEFAULT 0
);

-- MEDICINES: Master list of medicines
CREATE TABLE medicines (
    medicine_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    description TEXT,
    generic_name TEXT,
    manufacturer TEXT
);

-- PHARMACY_MEDICINES: Medicine stock & availability at pharmacies
CREATE TABLE pharmacy_medicines (
    pharmacy_medicine_id INTEGER PRIMARY KEY,
    pharmacy_id INTEGER NOT NULL REFERENCES pharmacies(pharmacy_id) ON DELETE CASCADE,
    medicine_id INTEGER NOT NULL REFERENCES medicines(medicine_id) ON DELETE CASCADE,
    stock_quantity INTEGER DEFAULT 0,
    UNIQUE(pharmacy_id, medicine_id)
);

-- PATIENT REPORTS: Stores diagnostic reports, images, documents etc.
CREATE TABLE patient_reports (
    report_id INTEGER PRIMARY KEY,
    patient_id INTEGER NOT NULL REFERENCES patients(patient_id) ON DELETE CASCADE,
    doctor_id INTEGER REFERENCES doctors(doctor_id),
    report_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    report_type TEXT,
    description TEXT,
    file_path TEXT -- path to stored file if applicable
);

-- CONSULTATIONS: Telemedicine consultations between patient and doctor
CREATE TABLE consultations (
    consultation_id INTEGER PRIMARY KEY,
    patient_id INTEGER NOT NULL REFERENCES patients(patient_id) ON DELETE CASCADE,
    doctor_id INTEGER NOT NULL REFERENCES doctors(doctor_id) ON DELETE CASCADE,
    consultation_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    status TEXT CHECK(status IN ('scheduled', 'completed', 'cancelled')) DEFAULT 'scheduled',
    notes TEXT,
    offline_data TEXT -- store offline session data in base64/json if needed
);

-- PRESCRIPTIONS: Medicines prescribed by doctors for a consultation
CREATE TABLE prescriptions (
    prescription_id INTEGER PRIMARY KEY,
    consultation_id INTEGER NOT NULL REFERENCES consultations(consultation_id) ON DELETE CASCADE,
    medicine_id INTEGER NOT NULL REFERENCES medicines(medicine_id) ON DELETE RESTRICT,
    dosage TEXT,
    frequency TEXT,
    duration TEXT,
    notes TEXT
);

-- ALTERNATIVE_MEDICINES: Alternatives suggested by pharmacist if prescribed medicine unavailable
CREATE TABLE alternative_medicines (
    alt_medicine_id INTEGER PRIMARY KEY,
    prescription_id INTEGER NOT NULL REFERENCES prescriptions(prescription_id) ON DELETE CASCADE,
    alternative_medicine_id INTEGER NOT NULL REFERENCES medicines(medicine_id) ON DELETE RESTRICT,
    reason TEXT
);

-- PAYMENTS: For consultation or medicine purchase
CREATE TABLE payments (
    payment_id INTEGER PRIMARY KEY,
    user_id INTEGER NOT NULL REFERENCES users(user_id) ON DELETE CASCADE,
    amount REAL NOT NULL,
    payment_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    payment_method TEXT,
    status TEXT CHECK(status IN ('pending', 'completed', 'failed')) DEFAULT 'pending',
    description TEXT
);

-- EMERGENCY ALERTS: Records emergency button presses
CREATE TABLE emergency_alerts (
    alert_id INTEGER PRIMARY KEY,
    patient_id INTEGER NOT NULL REFERENCES patients(patient_id) ON DELETE CASCADE,
    alert_type TEXT CHECK(alert_type IN ('accident', 'shooting', 'other')) NOT NULL,
    alert_time DATETIME DEFAULT CURRENT_TIMESTAMP,
    hospital_alerted INTEGER REFERENCES organizations(organization_id),
    police_alerted BOOLEAN DEFAULT FALSE,
    details TEXT
);

-- AI_CHAT_MESSAGES: Messages sent/received in AI chat (patient-doctor assistant)
CREATE TABLE ai_chat_messages (
    message_id INTEGER PRIMARY KEY,
    consultation_id INTEGER NOT NULL REFERENCES consultations(consultation_id) ON DELETE CASCADE,
    sender_role TEXT CHECK(sender_role IN ('patient', 'doctor', 'ai')) NOT NULL,
    message_type TEXT CHECK(message_type IN ('text', 'voice', 'file', 'image')) NOT NULL,
    message_content TEXT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- SYMPTOM_CHECKLIST: Minor symptom checklist submitted by patient during AI chat
CREATE TABLE symptom_checklist (
    checklist_id INTEGER PRIMARY KEY,
    consultation_id INTEGER NOT NULL REFERENCES consultations(consultation_id) ON DELETE CASCADE,
    symptom TEXT NOT NULL,
    is_present BOOLEAN NOT NULL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);