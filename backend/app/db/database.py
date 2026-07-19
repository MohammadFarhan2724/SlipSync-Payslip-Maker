import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

load_dotenv()

SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit = False, autoflush= False, bind=engine)
Base = declarative_base() # Base is the parent class for all ORM Models

def get_db():
    db = SessionLocal() # Opens a session
    try:
        yield db # You read, add, update or delete data
    finally:
        db.close() # Ends the session

def create_table():
    Base.metadata.create_all(bind = engine) # Creates all tables defined by the ORM models using this engine (if they don't already exist)