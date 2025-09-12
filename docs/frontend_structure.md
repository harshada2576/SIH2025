# Telemedicine & Medical Assistance App – SIH Project

This document explains the **user flow and screen structure** of our mobile application prototype.  
The app is designed to connect patients with doctors, manage appointments, prescriptions, and enable online medicine ordering.

---

## 📌 App Structure

### 1. Home Screen
- **Sections:**
  - 👨‍⚕️ Doctors  
  - 💊 Medicals (Pharmacy)  
  - 🩸 Blood Donors  
  - 🧰 Lifeline Skills  
  - 🚨 Emergency  
- Acts as the main navigation hub.

---

### 2. Doctor Module

#### a. Doctor Type Selection
- Categories displayed with icons (Eye, Dental, etc.)
- Helps user filter doctors by specialization.

#### b. List of Doctors Available
- Shows:
  - Doctor’s **Name**
  - **Profile Picture**
  - **Ratings / Experience**
- Buttons:
  - **Book Appointment**
  - **Consult Online**

#### c. Doctor Profile
- Details shown:
  - Doctor’s photo & bio  
  - Experience & specialization  
  - Short description  
- Options to:
  - Book Appointment  
  - Start Online Consultation  

#### d. Appointment Slots
- Timings:
  - 09:00–11:00 AM  
  - 02:00–05:30 PM  
  - 08:00–10:30 PM  
- Charges:
  - Morning ₹299  
  - Evening ₹299  

#### e. Queue & Payment
- Shows number of people waiting in queue  
- Secure payment option:
  - **Pay ₹99 to confirm booking**

---

### 3. Patient Module

#### a. Appointment Schedule
- Displays confirmed appointments:
  - Patient Name  
  - Date & Time of consultation  

#### b. Patient Medical History
- Patient profile with:
  - Basic details  
  - Previous health history  
  - Prescriptions & doctor notes  

---

### 4. Prescription & Medicine Module

#### a. Prescription Section
- Digital prescriptions from doctors (e.g., Dr. Karan, Dr. Ram).  
- Securely stored & sharable.  

#### b. Medicine Ordering
- Options:
  - Medico  
  - HealthPlus  
  - Generic Medicines  
- Upload prescription option.  

#### c. Pharmacy Listing
- Example pharmacies:
  - Vishal Pharma – Total: ₹242  
  - Aria Medical – Total: ₹290  
- Features:
  - Home delivery option  
  - Real-time availability  

---

## 🔑 Key Features
- Online doctor consultation  
- Appointment scheduling & payments  
- Digital health record management  
- Online medicine ordering & delivery  
- Emergency support & blood donor info  

---

## 📂 Folder Structure (for GitHub)
```

docs/
│
├── README.md               # Project overview
├── app\_flow\.md             # This document (App structure & screens)
├── architecture.md         # System architecture & backend design
└── ui\_wireframes/          # Canva screenshots of the prototype
├── home.png
├── doctor\_module.png
├── patient\_module.png
└── medicine\_module.png

```

---

## 🚀 Usage in SIH
This flow demonstrates the **end-to-end journey** of a patient:  
**Home → Select Doctor → Book & Pay → Consultation → Prescription → Order Medicines.**  
It ensures **accessibility, affordability, and faster healthcare delivery** especially for **villages and semi-urban areas**.
```

---
