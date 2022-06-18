from fastapi import APIRouter

from endpoints import users_api

api_router = APIRouter()

api_router.include_router(users_api.router, prefix="/users", tags=["users"])



