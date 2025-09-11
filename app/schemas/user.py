from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    email: str
    password: str
    is_doctor: bool = False

class UserLogin(BaseModel):
    username: str
    password: str

class UserOut(BaseModel):
    id: int
    username: str
    email: str
    is_doctor: bool

    class Config:
        orm_mode = True

