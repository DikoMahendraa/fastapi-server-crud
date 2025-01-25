from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, DateTime, Integer
import datetime

def get_timestamp():
  return datetime.datetime.now()
  

BASE = declarative_base()

# creating our model or table
class Users(BASE):
  __tablename__: str = "users"
  _id = Column(Integer, primary_key=True, autoincrement=True)
  name = Column(String)
  email = Column(String)
  role = Column(String)
  timestamp = Column(DateTime, default=get_timestamp())


def __init__(self, name, email, role):
  self.name = name
  self.email = email
  self.role = role