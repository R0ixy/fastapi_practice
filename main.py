from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from endpoints.routes import api_router
from database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(api_router, prefix='/api')


app.mount("/", StaticFiles(directory="client/build", html=True), name="static")

# For debugging
# import uvicorn
#
# if __name__ == "__main__":
#     uvicorn.run(app, host="localhost", port=8000)
