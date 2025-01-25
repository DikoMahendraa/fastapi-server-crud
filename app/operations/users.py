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

# get user detail
def get_detail_user(id: int):
  try:
    criteria = {"_id": id}
    res = db_session.query(Users).filter_by(**criteria).one_or_none()

    if res is not None:
      return {
        "status": "success",
        "data": decode.decode_user(res)
      }
    else:
        return {
        "status": "error",
        "message": f"record with id {id} do not exist"
      }
  
  except Exception as e:
    return {
      "status": "error",
      "message": e
    }

# update a user


# delete a user



print(get_detail_user(12))