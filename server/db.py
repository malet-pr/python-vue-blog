from sqlalchemy import (Column, Integer, MetaData, String, Table, ForeignKey, create_engine)
from databases import Database

DATABASE_URL = 'postgresql://pyblog:pyblog@localhost/py_blog'

engine = create_engine(DATABASE_URL)
metadata = MetaData()

users = Table(
    'users',
    metadata,
    Column('user_id', Integer, primary_key=True),
    Column('email', String(25), unique=True),
    Column('password', String(25), nullable=False) ## guardar en base64
)

users_details = Table(
    'user_details',
    metadata,
    Column('user_id', ForeignKey("users.user_id"), primary_key=True),
    Column('primary_email', ForeignKey("users.email")),
    Column('first_name', String(15), nullable=False),
    Column('middle_name', String(15), nullable=True),
    Column('last_name', String(25), nullable=False)
    ## agregar más campos
)

database = Database(DATABASE_URL)


