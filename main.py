import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def index():
    return {"message": "API is working"}


def start():
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)


if __name__ == "__main__":
    start()
