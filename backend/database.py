from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()
PG_HOST = str(os.getenv("PG_HOST"))
PG_USER = str(os.getenv("PG_USER"))
PG_PASS = str(os.getenv("PG_PASS"))
PG_PORT = str(os.getenv("PG_PORT"))
DB_NAME = str(os.getenv("DB_NAME"))

print(PG_PORT, PG_USER, PG_PASS, PG_HOST, DB_NAME)
#SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
SQLALCHEMY_DATABASE_URL = f"postgresql://{PG_USER}:{PG_PASS}@{PG_HOST}:{PG_PORT}/{DB_NAME}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()