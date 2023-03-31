from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, ARRAY, Enum
from sqlalchemy.orm import relationship
import enum

from .database import Base

class Receiver(Base):
    __tablename__ = "receiver"

    

    id = Column(Integer, primary_key=True, index=True)
    sms_category = Column(String)
    number_list = Column(ARRAY(String))
    user_id = Column(Integer, ForeignKey("user.id"))

    creator = relationship("User")


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    email = Column(String)
    password = Column(String)

    sentsms = relationship("SMSlog", back_populates="sender")

class SMSlog(Base):
    __tablename__ = "smslog"

    id = Column(Integer, primary_key=True, index=True)
    receiver_id = Column(Integer, ForeignKey("receiver.id"))
    user_id = Column(Integer, ForeignKey("user.id"))
    text = Column(String)
    source_addr = Column(String)

    
    sender = relationship("User", back_populates="sentsms")
    receiver = relationship("Receiver")

class NETWORK_CHOISE(enum.Enum):
    cn = 'CN'
    rn = 'RN'

class CRITERIA_CHOISE(enum.Enum):
    a2 = 'A2'
    a3 = 'A3'
    a4 = 'A4'
    a5 = 'A5'
    an = 'Andijan'
    bh = 'Bukhara'
    dz = 'Djizzakh'
    fr = 'Fergana'
    sr = 'Sirdarya'
    ks = 'Kashkadarya'
    nm = 'Namangan'
    nv = 'Navoi'
    kr = 'Karakalpakstan'
    sm = 'Samarkand'
    ts = 'Tashkent'
    su = 'Surkhandarya'
    kh = 'Khorezm'

class NOTIFICATION_CHOISE(enum.Enum):
    internet = 'Internet Incidents'
    roaming = 'Roaming Incidents'
    core = 'Core Incidents'
    power = 'Power Incidents'
    controller = 'BSC/RNC Incidents'
    chronic = 'Chronic-Down Sites'
    hub = 'HUB Sites Incidents'
    report = 'Report Message'

class SMSReceivers(Base):
    __tablename__ = "smsreceiver"

    id = Column(Integer, primary_key=True, index=True)
    network = Column(Enum(NETWORK_CHOISE), nullable=False)
    criteria = Column(Enum(CRITERIA_CHOISE), nullable=False)
    notification = Column(Enum(NOTIFICATION_CHOISE), nullable=False)
    tel_number = Column(String(12), nullable=False)
    name = Column(String, nullable=False)