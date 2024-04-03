from fastapi import Header, APIRouter, HTTPException, status
from users.user import UserIn, UserOut
import users.db_users
import api_key
from sqlalchemy import exc

router = APIRouter()

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
        
@router.post("/user", status_code=201)
async def add_user(payload: UserIn):
    new_user = payload.model_dump(exclude_unset=True)
    db_user = await users.db_users.email_exists(new_user['email'])
    print(db_user)
    if db_user:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, detail="The email is already in use.")
    try:
        user_id = await users.db_users.add_user(payload)
        response = {
            'user_id': user_id,
            **payload.model_dump()
        }
        return response
    except:
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Unable to insert the user")
    