import stackprinter
import uvicorn
from fastapi import FastAPI
from fastapi_pagination import add_pagination

from app.routers import users

stackprinter.set_excepthook()

app = FastAPI()
app.include_router(users.router)

add_pagination(app)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
