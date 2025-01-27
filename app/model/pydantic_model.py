from pydantic import BaseModel
from enum import Enum as PyEnum
from model.sql_users_model import RoleEnum

class Users(BaseModel):
  name: str
  email: str
  role: RoleEnum