from fastapi import FastAPI
from routes.user import user
from routes.auth import authRouter
from routes.post import post
import uvicorn

app = FastAPI()

# route public
app.include_router(authRouter)
app.include_router(user)

# route private
app.include_router(post)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=5000, log_level="info")