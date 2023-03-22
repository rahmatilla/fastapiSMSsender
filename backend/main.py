from fastapi import FastAPI
from .database import engine
from . import models
from .routers import receiver, user, authentication


app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(authentication.router)
app.include_router(receiver.router)
app.include_router(user.router)



