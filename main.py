from fastapi import FastAPI
from routes.user import user
import uvicorn

app = FastAPI()
app.include_router(user)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=5000, log_level="info")