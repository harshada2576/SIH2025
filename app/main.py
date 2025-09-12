from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from app.db.database import Base, engine
from app.api.endpoints import auth, doctor, patient, translate

Base.metadata.create_all(bind=engine)

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change this in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(doctor.router, prefix="/doctor", tags=["doctor"])
app.include_router(patient.router, prefix="/patient", tags=["patient"])
app.include_router(translate.router, prefix="/utils", tags=["translate"])

