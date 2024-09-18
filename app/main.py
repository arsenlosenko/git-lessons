import uvicorn
from fastapi import FastAPI

app = FastAPI()

users = [
    {"id": 1, "name": "User One"},
    {"id": 2, "name": "User Two"},
    {"id": 3, "name": "User Three"},
]


@app.get("/")
async def index():
    return {"message": "API is working"}


@app.get("/users")
async def get_users():
    user_info = users
    return {"users": user_info}


@app.get("/users/{user_id}")
async def get_user_info(user_id: int):
    user_detail = [item for item in users if item["id"] == user_id]
    return {"user_info": user_detail}


def start():
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)


if __name__ == "__main__":
    start()
