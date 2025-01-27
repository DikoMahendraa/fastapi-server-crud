from fastapi import APIRouter
from model.pydantic_model import Users,  RoleEnum
import operations.users as db
import all_routes

user_route = APIRouter()

# create a new user
@user_route.post(all_routes.user_create)
def new_user(data: Users):
  data = dict(data)
  response = db.create_user(data["name"], data["email"], data["role"])

  return response

# get all users
@user_route.get(all_routes.user_all)
def get_all_users():
  response = db.get_all_users()

  return response


# get detail user
@user_route.get(all_routes.user_detail)
def get_user_detail(id: int):
  response = db.get_detail_user(id)

  return response

# update user
@user_route.put(all_routes.user_update)
def update_user(id: int, name: str = None, email: str = None, role: str = RoleEnum):
  response = db.update_detail_user(id, name, email, role)
  return response

# delete user
@user_route.delete(all_routes.user_delete)
def delete_user(id: int):
  response = db.delete_user(id)

  return response


