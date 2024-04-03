from typing import List
from fastapi import Header, APIRouter, HTTPException, status
from users.user import UserIn, UserOut, UserUpdate, UserDetailsIn, UserDetailsOut, UserDetailsUpdate
import users.db_users
from sqlalchemy import exc

router = APIRouter()

@router.get("/user", response_model=List[UserOut])
async def get_all_users():
    return await users.db_users.get_all_users()

@router.get('/user/{id}')
async def get_user(id: int):
    return await users.db_users.get_user(id)

@router.put('/user/{id}')
async def replace_user(id: int, payload: UserIn):
    pass

@router.patch('/user/{id}',status_code=204)
async def update_user(id: int, payload: UserUpdate):
    pass

@router.delete('/user/{id}',status_code=204)
async def delete_user(id: int):
    pass

## esta ruta debería estar disponible sólo para administradores
@router.get("/user/details/", response_model=List[UserDetailsOut])
async def get_all_users_details():
    return await users.db_users.get_all_users_details()

@router.get('/user/details/{id}')
async def get_user_details(id: int):
    return await users.db_users.get_user_details(id)

@router.post("/user/details/")
async def add_user_details(payload: UserDetailsIn):
    pass

@router.put('/user/details/{id}')
async def replace_user_details(id: int, payload: UserIn):
    pass

@router.patch('/user/details/{id}',status_code=204)
async def update_user_details(id: int, payload: UserDetailsUpdate):
    pass

@router.delete('/user/details/{id}',status_code=204)
async def delete_details(id: int):
    pass
