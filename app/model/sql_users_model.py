from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, DateTime, Integer, Enum
import datetime
from enum import Enum as PyEnum

def get_timestamp():
    return datetime.datetime.now()

BASE = declarative_base()

# Define the enum class
class RoleEnum(PyEnum):
    ADMIN = "admin"
    SUPER_ADMIN = "super admin"
    USER = "user"

# Creating our model or table
class Users(BASE):
    __tablename__ = "users"
    _id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=True)
    role = Column(Enum(RoleEnum), nullable=False)
    timestamp = Column(DateTime, default=get_timestamp)

    def __init__(self, name: str, email: str, role: RoleEnum):
        self.name = name
        self.email = email
        self.role = role
