def decode_user(doc) -> dict:
  return {
    '_id': doc._id,
    'name': doc.name,
    'email': doc.email,
    'role': doc.role,
    'timestamp': doc.timestamp,
  }


def decode_users(docs) -> list:
  return [
    # looping the data array and put it into decode_user function
    decode_user(doc) for doc in docs
  ]