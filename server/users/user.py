from pydantic import BaseModel
from typing import List, Optional

class UserIn(BaseModel):
    email: str
    password: str

class UserOut(UserIn):
    user_id: int

class UserUpdate(UserIn):
    email: Optional[str] = None
    password: Optional[str] = None

class UserDetailsIn(BaseModel):
    first_name: Optional[str] = None
    middle_name: Optional[str] = None
    last_name: Optional[str] = None
    
class UserDetailsOut(UserDetailsIn):
    user_id: int 
    primary_email: str

class UserDetailsUpdate(UserDetailsIn):
    first_name: Optional[str] = None
    middle_name: Optional[str] = None
    last_name: Optional[str] = None
    
