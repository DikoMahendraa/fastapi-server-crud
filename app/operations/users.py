import sys
sys.path.append("./")

from connection import db_session
from model.sql_users_model import Users
import decodes.users as decode

# create a users
def create_user(name: str, email: str, role: str) -> dict:
  try:
    req = Users(name, email, role)
    db_session.add(req)
    db_session.commit()
    return {
      "status": "success",
      "message": "user created!"
    }

  except Exception as e:
    return {
      "status": "error",
      "message": e 
    }

# get all users list
def get_all_users() -> dict:
  try:
    req = db_session.query(Users).all()
    users = decode.decode_users(req)

    return {
      "status": "success",
      "data": users
    }
  except Exception as e:
    return {
      "status": "error",
      "message": e
    }


# update a user


# delete a user

# res = create_user(f"Name Diko {index}", f"diko.dev9{index}@gmail.com", "beginner")
# print(f"res from api: {res}")

res = get_all_users()

print(res)