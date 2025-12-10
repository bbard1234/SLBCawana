from pydantic import BaseModel, EmailStr
from typing import Any, Dict, Optional, List

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class LoginRequest(BaseModel):
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: int
    email: EmailStr
    is_admin: bool
    class Config:
        from_attributes = True

class ClassIn(BaseModel):
    name: str
    term: Optional[str] = None

class ClassOut(ClassIn):
    id: int
    class Config:
        from_attributes = True

class SubmissionIn(BaseModel):
    class_id: int
    answers: Dict[str, Any]  # key = field id from schema

class SubmissionOut(BaseModel):
    id: int
    class_id: int
    user_id: int
    created_at: str
    answers: Dict[str, Any]
    class Config:
        from_attributes = True
