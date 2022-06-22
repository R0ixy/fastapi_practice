from fastapi import APIRouter

from endpoints import users_api, auth

api_router = APIRouter()

api_router.include_router(users_api.router, prefix='/users', tags=['users'])
api_router.include_router(auth.router, tags=['auth'])
