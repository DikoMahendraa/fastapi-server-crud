from pydantic import BaseModel

class Employee(BaseModel):
    id: int
    name: str
    username: str
    email: str
    role: str

    class Config:
        from_attributes = True  # Enable ORM compatibility