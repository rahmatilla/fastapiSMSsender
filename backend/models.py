from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, ARRAY
from sqlalchemy.orm import relationship

from .database import Base

class Receiver(Base):
    __tablename__ = "receiver"

    id = Column(Integer, primary_key=True, index=True)
    category = Column(String)
    number_list = Column(ARRAY(String))
    user_id = Column(Integer, ForeignKey("user.id"))

    creator = relationship("User", back_populates="receiver")

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    email = Column(String)
    password = Column(String)

    receiver = relationship("Receiver", back_populates="creator")
