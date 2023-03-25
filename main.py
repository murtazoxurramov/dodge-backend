from fastapi import FastAPI

from routers import register_routers


app = FastAPI()
register_routers(app=app, prefix="/api/v1")
