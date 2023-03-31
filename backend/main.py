from fastapi import FastAPI
from .database import engine
from . import models
from .routers import receiver, user, authentication, smslog, smsreceivers


app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(authentication.router)
app.include_router(smsreceivers.router)
app.include_router(receiver.router)
app.include_router(user.router)
app.include_router(smslog.router)





