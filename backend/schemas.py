from pydantic import BaseModel
from typing import List, Optional
from enum import Enum
from .models import NETWORK_CHOISE, CRITERIA_CHOISE, NOTIFICATION_CHOISE

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
    receiver: Receiver
    sender: ShowUser
    text: str
    source_addr: str

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

# class NETWORK_CHOISE(str, Enum):
#     cn = 'CN'
#     rn = 'RN'

# class CRITERIA_CHOISE(str, Enum):
#     a2 = 'A2'
#     a3 = 'A3'
#     a4 = 'A4'
#     a5 = 'A5'
#     an = 'Andijan'
#     bh = 'Bukhara'
#     dz = 'Djizzakh'
#     fr = 'Fergana'
#     sr = 'Sirdarya'
#     ks = 'Kashkadarya'
#     nm = 'Namangan'
#     nv = 'Navoi'
#     kr = 'Karakalpakstan'
#     sm = 'Samarkand'
#     ts = 'Tashkent'
#     su = 'Surkhandarya'
#     kh = 'Khorezm'

# class NOTIFICATION_CHOISE(str, Enum):
#     internet = 'Internet Incidents'
#     roaming = 'Roaming Incidents'
#     core = 'Core Incidents'
#     power = 'Power Incidents'
#     controller = 'BSC/RNC Incidents'
#     chronic = 'Chronic-Down Sites'
#     hub = 'HUB Sites Incidents'
#     report = 'Report Message'

class SMSReceivers(BaseModel):
    network: Optional[NETWORK_CHOISE]
    criteria: Optional[CRITERIA_CHOISE]
    notification: Optional[NOTIFICATION_CHOISE]
    tel_number: str
    name: str



    