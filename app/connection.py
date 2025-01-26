from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from decouple import config

from model.sql_users_model import BASE

db_user = config("DB_USER", default="postgres")
db_port = config("DB_PORT", default=5400)
db_host = config("DB_HOST", default="localhost")
db_password = config("DB_PASSWORD", default="admin")


uri: str = F"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/defaultdb"

engine = create_engine(uri)

BASE.metadata.create_all(bind = engine)

# session
session = sessionmaker(
  bind=engine,
  autoflush=True
)

db_session  = session()

try:
  connection = engine.connect()
  connection.close()
  print('ping, Connected')
except Exception as e:
  print(f'Error: {str(e)}')
