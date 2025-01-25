import sys
sys.path.append("./")

from connection import db_session
from model.sql_users_model import Users

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


# update a user


# delete a user

for index, x in enumerate([1, 2, 3, 4, 5]):
  res = create_user(f"Name Diko {index}", f"diko.dev9{index}@gmail.com", "beginner")




print(f"res from api: {res}")