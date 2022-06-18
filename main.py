from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from endpoints.routes import api_router
import models

models.Base.metadata.create_all()

app = FastAPI()

app.include_router(api_router, prefix='/api')


app.mount("/", StaticFiles(directory="client/build", html=True), name="static")
