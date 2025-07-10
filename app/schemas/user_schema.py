from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    nome: str
    email: EmailStr

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int

    class Config:
        from_attributes = True