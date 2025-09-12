# app/main

from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.db.database import Base, engine
from app.api.endpoints import auth, doctor, patient, translate, register, appointments, payments

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace with actual frontend domain in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Static files and templates
app.mount("/static", StaticFiles(directory="frontend/static"), name="static")
templates = Jinja2Templates(directory="frontend/templates")

# DB setup (deferred to startup)
@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)

# Router
app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(doctor.router, prefix="/doctor", tags=["doctor"])
app.include_router(patient.router, prefix="/patient", tags=["patient"])
app.include_router(translate.router, prefix="/utils", tags=["translate"])
app.include_router(register.router, prefix="/register", tags=["register"])
app.include_router(appointments.router, prefix="/appointments", tags=["appointments"])
app.include_router(payments.router, prefix="/payments", tags=["payments"])

