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
    return {"users": users}


def start():
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)


if __name__ == "__main__":
    start()
