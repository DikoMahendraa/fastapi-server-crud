from fastapi import FastAPI
from routes.users import user_route

app = FastAPI()

app.include_router(user_route)