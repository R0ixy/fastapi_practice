from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def get_users():
    return {"message": f"Hello "}


@router.get('/{id}')
async def get_one_user(id: int):
    return {f'user:{id}'}
