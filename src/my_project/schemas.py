from pydantic import BaseModel

class StatusResponse(BaseModel):
    status: str

class UserResponse(BaseModel):
    name: str
    email: str

class User(BaseModel):
    login: str
    name: str
    email: str
    password: str

class Pet(BaseModel):
    name: str
    nickname: str
    id: int

class PetResponse(BaseModel):
    name: str
    nickname: str