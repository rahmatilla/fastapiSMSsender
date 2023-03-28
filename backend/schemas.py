from pydantic import BaseModel
from typing import List, Optional

class Receiver(BaseModel):
    sms_category: str
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
    sms_category: str
    number_list: list[str]
    creator: ShowUser

    class Config():
        orm_mode = True

class SMSlog(BaseModel):
    receiver = Receiver
    sender = ShowUser
    text = str
    source_addr = str

    class Config():
        orm_mode = True


class SendSMS(BaseModel):
    sms_category: str
    text: str
    source_addr: str

class Login(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None



    