# app/main

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from app.api.endpoints import auth, doctor, patient, translate, register, appointments, payments, pharmacy, prescriptions, medicines

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="frontend/static"), name="static")
templates = Jinja2Templates(directory="frontend/templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(doctor.router, prefix="/doctor", tags=["doctor"])
app.include_router(patient.router, prefix="/patient", tags=["patient"])
app.include_router(translate.router, prefix="/utils", tags=["utils"])
app.include_router(register.router, prefix="/register", tags=["register"])
app.include_router(appointments.router, prefix="/appointments", tags=["appointments"])
app.include_router(payments.router, prefix="/payments", tags=["payments"])
app.include_router(pharmacy.router, prefix="/pharmacy", tags=["pharmacy"])
app.include_router(prescriptions.router, prefix="/prescriptions", tags=["prescriptions"])
app.include_router(medicines.router, prefix="/medicines", tags=["medicines"])

@app.get("/login", response_class=HTMLResponse)
async def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.get("/patient/register", response_class=HTMLResponse)
async def patient_register_page(request: Request):
    return templates.TemplateResponse("patient_registration.html", {"request": request})

@app.get("/doctor/register", response_class=HTMLResponse)
async def doctor_register_page(request: Request):
    return templates.TemplateResponse("registerdoctor.html", {"request": request})

@app.get("/pharmacy/register", response_class=HTMLResponse)
async def pharmacy_register_page(request: Request):
    return templates.TemplateResponse("pharmacy_reg.html", {"request": request})

@app.get("/forgot-password", response_class=HTMLResponse)
async def forgot_password_page(request: Request):
    return templates.TemplateResponse("forgotpassword.html", {"request": request})

@app.get("/doctors", response_class=HTMLResponse)
async def doctors_page(request: Request):
    return templates.TemplateResponse("listofdocavailable.html", {"request": request})

@app.get("/doctor/info/{doctor_id}", response_class=HTMLResponse)
async def doctor_info_page(request: Request, doctor_id: int):
    return templates.TemplateResponse("docinfo.html", {"request": request, "doctor_id": doctor_id})

@app.get("/patient/info", response_class=HTMLResponse)
async def patient_info_page(request: Request):
    return templates.TemplateResponse("patientinfo.html", {"request": request})

@app.get("/book/online", response_class=HTMLResponse)
async def book_online_page(request: Request):
    return templates.TemplateResponse("bookonline.html", {"request": request})

@app.get("/book/offline", response_class=HTMLResponse)
async def book_offline_page(request: Request):
    return templates.TemplateResponse("bookoffline.html", {"request": request})

@app.get("/pharmacy/prescriptions", response_class=HTMLResponse)
async def pharmacy_prescriptions_page(request: Request):
    return templates.TemplateResponse("pharmacyhome.html", {"request": request})

@app.get("/medicines/compare", response_class=HTMLResponse)
async def medicines_compare_page(request: Request):
    return templates.TemplateResponse("bill.html", {"request": request})
