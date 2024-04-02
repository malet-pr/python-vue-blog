from users.user import UserIn, UserDetailsIn
from db import users, users_details, database

async def user_exists(email: str, password: str):
    query = users.select().where(users.c.email == email and users.c.password == password)
    data = await database.execute(query=query)
    if(data != None):
        return True
    return False

async def add_user(payload: UserIn):
    query = users.insert().values(**payload.model_dump())
    return await database.execute(query=query)

async def get_all_users():
    query = users.select()
    return await database.fetch_all(query=query)

async def get_user(id:int):
    query = users.select().where(users.c.id==id)
    return await database.fetch_one(query=query)

async def delete_user(id: int):
    query = users.delete().where(users.c.id==id)
    return await database.execute(query=query)

async def update_user(id: int, payload: UserIn):
    query = (users.update().where(users.c.id == id).values(**payload.model_dump()))
    return await database.execute(query=query)

async def add_user_details(payload: UserDetailsIn):
    query = users.insert().values(**payload.model_dump())
    return await database.execute(query=query)

async def get_all_users_details():
    query = users_details.select()
    return await database.fetch_all(query=query)

async def get_user_details(id:int):
    query = users_details.select().where(users_details.c.id==id)
    return await database.fetch_one(query=query)

async def delete_user_details(id: int):
    query = users_details.delete().where(users_details.c.id==id)
    return await database.execute(query=query)

async def update_details(id: int, payload: UserDetailsIn):
    query = (users_details.update().where(users_details.c.id == id).values(**payload.model_dump()))
    return await database.execute(query=query)
