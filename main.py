from fastapi import FastAPI, Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
# from fastapi.staticfiles import StaticFiles

from endpoints.routes import api_router
from database import db
from core.celery_config import celery_app

app = FastAPI()
celery = celery_app


@app.on_event('startup')
async def startup():
    await db.create_all()


@app.on_event('shutdown')
async def shutdown():
    await db.close()


app.include_router(api_router, prefix='/api')


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    print(await request.body())
    print(exc.errors())
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({'detail': 'Incorrect input'}),
    )


# app.mount("/", StaticFiles(directory="client/build", html=True), name="static")

# For debugging
# import uvicorn

# if __name__ == "__main__":
#     uvicorn.run(app, host="localhost", port=8000)
