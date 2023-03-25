from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, ARRAY
from sqlalchemy.orm import relationship

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
