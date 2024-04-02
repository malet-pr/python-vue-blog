from fastapi import Header, APIRouter, HTTPException, status
from users.user import UserIn, UserOut
import users.db_users
import api_key

router = APIRouter()

@router.get("/")
async def get_testroute():
    return "OK"

@router.post("/login")
async def login(payload: UserIn):
    user = payload.model_dump(exclude_unset=True)
    user_exists = await users.db_users.user_exists(user['email'],user['password'])
    if(user_exists):
        key = api_key.generate_api_key() 
        value = api_key.generate_value(user['email'],user['password'])
        api_key.store_key_value(key,value)
        return key
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="Incorrect user or password"
    )  
        
        