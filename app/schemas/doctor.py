# app/schemas/doctor

from pydantic import BaseModel, EmailStr, Field
from datetime import date
from typing import List, Dict, Optional

class RegisterDoctorRequest(BaseModel):
    first_name: str = Field(..., alias="firstName")
    middle_name: Optional[str] = Field(None, alias="middleName")
    last_name: str = Field(..., alias="lastName")
    gender: Optional[str]
    date_of_birth: date = Field(None, alias="dateOfBirth")  # Could use date type if you want
    phone: str
    email: EmailStr
    password: str
    
    registration_number: Optional[str] = Field(None, alias="registrationNumber")
    medical_council: Optional[str] = Field(None, alias="medicalCouncil")
    specialization: Optional[str]
    sub_specialization: Optional[str] = Field(None, alias="subSpecialization")
    experience: Optional[int]
    qualifications: Optional[str]
    
    hospital_name: Optional[str] = Field(None, alias="hospitalName")
    consultation_type: Optional[str] = Field(None, alias="consultationType")
    hospital_address: Optional[str] = Field(None, alias="hospitalAddress")
    consultation_fee: Optional[float] = Field(None, alias="consultationFee")
    online_fee: Optional[float] = Field(None, alias="onlineFee")
    available_timings: Optional[Dict[str, List[str]]] = Field(default_factory=dict, alias="availableTimings")
    
    account_holder_name: Optional[str] = Field(None, alias="accountHolderName")
    account_number: Optional[str] = Field(None, alias="accountNumber")
    ifsc_code: Optional[str] = Field(None, alias="ifscCode")
    bank_name: Optional[str] = Field(None, alias="bankName")
    pan_number: Optional[str] = Field(None, alias="panNumber")
    gst_number: Optional[str] = Field(None, alias="gstNumber")
    upi_id: Optional[str] = Field(None, alias="upiId")
    
    languages: List[str] = Field(default_factory=list)
    emergency_contact: Optional[str] = Field(None, alias="emergencyContact")
    bio: Optional[str]
    
    confirm_details: bool = Field(..., alias="confirmDetails")
    agree_terms: bool = Field(..., alias="agreeTerms")

