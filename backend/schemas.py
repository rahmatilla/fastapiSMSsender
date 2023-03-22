from pydantic import BaseModel
from typing import List, Optional

class Receiver(BaseModel):
    category: str
    number_list: list[str]



class User(BaseModel):
    username: str
    email: str
    password: str

class ShowUser(BaseModel):
    username: str
    email: str

    class Config():
        orm_mode = True

class ShowReceiver(BaseModel):
    category: str
    number_list: list[str]
    creator: ShowUser

    class Config():
        orm_mode = True

class Login(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None