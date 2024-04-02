from fastapi import FastAPI, Depends
from routers import secure, public, users, blogs
from auth import get_user
from db import metadata, database, engine
from contextlib import asynccontextmanager

metadata.create_all(engine)

@asynccontextmanager
async def lifespan(app: FastAPI):
    await database.connect()
    yield
    await database.disconnect()

app = FastAPI(lifespan=lifespan)

app.include_router(
    public.router,
    prefix="/blog"
)
app.include_router(
    secure.router,
    prefix="/blog/secure",
    dependencies=[Depends(get_user)]
)

app.include_router(
    users.router,
    prefix="/blog",
    dependencies=[Depends(get_user)]
)

"""
app.include_router(
    blogs.router,
    prefix="/blog",
    dependencies=[Depends(get_user)]
)
 """