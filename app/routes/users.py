from fastapi import APIRouter
from model.pydantic_model import Users
import operations.users as db
import all_routes

user_route = APIRouter()

# create a new user
@user_route.post(all_routes.user_create)
def new_user(data: Users):
  data = dict(data)
  res = db.create_user(data["name"], data["email"], data["role"])

  return res

# get all users
@user_route.get(all_routes.user_all)
def get_all_users():
  res = db.get_all_users()

  return res